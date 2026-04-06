#!/usr/bin/env powershell
# 一键部署本地 AI 音乐生成模型
# 自动检测环境并安装所需依赖

$ErrorActionPreference = "Stop"

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  🎵 AI DJ 本地模型一键部署工具" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# 检查 Python
Write-Host "📋 检查 Python 环境..." -ForegroundColor Yellow
$pythonVersion = python --version 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ 未找到 Python！请先安装 Python 3.9+" -ForegroundColor Red
    Write-Host "   下载地址: https://www.python.org/downloads/" -ForegroundColor Gray
    exit 1
}
Write-Host "✅ $pythonVersion" -ForegroundColor Green

# 检查 pip
Write-Host "📦 检查 pip..." -ForegroundColor Yellow
$pipVersion = python -m pip --version 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ pip 未安装！" -ForegroundColor Red
    exit 1
}
Write-Host "✅ pip 已安装" -ForegroundColor Green

# 升级 pip
Write-Host "⬆️  升级 pip..." -ForegroundColor Yellow
python -m pip install --upgrade pip | Out-Null
Write-Host "✅ pip 已升级" -ForegroundColor Green
Write-Host ""

# 检测 CUDA
Write-Host "🎮 检测 GPU/CUDA..." -ForegroundColor Yellow
try {
    $nvidiaOutput = nvidia-smi 2>&1
    if ($LASTEXITCODE -eq 0) {
        Write-Host "✅ 检测到 NVIDIA GPU" -ForegroundColor Green
        $cudaVersion = ($nvidiaOutput | Select-String "CUDA Version:").ToString()
        Write-Host "   $cudaVersion" -ForegroundColor Gray
        $hasGPU = $true
    } else {
        Write-Host "⚠️  未检测到 NVIDIA GPU，将使用 CPU" -ForegroundColor Yellow
        $hasGPU = $false
    }
} catch {
    Write-Host "⚠️  未检测到 NVIDIA GPU，将使用 CPU" -ForegroundColor Yellow
    $hasGPU = $false
}
Write-Host ""

# 安装 PyTorch
Write-Host "🔥 安装 PyTorch..." -ForegroundColor Yellow
if ($hasGPU) {
    Write-Host "   安装 CUDA 版本..." -ForegroundColor Gray
    python -m pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
} else {
    Write-Host "   安装 CPU 版本..." -ForegroundColor Gray
    python -m pip install torch torchvision torchaudio
}
if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ PyTorch 安装失败！" -ForegroundColor Red
    exit 1
}
Write-Host "✅ PyTorch 安装完成" -ForegroundColor Green
Write-Host ""

# 验证 PyTorch
Write-Host "🔍 验证 PyTorch 安装..." -ForegroundColor Yellow
python -c "import torch; print(f'PyTorch: {torch.__version__}'); print(f'CUDA可用: {torch.cuda.is_available()}')" | ForEach-Object {
    Write-Host "   $_" -ForegroundColor Gray
}
Write-Host ""

# 安装 AudioCraft
Write-Host "🎵 安装 AudioCraft..." -ForegroundColor Yellow
python -m pip install audiocraft
if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ AudioCraft 安装失败！" -ForegroundColor Red
    exit 1
}
Write-Host "✅ AudioCraft 安装完成" -ForegroundColor Green
Write-Host ""

# 安装额外依赖
Write-Host "📚 安装额外依赖..." -ForegroundColor Yellow
python -m pip install transformers accelerate psutil
Write-Host "✅ 额外依赖安装完成" -ForegroundColor Green
Write-Host ""

# 预下载模型
Write-Host "📥 预下载 MusicGen Small 模型..." -ForegroundColor Yellow
Write-Host "   （约 1GB，请耐心等待）" -ForegroundColor Gray
python -c "
from audiocraft.models import MusicGen
print('正在下载模型...')
model = MusicGen.get_pretrained('facebook/musicgen-small')
print('模型下载完成！')
"
if ($LASTEXITCODE -ne 0) {
    Write-Host "⚠️  模型下载失败，将在首次使用时自动下载" -ForegroundColor Yellow
} else {
    Write-Host "✅ 模型下载完成" -ForegroundColor Green
}
Write-Host ""

# 测试生成
Write-Host "🧪 测试生成..." -ForegroundColor Yellow
Write-Host "   生成 5 秒测试音频..." -ForegroundColor Gray
python 13_tools/scripts/make_dj_track_local.py --idea "test" --duration 5 --model facebook/musicgen-small 2>&1 | Out-Null
if ($LASTEXITCODE -eq 0) {
    Write-Host "✅ 测试生成成功！" -ForegroundColor Green
} else {
    Write-Host "⚠️  测试生成失败，但安装已完成" -ForegroundColor Yellow
}
Write-Host ""

# 完成
Write-Host "========================================" -ForegroundColor Green
Write-Host "  🎉 部署完成！" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host ""
Write-Host "💡 使用方法:" -ForegroundColor Cyan
Write-Host "   1. 一句话生成:" -ForegroundColor White
Write-Host "      python generate_demo_local.py" -ForegroundColor Gray
Write-Host ""
Write-Host "   2. 使用本地模型脚本:" -ForegroundColor White
Write-Host "      python 13_tools/scripts/make_dj_track_local.py --idea '你的想法' --cuda" -ForegroundColor Gray
Write-Host ""
Write-Host "   3. 启动交互式菜单:" -ForegroundColor White
Write-Host "      .\start.ps1" -ForegroundColor Gray
Write-Host ""
Write-Host "📖 查看详细指南:" -ForegroundColor Cyan
Write-Host "   LOCAL_DEPLOYMENT_GUIDE.md" -ForegroundColor Gray
Write-Host ""
