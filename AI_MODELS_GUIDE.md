# 🤖 AI 音乐生成模型完整指南

> 本指南整理了所有可用的云端和本地 AI 音乐生成模型，帮助你选择最适合的方案！

---

## ☁️ 云端模型（Cloud API）

### 1. MiniMax Music（本项目已集成）

| 属性 | 详情 |
|------|------|
| **提供商** | MiniMax (中国) |
| **官网** | https://platform.minimax.io/ |
| **模型版本** | Music 2.5 (2026 最新) |
| **音质** | ⭐⭐⭐⭐⭐ 专业级 |
| **生成速度** | ~30-60 秒 |
| **成本** | 需要 API Key（有免费额度） |
| **网络要求** | 需要联网 |
| **中文支持** | ✅ 完美支持 |

**优点：**
- 音质极佳，接近商业发行质量
- 支持 14+ 结构标签（Intro/Verse/Chorus/Drop 等）
- 支持歌词生成
- 支持多种风格

**缺点：**
- 需要 API Key
- 需要联网
- 有使用限制（免费额度用完后收费）

**本项目使用方法：**
```powershell
python 13_tools/scripts/make_dj_track_minimax.py --idea "你的想法" --style "House"
```

---

### 2. Suno AI

| 属性 | 详情 |
|------|------|
| **官网** | https://www.suno.ai/ |
| **模型版本** | Suno v3 |
| **音质** | ⭐⭐⭐⭐⭐ 极高 |
| **生成速度** | ~30 秒 |
| **成本** | 免费额度 + 付费订阅 |
| **网络要求** | 需要联网 |
| **中文支持** | ✅ 支持 |

**优点：**
- 目前公认最强的 AI 音乐生成
- 人声质量极高
- 支持完整歌曲结构
- 支持歌词创作

**缺点：**
- 免费版有水印
- 商业使用需要付费
- API 访问受限

**使用方法：**
- 直接访问官网使用网页版
- 或使用第三方 API 封装

---

### 3. Udio

| 属性 | 详情 |
|------|------|
| **官网** | https://www.udio.com/ |
| **音质** | ⭐⭐⭐⭐⭐ 极高 |
| **生成速度** | ~30-60 秒 |
| **成本** | 免费额度 + 付费订阅 |
| **网络要求** | 需要联网 |
| **中文支持** | ⚠️ 有限 |

**优点：**
- 与 Suno 齐名的顶级模型
- 音乐质量极高
- 支持多种风格

**缺点：**
- 中文支持不如 Suno
- 免费版有限制

---

### 4. Stable Audio（Stability AI）

| 属性 | 详情 |
|------|------|
| **提供商** | Stability AI |
| **官网** | https://www.stableaudio.com/ |
| **音质** | ⭐⭐⭐⭐ 很好 |
| **生成速度** | ~20-40 秒 |
| **成本** | 免费版 + 付费订阅 |
| **网络要求** | 需要联网 |
| **中文支持** | ⚠️ 提示词需英文 |

**优点：**
- 生成速度快
- 支持音频到音频生成
- 可以生成音效和氛围音乐

**缺点：**
- 不如 Suno/Udio 适合歌曲
- 更适合背景音乐/音效

---

### 5. Google MusicLM / Lyria

| 属性 | 详情 |
|------|------|
| **提供商** | Google |
| **状态** | 仅内部使用/有限开放 |
| **音质** | ⭐⭐⭐⭐ 很好 |
| **可用性** | 大多数用户无法使用 |

**注意：** 目前主要供研究人员和特定合作伙伴使用，普通用户暂无法使用。

---

### 6. OpenAI Jukebox

| 属性 | 详情 |
|------|------|
| **提供商** | OpenAI |
| **状态** | 开源但已停止维护 |
| **音质** | ⭐⭐⭐ 一般 |
| **可用性** | 可以自己部署 |

**注意：** 虽然是开创性工作，但音质已落后于新模型，且需要大量计算资源。

---

## 🏠 本地模型（Local Deployment）

### 1. MusicGen（Meta）- 本项目已集成

| 属性 | 详情 |
|------|------|
| **提供商** | Meta (Facebook) |
| **开源地址** | https://github.com/facebookresearch/audiocraft |
| **模型大小** | Small(300M) / Medium(1.5B) / Large(3.3B) / Melody(3.3B) |
| **音质** | ⭐⭐⭐⭐ 很好 |
| **生成速度** | CPU: 慢 / GPU: 快 |
| **成本** | 完全免费 |
| **网络要求** | 首次下载后完全离线 |
| **显存需求** | Small: 4GB / Large: 12GB+ |

**优点：**
- ✅ 完全免费
- ✅ 完全离线（隐私保护）
- ✅ 可商用（MIT 许可证）
- ✅ 多种模型大小可选
- ✅ 支持旋律条件生成（Melody 模型）

**缺点：**
- 需要较好的硬件（GPU 推荐）
- 首次下载模型较大（1-6GB）
- 音质略低于顶级云端模型

**本项目使用方法：**
```powershell
# Small 模型（快速，适合测试）
python 13_tools/scripts/make_dj_track_local.py --idea "你的想法" --model facebook/musicgen-small

# Large 模型（最佳质量）
python 13_tools/scripts/make_dj_track_local.py --idea "你的想法" --model facebook/musicgen-large --cuda
```

**安装方法：**
```powershell
pip install torch audiocraft
```

