#!/usr/bin/env powershell
# One-shot setup for the optional local MusicGen/AudioCraft environment.

$ErrorActionPreference = "Stop"

function Write-Step($Message) {
    Write-Host ""
    Write-Host $Message -ForegroundColor Cyan
}

function Require-Command($Command, $Hint) {
    & $Command --version *> $null
    if ($LASTEXITCODE -ne 0) {
        Write-Host "Missing command: $Command" -ForegroundColor Red
        Write-Host $Hint -ForegroundColor Yellow
        exit 1
    }
}

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  AI DJ Local MusicGen Setup" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan

Write-Step "Checking Python..."
Require-Command "python" "Install Python 3.10 or 3.11 from https://www.python.org/downloads/"

$pythonVersion = python --version 2>&1
Write-Host "Detected: $pythonVersion" -ForegroundColor Green

$pyVersionInfo = python -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')"
if ($LASTEXITCODE -ne 0) {
    Write-Host "Unable to detect Python version." -ForegroundColor Red
    exit 1
}

$pyParts = $pyVersionInfo.Trim().Split(".")
$pyMajor = [int]$pyParts[0]
$pyMinor = [int]$pyParts[1]

if ($pyMajor -gt 3 -or ($pyMajor -eq 3 -and $pyMinor -ge 12)) {
    Write-Host "AudioCraft/MusicGen setup is not supported on Python $pyVersionInfo." -ForegroundColor Red
    Write-Host "AudioCraft 1.3.0 pins torch==2.1.0, which is not available for Python 3.12." -ForegroundColor Yellow
    Write-Host ""
    Write-Host "Create a separate Python 3.10 or 3.11 environment instead:" -ForegroundColor Yellow
    Write-Host "  py -3.11 -m venv .venv-musicgen" -ForegroundColor Gray
    Write-Host "  .\.venv-musicgen\Scripts\activate" -ForegroundColor Gray
    Write-Host "  python -m pip install --upgrade pip" -ForegroundColor Gray
    Write-Host "  python -m pip install torch torchvision torchaudio audiocraft" -ForegroundColor Gray
    exit 1
}

Write-Step "Checking pip..."
python -m pip --version
if ($LASTEXITCODE -ne 0) {
    Write-Host "pip is not available for this Python." -ForegroundColor Red
    exit 1
}

Write-Step "Upgrading pip..."
python -m pip install --upgrade pip

Write-Step "Checking GPU/CUDA..."
$hasGPU = $false
try {
    nvidia-smi
    if ($LASTEXITCODE -eq 0) {
        $hasGPU = $true
        Write-Host "NVIDIA GPU detected." -ForegroundColor Green
    }
} catch {
    $hasGPU = $false
}

Write-Step "Installing PyTorch..."
if ($hasGPU) {
    python -m pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
} else {
    python -m pip install torch torchvision torchaudio
}
if ($LASTEXITCODE -ne 0) {
    Write-Host "PyTorch installation failed." -ForegroundColor Red
    exit 1
}

Write-Step "Verifying PyTorch..."
python -c "import torch; print(f'PyTorch: {torch.__version__}'); print(f'CUDA available: {torch.cuda.is_available()}')"

Write-Step "Installing AudioCraft and helpers..."
python -m pip install audiocraft transformers accelerate psutil
if ($LASTEXITCODE -ne 0) {
    Write-Host "AudioCraft installation failed." -ForegroundColor Red
    exit 1
}

Write-Step "Pre-downloading MusicGen Small..."
python -c "from audiocraft.models import MusicGen; print('Downloading model...'); MusicGen.get_pretrained('facebook/musicgen-small'); print('Model ready.')"
if ($LASTEXITCODE -ne 0) {
    Write-Host "Model pre-download failed; it may still download on first use." -ForegroundColor Yellow
}

Write-Step "Running a short generation smoke test..."
python 13_tools/scripts/make_dj_track_local.py --idea "test" --duration 5 --model facebook/musicgen-small
if ($LASTEXITCODE -eq 0) {
    Write-Host "Local MusicGen generation smoke test passed." -ForegroundColor Green
} else {
    Write-Host "Local MusicGen generation smoke test failed after installation." -ForegroundColor Yellow
}

Write-Host ""
Write-Host "Setup finished. Try:" -ForegroundColor Green
Write-Host "  python generate_demo_local.py" -ForegroundColor Gray
Write-Host "  python 13_tools/scripts/make_dj_track_local.py --idea 'your idea' --cuda" -ForegroundColor Gray
