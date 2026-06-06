"""
ACE-Step 本地歌词生成器
用于生成本地带歌词的 DJ 音乐

用法:
    python make_dj_track_ace_step.py --lyrics "你的歌词" --prompt "风格描述"
    python make_dj_track_ace_step.py --theme "DJ派对" --style "House"
"""

import os
import sys
import argparse
import datetime
import importlib.util
import subprocess
import time
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
ACE_STEP_PATH = REPO_ROOT / "13_tools" / "ace_step"


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")


# 歌词模板库
LYRICS_TEMPLATES = {
    "House": {
        "prompt": "Electronic House music, upbeat, dance, club, bass, 120 BPM",
        "lyrics": """[Verse 1]
Feel the rhythm in the night
Lights are flashing, everything's right
Moving to the beat we own
In this house we call our home

[Chorus]
Let the bass drop, feel the flow
House music makes us glow
Dancing till the morning light
This is our night, feel so right

[Drop]
Feel the beat
Feel the bass
Move your body
Feel the space

[Verse 2]
Turn the music up so loud
Lost inside this happy crowd
Every beat connects our hearts
This is where the magic starts

[Chorus]
Let the bass drop, feel the flow
House music makes us glow
Dancing till the morning light
This is our night, feel so right

[Bridge]
When the DJ plays our song
We all know where we belong
In the rhythm of the night
Everything will be alright

[Outro]
Keep on dancing
Keep on moving
House music
Forever grooving
"""
    },
    "Techno": {
        "prompt": "Electronic Techno music, dark, industrial, repetitive, heavy bass, 130 BPM",
        "lyrics": """[Verse 1]
Dark beats echo through the night
Machine sounds, industrial might
Pulse is rising, feel the power
This is our electric hour

[Chorus]
Techno beats, techno dreams
Nothing's ever what it seems
Lost inside the digital sound
Where the lost ones can be found

[Drop]
Beat drops
System overload
Feel the power
Explode

[Verse 2]
Synthesizers paint the dark
Every beat becomes a spark
In this world of code and wire
We become the electric fire

[Chorus]
Techno beats, techno dreams
Nothing's ever what it seems
Lost inside the digital sound
Where the lost ones can be found

[Bridge]
When the machines take control
Let the rhythm move your soul
In the darkness we unite
Techno is our light tonight

[Outro]
Repeat
Reset
Reload
Techno
"""
    },
    "Trance": {
        "prompt": "Electronic Trance music, uplifting, melodic, ethereal, emotional, 138 BPM",
        "lyrics": """[Verse 1]
Floating through the starlit sky
Euphoria is drawing nigh
Melodies that touch the soul
Trance music makes us whole

[Chorus]
Take me higher, take me far
Beyond the moon, beyond the star
In this trance we find our way
To a better brighter day

[Drop]
Ascend
Elevate
Transcend
Liberate

[Verse 2]
Hands are reaching for the light
We are infinite tonight
Every note a sacred prayer
Music takes us anywhere

[Chorus]
Take me higher, take me far
Beyond the moon, beyond the star
In this trance we find our way
To a better brighter day

[Bridge]
When the melody unfolds
Stories waiting to be told
In the arms of sound we trust
This is more than just a must

[Outro]
Fly away
Dream again
Trance forever
Amen
"""
    }
}


def create_dj_lyrics(theme: str, style: str = "House") -> tuple:
    """根据主题和风格创建歌词"""
    if style in LYRICS_TEMPLATES:
        template = LYRICS_TEMPLATES[style]
        return template["lyrics"], template["prompt"]

    # 默认 House 风格
    return LYRICS_TEMPLATES["House"]["lyrics"], LYRICS_TEMPLATES["House"]["prompt"]


def resolve_lyrics_and_prompt(args: argparse.Namespace) -> tuple[str, str]:
    """Resolve user input while allowing prompt-only or lyrics-only custom runs."""
    template_lyrics, template_prompt = create_dj_lyrics(args.theme or "DJ派对", args.style)
    lyrics = args.lyrics if args.lyrics else template_lyrics
    prompt = args.prompt if args.prompt else template_prompt
    return lyrics, prompt


def _git_value(args: list[str]) -> str:
    try:
        result = subprocess.run(
            ["git", "-C", str(ACE_STEP_PATH), *args],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            check=False,
        )
    except FileNotFoundError:
        return "git not found"

    if result.returncode != 0:
        return (result.stderr or result.stdout).strip() or "unavailable"
    return result.stdout.strip()


