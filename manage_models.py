#!/usr/bin/env python3
"""
本地AI模型管理工具
管理、切换、删除本地音乐生成模型
"""

import sys
import argparse
import subprocess
import os
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

MODELS = {
    "1": {"name": "MusicGen Small", "id": "facebook/musicgen-small", "size": "~1GB", "quality": "⭐⭐⭐", "speed": "⚡⚡⚡", "vram": "4GB"},
    "2": {"name": "MusicGen Medium", "id": "facebook/musicgen-medium", "size": "~3GB", "quality": "⭐⭐⭐⭐", "speed": "⚡⚡", "vram": "8GB"},
    "3": {"name": "MusicGen Large", "id": "facebook/musicgen-large", "size": "~6GB", "quality": "⭐⭐⭐⭐⭐", "speed": "⚡", "vram": "12GB+"},
    "4": {"name": "MusicGen Melody", "id": "facebook/musicgen-melody", "size": "~6GB", "quality": "⭐⭐⭐⭐⭐", "speed": "⚡", "vram": "12GB+"},
}

REPO_ROOT = Path(__file__).resolve().parent
MUSICGEN_VENV_DIR = ".venv-musicgen"


def musicgen_venv_python(repo_root: Path = REPO_ROOT) -> Path:
    if os.name == "nt":
        return repo_root / MUSICGEN_VENV_DIR / "Scripts" / "python.exe"
    return repo_root / MUSICGEN_VENV_DIR / "bin" / "python"


def python_has_audiocraft(python_executable: str | Path = sys.executable) -> bool:
    try:
        result = subprocess.run(
            [
                str(python_executable),
                "-c",
                "import importlib.util; raise SystemExit(0 if importlib.util.find_spec('audiocraft') else 1)",
            ],
            capture_output=True,
            text=True,
            timeout=20,
        )
    except (OSError, subprocess.SubprocessError):
        return False
    return result.returncode == 0


def get_musicgen_python(repo_root: Path = REPO_ROOT) -> str | None:
    venv_python = musicgen_venv_python(repo_root)
    if venv_python.exists():
        return str(venv_python)
    if python_has_audiocraft(sys.executable):
        return sys.executable
    return None


def print_musicgen_setup_hint():
    print("MusicGen/AudioCraft environment is not ready.")
    print("Run:")
    print("  .\\setup_local_models.ps1")
    print("Then retry this command.")

def print_header():
    print("=" * 60)
    print("🎵 AI DJ 本地模型管理工具")
    print("=" * 60)
    print()

def list_models():
    """列出所有可用模型"""
    print("📋 可用模型列表:")
    print()
    print(f"{'ID':<4} {'名称':<20} {'大小':<8} {'音质':<8} {'速度':<8} {'显存需求':<10}")
    print("-" * 60)
    for key, model in MODELS.items():
        print(f"{key:<4} {model['name']:<20} {model['size']:<8} {model['quality']:<8} {model['speed']:<8} {model['vram']:<10}")
    print()

def download_model(model_id):
    """下载指定模型"""
    print(f"📥 正在下载模型: {model_id}")
    print("   这可能需要几分钟，请耐心等待...")
    print()
    
    try:
        from audiocraft.models import MusicGen
        model = MusicGen.get_pretrained(model_id)
        print(f"✅ 模型下载完成: {model_id}")
        return True
    except Exception as e:
        print(f"❌ 下载失败: {e}")
        return False

