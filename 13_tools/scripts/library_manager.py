#!/usr/bin/env python3
"""
DJ Library Manager
Manage and organize your AI-generated DJ tracks.
"""

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def scan_library() -> List[Dict[str, Any]]:
    """Scan the library and collect track information."""
    root = _repo_root()
    dj_ready_dir = root / "08_exports" / "dj_ready"
    metadata_dir = root / "04_generations" / "metadata"

    tracks = []

    if not dj_ready_dir.exists():
        return tracks

    for audio_file in dj_ready_dir.glob("*.mp3"):
        track_info = {
            "filename": audio_file.name,
            "path": str(audio_file),
            "size_bytes": audio_file.stat().st_size,
            "modified_time": datetime.fromtimestamp(audio_file.stat().st_mtime).isoformat()
        }

        # Look for corresponding metadata
        stem = audio_file.stem
        meta_file = metadata_dir / f"{stem}.json"
        if meta_file.exists():
            try:
                with meta_file.open("r", encoding="utf-8") as f:
                    meta = json.load(f)
                track_info["metadata"] = meta
                params = meta.get("params", {})
                track_info.update({
                    "style": params.get("style", ""),
                    "bpm": params.get("bpm", ""),
                    "key": params.get("key", ""),
                    "idea": params.get("idea", ""),
                    "instrumental": params.get("instrumental", False)
                })
            except Exception as e:
                track_info["metadata_error"] = str(e)

        tracks.append(track_info)

    return sorted(tracks, key=lambda x: x["modified_time"], reverse=True)


def list_tracks(tracks: List[Dict[str, Any]], filter_style: Optional[str] = None,
                filter_bpm_min: Optional[int] = None, filter_bpm_max: Optional[int] = None) -> None:
    """List all tracks with optional filtering."""
    filtered_tracks = tracks

    if filter_style:
        filtered_tracks = [t for t in filtered_tracks if filter_style.lower() in str(t.get("style", "")).lower()]

    if filter_bpm_min is not None:
        filtered_tracks = [t for t in filtered_tracks if isinstance(t.get("bpm"), int) and t["bpm"] >= filter_bpm_min]

    if filter_bpm_max is not None:
        filtered_tracks = [t for t in filtered_tracks if isinstance(t.get("bpm"), int) and t["bpm"] <= filter_bpm_max]

    if not filtered_tracks:
        print("📭 没有找到符合条件的曲目")
        return

    print(f"\n🎵 曲目库 ({len(filtered_tracks)} 首):")
    print("=" * 80)
    for i, track in enumerate(filtered_tracks, 1):
        style = track.get("style", "N/A")
        bpm = track.get("bpm", "N/A")
        key = track.get("key", "N/A") if track.get("key") else "N/A"
        idea = track.get("idea", "")[:50] + "..." if len(str(track.get("idea", ""))) > 50 else str(track.get("idea", ""))

        print(f"\n{i}. {track['filename']}")
        print(f"   风格: {style} | BPM: {bpm} | Key: {key}")
        print(f"   创意: {idea}")
        print(f"   修改时间: {track['modified_time'][:19]}")

    print("\n" + "=" * 80)


def show_track_details(tracks: List[Dict[str, Any]], filename: str) -> None:
    """Show detailed information for a specific track."""
    track = next((t for t in tracks if t["filename"] == filename), None)
    if not track:
        print(f"❌ 找不到曲目: {filename}", file=sys.stderr)
        return

    print(f"\n📋 曲目详情: {track['filename']}")
    print("=" * 80)
    print(f"路径: {track['path']}")
    print(f"大小: {track['size_bytes'] / 1024 / 1024:.2f} MB")
    print(f"修改时间: {track['modified_time']}")

    if "metadata" in track:
        meta = track["metadata"]
        print(f"\n🎛️  生成参数:")
        params = meta.get("params", {})
        for key, value in params.items():
            print(f"  {key}: {value}")
        print(f"\n📝 提示词: {meta.get('prompt', '')}")

    print("\n" + "=" * 80)


