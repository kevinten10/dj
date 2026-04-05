# AI-DJ 工作区 (2026 版) 🎧

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![MiniMax Music 2.5](https://img.shields.io/badge/AI--Model-MiniMax%20Music%202.5-orange.svg)](https://platform.minimax.io/)

> **AI 创意与专业 DJ 表演之间的桥梁。**
> 一个结构化的工作区，用于生成、分析和练习 AI 生成的曲目。专为 **Hercules** 控制器和 **DJUCED** 优化。

---

## ⚡ 快速开始（30秒上手）

### 如果你是零基础（推荐从这里开始！）

1. **双击运行**：
   ```
   start.ps1
   ```

2. **然后看这个**：
   - 🚀 [30分钟快速上手指南](12_docs/quickstart_guide.md) - 30分钟完成第一次混音！
   - 📖 [Hercules Inpulse 200 MK2 完全指南](12_docs/hercules_inpulse_200_mk2_guide.md) - 你的专属设备教程！

### Windows 用户

双击运行：
```
start.ps1
```

或者在 PowerShell 中：
```powershell
.\start.ps1
```

### 所有人

```powershell
# 1. 安装依赖
python -m pip install -r requirements.txt

# 2. 启动交互式菜单
python 13_tools/scripts/interactive_generator.py
```

就这么简单！剩下的交给菜单引导你完成！

---

## 🌟 核心功能

- 🤖 **MiniMax Music 2.5 云端支持**：使用最新的 2026 模型，14+ 结构标签，精准的曲目编排。
- 🏠 **本地模型支持**：使用 MusicGen (Meta) 离线生成音乐，多种模型大小（300M 到 3.3B 参数）。
- 🎚️ **DJ 友好编排**：自动生成 `[Intro]` 和 `[Outro]` 段落，专为无缝混音设计。
- 🧪 **高保真音频**：生成 320kbps MP3 或 WAV 文件，44.1kHz 采样率，确保俱乐部级别的低频和清晰度。
- 📊 **自动元数据**：每首歌都存档完整的生成提示词、歌词和 API 响应，供将来参考。
- ⚖️ **2026 合规性**：预配置的 C2PA 水印和商业权利验证清单。
- 📚 **完整学习路径**：从入门到高级，结构化课程和练习计划。
- 🎨 **风格预设**：12+ 预配置音乐风格（Deep House、Techno、Trance 等），带优化提示词。
- 📁 **曲目库管理**：组织、筛选和创建 AI 生成曲目的 Set List。

---

## 📂 工作区结构

```text
dj/
├── 04_generations/          # [曲目存档]
│   ├── audio/raw/           # 脚本生成的每首歌
│   └── metadata/            # 每首歌的提示词/API 日志
├── 08_exports/              # [DJ 曲库]
│   ├── dj_ready/            # 已选择的曲目，供 DJUCED 导入
│   └── set_lists/           # 创建的 Set List
├── 12_docs/                 # [知识库]
│   ├── quickstart_guide.md  # 30分钟快速上手指南（必读！）
│   ├── hercules_inpulse_200_mk2_guide.md  # 你的专属设备指南
│   ├── learning_path.md     # 完整的入门到高级 DJ 课程
│   ├── techniques_library.md # DJ 技巧综合参考
│   ├── local_models.md      # 本地模型使用指南
│   └── checklists/          # 质量和许可标准
└── 13_tools/                # [自动化工具]
    ├── scripts/
    │   ├── make_dj_track_minimax.py   # 云端曲目生成器
    │   ├── make_dj_track_local.py     # 本地模型生成器
    │   ├── practice_plan.py            # 练习计划生成器
    │   ├── generate_with_preset.py     # 基于预设的生成器
    │   ├── library_manager.py          # 曲目库管理器
    │   └── interactive_generator.py    # 交互式菜单（推荐！）
    ├── presets/
    │   └── styles.json       # 12+ 风格预设
    └── configs/              # 环境模板
```

---

## 🚀 开始使用

### 1. 安装

克隆仓库并安装所需依赖：
```powershell
git clone https://github.com/kevinten10/dj.git
cd dj
python -m pip install -r requirements.txt
```

### 2. 配置凭据（云端 API）

复制环境模板并添加你的 [MiniMax API Key](https://platform.minimax.io/)：
```powershell
cp 13_tools/configs/minimax_env.example.ps1 13_tools/configs/minimax_env.ps1
# 编辑 minimax_env.ps1 并添加你的 key，然后运行：
. .\13_tools\configs\minimax_env.ps1
```

### 3. 生成曲目

#### 选项 A：交互式菜单（推荐，最简单！）

```powershell
.\start.ps1
# 或
python 13_tools/scripts/interactive_generator.py
```

#### 选项 B：云端 API (MiniMax)

生成一首高能量的 Techno 练习曲：
```powershell
python 13_tools/scripts/make_dj_track_minimax.py --idea "Peak hour techno, industrial warehouse vibe" --style "Techno" --bpm 128 --instrumental --play
```

#### 选项 C：本地模型 (MusicGen)

使用 Meta 的 MusicGen 离线生成音乐：
```powershell
# 使用 Small 模型基础生成
python 13_tools/scripts/make_dj_track_local.py --idea "Midnight Tech House party" --style "Tech House" --bpm 126 --duration 90 --play

# 使用 GPU 加速（如果你有 NVIDIA GPU）
python 13_tools/scripts/make_dj_track_local.py --idea "Cyberpunk Techno" --style "Techno" --bpm 130 --cuda --play
```

详细设置说明请查看 [本地模型指南](12_docs/local_models.md)。

#### 选项 D：使用风格预设

列出可用预设：
```powershell
python 13_tools/scripts/generate_with_preset.py --list
```

使用预设生成：
```powershell
python 13_tools/scripts/generate_with_preset.py --preset tech_house --idea "Friday night party vibe" --instrumental --play
```

### 4. 获取练习计划

生成个性化练习计划：
```powershell
# 新手计划
python 13_tools/scripts/practice_plan.py --level beginner --save

# 进阶
python 13_tools/scripts/practice_plan.py --level intermediate --save
```

### 5. 管理你的曲库

列出所有曲目：
```powershell
python 13_tools/scripts/library_manager.py list
```

按风格和 BPM 筛选：
```powershell
python 13_tools/scripts/library_manager.py list --style "Tech House" --bpm-min 120 --bpm-max 130
```

创建 Set List：
```powershell
python 13_tools/scripts/library_manager.py setlist --name "My First Set" --tracks 1,3,5,7
```

---

## 🎧 DJUCED 工作流 (2026)

1. **导入**：从 `08_exports/dj_ready/` 拖放文件到 DJUCED。
2. **分析**：使用 **DJUCED 6.5+ Autohotcue** 自动设置 Intro/Chorus/Outro 标记。
3. **校准**：在 Prepare 模式检查 **Beatgrid**（AI 曲目可能需要细微的网格调整）。
4. **混音**：使用 DJUCED 中专用的 **Stems** 视图实时分离 AI 生成的人声和鼓组。

---

## 📘 文档和资源

- 🚀 **[30分钟快速上手指南](12_docs/quickstart_guide.md)** - 零基础必读！
- 📖 **[Hercules Inpulse 200 MK2 指南](12_docs/hercules_inpulse_200_mk2_guide.md)** - 你的专属设备教程！
- 📚 **[学习路径](12_docs/learning_path.md)** - 完整的入门到高级 DJ 课程。
- 🎯 **[技巧库](12_docs/techniques_library.md)** - DJ 技巧综合参考。
- 🏠 **[本地模型指南](12_docs/local_models.md)** - 使用 MusicGen 离线生成音乐。
- 📖 **[AI-DJ 教程](12_docs/ai_djuced_tutorial.md)** - 从提示词到表演的完整指南。
- ✅ **[质量清单](12_docs/release_checklist/dj_ready_checklist.md)** - 曲目进入曲库前的标准。
- ⚖️ **[许可指南](12_docs/licenses/terms_checklist.md)** - 了解 2026 商业权利和 C2PA。

---

## 🤝 贡献

欢迎贡献！无论是更好的提示词、改进的脚本还是新教程，欢迎提交 Pull Request。

## ⚖️ 许可证

根据 **MIT 许可证**分发。有关更多信息，请参阅 `LICENSE`。

---

*用 ❤️ 为 AI-DJ 社区创建。*
