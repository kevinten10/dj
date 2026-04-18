#!/usr/bin/env python3
"""
DJ 曲目生成器 - 支持歌词生成
使用 MiniMax 云端 API 生成带歌词的完整音乐
"""

from __future__ import annotations

import argparse
import datetime as _dt
import json
import logging
import os
import platform
import subprocess
import sys
from pathlib import Path
from typing import Any, Dict, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger("ai-dj-lyrics")


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def _now_stamp() -> str:
    return _dt.datetime.now().strftime("%Y%m%d_%H%M%S")


def _slugify(s: str, max_len: int = 48) -> str:
    import re
    slug_re = re.compile(r"[^a-zA-Z0-9\u4e00-\u9fff_-]+")
    s = s.strip().replace(" ", "_")
    s = slug_re.sub("_", s)
    s = s.strip("_-")
    if not s:
        return "track"
    return s[:max_len]


def _start_file(path: Path) -> None:
    system = platform.system().lower()
    try:
        if system.startswith("windows"):
            os.startfile(str(path))
        elif system == "darwin":
            subprocess.run(["open", str(path)], check=False)
        else:
            subprocess.run(["xdg-open", str(path)], check=False)
    except Exception as e:
        logger.warning(f"Failed to open file automatically: {e}")


def generate_lyrics(theme: str, style: str) -> str:
    """
    使用 AI 生成歌词
    这里使用简单的模板生成，如果需要更好的歌词，可以调用 GPT 或其他 LLM API
    """
    lyrics_templates = {
        "House": {
            "structure": "[Verse 1]\n{verse1}\n\n[Chorus]\n{chorus}\n\n[Verse 2]\n{verse2}\n\n[Chorus]\n{chorus}\n\n[Drop]\n{drop}\n\n[Bridge]\n{bridge}\n\n[Chorus]\n{chorus}\n\n[Outro]\n{outro}",
            "verses": [
                "Feel the rhythm in the air\nLights are flashing everywhere\nBodies moving to the beat\nDancing on the floor tonight",
                "Lost inside the melody\nDancing wild and feeling free\nNight is young and we're alive\nThis is where we come to thrive",
                "Heartbeat syncs with every bass\nTime and space begin to fade\nNothing else but you and me\nIn this moment we are free"
            ],
            "choruses": [
                "We are the night\nWe are the light\nDancing together\nForever tonight",
                "Move your body\nFeel the energy\nHouse music is calling\nThis is our story",
                "Let the rhythm guide you\nLet the music take control\nHouse is in our souls tonight\nThis is what we came for"
            ],
            "drops": [
                "Drop!\nFeel the bass\nDrop!\nMove your body\nDrop!\nLose control\nDrop!\nDance all night",
                "Hands up!\nFeel the energy!\nDrop the bass!\nLet it go!\nMove! Move! Move!",
                "Here we go!\n3, 2, 1, DROP!\nFeel it in your soul!\nLet the music take control!"
            ],
            "bridges": [
                "Close your eyes and feel\nThis is real\nNothing else matters now\nJust this moment, take a bow",
                "When the music stops\nWe'll still be here\nDancing in our hearts\nForever and always"
            ],
            "outros": [
                "As the night fades away\nWe'll remember this day\nHouse music will remain\nIn our hearts, again and again",
                "The music plays on\nInto the dawn\nUntil we meet again\nOn the dance floor, my friend"
            ]
        },
        "Techno": {
            "structure": "[Intro]\n{intro}\n\n[Verse]\n{verse}\n\n[Build]\n{build}\n\n[Drop]\n{drop}\n\n[Verse]\n{verse2}\n\n[Build]\n{build}\n\n[Drop]\n{drop}\n\n[Outro]\n{outro}",
            "intros": [
                "System online\nInitializing sequence\nPreparing for launch\n3... 2... 1...",
                "Enter the void\nDarkness surrounds\nBut the beat goes on\nInto the unknown"
            ],
            "verses": [
                "Industrial sounds in the warehouse tonight\nSteel and concrete, the rhythm takes flight\nMachines are humming, the bass is deep\nThis is techno, this is the beat",
                "Underground, we come alive\nIn the darkness, we will thrive\nPulsing bass and synthetic sounds\nThis is where the lost are found",
                "Circuit boards and flashing lights\nProgramming the perfect night\nCode and rhythm intertwine\nThis is the techno design"
            ],
            "builds": [
                "Feel it building\nHigher and higher\nCan't stop now\nWe're going higher\nBuild! Build! Build!",
                "The tension rises\nPressure mounting\nEnergy spiking\nHere it comes!",
                "Countdown initiated\nSystem overload\nBreaking point reached\nDROP!"
            ],
            "drops": [
                "TECHNO!\nDark and heavy\nTECHNO!\nFeel the power\nTECHNO!\nUnderground\nTECHNO!\nAll night long",
                "DROP THE BEAT!\nFeel the bass!\nThis is techno!\nNo retreat!\nMove! Move! Move!"
            ],
            "outros": [
                "System shutting down\nBut the music lives on\nIn our memories\nUntil the next dawn",
                "The warehouse empties\nBut the rhythm stays\nTechno forever\nIn our DNA"
            ]
        },
        "Trance": {
            "structure": "[Intro]\n{intro}\n\n[Verse 1]\n{verse1}\n\n[Build]\n{build}\n\n[Drop]\n{drop}\n\n[Bridge]\n{bridge}\n\n[Verse 2]\n{verse2}\n\n[Build]\n{build}\n\n[Final Drop]\n{finaldrop}\n\n[Outro]\n{outro}",
            "intros": [
                "Close your eyes\nAnd drift away\nInto the trance\nWhere dreams come true",
                "Beyond the stars\nBeyond the sky\nWe're flying high\nOn waves of sound"
            ],
            "verses": [
                "Emotions flowing through the night\nCarried on a sea of light\nEvery heartbeat, every breath\nTaking us beyond our death",
                "Melodies that touch the soul\nMaking broken spirits whole\nIn this trance we find our way\nTo a brighter day",
                "Floating on a cloud of sound\nElevated, off the ground\nEvery note a guiding star\nTaking us to who we are"
            ],
            "builds": [
                "Rising, rising, can't you feel\nThis euphoria is real\nTaking flight, soaring high\nTrance will make you fly",
                "Energy building\nHeart rate increasing\nWe're almost there\nHold on tight!",
                "The moment is coming\nCan you feel it\nThe release\nThe transcendence"
            ],
            "drops": [
                "Fly! Into the night\nFly! On waves of light\nFly! Beyond the stars\nFly! This is who we are",
                "Take me away\nTo another place\nWhere music heals\nAnd time stands still",
                "This is trance\nThis is love\nThis is what\nWe're dreaming of"
            ],
            "finaldrops": [
                "Final flight!\nInto the light!\nTranscendence now!\nWe've made it through!",
                "The ultimate drop!\nPure emotion!\nPure energy!\nPure trance!"
            ],
            "outros": [
                "As we return to earth\nWe carry this feeling\nThe magic of trance\nWill stay with us forever",
                "The journey ends\nBut the music plays on\nUntil we trance again\nGood night, my friends"
            ]
        }
    }

    import random
    
    # 选择最接近的模板
    style_key = style.lower()
    if "house" in style_key:
        template = lyrics_templates["House"]
    elif "techno" in style_key:
        template = lyrics_templates["Techno"]
    elif "trance" in style_key:
        template = lyrics_templates["Trance"]
    else:
        # 默认使用 House 模板
        template = lyrics_templates["House"]
    
    # 根据主题替换关键词
    theme_keywords = theme.lower()
    
    # 生成歌词
    lyrics = template["structure"].format(
        intro=random.choice(template.get("intros", ["(Instrumental)"])),
        verse1=random.choice(template["verses"]),
        verse2=random.choice([v for v in template["verses"] if v != template["verses"][0]]),
        chorus=random.choice(template["choruses"]),
        build=random.choice(template.get("builds", ["Build up..."])),
        drop=random.choice(template["drops"]),
        finaldrop=random.choice(template.get("finaldrops", template["drops"])),
        bridge=random.choice(template.get("bridges", ["(Bridge)"])),
        outro=random.choice(template.get("outros", ["(Outro)"]))
    )
    
    return lyrics


