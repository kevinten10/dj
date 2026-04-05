# AI-DJ 启动脚本
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  🎧 AI-DJ 工作区启动器" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# 检查Python
try {
    $pythonPath = Get-Command python -ErrorAction Stop
    Write-Host "✅ Python 已找到: $($pythonPath.Source)" -ForegroundColor Green
}
catch {
    Write-Host "❌ 未找到 Python！请先安装 Python 3.9+" -ForegroundColor Red
    Read-Host "按 Enter 退出"
    exit 1
}

# 切换到脚本目录
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $scriptDir

Write-Host ""
Write-Host "请选择操作:" -ForegroundColor Yellow
Write-Host "1. 🎨 启动交互式生成器（推荐）" -ForegroundColor White
Write-Host "2. 📖 查看文档" -ForegroundColor White
Write-Host "3. ⚙️  配置 MiniMax API" -ForegroundColor White
Write-Host "0. 退出" -ForegroundColor White
Write-Host ""

$choice = Read-Host "请输入选项 (默认: 1)"
if ([string]::IsNullOrWhiteSpace($choice)) { $choice = "1" }

switch ($choice) {
    "1" {
        Write-Host ""
        Write-Host "🚀 启动交互式生成器..." -ForegroundColor Cyan
        Write-Host ""
        python 13_tools/scripts/interactive_generator.py
    }
    "2" {
        Write-Host ""
        Write-Host "📖 可用文档:" -ForegroundColor Yellow
        Write-Host "1. DJ 学习路径" -ForegroundColor White
        Write-Host "2. DJ 技巧库" -ForegroundColor White
        Write-Host "3. 本地模型使用指南" -ForegroundColor White
        Write-Host "4. AI-DJ 教程" -ForegroundColor White
        $docChoice = Read-Host "选择文档 (1-4, 默认: 1)"
        if ([string]::IsNullOrWhiteSpace($docChoice)) { $docChoice = "1" }
        
        $docMap = @{
            "1" = "12_docs/learning_path.md"
            "2" = "12_docs/techniques_library.md"
            "3" = "12_docs/local_models.md"
            "4" = "12_docs/ai_djuced_tutorial.md"
        }
        
        if ($docMap.ContainsKey($docChoice)) {
            Write-Host "📖 打开文档..." -ForegroundColor Cyan
            Start-Process $docMap[$docChoice]
        }
        else {
            Write-Host "⚠️  无效选项" -ForegroundColor Yellow
        }
    }
    "3" {
        Write-Host ""
        Write-Host "⚙️  配置 MiniMax API" -ForegroundColor Yellow
        $envFile = "13_tools/configs/minimax_env.ps1"
        $exampleFile = "13_tools/configs/minimax_env.example.ps1"
        
        if (-not (Test-Path $envFile)) {
            if (Test-Path $exampleFile) {
                Copy-Item $exampleFile $envFile
                Write-Host "✅ 已创建配置文件: $envFile" -ForegroundColor Green
            }
            else {
                Write-Host "❌ 找不到示例配置文件!" -ForegroundColor Red
            }
        }
        
        if (Test-Path $envFile) {
            Write-Host "📝 打开配置文件..." -ForegroundColor Cyan
            Start-Process notepad $envFile
            Write-Host ""
            Write-Host "💡 编辑完成后，运行: . .\13_tools\configs\minimax_env.ps1" -ForegroundColor Gray
        }
    }
    "0" {
        Write-Host ""
        Write-Host "👋 再见！" -ForegroundColor Cyan
    }
    default {
        Write-Host "⚠️  无效选项" -ForegroundColor Yellow
    }
}

Write-Host ""
Read-Host "按 Enter 退出"
