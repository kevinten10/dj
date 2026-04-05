#!/usr/bin/env python3
"""
Interactive DJ Track Generator
Easy to use menu-driven interface for generating DJ music.
"""

import sys
from pathlib import Path


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def load_presets() -> dict:
    """Load style presets."""
    try:
        import json
        presets_path = _repo_root() / "13_tools" / "presets" / "styles.json"
        with presets_path.open("r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {"presets": {}}


def print_header():
    print("\n" + "=" * 60)
    print("🎧 AI-DJ 交互式生成器")
    print("=" * 60)


def print_main_menu():
    print("\n请选择:")
    print("1. 🎵 使用云端 API (MiniMax) 生成")
    print("2. 🏠 使用本地模型 (MusicGen) 生成")
    print("3. 📋 获取练习计划")
    print("4. 📁 管理曲目库")
    print("5. 📚 查看文档")
    print("0. 退出")


def print_cloud_menu():
    print("\n--- 云端 API 生成 ---")
    print("1. 基本生成 (自定义)")
    print("2. 使用风格预设")
    print("0. 返回主菜单")


def print_local_menu():
    print("\n--- 本地模型生成 ---")
    print("1. 基本生成 (Small 模型)")
    print("2. 使用 Medium 模型 (更高质量)")
    print("3. 使用 Large 模型 (最佳质量)")
    print("4. 自定义参数")
    print("0. 返回主菜单")


def get_input(prompt: str, default: str = "") -> str:
    if default:
        result = input(f"{prompt} [{default}]: ").strip()
        return result if result else default
    return input(f"{prompt}: ").strip()


def get_int_input(prompt: str, default: int, min_val: int = None, max_val: int = None) -> int:
    while True:
        try:
            val = get_input(prompt, str(default))
            result = int(val)
            if min_val is not None and result < min_val:
                print(f"⚠️  值不能小于 {min_val}")
                continue
            if max_val is not None and result > max_val:
                print(f"⚠️  值不能大于 {max_val}")
                continue
            return result
        except ValueError:
            print(f"⚠️  请输入有效的数字")


def get_yes_no(prompt: str, default: bool = False) -> bool:
    default_str = "Y/n" if default else "y/N"
    while True:
        val = get_input(f"{prompt} [{default_str}]", "").lower().strip()
        if val in ["y", "yes"]:
            return True
        if val in ["n", "no"]:
            return False
        if val == "":
            return default
        print("⚠️  请输入 y 或 n")


def run_cloud_generate():
    print("\n--- 云端 API 生成 ---")
    
    idea = get_input("曲目创意/主题", "午夜 Tech House 派对")
    style = get_input("音乐风格", "Tech House")
    bpm = get_int_input("BPM", 128, 60, 200)
    instrumental = get_yes_no("生成器乐曲目？", True)
    play = get_yes_no("生成后自动播放？", True)
    
    cmd = [
        sys.executable,
        str(_repo_root() / "13_tools" / "scripts" / "make_dj_track_minimax.py"),
        "--idea", idea,
        "--style", style,
        "--bpm", str(bpm)
    ]
    if instrumental:
        cmd.append("--instrumental")
    if play:
        cmd.append("--play")
    
    print(f"\n🚀 执行命令: {' '.join(cmd)}")
    import subprocess
    subprocess.run(cmd)


def run_cloud_preset():
    print("\n--- 使用风格预设 ---")
    
    presets = load_presets()
    if not presets["presets"]:
        print("⚠️  未找到预设文件")
        return
    
    print("\n可用预设:")
    preset_list = list(presets["presets"].items())
    for i, (key, preset) in enumerate(preset_list, 1):
        print(f"{i}. {preset['name']} ({preset['default_bpm']} BPM)")
    print("0. 返回")
    
    choice = get_int_input("选择预设", 0, 0, len(preset_list))
    if choice == 0:
        return
    
    preset_key, preset = preset_list[choice - 1]
    
    idea = get_input("添加额外创意（可选）", "")
    instrumental = get_yes_no("生成器乐曲目？", True)
    play = get_yes_no("生成后自动播放？", True)
    
    cmd = [
        sys.executable,
        str(_repo_root() / "13_tools" / "scripts" / "generate_with_preset.py"),
        "--preset", preset_key,
        "--idea", idea if idea else preset["description"]
    ]
    if instrumental:
        cmd.append("--instrumental")
    if play:
        cmd.append("--play")
    
    print(f"\n🚀 执行命令: {' '.join(cmd)}")
    import subprocess
    subprocess.run(cmd)


def run_local_generate(model_size: str = "small"):
    model_map = {
        "small": "facebook/musicgen-small",
        "medium": "facebook/musicgen-medium",
        "large": "facebook/musicgen-large"
    }
    
    print(f"\n--- 本地模型生成 ({model_size}) ---")
    
    idea = get_input("曲目创意/主题", "午夜 Tech House 派对")
    style = get_input("音乐风格", "Tech House")
    bpm = get_int_input("BPM", 128, 60, 200)
    duration = get_int_input("时长（秒）", 90, 10, 600)
    
    use_cuda = get_yes_no("使用 GPU (CUDA) 加速？", False)
    play = get_yes_no("生成后自动播放？", True)
    
    cmd = [
        sys.executable,
        str(_repo_root() / "13_tools" / "scripts" / "make_dj_track_local.py"),
        "--idea", idea,
        "--style", style,
        "--bpm", str(bpm),
        "--duration", str(duration),
        "--model", model_map[model_size]
    ]
    if use_cuda:
        cmd.append("--cuda")
    if play:
        cmd.append("--play")
    
    print(f"\n🚀 执行命令: {' '.join(cmd)}")
    import subprocess
    subprocess.run(cmd)


def run_local_custom():
    print("\n--- 本地模型自定义生成 ---")
    
    idea = get_input("曲目创意/主题", "午夜 Tech House 派对")
    style = get_input("音乐风格", "Tech House")
    bpm = get_int_input("BPM", 128, 60, 200)
    duration = get_int_input("时长（秒）", 90, 10, 600)
    
    print("\n模型选择:")
    print("1. Small (300M, 快速)")
    print("2. Medium (1.5B, 平衡)")
    print("3. Large (3.3B, 高质量)")
    model_choice = get_int_input("选择模型", 1, 1, 3)
    
    model_map = {
        1: "facebook/musicgen-small",
        2: "facebook/musicgen-medium",
        3: "facebook/musicgen-large"
    }
    
    temperature = get_float_input("温度参数 (0.0-2.0)", 1.0, 0.0, 2.0)
    cfg = get_float_input("CFG 系数 (1.0-10.0)", 3.0, 1.0, 10.0)
    
    use_cuda = get_yes_no("使用 GPU (CUDA) 加速？", False)
    play = get_yes_no("生成后自动播放？", True)
    
    cmd = [
        sys.executable,
        str(_repo_root() / "13_tools" / "scripts" / "make_dj_track_local.py"),
        "--idea", idea,
        "--style", style,
        "--bpm", str(bpm),
        "--duration", str(duration),
        "--model", model_map[model_choice],
        "--temperature", str(temperature),
        "--cfg", str(cfg)
    ]
    if use_cuda:
        cmd.append("--cuda")
    if play:
        cmd.append("--play")
    
    print(f"\n🚀 执行命令: {' '.join(cmd)}")
    import subprocess
    subprocess.run(cmd)


def get_float_input(prompt: str, default: float, min_val: float = None, max_val: float = None) -> float:
    while True:
        try:
            val = get_input(prompt, str(default))
            result = float(val)
            if min_val is not None and result < min_val:
                print(f"⚠️  值不能小于 {min_val}")
                continue
            if max_val is not None and result > max_val:
                print(f"⚠️  值不能大于 {max_val}")
                continue
            return result
        except ValueError:
            print(f"⚠️  请输入有效的数字")


def run_practice_plan():
    print("\n--- 练习计划 ---")
    print("1. 新手计划")
    print("2. 进阶计划")
    print("3. 高级计划")
    print("0. 返回")
    
    choice = get_int_input("选择计划", 0, 0, 3)
    if choice == 0:
        return
    
    level_map = {1: "beginner", 2: "intermediate", 3: "advanced"}
    save = get_yes_no("保存到文件？", True)
    
    cmd = [
        sys.executable,
        str(_repo_root() / "13_tools" / "scripts" / "practice_plan.py"),
        "--level", level_map[choice]
    ]
    if save:
        cmd.append("--save")
    
    import subprocess
    subprocess.run(cmd)


def run_library_manager():
    print("\n--- 曲目库管理 ---")
    print("1. 列出所有曲目")
    print("2. 按风格筛选")
    print("3. 创建 Set List")
    print("0. 返回")
    
    choice = get_int_input("选择操作", 0, 0, 3)
    if choice == 0:
        return
    
    cmd = [
        sys.executable,
        str(_repo_root() / "13_tools" / "scripts" / "library_manager.py")
    ]
    
    if choice == 1:
        cmd.append("list")
    elif choice == 2:
        style = get_input("输入风格", "Tech House")
        cmd.extend(["list", "--style", style])
    elif choice == 3:
        print("请先运行 'list' 查看曲目索引")
        name = get_input("Set List 名称", "我的 Set")
        tracks = get_input("曲目索引（逗号分隔）", "1,2,3")
        cmd.extend(["setlist", "--name", name, "--tracks", tracks])
    
    import subprocess
    subprocess.run(cmd)


def show_docs():
    print("\n--- 文档 ---")
    print("1. DJ 学习路径")
    print("2. DJ 技巧库")
    print("3. 本地模型使用指南")
    print("4. AI-DJ 教程")
    print("0. 返回")
    
    choice = get_int_input("选择文档", 0, 0, 4)
    if choice == 0:
        return
    
    doc_map = {
        1: "12_docs/learning_path.md",
        2: "12_docs/techniques_library.md",
        3: "12_docs/local_models.md",
        4: "12_docs/ai_djuced_tutorial.md"
    }
    
    doc_path = _repo_root() / doc_map[choice]
    if doc_path.exists():
        print(f"\n📖 打开: {doc_path}")
        import os
        import platform
        import subprocess
        system = platform.system().lower()
        if system.startswith("windows"):
            os.startfile(str(doc_path))
        elif system == "darwin":
            subprocess.run(["open", str(doc_path)], check=False)
        else:
            subprocess.run(["xdg-open", str(doc_path)], check=False)
    else:
        print(f"⚠️  文档未找到: {doc_path}")


def main():
    while True:
        print_header()
        print_main_menu()
        
        choice = get_int_input("\n请输入选项", 0, 0, 5)
        
        if choice == 0:
            print("\n👋 再见！")
            break
        elif choice == 1:
            while True:
                print_cloud_menu()
                sub_choice = get_int_input("请输入选项", 0, 0, 2)
                if sub_choice == 0:
                    break
                elif sub_choice == 1:
                    run_cloud_generate()
                elif sub_choice == 2:
                    run_cloud_preset()
        elif choice == 2:
            while True:
                print_local_menu()
                sub_choice = get_int_input("请输入选项", 0, 0, 4)
                if sub_choice == 0:
                    break
                elif sub_choice == 1:
                    run_local_generate("small")
                elif sub_choice == 2:
                    run_local_generate("medium")
                elif sub_choice == 3:
                    run_local_generate("large")
                elif sub_choice == 4:
                    run_local_custom()
        elif choice == 3:
            run_practice_plan()
        elif choice == 4:
            run_library_manager()
        elif choice == 5:
            show_docs()
        
        input("\n按 Enter 继续...")


if __name__ == "__main__":
    main()
