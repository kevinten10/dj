# AI + DJUCED（Hercules）新手教程：从 Idea 到「可播放的 DJ 歌曲」

你想要的是：
- 你给出一个 idea（一句话）。
- 自动生成一首“DJ 歌曲”（至少是一个可播放的音频文件）。
- 在电脑上播放；最好还能导入 DJUCED，用你的 Hercules 控制器练习。

本教程基于 2026 年最新 AI 音乐模型与 DJUCED 6.5.x 工作流。

---

## 0) 快速开始（最短路径）

1. 申请并准备 MiniMax API Key。
2. 在 PowerShell 设置环境变量：

```powershell
$env:MINIMAX_API_KEY = "你的key"
$env:MINIMAX_API_BASE = "https://api.minimax.io"
```

3. 安装脚本依赖：

```powershell
python -m pip install -r requirements.txt
```

4. 一句话生成并播放：

```powershell
python 13_tools/scripts/make_dj_track_minimax.py --idea "赛博朋克夜店，霓虹雨夜，128BPM，鼓点清晰，适合新手练习混音" --model "music-2.5" --play
```

---

## 1) 你这套设备到底是什么

- **Hercules DJ 控制器**：控制器需要电脑上的 DJ 软件来出声、读歌、对拍。
- **DJUCED**：Hercules 的官方 DJ 软件。推荐使用 **Windows 11** 或 **macOS 14+** 环境。

---

## 2) 术语表（DJ 新手版）

- **Beatgrid（节拍网格）**：软件在波形上画的节拍线；同步 (SYNC) 和循环 (Loop) 都依赖它。
- **Hot Cue**：可快速触发的标记点。
- **Stem（分轨）**：将歌曲拆分为鼓、贝斯、人声等。DJUCED 支持实时分轨。
- **Tempo drift（速度漂移）**：AI 歌曲常见的速度不稳定现象，需要手动校准网格。

---

## 3) 自动化生成链路

### 3.1 为什么 MiniMax 更适合自动化

MiniMax 提供专业的 API 流程：
1. `lyrics_generation`：自动生成结构化歌词。
2. `music_generation`：使用 **MiniMax Music 2.5** 旗舰模型。

### 3.2 Music 2.5 核心优势 (2026)

- **精细化控制**：支持 14 种结构标签（`[Intro]`, `[Drop]`, `[Outro]` 等）。
- **Music 2.5+ (Instrumental)**：专为 DJ 设计的器乐模型，支持 100+ 乐器，输出纯净。
- **高保真**：解决了音频浑浊问题，适合俱乐部系统播放。

---

## 4) 把歌放进 DJUCED 并“变得好混”

### 4.1 导入与分析（DJUCED 6.5.2 更新）

- **Autohotcue Analysis**：PRO 版本会自动在 Intro、Chorus、Outro 处打点。
- **音频限制器**：Master 输出内置限制器，有效防止 AI 歌曲爆音。

### 4.2 Prepare（准备歌曲）核心技能

- **检查 Beatgrid**：在 Prepare 模式手动校准 AI 歌曲的节拍网格。
- **设置 Hot Cue**：至少设置 4 个点：Intro, Break, Drop, Outro。

---

## 5) 常见问题排查

- **读不进文件**：检查是否为 MP3/WAV/FLAC。
- **Windows 没声音**：确保启用了媒体功能，并检查驱动 (ASIO)。
- **对不上拍**：在 Prepare 模式关闭 `Snap to grid` 后微调。

---

## 6) 选型建议：2026 最新动态

### 6.1 Suno v5.5 (个性化创作)

- **Voices**：支持录入自己的声音作为音色。
- **限制**：免费版无法下载，需订阅 Pro 以上版本才能导出文件。

### 6.2 Udio v4 (专业与合规)

- **Stem Export**：支持 48kHz 无损分轨导出（鼓组、人声等），DJ 混音神器。
- **合规性**：包含 C2PA 元数据，符合 2026 行业识别标准。

### 6.3 Stable Audio 2.5

- **极速生成**：8步采样，秒级生成 3 分钟曲目。
- **商业许可**：年入 $100万 以下通过订阅即可获得商业权。

---

## 7) 参考链接

- [MiniMax Developer Platform](https://platform.minimax.io/)
- [Suno AI](https://suno.com/)
- [Udio AI](https://udio.com/)
- [DJUCED Release Notes](https://www.djuced.com/djuced-release-notes/)
