# 本地 AI 模型使用指南

本指南将帮助你使用本地部署的 AI 模型生成 DJ 音乐，无需依赖外部 API。

---

## 🎵 支持的本地模型

### 1. MusicGen (Meta)

MusicGen 是 Meta 开源的文本到音乐生成模型，有多个版本可选：

| 模型 | 参数 | 显存需求 | 磁盘空间 | 推荐场景 |
|------|------|----------|----------|----------|
| `facebook/musicgen-small` | 300M | 4GB+ | ~1GB | 入门级，CPU 可运行 |
| `facebook/musicgen-medium` | 1.5B | 8GB+ | ~3GB | 平衡选择 |
| `facebook/musicgen-large` | 3.3B | 12GB+ | ~6GB | 高质量生成 |
| `facebook/musicgen-melody` | 3.3B | 12GB+ | ~6GB | 支持旋律条件 |

---

## 🛠️ 环境配置

### 方法一：使用 PyTorch（推荐）

#### 1. 安装基础依赖

```powershell
# 升级 pip
python -m pip install --upgrade pip

# 安装 PyTorch (选择适合你系统的版本)

# Windows - CUDA 版本 (推荐，如果你有 NVIDIA GPU)
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121

# Windows - CPU 版本
pip install torch torchvision torchaudio

# macOS
pip install torch torchvision torchaudio
```

#### 2. 安装 Audiocraft (MusicGen)

```powershell
# 安装 audiocraft
pip install audiocraft

# 可选：安装额外依赖
pip install transformers accelerate
```

#### 3. 验证安装

```powershell
python -c "import torch; import audiocraft; print('✅ 安装成功!'); print(f'PyTorch: {torch.__version__}'); print(f'CUDA可用: {torch.cuda.is_available()}')"
```

---

## 🚀 快速开始

### 基础使用

使用最小模型（small）生成曲目：

```powershell
python 13_tools/scripts/make_dj_track_local.py --idea "午夜 Tech House 派对" --style "Tech House" --bpm 126 --duration 90 --play
```

### 使用 GPU 加速

如果你有 NVIDIA GPU，添加 `--cuda` 参数：

```powershell
python 13_tools/scripts/make_dj_track_local.py --idea "赛博朋克 Techno" --style "Techno" --bpm 130 --duration 120 --cuda --play
```

### 使用更大的模型

```powershell
# 使用 medium 模型
python 13_tools/scripts/make_dj_track_local.py --idea "夏日 Deep House" --style "Deep House" --bpm 118 --model "facebook/musicgen-medium" --cuda

# 使用 large 模型 (需要更多显存)
python 13_tools/scripts/make_dj_track_local.py --idea "史诗 Progressive Trance" --style "Trance" --bpm 138 --model "facebook/musicgen-large" --cuda
```

---

## 🎛️ 高级参数调优

### 温度参数 (Temperature)

控制生成的随机性：

```powershell
# 保守生成（更可预测）
python 13_tools/scripts/make_dj_track_local.py --idea "标准 House 节拍" --temperature 0.7

# 创意生成（更多变化）
python 13_tools/scripts/make_dj_track_local.py --idea "实验电子" --temperature 1.5
```

### CFG 系数 (Classifier-Free Guidance)

控制提示词遵循程度：

```powershell
# 严格遵循提示词
python 13_tools/scripts/make_dj_track_local.py --idea "只有底鼓和贝斯" --cfg 5.0

# 更自由的创作
python 13_tools/scripts/make_dj_track_local.py --idea "自由氛围" --cfg 1.5
```

### 采样参数

```powershell
# Top-k 采样
python 13_tools/scripts/make_dj_track_local.py --idea "..." --top-k 100

# Top-p (nucleus) 采样
python 13_tools/scripts/make_dj_track_local.py --idea "..." --top-p 0.9
```

---

## 💡 使用技巧

### 1. 提示词工程

好的提示词 = 更好的结果：

