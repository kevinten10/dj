#!/usr/bin/env python3
"""
一句话生成DJ音乐并自动播放
最简单的使用方式：直接运行，输入你的想法，音乐自动生成并播放！
"""

import sys
import subprocess
import os
import platform
from pathlib import Path

# 配置默认参数
DEFAULT_STYLE = "House"
DEFAULT_BPM = 120
DEFAULT_DURATION = 90  # 秒

def get_repo_root():
    """获取仓库根目录"""
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

def generate_music(idea, style=DEFAULT_STYLE, bpm=DEFAULT_BPM, duration=DEFAULT_DURATION):
    """
    生成音乐
    
    参数:
        idea: 你的想法/描述
        style: 音乐风格 (默认: House)
        bpm: 速度 (默认: 120)
        duration: 时长秒数 (默认: 90)
    """
    repo_root = get_repo_root()
    
    # 构建命令（注意：make_dj_track_minimax.py 不支持 --duration 参数）
    cmd = [
        sys.executable,
        str(repo_root / "13_tools" / "scripts" / "make_dj_track_minimax.py"),
        "--idea", idea,
        "--style", style,
        "--bpm", str(bpm),
        "--instrumental",
        "--play"
    ]
    
    print(f"🎵 正在生成音乐...")
    print(f"   想法: {idea}")
    print(f"   风格: {style} | BPM: {bpm} | 时长: {duration}秒")
    print()
    
    try:
        # 运行生成命令
        result = subprocess.run(cmd, capture_output=True, text=True, cwd=repo_root)
        
        if result.returncode != 0:
            print(f"❌ 生成失败: {result.stderr}")
            return None
        
        # 从输出中提取文件路径
        output = result.stdout
        
        # 查找生成的文件（通常在 08_exports/dj_ready/）
        exports_dir = repo_root / "08_exports" / "dj_ready"
        
        if exports_dir.exists():
            # 获取最新的文件
            files = sorted(exports_dir.glob("*.mp3"), key=lambda x: x.stat().st_mtime, reverse=True)
            if files:
                return files[0]
        
        return None
        
    except Exception as e:
        print(f"❌ 错误: {e}")
        return None

def main():
    """主函数"""
    print("=" * 60)
    print("🎧 一句话生成DJ音乐")
    print("=" * 60)
    print()
    
    # 获取用户输入
    if len(sys.argv) > 1:
        # 从命令行参数获取
        idea = " ".join(sys.argv[1:])
    else:
        # 交互式输入
        print("💡 请输入你的想法（描述你想要的音乐）：")
        print("   例如: 午夜派对氛围，有强烈的底鼓")
        print("   例如: 轻松的海滩日落感觉")
        print("   例如: 高能健身房训练音乐")
        print()
        idea = input("你的想法: ").strip()
    
    if not idea:
        print("❌ 请输入你的想法！")
        return 1
    
    # 智能分析用户输入，提取风格
    idea_lower = idea.lower()
    style = DEFAULT_STYLE
    bpm = DEFAULT_BPM
    
    # 根据关键词自动选择风格
    if any(word in idea_lower for word in ["techno", "工业", "黑暗"]):
        style = "Techno"
        bpm = 130
    elif any(word in idea_lower for word in ["trance", "史诗", "情感"]):
        style = "Trance"
        bpm = 138
    elif any(word in idea_lower for word in ["deep", "放松", "温暖"]):
        style = "Deep House"
        bpm = 122
    elif any(word in idea_lower for word in ["tech", "机械", "派对"]):
        style = "Tech House"
        bpm = 126
    elif any(word in idea_lower for word in ["drum", "bass", "dnb"]):
        style = "Drum & Bass"
        bpm = 174
    
    # 如果用户指定了BPM，提取它
    import re
    bpm_match = re.search(r'(\d+)\s*bpm', idea_lower)
    if bpm_match:
        bpm = int(bpm_match.group(1))
    
    # 生成音乐
    print()
    music_file = generate_music(idea, style, bpm)
    
    if music_file and music_file.exists():
        print()
        print(f"✅ 音乐生成成功！")
        print(f"📁 文件位置: {music_file}")
        print()
        print("🎶 正在播放...")
        
        # 播放音乐
        if play_audio(music_file):
            print()
            print("🎉 享受你的音乐吧！")
            print()
            print("💡 提示：")
            print("   • 音乐文件保存在: 08_exports/dj_ready/")
            print("   • 你可以直接拖入 DJUCED 软件进行混音")
            print("   • 使用 start.ps1 可以启动完整功能菜单")
        else:
            print()
            print(f"📂 请手动打开文件: {music_file}")
        
        return 0
    else:
        print()
        print("❌ 音乐生成失败，请检查:")
        print("   1. 是否配置了 MiniMax API Key")
        print("   2. 网络连接是否正常")
        print("   3. 查看 13_tools/configs/minimax_env.ps1 配置")
        return 1

if __name__ == "__main__":
    sys.exit(main())