def export_library(tracks: List[Dict[str, Any]], output_path: Path) -> None:
    """Export library to JSON file."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    export_data = {
        "exported_at": datetime.now().isoformat(),
        "total_tracks": len(tracks),
        "tracks": tracks
    }
    with output_path.open("w", encoding="utf-8") as f:
        json.dump(export_data, f, indent=2, ensure_ascii=False)
    print(f"✅ 曲目库已导出到: {output_path}")


def create_set_list(tracks: List[Dict[str, Any]], name: str, track_indices: List[int]) -> None:
    """Create a set list from selected track indices."""
    root = _repo_root()
    set_lists_dir = root / "08_exports" / "set_lists"
    set_lists_dir.mkdir(parents=True, exist_ok=True)

    selected_tracks = []
    for idx in track_indices:
        if 1 <= idx <= len(tracks):
            selected_tracks.append(tracks[idx - 1])
        else:
            print(f"⚠️  跳过无效索引: {idx}")

    if not selected_tracks:
        print("❌ 没有选择有效的曲目", file=sys.stderr)
        return

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    set_list_path = set_lists_dir / f"set_{name}_{timestamp}.json"

    set_list = {
        "name": name,
        "created_at": datetime.now().isoformat(),
        "tracks": [
            {
                "filename": t["filename"],
                "path": t["path"],
                "style": t.get("style", ""),
                "bpm": t.get("bpm", ""),
                "order": i + 1
            }
            for i, t in enumerate(selected_tracks)
        ]
    }

    with set_list_path.open("w", encoding="utf-8") as f:
        json.dump(set_list, f, indent=2, ensure_ascii=False)

    print(f"\n✅ Set List 已创建: {set_list_path}")
    print(f"\n🎧 曲目顺序:")
    for i, t in enumerate(selected_tracks, 1):
        print(f"{i}. {t['filename']} ({t.get('style', 'N/A')} @ {t.get('bpm', 'N/A')} BPM)")


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description="DJ 曲目库管理工具")
    subparsers = parser.add_subparsers(dest="command", help="可用命令")

    # List command
    list_parser = subparsers.add_parser("list", help="列出所有曲目")
    list_parser.add_argument("--style", help="按风格筛选")
    list_parser.add_argument("--bpm-min", type=int, help="最低 BPM")
    list_parser.add_argument("--bpm-max", type=int, help="最高 BPM")

    # Show command
    show_parser = subparsers.add_parser("show", help="显示曲目详情")
    show_parser.add_argument("filename", help="曲目文件名")

    # Export command
    export_parser = subparsers.add_parser("export", help="导出曲目库")
    export_parser.add_argument("--output", "-o", help="输出文件路径")

    # Set list command
    setlist_parser = subparsers.add_parser("setlist", help="创建 Set List")
    setlist_parser.add_argument("--name", "-n", required=True, help="Set List 名称")
    setlist_parser.add_argument("--tracks", "-t", required=True, help="曲目索引（逗号分隔，例如: 1,3,5）")

    args = parser.parse_args(argv)

    tracks = scan_library()

    if args.command == "list":
        list_tracks(tracks, args.style, args.bpm_min, args.bpm_max)
    elif args.command == "show":
        show_track_details(tracks, args.filename)
    elif args.command == "export":
        root = _repo_root()
        output = Path(args.output) if args.output else root / "08_exports" / f"library_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        export_library(tracks, output)
    elif args.command == "setlist":
        try:
            track_indices = [int(x.strip()) for x in args.tracks.split(",")]
            create_set_list(tracks, args.name, track_indices)
        except ValueError:
            print("❌ 错误: 请使用逗号分隔的数字索引", file=sys.stderr)
            return 1
    else:
        parser.print_help()

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
