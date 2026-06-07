#!/usr/bin/env powershell
# One-shot setup for the optional local MusicGen/AudioCraft environment.

param(
    [string]$VenvPath = ".venv-musicgen",
    [string]$Python = "",
    [switch]$CheckOnly,
    [switch]$SkipModelDownload,
    [switch]$SkipSmoke
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

function Write-Step {
    param([string]$Message)
    Write-Host ""
    Write-Host $Message -ForegroundColor Cyan
}

function Get-CandidateLabel {
    param([string[]]$Candidate)
    return ($Candidate -join " ")
}

function Invoke-CandidatePython {
    param(
        [string[]]$Candidate,
        [string]$Code
    )

    $exe = $Candidate[0]
    $args = @()
    if ($Candidate.Count -gt 1) {
        $args = $Candidate[1..($Candidate.Count - 1)]
    }

    try {
        & $exe @args -c $Code 2>$null
    }
    catch {
        return $null
    }
}

function Get-CompatiblePython {
    $candidates = @()
    if (-not [string]::IsNullOrWhiteSpace($Python)) {
        $candidates += ,@($Python)
    }
    $candidates += ,@("py", "-3.11")
    $candidates += ,@("py", "-3.10")
    $candidates += ,@("python")

    foreach ($candidate in $candidates) {
        $probe = Invoke-CandidatePython `
            -Candidate $candidate `
            -Code "import sys; print(f'{sys.executable}|{sys.version_info.major}.{sys.version_info.minor}')"

        if ($LASTEXITCODE -ne 0 -or [string]::IsNullOrWhiteSpace($probe)) {
            continue
        }

        $parts = $probe.Trim().Split("|")
        if ($parts.Count -ne 2) {
            continue
        }

        $version = $parts[1]
        if ($version -eq "3.10" -or $version -eq "3.11") {
            return [pscustomobject]@{
                Candidate = $candidate
                Executable = $parts[0]
                Version = $version
                Label = Get-CandidateLabel $candidate
            }
        }

        Write-Host "Skipping $(Get-CandidateLabel $candidate): Python $version is not supported by AudioCraft 1.3.0." -ForegroundColor Yellow
    }

    return $null
}

function Invoke-VenvPython {
    param(
        [string]$VenvPython,
        [string[]]$Arguments
    )
    & $VenvPython @Arguments
    if ($LASTEXITCODE -ne 0) {
        throw "Command failed: $VenvPython $($Arguments -join ' ')"
    }
}

function Test-NvidiaGpu {
    try {
        nvidia-smi *> $null
        return ($LASTEXITCODE -eq 0)
    }
    catch {
        return $false
    }
}

$repoRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $repoRoot

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  AI-DJ Local MusicGen Setup" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan

Write-Step "Finding a compatible Python..."
$compatiblePython = Get-CompatiblePython

if ($null -eq $compatiblePython) {
    Write-Host "No Python 3.10 or 3.11 runtime was found." -ForegroundColor Red
    Write-Host "AudioCraft 1.3.0 pins torch==2.1.0, so Python 3.12 is not supported for MusicGen." -ForegroundColor Yellow
    Write-Host ""
    Write-Host "Install Python 3.11, then rerun:" -ForegroundColor Yellow
    Write-Host "  py -3.11 --version" -ForegroundColor Gray
    Write-Host "  .\setup_local_models.ps1" -ForegroundColor Gray
    exit 1
}

Write-Host "Using $($compatiblePython.Label): $($compatiblePython.Executable) (Python $($compatiblePython.Version))" -ForegroundColor Green

$venvPython = Join-Path $repoRoot (Join-Path $VenvPath "Scripts\python.exe")

if ($CheckOnly) {
    if (Test-Path $venvPython) {
        Write-Host "Existing MusicGen venv found: $venvPython" -ForegroundColor Green
    }
    else {
        Write-Host "MusicGen venv would be created at: $VenvPath" -ForegroundColor Yellow
    }
    Write-Host "Check complete. No packages were installed." -ForegroundColor Green
    exit 0
}

if (-not (Test-Path $venvPython)) {
    Write-Step "Creating MusicGen virtual environment..."
    $candidate = [string[]]$compatiblePython.Candidate
    $exe = $candidate[0]
    $args = @()
    if ($candidate.Count -gt 1) {
        $args = $candidate[1..($candidate.Count - 1)]
    }
    & $exe @args -m venv $VenvPath
    if ($LASTEXITCODE -ne 0) {
        throw "Failed to create virtual environment with $($compatiblePython.Label)."
    }
}
else {
    Write-Step "Using existing MusicGen virtual environment..."
}

Write-Host "Venv Python: $venvPython" -ForegroundColor Green

Write-Step "Checking pip..."
Invoke-VenvPython $venvPython @("-m", "pip", "--version")

Write-Step "Upgrading pip..."
Invoke-VenvPython $venvPython @("-m", "pip", "install", "--upgrade", "pip")

$hasGpu = Test-NvidiaGpu
if ($hasGpu) {
    Write-Step "Installing AudioCraft-compatible PyTorch with CUDA 12.1 wheels..."
    Invoke-VenvPython $venvPython @(
        "-m", "pip", "install",
        "torch==2.1.0", "torchvision==0.16.0", "torchaudio==2.1.0",
        "--index-url", "https://download.pytorch.org/whl/cu121"
    )
}
else {
    Write-Step "Installing AudioCraft-compatible PyTorch CPU wheels..."
    Invoke-VenvPython $venvPython @(
        "-m", "pip", "install",
        "torch==2.1.0", "torchvision==0.16.0", "torchaudio==2.1.0"
    )
}

Write-Step "Installing AudioCraft and helpers..."
Invoke-VenvPython $venvPython @(
    "-m", "pip", "install",
    "audiocraft==1.3.0", "transformers", "accelerate", "psutil"
)

Write-Step "Verifying imports..."
Invoke-VenvPython $venvPython @(
    "-c",
    "import torch; from audiocraft.models import MusicGen; print(f'PyTorch: {torch.__version__}'); print(f'CUDA available: {torch.cuda.is_available()}'); print('AudioCraft import OK')"
)

if (-not $SkipModelDownload) {
    Write-Step "Pre-downloading MusicGen Small..."
    Invoke-VenvPython $venvPython @(
        "-c",
        "from audiocraft.models import MusicGen; print('Downloading model...'); MusicGen.get_pretrained('facebook/musicgen-small'); print('Model ready.')"
    )
}

if (-not $SkipSmoke) {
    Write-Step "Running a short generation smoke test..."
    Invoke-VenvPython $venvPython @(
        "13_tools/scripts/make_dj_track_local.py",
        "--idea", "test",
        "--duration", "5",
        "--model", "facebook/musicgen-small"
    )
}

Write-Host ""
Write-Host "Setup finished. Activate the venv with:" -ForegroundColor Green
Write-Host "  .\$VenvPath\Scripts\activate" -ForegroundColor Gray
Write-Host "Then try:" -ForegroundColor Green
Write-Host "  python generate_demo_local.py" -ForegroundColor Gray
Write-Host "  python 13_tools/scripts/make_dj_track_local.py --idea 'your idea' --cuda" -ForegroundColor Gray
