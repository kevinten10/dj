#!/usr/bin/env python3
"""
系统配置检查脚本
检查本机是否适合部署本地 AI 音乐生成模型
"""

import sys
import subprocess
import os
import importlib.util
from pathlib import Path
from typing import Callable, Sequence


REPO_ROOT = Path(__file__).resolve().parent
MUSICGEN_VENV_DIR = ".venv-musicgen"


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

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
        if importlib.util.find_spec(module):
            installed.append(name)
        else:
            missing.append(name)
    
    if installed:
        print(f"✅ 已安装: {', '.join(installed)}")
    if missing:
        print(f"⚠️  未安装: {', '.join(missing)}")
    
    return len(missing) == 0, missing


def _musicgen_venv_python(repo_root: Path = REPO_ROOT) -> Path:
    if os.name == "nt":
        return repo_root / MUSICGEN_VENV_DIR / "Scripts" / "python.exe"
    return repo_root / MUSICGEN_VENV_DIR / "bin" / "python"


def _default_musicgen_python_candidates() -> list[list[str]]:
    if os.name == "nt":
        return [["py", "-3.11"], ["py", "-3.10"], ["python"]]
    return [["python3.11"], ["python3.10"], ["python3"]]


def _probe_python_candidate(
    candidate: Sequence[str],
    runner: Callable[..., subprocess.CompletedProcess] = subprocess.run,
) -> tuple[str, str] | None:
    try:
        result = runner(
            [
                *candidate,
                "-c",
                "import sys; print(f'{sys.executable}|{sys.version_info.major}.{sys.version_info.minor}')",
            ],
            capture_output=True,
            text=True,
            timeout=10,
        )
    except (OSError, subprocess.SubprocessError):
        return None

    if result.returncode != 0:
        return None

    parts = result.stdout.strip().split("|")
    if len(parts) != 2:
        return None
    return parts[0], parts[1]


def get_musicgen_environment_status(
    repo_root: Path = REPO_ROOT,
    candidates: Sequence[Sequence[str]] | None = None,
    runner: Callable[..., subprocess.CompletedProcess] = subprocess.run,
) -> tuple[bool, list[str]]:
    messages = []
    venv_python = _musicgen_venv_python(repo_root)

    if venv_python.exists():
        try:
            result = runner(
                [
                    str(venv_python),
                    "-c",
                    (
                        "import importlib.util, sys; "
                        "missing=[m for m in ('torch','audiocraft') if importlib.util.find_spec(m) is None]; "
                        "print(f'{sys.version_info.major}.{sys.version_info.minor}|{','.join(missing)}')"
                    ),
                ],
                capture_output=True,
                text=True,
                timeout=20,
            )
        except (OSError, subprocess.SubprocessError) as exc:
            return False, [f"{MUSICGEN_VENV_DIR} exists, but its Python could not run: {exc}"]

        if result.returncode != 0:
            return False, [f"{MUSICGEN_VENV_DIR} Python failed: {result.stderr.strip()}"]

        version_text, _, missing_text = result.stdout.strip().partition("|")
        if version_text not in {"3.10", "3.11"}:
            messages.append(f"{MUSICGEN_VENV_DIR} uses Python {version_text}; expected Python 3.10 or 3.11.")

        missing = [item for item in missing_text.split(",") if item]
        if missing:
            messages.append(f"{MUSICGEN_VENV_DIR} is missing: {', '.join(missing)}.")

        if messages:
            messages.append("Run: .\\setup_local_models.ps1")
            return False, messages

        return True, [f"{MUSICGEN_VENV_DIR} is ready for MusicGen/AudioCraft."]

    candidate_commands = candidates if candidates is not None else _default_musicgen_python_candidates()
    compatible = []
    incompatible = []
    for candidate in candidate_commands:
        probe = _probe_python_candidate(candidate, runner=runner)
        if probe is None:
            continue
        executable, version_text = probe
        label = " ".join(candidate)
        if version_text in {"3.10", "3.11"}:
            compatible.append(f"{label} -> {executable} (Python {version_text})")
        else:
            incompatible.append(f"{label} is Python {version_text}")

    if compatible:
        return False, [
            f"{MUSICGEN_VENV_DIR} is missing.",
            f"Compatible runtime found: {compatible[0]}.",
            "Run: .\\setup_local_models.ps1",
        ]

    messages.append(f"{MUSICGEN_VENV_DIR} is missing.")
    messages.append("No Python 3.10 or 3.11 runtime was found for AudioCraft/MusicGen.")
    if incompatible:
        messages.append("Detected incompatible runtimes: " + "; ".join(incompatible) + ".")
    messages.append("Install Python 3.11, then run: .\\setup_local_models.ps1")
    return False, messages


