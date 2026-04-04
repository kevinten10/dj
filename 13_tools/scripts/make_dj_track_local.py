#!/usr/bin/env python3
"""
DJ-ready track generator using LOCAL AI models.
Supports MusicGen and other local audio generation models.
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
logger = logging.getLogger("ai-dj-local")


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def _now_stamp() -> str:
    return _dt.datetime.now().strftime("%Y%m%d_%H%M%S")


def _slugify(s: str, max_len: int = 48) -> str:
    import re
    slug_re = re.compile(r"[^a-zA-Z0-9_-]+")
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


def generate_with_musicgen(
    prompt: str,
    duration: int,
    model_name: str,
    output_path: Path,
    temperature: float = 1.0,
    top_k: int = 250,
    top_p: float = 0.0,
    cfg_coef: float = 3.0,
    use_cuda: bool = False
) -> None:
    """
    Generate audio using MusicGen.
    
    Models available:
    - facebook/musicgen-small (300M params, ~1GB)
    - facebook/musicgen-medium (1.5B params, ~3GB)
    - facebook/musicgen-large (3.3B params, ~6GB)
    - facebook/musicgen-melody (3.3B params, melody-conditioned)
    """
    logger.info(f"🎵 使用 MusicGen 模型: {model_name}")
    logger.info(f"📝 提示词: {prompt[:80]}...")
    logger.info(f"⏱️  时长: {duration}秒")
    
    try:
        import torch
        from audiocraft.models import MusicGen
        from audiocraft.data.audio import audio_write
    except ImportError:
        logger.error("❌ 缺少依赖! 请运行: pip install torch audiocraft")
        logger.error("或者查看文档: 12_docs/local_models.md")
        raise RuntimeError("需要安装 audiocraft 和 torch")
    
    # Set device
    if use_cuda and torch.cuda.is_available():
        device = "cuda"
        logger.info("🚀 使用 CUDA (GPU)")
    elif use_cuda and torch.backends.mps.is_available():
        device = "mps"
        logger.info("🚀 使用 MPS (Apple Silicon)")
    else:
        device = "cpu"
        logger.info("💻 使用 CPU (较慢，建议使用 GPU)")
    
    logger.info(f"📥 加载模型 {model_name}...")
    model = MusicGen.get_pretrained(model_name, device=device)
    
    # Set generation parameters
    model.set_generation_params(
        duration=duration,
        temperature=temperature,
        top_k=top_k,
        top_p=top_p if top_p > 0 else None,
        cfg_coef=cfg_coef
    )
    
    logger.info("🎨 开始生成...")
    descriptions = [prompt]
    wav = model.generate(descriptions)
    
    logger.info("💾 保存音频...")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    audio_write(
        str(output_path.with_suffix("")),
        wav[0].cpu(),
        model.sample_rate,
        strategy="loudness",
        loudness_compressor=True
    )
    
    logger.info(f"✅ 音频已保存到: {output_path}")


def main(argv: list[str]) -> int:
    p = argparse.ArgumentParser(description="本地 AI DJ 曲目生成器")
    p.add_argument("--idea", "-i", required=True, help="曲目创意/主题")
    p.add_argument("--style", "-s", default="", help="音乐风格 (例如: Techno, House)")
    p.add_argument("--bpm", "-b", type=int, default=128, help="目标 BPM")
    p.add_argument("--duration", "-d", type=int, default=120, help="音频时长（秒）")
    p.add_argument("--model", "-m", default="facebook/musicgen-small", 
                   choices=["facebook/musicgen-small", "facebook/musicgen-medium", 
                            "facebook/musicgen-large", "facebook/musicgen-melody"],
                   help="使用的模型")
    p.add_argument("--temperature", "-t", type=float, default=1.0, 
                   help="温度参数 (0.0-2.0, 越高越随机)")
    p.add_argument("--top-k", type=int, default=250, help="Top-k 采样")
    p.add_argument("--top-p", type=float, default=0.0, help="Top-p 采样 (0=禁用)")
    p.add_argument("--cfg", type=float, default=3.0, help="CFG 系数")
    p.add_argument("--cuda", action="store_true", help="使用 CUDA (如果可用)")
    p.add_argument("--play", action="store_true", help="生成后自动播放")
    p.add_argument("--verbose", "-v", action="store_true", help="启用调试日志")
    
    args = p.parse_args(argv)
    if args.verbose:
        logger.setLevel(logging.DEBUG)
    
    root = _repo_root()
    stamp = _now_stamp()
    slug = _slugify(args.style or args.idea)
    
    raw_audio_path = root / "04_generations" / "audio" / "raw" / f"{stamp}_{slug}.wav"
    out_audio_path = root / "08_exports" / "dj_ready" / f"{stamp}_{slug}.wav"
    meta_path = root / "04_generations" / "metadata" / f"{stamp}_{slug}.json"
    
    # Build prompt
    prompt_parts = []
    if args.style:
        prompt_parts.append(f"Genre: {args.style}")
    prompt_parts.append(f"BPM: {args.bpm}")
    prompt_parts.append("Structure: [Intro], [Verse], [Build Up], [Drop], [Break], [Drop], [Outro]")
    prompt_parts.append("Mix: Clear kicks, professional mixing, DJ-friendly")
    prompt_parts.append(f"Theme: {args.idea}")
    music_prompt = ", ".join(prompt_parts)
    
    try:
        generate_with_musicgen(
            prompt=music_prompt,
            duration=args.duration,
            model_name=args.model,
            output_path=raw_audio_path,
            temperature=args.temperature,
            top_k=args.top_k,
            top_p=args.top_p,
            cfg_coef=args.cfg,
            use_cuda=args.cuda
        )
        
        # Copy to exports
        out_audio_path.parent.mkdir(parents=True, exist_ok=True)
        if raw_audio_path.exists():
            out_audio_path.write_bytes(raw_audio_path.read_bytes())
        
        # Save metadata
        meta_info = {
            "version": "2026.1-local",
            "timestamp": stamp,
            "params": vars(args),
            "prompt": music_prompt,
            "model": args.model,
            "generator": "local_musicgen"
        }
        meta_path.parent.mkdir(parents=True, exist_ok=True)
        meta_path.write_text(json.dumps(meta_info, indent=2, ensure_ascii=False), encoding="utf-8")
        
        logger.info(f"🎉 成功! 曲目已导出到: {out_audio_path}")
        
        if args.play and out_audio_path.exists():
            _start_file(out_audio_path)
        
        return 0
        
    except Exception as e:
        logger.error(f"❌ 生成失败: {e}")
        if args.verbose:
            import traceback
            traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
