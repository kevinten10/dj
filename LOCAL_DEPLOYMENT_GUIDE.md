# 🏠 本地 AI 音乐生成模型部署指南

> 完整教程：从零开始部署本地 AI 音乐生成模型，无需联网，完全免费！

---

## 📋 目录

1. [系统要求检查](#-第一步系统要求检查)
2. [环境准备](#-第二步环境准备)
3. [安装 PyTorch](#-第三步安装-pytorch)
4. [安装 AudioCraft](#-第四步安装-audiocraft)
5. [下载模型](#-第五步下载模型)
6. [测试生成](#-第六步测试生成)
7. [常见问题解决](#-常见问题解决)

---

## 🔍 第一步：系统要求检查

### 运行系统检查脚本

```powershell
python check_system.py
```

这个脚本会检查：
- ✅ Python 版本（需要 3.9+）
- ✅ 磁盘空间（建议 10GB+）
- ✅ 内存大小（建议 8GB+）
- ✅ GPU/CUDA 支持
- ✅ 已安装的依赖

### 最低配置要求

| 组件 | 最低要求 | 推荐配置 |
|------|---------|---------|
| **Python** | 3.9+ | 3.10-3.12 |
| **磁盘空间** | 10 GB | 20 GB+ |
| **内存** | 8 GB | 16 GB+ |
| **GPU** | 无（CPU可用） | NVIDIA GTX 1060 6GB+ |
| **显存** | N/A | 6GB+ |

### 不同模型的硬件需求

| 模型 | 显存需求 | 内存需求 | 适合场景 |
|------|---------|---------|---------|
| **MusicGen Small** | 4GB | 8GB | 快速测试、CPU运行 |
| **MusicGen Medium** | 8GB | 12GB | 平衡选择 |
| **MusicGen Large** | 12GB+ | 16GB | 最佳音质 |
| **MusicGen Melody** | 12GB+ | 16GB | 旋律条件生成 |

---

## 🛠️ 第二步：环境准备

### 1. 确认 Python 版本

```powershell
python --version
# 应该显示 Python 3.9.x 或更高版本
```

如果版本过低，请从 [python.org](https://www.python.org/downloads/) 下载最新版。

### 2. 创建虚拟环境（推荐）

```powershell
# 创建虚拟环境
python -m venv venv

# 激活虚拟环境
# Windows:
.\venv\Scripts\activate

# macOS/Linux:
source venv/bin/activate
```

### 3. 升级 pip

```powershell
python -m pip install --upgrade pip
```

---

## 🔥 第三步：安装 PyTorch

PyTorch 是深度学习框架，根据你的硬件选择安装方式：

### 方案 A：有 NVIDIA GPU（推荐）

首先检查你的 CUDA 版本：

```powershell
nvidia-smi
```

查看右上角的 "CUDA Version"。

#### CUDA 12.1（最常见）

```powershell
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```

#### CUDA 11.8

```powershell
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

#### CUDA 12.4（最新）

```powershell
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124
```

### 方案 B：只有 CPU

```powershell
pip install torch torchvision torchaudio
```

⚠️ **注意**：CPU 版本生成速度会很慢，建议仅用于测试 Small 模型。

### 验证 PyTorch 安装

```powershell
python -c "import torch; print('PyTorch:', torch.__version__); print('CUDA:', torch.cuda.is_available()); print('GPU:', torch.cuda.get_device_name(0) if torch.cuda.is_available() else 'None')"
```

**期望输出：**
```
PyTorch: 2.2.0+cu121
CUDA: True
GPU: NVIDIA GeForce RTX 3060
```

---

## 🎵 第四步：安装 AudioCraft

AudioCraft 是 Meta 开源的音频生成库，包含 MusicGen 模型。

### 安装方式

```powershell
pip install audiocraft
```

### 验证安装

```powershell
python -c "from audiocraft.models import MusicGen; print('AudioCraft 安装成功!')"
```

### 可选：安装额外依赖（推荐）

```powershell
pip install transformers accelerate
```

---

## 📥 第五步：下载模型

模型会在**首次使用时自动下载**，但你也可以预先下载：

### 使用脚本预下载

```powershell
python -c "
from audiocraft.models import MusicGen
print('正在下载 MusicGen Small 模型...')
model = MusicGen.get_pretrained('facebook/musicgen-small')
print('下载完成!')
"
```

### 模型文件位置

下载的模型会保存在：
- **Windows**: `C:\Users\你的用户名\.cache\huggingface\hub\`
- **macOS/Linux**: `~/.cache/huggingface/hub/`

### 模型大小

| 模型 | 大小 | 下载时间（宽带） |
|------|------|----------------|
| Small | ~1 GB | 2-5 分钟 |
| Medium | ~3 GB | 5-10 分钟 |
| Large | ~6 GB | 10-20 分钟 |
| Melody | ~6 GB | 10-20 分钟 |

---

## 🎧 第六步：测试生成

### 快速测试（Small 模型）

```powershell
python 13_tools/scripts/make_dj_track_local.py --idea "测试音乐，简单的节拍" --model facebook/musicgen-small --duration 10
```

### 完整测试（根据你的配置选择）

**如果你有 12GB+ 显存：**
```powershell
python 13_tools/scripts/make_dj_track_local.py --idea "Tech House派对音乐，清晰的底鼓" --model facebook/musicgen-large --cuda --duration 30
```

**如果你有 6-8GB 显存：**
```powershell
python 13_tools/scripts/make_dj_track_local.py --idea "Deep House放松音乐，温暖的感觉" --model facebook/musicgen-medium --cuda --duration 30
```

**如果你只有 CPU：**
```powershell
python 13_tools/scripts/make_dj_track_local.py --idea "简单的House节拍，适合练习" --model facebook/musicgen-small --duration 10
```

### 预期生成时间

| 配置 | Small 模型 (10秒音频) | Large 模型 (30秒音频) |
|------|----------------------|----------------------|
| RTX 4090 | ~5 秒 | ~15 秒 |
| RTX 3060 | ~10 秒 | ~30 秒 |
| GTX 1060 | ~20 秒 | ~60 秒 |
| CPU (i7) | ~2-3 分钟 | ~10 分钟+ |

---

## 🚀 使用本项目生成音乐

### 方式一：使用本地模型脚本

```powershell
# 基本用法
python 13_tools/scripts/make_dj_track_local.py --idea "你的想法" --style "House" --bpm 120

# 使用 GPU 加速
python 13_tools/scripts/make_dj_track_local.py --idea "你的想法" --cuda

# 指定模型大小
python 13_tools/scripts/make_dj_track_local.py --idea "你的想法" --model facebook/musicgen-large

# 指定时长（秒）
python 13_tools/scripts/make_dj_track_local.py --idea "你的想法" --duration 60
```

### 方式二：使用 Demo 生成器

```powershell
python generate_demo_local.py
```

### 方式三：交互式菜单

```powershell
.\start.ps1
# 然后选择 "本地模型生成"
```

---

## ❗ 常见问题解决

### 问题 1：CUDA out of memory（显存不足）

**解决方案：**
```powershell
# 使用更小的模型
--model facebook/musicgen-small

# 减少生成时长
--duration 10

# 使用 CPU（慢但稳定）
# 移除 --cuda 参数
```

### 问题 2：模型下载很慢或失败

**解决方案：**

1. **使用镜像源（中国用户）**
   ```powershell
   # 设置 HuggingFace 镜像
   set HF_ENDPOINT=https://hf-mirror.com
   ```

2. **手动下载模型**
   - 访问 https://huggingface.co/facebook/musicgen-small
   - 下载模型文件
   - 放入 `~/.cache/huggingface/hub/`

### 问题 3：CPU 生成太慢

**解决方案：**
- 使用 Small 模型
- 减少生成时长到 10-20 秒
- 考虑使用云端 API 代替

### 问题 4：ImportError: No module named 'audiocraft'

**解决方案：**
```powershell
# 重新安装
pip uninstall audiocraft
pip install audiocraft

# 或者使用 conda
conda install -c conda-forge audiocraft
```

### 问题 5：音频生成成功但无法播放

**解决方案：**
- 检查文件是否在 `08_exports/dj_ready/`
- 使用 VLC 或 Windows Media Player 播放
- 检查音频文件是否完整

---

## 💡 优化建议

### 1. 使用 SSD
模型文件较大（1-6GB），使用 SSD 可以显著加快加载速度。

### 2. 保持模型缓存
不要删除 `~/.cache/huggingface/` 目录，否则需要重新下载模型。

### 3. 批量生成
如果需要生成多首音乐，建议写一个脚本：

```powershell
# batch_generate.ps1
$styles = @("House", "Techno", "Trance")

foreach ($style in $styles) {
    python 13_tools/scripts/make_dj_track_local.py --idea "$style 练习曲" --style $style --model facebook/musicgen-small
}
```

### 4. 监控显存使用
```powershell
# 在另一个终端运行
nvidia-smi -l 1
```

---

## 📊 性能优化对比

| 优化项 | 优化前 | 优化后 | 提升 |
|--------|--------|--------|------|
| 使用 GPU 代替 CPU | 3分钟 | 10秒 | 18x |
| 使用 Small 代替 Large | 60秒 | 10秒 | 6x |
| 使用 SSD 代替 HDD | 30秒 | 10秒 | 3x |
| 减少时长 60s→30s | 60秒 | 30秒 | 2x |

---

## 🎯 下一步

部署成功后，你可以：

1. **生成练习曲**：用于 DJ 练习
2. **批量生成**：创建你的曲库
3. **尝试不同模型**：Small/Medium/Large 对比
4. **调整参数**：temperature、top_k 等

查看完整使用指南：[AI_MODELS_GUIDE.md](AI_MODELS_GUIDE.md)

---

## 📞 获取帮助

如果遇到问题：

1. 运行 `python check_system.py` 检查配置
2. 查看 [AudioCraft GitHub](https://github.com/facebookresearch/audiocraft)
3. 查看 [PyTorch 安装指南](https://pytorch.org/get-started/locally/)

---

**祝你部署顺利！享受本地 AI 音乐生成的乐趣！** 🎵✨