---

### 2. Riffusion

| 属性 | 详情 |
|------|------|
| **开源地址** | https://github.com/riffusion/riffusion |
| **技术** | Stable Diffusion for Audio |
| **音质** | ⭐⭐⭐ 一般 |
| **特点** | 实时生成，适合交互式应用 |
| **成本** | 免费开源 |

**优点：**
- 可以实时生成
- 支持通过图像生成音乐
- 轻量级

**缺点：**
- 音质不如 MusicGen
- 更适合实验/艺术用途

---

### 3. AudioLDM / AudioLDM 2

| 属性 | 详情 |
|------|------|
| **提供商** | 学术研究项目 |
| **开源地址** | https://github.com/haoheliu/AudioLDM |
| **音质** | ⭐⭐⭐⭐ 很好 |
| **特点** | 基于 Latent Diffusion |
| **成本** | 免费开源 |

**优点：**
- 音质不错
- 支持文本到音频
- 支持音频编辑

**缺点：**
- 设置较复杂
- 社区支持不如 MusicGen

---

### 4. Stable Audio Open

| 属性 | 详情 |
|------|------|
| **提供商** | Stability AI |
| **开源地址** | https://github.com/Stability-AI/stable-audio-tools |
| **音质** | ⭐⭐⭐⭐ 很好 |
| **特点** | Stable Audio 的开源版本 |
| **成本** | 免费开源 |

**优点：**
- 商业级音质
- 支持较长音频（最长 47 秒）
- 完全开源可商用

**缺点：**
- 需要较好的 GPU
- 设置相对复杂

---

### 5. MAGNeT（Meta）

| 属性 | 详情 |
|------|------|
| **提供商** | Meta |
| **开源地址** | https://github.com/facebookresearch/audiocraft/blob/main/docs/MAGNET.md |
| **音质** | ⭐⭐⭐⭐ 很好 |
| **特点** | MusicGen 的改进版，更快 |
| **成本** | 免费开源 |

**优点：**
- 比 MusicGen 生成更快
- 音质相当
- 非自回归生成

**缺点：**
- 较新，社区资源较少
- 需要 audiocraft 最新版

---

## 📊 模型对比总表

### 云端模型对比

| 模型 | 音质 | 速度 | 成本 | 中文 | 推荐场景 |
|------|:----:|:----:|:----:|:----:|----------|
| **MiniMax** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | 免费额度 | ✅ | 本项目默认，中文友好 |
| **Suno** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | 免费+付费 | ✅ | 最高音质，歌曲创作 |
| **Udio** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | 免费+付费 | ⚠️ | 最高音质，英文为主 |
| **Stable Audio** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | 免费+付费 | ⚠️ | 音效/背景音乐 |

### 本地模型对比

| 模型 | 音质 | 速度 | 显存 | 易用性 | 推荐场景 |
|------|:----:|:----:|:----:|:------:|----------|
| **MusicGen Small** | ⭐⭐⭐ | ⭐⭐⭐ | 4GB | ⭐⭐⭐⭐⭐ | 快速测试，CPU可用 |
| **MusicGen Large** | ⭐⭐⭐⭐ | ⭐⭐⭐ | 12GB | ⭐⭐⭐⭐⭐ | 最佳本地音质 |
| **Stable Audio Open** | ⭐⭐⭐⭐ | ⭐⭐⭐ | 8GB | ⭐⭐⭐ | 商业级本地生成 |
| **MAGNeT** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | 8GB | ⭐⭐⭐⭐ | 快速本地生成 |

---

## 🎯 选择建议

### 如果你是初学者

**推荐方案：**
1. **先用 MiniMax（云端）** - 本项目已集成，中文友好
2. **再试 MusicGen Small（本地）** - 了解本地生成流程

### 如果你追求最高音质

**推荐方案：**
1. **Suno / Udio（云端）** - 目前最强音质
2. **MusicGen Large（本地）** - 本地最强

### 如果你需要大量生成

**推荐方案：**
1. **MusicGen（本地）** - 完全免费，无限制
2. **Stable Audio Open（本地）** - 商业级质量

### 如果你关注隐私

**推荐方案：**
1. **MusicGen（本地）** - 完全离线
2. **Stable Audio Open（本地）** - 完全离线

---

## 🚀 快速开始

### 云端方案（MiniMax - 本项目已集成）

```powershell
# 1. 获取 API Key
# 访问 https://platform.minimax.io/

# 2. 配置环境
. .\13_tools\configs\minimax_env.ps1

# 3. 生成音乐
python 13_tools/scripts/make_dj_track_minimax.py --idea "你的想法"
```

### 本地方案（MusicGen - 本项目已集成）

```powershell
# 1. 安装依赖
pip install torch audiocraft

# 2. 生成音乐（首次会自动下载模型）
python 13_tools/scripts/make_dj_track_local.py --idea "你的想法" --model facebook/musicgen-small
```

---

## 📚 更多资源

- [MusicGen 论文](https://arxiv.org/abs/2306.05284)
- [AudioCraft 文档](https://facebookresearch.github.io/audiocraft/)
- [Suno 官网](https://www.suno.ai/)
- [Udio 官网](https://www.udio.com/)
- [MiniMax 平台](https://platform.minimax.io/)

---

*最后更新：2026年4月 | AI 音乐技术发展迅速，建议定期查看最新模型*