def _missing_ace_step_runtime_packages() -> list[str]:
    required_runtime_packages = ["torchcodec"]
    return [
        package
        for package in required_runtime_packages
        if importlib.util.find_spec(package) is None
    ]


def _print_ace_step_runtime_install_hint(missing_packages: list[str]) -> None:
    if not missing_packages:
        return

    print("缺少 ACE-Step 运行时依赖:")
    for package in missing_packages:
        print(f"  - {package}")
    print("建议安装:")
    print(f"  python -m pip install {' '.join(missing_packages)}")


def check_ace_step_setup() -> int:
    """Run a lightweight preflight without loading the ACE-Step model."""
    print("ACE-Step 本地环境检查")
    print("=" * 50)
    print(f"项目根目录: {REPO_ROOT}")
    print(f"ACE-Step 目录: {ACE_STEP_PATH}")

    if not ACE_STEP_PATH.exists():
        print("状态: 未安装")
        print("安装命令:")
        print("  git clone https://github.com/ace-step/ACE-Step.git 13_tools/ace_step")
        return 1

    print("状态: 已找到本地 clone")
    remote = _git_value(["remote", "get-url", "origin"])
    revision = _git_value(["rev-parse", "--short", "HEAD"])
    branch = _git_value(["branch", "--show-current"])
    print(f"远端: {remote}")
    print(f"分支: {branch}")
    print(f"版本: {revision}")

    if str(ACE_STEP_PATH) not in sys.path:
        sys.path.insert(0, str(ACE_STEP_PATH))

    ace_spec = importlib.util.find_spec("acestep")
    torch_spec = importlib.util.find_spec("torch")
    print(f"Python 包 acestep: {'可导入' if ace_spec else '不可导入'}")
    print(f"Python 包 torch: {'已安装' if torch_spec else '未安装'}")

    if not ace_spec:
        print("建议: 确认 13_tools/ace_step/acestep 存在，或重新克隆 ACE-Step。")
        return 1
    if not torch_spec:
        print("建议: 按 ACE-Step 文档安装 PyTorch 后再生成。")
        return 1

    missing_runtime_packages = _missing_ace_step_runtime_packages()
    if missing_runtime_packages:
        _print_ace_step_runtime_install_hint(missing_runtime_packages)
        return 1

    print("预检通过: 可以尝试生成或启动 Web UI。")
    return 0


def _build_generation_kwargs(
    *,
    duration: int,
    prompt: str,
    lyrics: str,
    infer_steps: int,
    guidance_scale: float,
    seed: int,
    output_path: str,
) -> dict:
    return {
        "audio_duration": duration,
        "prompt": prompt,
        "lyrics": lyrics,
        "infer_step": infer_steps,
        "guidance_scale": guidance_scale,
        "scheduler_type": "euler",
        "cfg_type": "cfg",
        "omega_scale": 10.0,
        "manual_seeds": str(seed) if seed != -1 else "",
        "guidance_interval": 0.5,
        "guidance_interval_decay": 0.0,
        "min_guidance_scale": 3.0,
        "use_erg_tag": False,
        "use_erg_lyric": False,
        "use_erg_diffusion": True,
        "oss_steps": [],
        "guidance_scale_text": 3.0,
        "guidance_scale_lyric": 3.0,
        "save_path": output_path,
    }