def get_minimax_config_status(environ=os.environ):
    api_key = environ.get("MINIMAX_API_KEY", "").strip()
    if not api_key:
        return False, "MINIMAX_API_KEY is not set."
    if api_key == "PASTE_YOUR_MINIMAX_API_KEY_HERE":
        return False, "MINIMAX_API_KEY is still the placeholder value."
    return True, "MINIMAX_API_KEY is configured."


def check_minimax_config():
    ready, message = get_minimax_config_status(os.environ)
    if ready:
        print(f"✅ {message}")
        print(f"   API base: {os.environ.get('MINIMAX_API_BASE', 'https://api.minimax.io')}")
    else:
        print(f"⚠️  {message}")
        print("   配置示例:")
        print("     cp 13_tools/configs/minimax_env.example.ps1 13_tools/configs/minimax_env.ps1")
        print("     notepad 13_tools/configs/minimax_env.ps1")
        print("     . .\\13_tools\\configs\\minimax_env.ps1")
    return ready


def get_ace_step_status(repo_root: Path = REPO_ROOT):
    issues = []
    ace_step_path = repo_root / "13_tools" / "ace_step"
    if not ace_step_path.exists():
        issues.append("13_tools/ace_step local clone is missing.")
        return False, issues

    if str(ace_step_path) not in sys.path:
        sys.path.insert(0, str(ace_step_path))

    for module_name in ("acestep", "torch", "soundfile"):
        if importlib.util.find_spec(module_name) is None:
            issues.append(f"Python module '{module_name}' is missing.")

    return len(issues) == 0, issues


def check_ace_step_readiness():
    ready, issues = get_ace_step_status(REPO_ROOT)
    if ready:
        print("✅ ACE-Step clone and runtime dependencies are available.")
        print("   Smoke test:")
        print("     python 13_tools/scripts/make_dj_track_ace_step.py --check")
    else:
        print("⚠️  ACE-Step is not ready:")
        for issue in issues:
            print(f"   - {issue}")
        print("   安装/检查:")
        print("     git clone https://github.com/ace-step/ACE-Step.git 13_tools/ace_step")
        print("     python -m pip install soundfile")
        print("     python 13_tools/scripts/make_dj_track_ace_step.py --check")
    return ready


def check_musicgen_readiness():
    ready, messages = get_musicgen_environment_status(REPO_ROOT)
    if ready:
        print(f"OK: {messages[0]}")
        print("   Smoke test:")
        print("     .\\.venv-musicgen\\Scripts\\python.exe 13_tools/scripts/make_dj_track_local.py --idea \"test\" --duration 5")
    else:
        print("WARN: MusicGen/AudioCraft local environment is not ready:")
        for message in messages:
            print(f"   - {message}")
    return ready


def print_audiocraft_install_hint():
    if sys.version_info >= (3, 12):
        print("  AudioCraft/MusicGen note:")
        print("    AudioCraft 1.3.0 pins torch==2.1.0, which is not available for Python 3.12.")
        print("    Use a separate Python 3.10 or 3.11 virtual environment for MusicGen.")
        print("    Example:")
        print("      py -3.11 -m venv .venv-musicgen")
        print("      .\\.venv-musicgen\\Scripts\\activate")
        print("      python -m pip install --upgrade pip")
        print("      python -m pip install torch torchvision torchaudio audiocraft")
    else:
        print("  python -m pip install torch torchvision torchaudio audiocraft")


def recommend_model(has_cuda, vram_gb, has_deps):
    """推荐合适的模型"""
    print("\n" + "="*60)
    print("🎯 模型推荐")
    print("="*60)
    
    if not has_deps:
        print("\n请先安装依赖:")
        print_audiocraft_install_hint()
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

    print("☁️  MiniMax 云端 API")
    print("-" * 40)
    check_minimax_config()
    print()

    print("🎤 ACE-Step 本地歌词模型")
    print("-" * 40)
    check_ace_step_readiness()
    print()

    print("MusicGen local instrumental model")
    print("-" * 40)
    check_musicgen_readiness()
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
        print_audiocraft_install_hint()
        print("\n3. 验证安装:")
        print("   python -c \"import torch; print('PyTorch:', torch.__version__); print('CUDA:', torch.cuda.is_available())\"")
    
    print("\n" + "="*60)
    print("✨ 检查完成!")
    print("="*60)
    
    return all(checks)

if __name__ == "__main__":
    main()
