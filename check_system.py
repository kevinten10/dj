#!/usr/bin/env python3
"""
系统配置检查脚本
检查本机是否适合部署本地 AI 音乐生成模型
"""

import sys
import subprocess
import os
from pathlib import Path

def check_python_version():
    """检查 Python 版本"""
    version = sys.version_info
    print(f"✅ Python 版本: {version.major}.{version.minor}.{version.micro}")
    
    if version.major < 3 or (version.major == 3 and version.minor < 9):
        print("❌ Python 版本过低，需要 3.9+")
        return False
    return True

def check_pip():
    """检查 pip 是否可用"""
    try:
        result = subprocess.run([sys.executable, "-m", "pip", "--version"], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ Pip: {result.stdout.strip()}")
            return True
    except:
        pass
    print("❌ Pip 不可用")
    return False

def check_disk_space():
    """检查磁盘空间"""
    try:
        import shutil
        total, used, free = shutil.disk_usage("/")
        free_gb = free // (2**30)
        print(f"✅ 磁盘剩余空间: {free_gb} GB")
        
        if free_gb < 10:
            print("⚠️  磁盘空间不足，建议至少 10GB")
            return False
        return True
    except:
        print("⚠️  无法检查磁盘空间")
        return True

def check_memory():
    """检查内存"""
    try:
        import psutil
        mem = psutil.virtual_memory()
        total_gb = mem.total // (2**30)
        available_gb = mem.available // (2**30)
        print(f"✅ 内存: {total_gb} GB (可用: {available_gb} GB)")
        
        if total_gb < 8:
            print("⚠️  内存较小，建议使用 Small 模型")
        return True
    except ImportError:
        print("⚠️  未安装 psutil，无法检查内存")
        print("   建议: pip install psutil")
        return True

def check_cuda():
    """检查 CUDA 支持"""
    try:
        import torch
        if torch.cuda.is_available():
            device_name = torch.cuda.get_device_name(0)
            memory_gb = torch.cuda.get_device_properties(0).total_memory / (2**30)
            print(f"✅ CUDA 可用: {device_name}")
            print(f"   显存: {memory_gb:.1f} GB")
            return True, memory_gb
        else:
            print("⚠️  CUDA 不可用，将使用 CPU 运行（较慢）")
            return False, 0
    except ImportError:
        print("⚠️  PyTorch 未安装")
        return False, 0

def check_dependencies():
    """检查关键依赖"""
    deps = {
        "torch": "PyTorch",
        "audiocraft": "AudioCraft",
        "transformers": "Transformers"
    }
    
    installed = []
    missing = []
    
    for module, name in deps.items():
        try:
            __import__(module)
            installed.append(name)
        except ImportError:
            missing.append(name)
    
    if installed:
        print(f"✅ 已安装: {', '.join(installed)}")
    if missing:
        print(f"⚠️  未安装: {', '.join(missing)}")
    
    return len(missing) == 0, missing

def recommend_model(has_cuda, vram_gb, has_deps):
    """推荐合适的模型"""
    print("\n" + "="*60)
    print("🎯 模型推荐")
    print("="*60)
    
    if not has_deps:
        print("\n请先安装依赖:")
        print("  pip install torch audiocraft")
        return
    
    if has_cuda:
        if vram_gb >= 12:
            print("\n✅ 你的配置很好！推荐使用:")
            print("  • MusicGen Large (3.3B) - 最佳音质")
            print("  • MAGNeT - 更快生成")
            print("\n命令示例:")
            print('  python 13_tools/scripts/make_dj_track_local.py --idea "你的想法" --model facebook/musicgen-large --cuda')
        elif vram_gb >= 6:
            print("\n✅ 你的配置不错！推荐使用:")
            print("  • MusicGen Medium (1.5B) - 平衡选择")
            print("  • MusicGen Melody (3.3B) - 支持旋律条件")
            print("\n命令示例:")
            print('  python 13_tools/scripts/make_dj_track_local.py --idea "你的想法" --model facebook/musicgen-medium --cuda')
        else:
            print("\n⚠️  显存较小，推荐使用:")
            print("  • MusicGen Small (300M) - 快速测试")
            print("\n命令示例:")
            print('  python 13_tools/scripts/make_dj_track_local.py --idea "你的想法" --model facebook/musicgen-small --cuda')
    else:
        print("\n⚠️  无 GPU，将使用 CPU 运行（较慢）")
        print("  • MusicGen Small (300M) - CPU 可用")
        print("\n命令示例:")
        print('  python 13_tools/scripts/make_dj_track_local.py --idea "你的想法" --model facebook/musicgen-small')
        print("\n💡 提示: CPU 生成较慢，建议先试用 Small 模型")

def main():
    print("="*60)
    print("🖥️  系统配置检查")
    print("="*60)
    print()
    
    # 检查各项配置
    checks = []
    
    print("📋 Python 环境")
    print("-" * 40)
    checks.append(check_python_version())
    checks.append(check_pip())
    print()
    
    print("💾 硬件资源")
    print("-" * 40)
    check_disk_space()
    check_memory()
    print()
    
    print("🎮 GPU 支持")
    print("-" * 40)
    has_cuda, vram_gb = check_cuda()
    print()
    
    print("📦 依赖检查")
    print("-" * 40)
    has_deps, missing = check_dependencies()
    print()
    
    # 推荐模型
    recommend_model(has_cuda, vram_gb, has_deps)
    
    # 安装指南
    if not has_deps:
        print("\n" + "="*60)
        print("🔧 安装指南")
        print("="*60)
        print("\n1. 安装 PyTorch (根据你的 CUDA 版本选择):")
        print("   # CUDA 12.1:")
        print("   pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121")
        print("   # CPU 版本:")
        print("   pip install torch torchvision torchaudio")
        print("\n2. 安装 AudioCraft:")
        print("   pip install audiocraft")
        print("\n3. 验证安装:")
        print("   python -c \"import torch; print('PyTorch:', torch.__version__); print('CUDA:', torch.cuda.is_available())\"")
    
    print("\n" + "="*60)
    print("✨ 检查完成!")
    print("="*60)
    
    return all(checks)

if __name__ == "__main__":
    main()