def generate_with_ace_step(
    lyrics: str,
    prompt: str,
    duration: int = -1,
    infer_steps: int = 50,
    guidance_scale: float = 7.0,
    seed: int = -1,
    output_path: str | None = None,
    cpu_offload: bool = True,
    bf16: bool = True
):
    """使用 ACE-Step 生成带歌词的音乐"""

    if not ACE_STEP_PATH.exists():
        raise FileNotFoundError(f"ACE-Step 目录不存在: {ACE_STEP_PATH}")

    if str(ACE_STEP_PATH) not in sys.path:
        sys.path.insert(0, str(ACE_STEP_PATH))

    from acestep.pipeline_ace_step import ACEStepPipeline

    if output_path is None:
        output_dir = REPO_ROOT / "04_generations" / "audio" / "raw"
        output_dir.mkdir(parents=True, exist_ok=True)
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        output_path = str(output_dir / f"ace_step_{timestamp}.wav")

    print(f"🎵 ACE-Step 本地歌词生成器")
    print(f"{'='*50}")
    print(f"📝 歌词: {len(lyrics)} 字符")
    print(f"🎨 风格: {prompt}")
    print(f"⏱️ 时长: {duration if duration > 0 else '随机'} 秒")
    print(f"🔢 步骤: {infer_steps}")
    print(f"🎯 引导: {guidance_scale}")
    print(f"🌱 种子: {seed}")
    print(f"💾 输出: {output_path}")
    print(f"{'='*50}")

    # 初始化管道
    print("🔄 正在加载模型...")
    pipeline = ACEStepPipeline(
        checkpoint_dir=None,  # 会自动下载
        dtype="bfloat16" if bf16 else "float32",
        torch_compile=False,
        cpu_offload=cpu_offload,
        overlapped_decode=False
    )

    print("✅ 模型加载完成!")
    print("🎶 开始生成音乐...")

    # 生成音乐
    start_time = time.time()

    try:
        pipeline(
            **_build_generation_kwargs(
                duration=duration,
                prompt=prompt,
                lyrics=lyrics,
                infer_steps=infer_steps,
                guidance_scale=guidance_scale,
                seed=seed,
                output_path=output_path,
            )
        )
    except ImportError as exc:
        if "torchcodec" in str(exc).lower():
            _print_ace_step_runtime_install_hint(["torchcodec"])
        raise

    elapsed = time.time() - start_time
    print(f"{'='*50}")
    print(f"✅ 生成成功!")
    print(f"⏱️ 用时: {elapsed:.2f} 秒")
    print(f"💾 文件: {output_path}")
    print(f"{'='*50}")

    return output_path


def main():
    parser = argparse.ArgumentParser(description="ACE-Step 本地歌词生成器")
    parser.add_argument("--check", action="store_true", help="检查 ACE-Step 本地环境，不加载模型")
    parser.add_argument("--lyrics", type=str, help="歌词文本")
    parser.add_argument("--prompt", type=str, help="风格描述")
    parser.add_argument("--theme", type=str, help="主题名称")
    parser.add_argument("--style", type=str, default="House", choices=["House", "Techno", "Trance"],
                        help="音乐风格")
    parser.add_argument("--duration", type=int, default=-1, help="音频时长（秒，-1为随机）")
    parser.add_argument("--steps", type=int, default=50, help="推理步骤数")
    parser.add_argument("--guidance", type=float, default=7.0, help="引导系数")
    parser.add_argument("--seed", type=int, default=-1, help="随机种子")
    parser.add_argument("--output", type=str, help="输出文件路径")
    parser.add_argument("--no-cpu-offload", action="store_true", help="禁用CPU offload（需要更多显存）")
    parser.add_argument("--fp32", action="store_true", help="使用float32精度（更慢但更兼容）")
    parser.add_argument("--dry-run", action="store_true", help="只解析参数并显示配置，不加载模型")

    args = parser.parse_args()

    if args.check:
        return check_ace_step_setup()

    # 确定歌词和提示
    lyrics, prompt = resolve_lyrics_and_prompt(args)

    if args.dry_run:
        print("ACE-Step 参数预览")
        print("=" * 50)
        print(f"风格: {args.style}")
        print(f"提示: {prompt}")
        print(f"歌词字符数: {len(lyrics)}")
        print(f"时长: {args.duration if args.duration > 0 else '随机'}")
        print(f"步骤: {args.steps}")
        print(f"引导: {args.guidance}")
        print(f"种子: {args.seed}")
        print(f"CPU Offload: {not args.no_cpu_offload}")
        print(f"精度: {'float32' if args.fp32 else 'bfloat16'}")
        return 0

    # 生成
    try:
        output_path = generate_with_ace_step(
            lyrics=lyrics,
            prompt=prompt,
            duration=args.duration,
            infer_steps=args.steps,
            guidance_scale=args.guidance,
            seed=args.seed,
            output_path=args.output,
            cpu_offload=not args.no_cpu_offload,
            bf16=not args.fp32
        )
    except ImportError as exc:
        if "torchcodec" in str(exc).lower():
            return 1
        raise

    print(f"\n🎉 完成！音乐已保存到: {output_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
