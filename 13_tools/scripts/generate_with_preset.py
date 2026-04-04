#!/usr/bin/env python3
"""
Generate DJ tracks using style presets.
Combines the preset system with the MiniMax generation script.
"""

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import Dict, Any


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def load_presets() -> Dict[str, Any]:
    """Load style presets from JSON file."""
    presets_path = _repo_root() / "13_tools" / "presets" / "styles.json"
    with presets_path.open("r", encoding="utf-8") as f:
        return json.load(f)


def list_presets() -> None:
    """List all available presets."""
    presets = load_presets()
    print("\n🎵 可用的风格预设:")
    print("=" * 60)
    for key, preset in presets["presets"].items():
        print(f"\n  {key}")
        print(f"    名称: {preset['name']}")
        print(f"    BPM: {preset['bpm_min']}-{preset['bpm_max']} (默认: {preset['default_bpm']})")
        print(f"    能量: {preset['energy_level']}")
        print(f"    描述: {preset['description']}")
    print("\n" + "=" * 60)


def get_preset(preset_name: str) -> Dict[str, Any]:
    """Get a specific preset by name."""
    presets = load_presets()
    preset = presets["presets"].get(preset_name)
    if not preset:
        raise ValueError(f"Preset '{preset_name}' not found. Use --list to see available presets.")
    return preset


def build_prompt(preset: Dict[str, Any], idea: str) -> str:
    """Build the final prompt using the preset template."""
    template = preset["prompt_template"]
    return template.replace("{idea}", idea)


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description="使用风格预设生成 DJ 曲目")
    parser.add_argument("--list", "-l", action="store_true",
                        help="列出所有可用预设")
    parser.add_argument("--preset", "-p",
                        help="使用的预设名称")
    parser.add_argument("--idea", "-i", default="",
                        help="曲目创意/主题")
    parser.add_argument("--bpm", type=int,
                        help="BPM (覆盖预设默认值)")
    parser.add_argument("--instrumental", action="store_true",
                        help="生成器乐曲目")
    parser.add_argument("--play", action="store_true",
                        help="生成后自动播放")
    parser.add_argument("--model", default="music-2.5",
                        help="MiniMax 模型")
    parser.add_argument("--dry-run", action="store_true",
                        help="仅显示命令，不执行")

    args = parser.parse_args(argv)

    if args.list:
        list_presets()
        return 0

    if not args.preset:
        print("❌ 错误: 请指定 --preset 或使用 --list 查看可用预设", file=sys.stderr)
        return 1

    try:
        preset = get_preset(args.preset)
    except ValueError as e:
        print(f"❌ 错误: {e}", file=sys.stderr)
        return 1

    bpm = args.bpm or preset["default_bpm"]
    style = preset["style"]
    prompt = build_prompt(preset, args.idea)

    print(f"\n🎧 使用预设: {preset['name']}")
    print(f"   风格: {style}")
    print(f"   BPM: {bpm}")
    print(f"   能量: {preset['energy_level']}")
    print(f"   提示词: {prompt[:80]}...")

    # Build the command for make_dj_track_minimax.py
    script_path = _repo_root() / "13_tools" / "scripts" / "make_dj_track_minimax.py"
    cmd = [
        sys.executable,
        str(script_path),
        "--idea", prompt,
        "--style", style,
        "--bpm", str(bpm),
        "--model", args.model
    ]

    if args.instrumental:
        cmd.append("--instrumental")
    if args.play:
        cmd.append("--play")

    print(f"\n📝 执行命令:")
    print(f"   {' '.join(cmd)}")

    if args.dry_run:
        print("\n✅ --dry-run: 命令未执行")
        return 0

    print("\n🚀 开始生成...")
    try:
        result = subprocess.run(cmd, check=True)
        return result.returncode
    except subprocess.CalledProcessError as e:
        print(f"❌ 生成失败: {e}", file=sys.stderr)
        return e.returncode


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
