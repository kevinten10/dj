#!/usr/bin/env python3
"""
Interactive DJ Track Generator
Easy to use menu-driven interface for generating DJ music.
"""

import sys
import importlib.util
import subprocess
from pathlib import Path


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def _format_command(cmd: list[str]) -> str:
    return subprocess.list2cmdline(cmd)


def _ace_step_path() -> Path:
    return _repo_root() / "13_tools" / "ace_step"


def _ace_step_importable(ace_step_path: Path) -> bool:
    path_text = str(ace_step_path)
    added_path = False
    if path_text not in sys.path:
        sys.path.insert(0, path_text)
        added_path = True

    try:
        return importlib.util.find_spec("acestep") is not None
    finally:
        if added_path:
            try:
                sys.path.remove(path_text)
            except ValueError:
                pass


def get_musicgen_python() -> str | None:
    root = _repo_root()
    root_text = str(root)
    added_path = False
    if root_text not in sys.path:
        sys.path.insert(0, root_text)
        added_path = True

    try:
        from manage_models import get_musicgen_python as _get_musicgen_python

        return _get_musicgen_python(root)
    finally:
        if added_path:
            try:
                sys.path.remove(root_text)
            except ValueError:
                pass


def print_musicgen_setup_hint() -> None:
    print("MusicGen/AudioCraft environment is not ready.")
    print("Run:")
    print("  .\\setup_local_models.ps1")
    print("Then retry local MusicGen generation.")


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
    print("3. 🎤 使用本地歌词模型 (ACE-Step) 生成 ⭐NEW")
    print("4. 📋 获取练习计划")
    print("5. 📁 管理曲目库")
    print("6. 📚 查看文档")
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
    try:
        if default:
            result = input(f"{prompt} [{default}]: ").strip()
            return result if result else default
        return input(f"{prompt}: ").strip()
    except EOFError:
        return default


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
    with_lyrics = get_yes_no("生成带歌词的曲目？", False)
    
    if with_lyrics:
        play = get_yes_no("生成后自动播放？", True)
        
        cmd = [
            sys.executable,
            str(_repo_root() / "13_tools" / "scripts" / "make_dj_track_with_lyrics.py"),
            "--idea", idea,
            "--style", style,
            "--bpm", str(bpm),
            "--with-lyrics"
        ]
        if play:
            cmd.append("--play")
        
        print(f"\n🚀 执行命令: {_format_command(cmd)}")
        import subprocess
        subprocess.run(cmd)
    else:
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
        
        print(f"\n🚀 执行命令: {_format_command(cmd)}")
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
    
    print(f"\n🚀 执行命令: {_format_command(cmd)}")
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
    
    python_executable = get_musicgen_python()
    if python_executable is None:
        print_musicgen_setup_hint()
        return

    cmd = [
        python_executable,
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
    
    print(f"\n🚀 执行命令: {_format_command(cmd)}")
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
    
    python_executable = get_musicgen_python()
    if python_executable is None:
        print_musicgen_setup_hint()
        return

    cmd = [
        python_executable,
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
    
    print(f"\n🚀 执行命令: {_format_command(cmd)}")
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
    print("4. 本地歌词模型对比")
    print("5. ACE-Step 部署报告")
    print("6. AI-DJ 教程")
    print("0. 返回")
    
    choice = get_int_input("选择文档", 0, 0, 6)
    if choice == 0:
        return
    
    doc_map = {
        1: "12_docs/learning_path.md",
        2: "12_docs/techniques_library.md",
        3: "12_docs/local_models.md",
        4: "12_docs/local_lyrics_models.md",
        5: "12_docs/ace_step_deployment_report.md",
        6: "12_docs/ai_djuced_tutorial.md"
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


def print_ace_menu():
    print("\n--- 本地歌词生成 (ACE-Step) ---")
    print("⚠️  注意：RTX 5060 Ti 可能存在兼容性问题")
    print("1. 生成 House 音乐（带歌词）")
    print("2. 生成 Techno 音乐（带歌词）")
    print("3. 生成 Trance 音乐（带歌词）")
    print("4. 自定义生成")
    print("5. 启动 Web UI (Gradio)")
    print("6. 检查 ACE-Step 环境")
    print("0. 返回主菜单")


def run_ace_step_generate(style: str = "House"):
    print(f"\n--- ACE-Step 生成 ({style}) ---")

    theme = get_input("主题/创意", "DJ派对")
    duration = get_int_input("时长（秒，-1为随机）", 30, -1, 300)
    steps = get_int_input("推理步骤（30-50，越多质量越好）", 30, 10, 100)

    print("\n高级设置:")
    cpu_offload = get_yes_no("启用 CPU Offload（减少显存使用）", True)
    bf16 = get_yes_no("使用 BF16 精度（更快）", True)

    cmd = [
        sys.executable,
        str(_repo_root() / "13_tools" / "scripts" / "make_dj_track_ace_step.py"),
        "--theme", theme,
        "--style", style,
        "--duration", str(duration),
        "--steps", str(steps)
    ]

    if not cpu_offload:
        cmd.append("--no-cpu-offload")
    if not bf16:
        cmd.append("--fp32")

    print(f"\n🚀 执行命令: {_format_command(cmd)}")
    import subprocess
    subprocess.run(cmd)


def run_ace_step_custom():
    print("\n--- ACE-Step 自定义生成 ---")

    lyrics = get_input("输入歌词（或留空使用模板）", "")
    prompt = get_input("风格描述", "Electronic House music, upbeat, dance, 120 BPM")
    duration = get_int_input("时长（秒）", 30, -1, 300)
    steps = get_int_input("推理步骤", 30, 10, 100)
    guidance = get_float_input("引导系数", 7.0, 1.0, 20.0)
    seed = get_int_input("随机种子（-1为随机）", -1, -1, 999999)

    cmd = [
        sys.executable,
        str(_repo_root() / "13_tools" / "scripts" / "make_dj_track_ace_step.py"),
        "--prompt", prompt,
        "--duration", str(duration),
        "--steps", str(steps),
        "--guidance", str(guidance),
        "--seed", str(seed)
    ]

    if lyrics:
        cmd.extend(["--lyrics", lyrics])

    print(f"\n🚀 执行命令: {_format_command(cmd)}")
    import subprocess
    subprocess.run(cmd)


def run_ace_step_webui():
    print("\n--- 启动 ACE-Step Web UI ---")
    print("🌐 启动后访问: http://localhost:7865")

    ace_step_path = _ace_step_path()
    if not ace_step_path.exists():
        print(f"❌ ACE-Step 目录不存在: {ace_step_path}")
        print("请先克隆 ACE-Step，或运行环境检查: python 13_tools/scripts/make_dj_track_ace_step.py --check")
        return

    if not _ace_step_importable(ace_step_path):
        print("❌ Python 包 acestep 不可导入。")
        print("请先安装 ACE-Step 依赖，或运行环境检查: python 13_tools/scripts/make_dj_track_ace_step.py --check")
        return

    port = get_int_input("端口号", 7865, 1000, 99999)
    cpu_offload = get_yes_no("启用 CPU Offload", True)

    cmd = [
        sys.executable, "-m", "acestep.gui",
        "--port", str(port)
    ]

    if cpu_offload:
        cmd.extend(["--cpu_offload", "true"])

    cmd.extend(["--bf16", "true", "--overlapped_decode", "true"])

    print(f"\n🚀 执行命令: {_format_command(cmd)}")
    print("⚠️  Web UI 启动后，请在浏览器中使用生成")

    try:
        subprocess.run(cmd, cwd=str(ace_step_path), check=False)
    except OSError as exc:
        print(f"❌ ACE-Step Web UI 启动失败: {exc}")
        print("请先运行环境检查: python 13_tools/scripts/make_dj_track_ace_step.py --check")


def run_ace_step_check():
    print("\n--- 检查 ACE-Step 环境 ---")
    cmd = [
        sys.executable,
        str(_repo_root() / "13_tools" / "scripts" / "make_dj_track_ace_step.py"),
        "--check",
    ]
    import subprocess
    subprocess.run(cmd)


def main():
    while True:
        print_header()
        print_main_menu()
        
        choice = get_int_input("\n请输入选项", 0, 0, 6)
        
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
            while True:
                print_ace_menu()
                sub_choice = get_int_input("请输入选项", 0, 0, 6)
                if sub_choice == 0:
                    break
                elif sub_choice == 1:
                    run_ace_step_generate("House")
                elif sub_choice == 2:
                    run_ace_step_generate("Techno")
                elif sub_choice == 3:
                    run_ace_step_generate("Trance")
                elif sub_choice == 4:
                    run_ace_step_custom()
                elif sub_choice == 5:
                    run_ace_step_webui()
                elif sub_choice == 6:
                    run_ace_step_check()
        elif choice == 4:
            run_practice_plan()
        elif choice == 5:
            run_library_manager()
        elif choice == 6:
            show_docs()
        
        input("\n按 Enter 继续...")


if __name__ == "__main__":
    main()