def main(argv: list[str]) -> int:
    p = argparse.ArgumentParser(description="AI DJ 带歌词曲目生成器")
    p.add_argument("--idea", "-i", required=True, help="曲目创意/主题")
    p.add_argument("--style", "-s", default="House", help="音乐风格")
    p.add_argument("--bpm", "-b", type=int, default=128, help="目标 BPM")
    p.add_argument("--with-lyrics", action="store_true", help="生成带歌词的曲目")
    p.add_argument("--lyrics-only", action="store_true", help="只生成歌词")
    p.add_argument("--play", action="store_true", help="生成后自动播放")
    p.add_argument("--verbose", "-v", action="store_true", help="启用调试日志")
    
    args = p.parse_args(argv)
    if args.verbose:
        logger.setLevel(logging.DEBUG)
    
    root = _repo_root()
    stamp = _now_stamp()
    slug = _slugify(args.style or args.idea)
    
    # 生成歌词
    if args.with_lyrics or args.lyrics_only:
        print("=" * 60)
        print("🎵 AI DJ 歌词生成器")
        print("=" * 60)
        print()
        print(f"📝 主题: {args.idea}")
        print(f"🎶 风格: {args.style}")
        print(f"🎼 BPM: {args.bpm}")
        print()
        
        lyrics = generate_lyrics(args.idea, args.style)
        
        # 保存歌词
        lyrics_path = root / "04_generations" / "metadata" / f"{stamp}_{slug}_lyrics.txt"
        lyrics_path.parent.mkdir(parents=True, exist_ok=True)
        lyrics_path.write_text(lyrics, encoding="utf-8")
        
        print("📄 生成的歌词:")
        print("-" * 60)
        print(lyrics)
        print("-" * 60)
        print()
        print(f"✅ 歌词已保存到: {lyrics_path}")
        print()
        
        if args.lyrics_only:
            return 0
    
    # 生成音乐（使用云端 API）
    if not args.lyrics_only:
        cmd = [
            sys.executable,
            str(root / "13_tools" / "scripts" / "make_dj_track_minimax.py"),
            "--idea", args.idea,
            "--style", args.style,
            "--bpm", str(args.bpm),
        ]
        if args.play:
            cmd.append("--play")
        
        logger.info("🎵 开始生成音乐...")
        logger.info(f"📝 提示词: {args.idea}")
        logger.info(f"🎶 风格: {args.style}")
        logger.info(f"🎼 BPM: {args.bpm}")
        
        try:
            result = subprocess.run(cmd, capture_output=True, text=True)
            if result.returncode != 0:
                logger.error(f"❌ 生成失败: {result.stderr}")
                return 1
            logger.info("✅ 音乐生成成功!")
            return 0
        except Exception as e:
            logger.error(f"❌ 生成失败: {e}")
            return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
