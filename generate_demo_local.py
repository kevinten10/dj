#!/usr/bin/env python3
"""
使用本地模型生成 Demo 音乐
无需 API Key，完全离线生成！
"""

import sys
import subprocess
import os
import platform
from pathlib import Path

def get_repo_root():
    return Path(__file__).parent.resolve()

def play_audio(file_path):
    """播放音频文件"""
    system = platform.system().lower()
    try:
        if system.startswith("windows"):
            os.startfile(str(file_path))
        elif system == "darwin":
            subprocess.run(["open", str(file_path)], check=False)
        else:
            subprocess.run(["xdg-open", str(file_path)], check=False)
        return True
    except Exception as e:
        print(f"❌ 播放失败: {e}")
        return False

def main():
    print("=" * 60)
    print("🎧 AI DJ Demo 生成器（本地模型版）")
    print("=" * 60)
    print()
    
    repo_root = get_repo_root()
    
    # 使用本地模型生成
    print("🎵 正在生成 Demo 音乐...")
    print("   风格: Tech House")
    print("   BPM: 124")
    print("   时长: 30秒（快速生成）")
    print()
    print("⏳ 首次运行需要下载模型（约1GB），请耐心等待...")
    print()
    
    cmd = [
        sys.executable,
        str(repo_root / "13_tools" / "scripts" / "make_dj_track_local.py"),
        "--idea", "AI DJ Demo, clear kick drum, tech house groove, DJ practice track",
        "--style", "Tech House",
        "--bpm", "124",
        "--duration", "30",
        "--model", "facebook/musicgen-small"
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, cwd=repo_root)
        
        if result.returncode != 0:
            print(f"❌ 生成失败: {result.stderr}")
            print()
            print("💡 可能的原因：")
            print("   1. 未安装本地模型依赖（audiocraft, torch）")
            print("   2. 内存不足")
            print()
            print("🔧 解决方法：")
            print("   pip install torch audiocraft")
            return 1
        
        # 查找生成的文件
        exports_dir = repo_root / "08_exports" / "dj_ready"
        
        if exports_dir.exists():
            files = sorted(exports_dir.glob("*.wav"), key=lambda x: x.stat().st_mtime, reverse=True)
            if files:
                music_file = files[0]
                print()
                print(f"✅ Demo 生成成功！")
                print(f"📁 文件位置: {music_file}")
                print()
                print("🎶 正在播放...")
                
                if play_audio(music_file):
                    print()
                    print("🎉 享受你的 Demo 音乐吧！")
                    print()
                    print("💡 提示：")
                    print("   • 这是使用本地 AI 模型生成的")
                    print("   • 无需 API Key，完全免费")
                    print("   • 文件保存在: 08_exports/dj_ready/")
                    print("   • 可以拖入 DJUCED 软件练习混音")
                else:
                    print(f"📂 请手动打开文件: {music_file}")
                
                return 0
        
        print("❌ 找不到生成的文件")
        return 1
        
    except Exception as e:
        print(f"❌ 错误: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main())
