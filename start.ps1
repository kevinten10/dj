# AI-DJ workspace launcher

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

function Wait-BeforeExit {
    if (-not [Console]::IsInputRedirected) {
        Read-Host "Press Enter to exit" | Out-Null
    }
}

function Exit-WithPause {
    param([int]$Code = 0)
    Write-Host ""
    Wait-BeforeExit
    exit $Code
}

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  AI-DJ Workspace Launcher" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

try {
    $pythonPath = Get-Command python -ErrorAction Stop
    Write-Host "OK: Python found at $($pythonPath.Source)" -ForegroundColor Green
}
catch {
    Write-Host "ERROR: Python was not found. Install Python 3.9+ first." -ForegroundColor Red
    Exit-WithPause 1
}

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $scriptDir

Write-Host ""
Write-Host "Choose an action:" -ForegroundColor Yellow
Write-Host "1. Start interactive generator (recommended)" -ForegroundColor White
Write-Host "2. Open documentation" -ForegroundColor White
Write-Host "3. Configure MiniMax API" -ForegroundColor White
Write-Host "4. Run system check" -ForegroundColor White
Write-Host "0. Exit" -ForegroundColor White
Write-Host ""

$choice = Read-Host "Enter option (default: 1)"
if ([string]::IsNullOrWhiteSpace($choice)) { $choice = "1" }

switch ($choice) {
    "1" {
        Write-Host ""
        Write-Host "Starting interactive generator..." -ForegroundColor Cyan
        Write-Host ""
        python 13_tools/scripts/interactive_generator.py
        Exit-WithPause $LASTEXITCODE
    }
    "2" {
        Write-Host ""
        Write-Host "Available documents:" -ForegroundColor Yellow
        Write-Host "1. Learning path" -ForegroundColor White
        Write-Host "2. Techniques library" -ForegroundColor White
        Write-Host "3. Local model guide" -ForegroundColor White
        Write-Host "4. Local lyrics model guide" -ForegroundColor White
        Write-Host "5. ACE-Step deployment report" -ForegroundColor White
        Write-Host "6. AI-DJ tutorial" -ForegroundColor White
        Write-Host "7. Project handoff status" -ForegroundColor White

        $docChoice = Read-Host "Choose document (1-7, default: 1)"
        if ([string]::IsNullOrWhiteSpace($docChoice)) { $docChoice = "1" }

        $docMap = @{
            "1" = "12_docs/learning_path.md"
            "2" = "12_docs/techniques_library.md"
            "3" = "12_docs/local_models.md"
            "4" = "12_docs/local_lyrics_models.md"
            "5" = "12_docs/ace_step_deployment_report.md"
            "6" = "12_docs/ai_djuced_tutorial.md"
            "7" = "12_docs/project_handoff_status.md"
        }

        if ($docMap.ContainsKey($docChoice)) {
            Write-Host "Opening documentation..." -ForegroundColor Cyan
            Invoke-Item $docMap[$docChoice]
            Exit-WithPause 0
        }

        Write-Host "Invalid document option." -ForegroundColor Yellow
        Exit-WithPause 1
    }
    "3" {
        Write-Host ""
        Write-Host "Configure MiniMax API" -ForegroundColor Yellow

        $envFile = "13_tools/configs/minimax_env.ps1"
        $exampleFile = "13_tools/configs/minimax_env.example.ps1"

        if (-not (Test-Path $envFile)) {
            if (Test-Path $exampleFile) {
                Copy-Item $exampleFile $envFile
                Write-Host "Created config file: $envFile" -ForegroundColor Green
            }
            else {
                Write-Host "Example config file not found: $exampleFile" -ForegroundColor Red
                Exit-WithPause 1
            }
        }

        Write-Host "Opening config file..." -ForegroundColor Cyan
        Start-Process notepad $envFile
        Write-Host ""
        Write-Host "After editing, load it with:" -ForegroundColor Gray
        Write-Host ". .\13_tools\configs\minimax_env.ps1" -ForegroundColor Gray
        Exit-WithPause 0
    }
    "4" {
        Write-Host ""
        Write-Host "Running system check..." -ForegroundColor Cyan
        Write-Host ""
        python check_system.py
        Exit-WithPause $LASTEXITCODE
    }
    "0" {
        Write-Host ""
        Write-Host "Goodbye." -ForegroundColor Cyan
        Exit-WithPause 0
    }
    default {
        Write-Host "Invalid option." -ForegroundColor Yellow
        Exit-WithPause 1
    }
}