```powershell
# 不好的提示词
--idea "好音乐"

# 好的提示词
--idea "午夜俱乐部场景，深邃的 Tech House，清晰的底鼓，滚动贝斯线，温暖的合成器垫，适合混音的清晰 Intro 和 Outro"
```

### 2. 生成时长建议

- **短片段测试**：30-60 秒，快速迭代想法
- **练习曲目**：90-120 秒，完整结构
- **表演曲目**：180-300 秒，完整歌曲

### 3. 批量生成

创建一个 PowerShell 脚本批量生成：

```powershell
# batch_generate.ps1
$ideas = @(
    "Deep House, 118 BPM,  soulful vibe",
    "Tech House, 126 BPM, driving beat",
    "Progressive House, 128 BPM, melodic"
)

foreach ($idea in $ideas) {
    python 13_tools/scripts/make_dj_track_local.py --idea $idea --style "House" --bpm 124 --duration 90 --cuda
}
```

---

## 🖥️ 硬件要求

### 最低配置 (CPU)
- **CPU**: 4 核心以上
- **内存**: 16GB+
- **磁盘空间**: 2GB+
- **预计速度**: 10-30 倍实时（即 30 秒音频需要 5-15 分钟）

### 推荐配置 (GPU)
- **GPU**: NVIDIA GPU 4GB+ VRAM
- **CPU**: 4 核心以上
- **内存**: 16GB+
- **磁盘空间**: 5GB+
- **预计速度**: 1-3 倍实时

### 理想配置
- **GPU**: NVIDIA RTX 3060 或更好 (8GB+ VRAM)
- **CPU**: 8 核心以上
- **内存**: 32GB+
- **磁盘空间**: 10GB+ SSD
- **预计速度**: 接近实时

---

## 🔧 故障排除

### 问题：CUDA 不可用

**解决方案**：
```powershell
# 检查 PyTorch CUDA 支持
python -c "import torch; print(torch.cuda.is_available())"

# 如果是 False，重新安装 CUDA 版本的 PyTorch
pip uninstall torch
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```

### 问题：显存不足 (OOM)

**解决方案**：
1. 使用更小的模型：`facebook/musicgen-small`
2. 减少生成时长：`--duration 30`
3. 使用 CPU 而不是 GPU（移除 `--cuda`）

### 问题：模型下载很慢

**解决方案**：
模型会自动缓存到 `~/.cache/huggingface/`，下载完成后会很快。

### 问题：音频质量不如预期

**改进方法**：
1. 使用更大的模型
2. 调整 temperature (0.7-1.2)
3. 优化提示词，更具体
4. 多次生成选择最佳的

---

## 📊 性能对比

| 模型 | CPU (i7) | GPU (RTX 3060) | 质量 |
|------|-----------|-----------------|------|
| Small | ~15x 实时 | ~2x 实时 | ⭐⭐⭐ |
| Medium | ~30x 实时 | ~3x 实时 | ⭐⭐⭐⭐ |
| Large | ~60x 实时 | ~5x 实时 | ⭐⭐⭐⭐⭐ |

---

## 🎓 进阶主题

### 使用预设与本地模型结合

你可以结合风格预设和本地模型：

```powershell
# 先查看可用预设
python 13_tools/scripts/generate_with_preset.py --list

# 然后使用提示词灵感作为本地模型的输入
python 13_tools/scripts/make_dj_track_local.py --idea "Tech House, driving beat, rolling bassline, crisp percussion, Friday night party vibe, DJ-ready with clear structure" --style "Tech House" --bpm 126 --cuda
```

### 与曲目库管理器配合

本地生成的曲目会自动保存到 `08_exports/dj_ready/`，可以使用库管理器：

```powershell
# 列出所有本地生成的曲目
python 13_tools/scripts/library_manager.py list
```

---

## 🤝 贡献

如果你发现更好的提示词或配置，欢迎分享！

---

*记住：本地模型需要一些耐心，但完全掌控在你手中！* 🎧