def test_model(model_id):
    """测试模型生成"""
    print(f"🧪 测试模型: {model_id}")
    print("   生成 5 秒测试音频...")
    
    repo_root = Path(__file__).parent.resolve()
    cmd = [
        sys.executable,
        str(repo_root / "13_tools" / "scripts" / "make_dj_track_local.py"),
        "--idea", "test audio",
        "--duration", "5",
        "--model", model_id
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
        if result.returncode == 0:
            print("✅ 测试成功！")
            return True
        else:
            print(f"❌ 测试失败: {result.stderr}")
            return False
    except Exception as e:
        print(f"❌ 错误: {e}")
        return False

def get_model_cache_size():
    """获取模型缓存大小"""
    import os
    cache_dir = Path.home() / ".cache" / "huggingface" / "hub"
    
    if not cache_dir.exists():
        return 0
    
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(cache_dir):
        for f in filenames:
            fp = Path(dirpath) / f
            total_size += fp.stat().st_size
    
    return total_size / (1024**3)  # Convert to GB


def download_model(model_id):
    """Download a MusicGen model with the configured MusicGen Python."""
    print(f"Downloading model: {model_id}")
    print("This may take a few minutes.")
    print()

    python_executable = get_musicgen_python()
    if python_executable is None:
        print_musicgen_setup_hint()
        return False

    try:
        result = subprocess.run(
            [
                python_executable,
                "-c",
                (
                    "import sys; "
                    "from audiocraft.models import MusicGen; "
                    "MusicGen.get_pretrained(sys.argv[1]); "
                    "print('Model ready.')"
                ),
                model_id,
            ],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            cwd=REPO_ROOT,
            timeout=60 * 60,
        )
        if result.stdout:
            print(result.stdout.strip())
        if result.returncode != 0:
            print(f"Download failed: {result.stderr.strip()}")
            return False
        print(f"Model downloaded: {model_id}")
        return True
    except Exception as e:
        print(f"Download failed: {e}")
        return False


def test_model(model_id):
    """Run a short MusicGen generation smoke test."""
    print(f"Testing model: {model_id}")

    python_executable = get_musicgen_python()
    if python_executable is None:
        print_musicgen_setup_hint()
        return False

    cmd = [
        python_executable,
        str(REPO_ROOT / "13_tools" / "scripts" / "make_dj_track_local.py"),
        "--idea",
        "test audio",
        "--duration",
        "5",
        "--model",
        model_id,
    ]

    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            cwd=REPO_ROOT,
        )
        if result.returncode == 0:
            print("Test succeeded.")
            return True
        print(f"Test failed: {result.stderr.strip()}")
        return False
    except Exception as e:
        print(f"Test failed: {e}")
        return False


def main(argv=None):
    parser = argparse.ArgumentParser(description="AI DJ 本地模型管理工具")
    parser.add_argument("--list", action="store_true", help="列出可用模型后退出")
    parser.add_argument("--cache-size", action="store_true", help="显示 Hugging Face 模型缓存大小后退出")
    parser.add_argument("--status", action="store_true", help="Check MusicGen/AudioCraft environment")
    args = parser.parse_args(argv)

    print_header()

    if args.list:
        list_models()
        return 0

    if args.cache_size:
        size = get_model_cache_size()
        print(f"💾 模型缓存大小: {size:.2f} GB")
        print("   缓存位置: ~/.cache/huggingface/hub/")
        return 0
    
    if args.status:
        python_executable = get_musicgen_python()
        if python_executable:
            print(f"MusicGen Python: {python_executable}")
            return 0
        print_musicgen_setup_hint()
        return 1

    try:
        while True:
            print("请选择操作:")
            print("1. 📋 查看可用模型")
            print("2. 📥 下载模型")
            print("3. 🧪 测试模型")
            print("4. 💾 查看缓存大小")
            print("0. 退出")
            print()

            choice = input("请输入选项: ").strip()

            if choice == "0":
                print("👋 再见！")
                return 0

            elif choice == "1":
                list_models()

            elif choice == "2":
                list_models()
                model_choice = input("请输入要下载的模型ID (1-4): ").strip()

                if model_choice in MODELS:
                    model_id = MODELS[model_choice]["id"]
                    if download_model(model_id):
                        test = input("是否测试生成? (y/n): ").strip().lower()
                        if test == "y":
                            test_model(model_id)
                else:
                    print("❌ 无效的选项")

            elif choice == "3":
                list_models()
                model_choice = input("请输入要测试的模型ID (1-4): ").strip()

                if model_choice in MODELS:
                    model_id = MODELS[model_choice]["id"]
                    test_model(model_id)
                else:
                    print("❌ 无效的选项")

            elif choice == "4":
                size = get_model_cache_size()
                print(f"💾 模型缓存大小: {size:.2f} GB")
                print("   缓存位置: ~/.cache/huggingface/hub/")
                print()

            else:
                print("❌ 无效的选项")

            input("\n按 Enter 继续...")
            print()
    except EOFError:
        print("\n未收到交互输入，已退出。可使用 --help 查看非交互命令。")
        return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
