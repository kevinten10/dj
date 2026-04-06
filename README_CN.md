# 🎧 AI-DJ 工作区 (2026 版) - 完整指南

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![MiniMax Music 2.5](https://img.shields.io/badge/AI--Model-MiniMax%20Music%202.5-orange.svg)](https://platform.minimax.io/)
[![Hercules Inpulse 200 MK2](https://img.shields.io/badge/Controller-Hercules%20Inpulse%20200%20MK2-green.svg)](https://www.hercules.com/dj)

> **AI 创意与专业 DJ 表演之间的桥梁** 💫
> 
> 一个结构化的工作区，用于生成、分析和练习 AI 生成的曲目。专为 **Hercules DJControl Inpulse 200 MK2** 和 **DJUCED** 优化。

---

## 📑 完整目录

**🚀 快速开始**
- [30秒上手](#-快速开始30秒上手)
- [推荐学习路径](#-推荐学习路径)

**📖 零基础完整教程**
- [第一步：认识设备](#-第一步认识你的-hercules-djcontrol-inpulse-200-mk2)
- [第二步：30分钟时间表](#-第二步30分钟快速上手时间表)
- [第三步：生成练习曲](#-第三步生成第一首练习曲)
- [第四步：基础操作](#-第四步基础操作5分钟学会)
- [第五步：第一次混音](#-第五步你的第一次混音超详细教程)
- [第六步：EQ 技巧](#-第六步eq的魔力让你的混音更专业)
- [第七步：第一周计划](#-第七步第一周练习计划每日任务清单)

**🎯 系统学习路径**
- [阶段一：基础入门（1-2周）](#-阶段一基础入门1-2-周)
- [阶段二：基础混音（3-4周）](#-阶段二基础混音3-4-周)
- [阶段三：进阶技巧（5-8周）](#-阶段三进阶技巧5-8-周)
- [阶段四：风格探索与创作（9-12周）](#-阶段四风格探索与创作9-12-周)

**🎨 DJ 技巧大全**
- [节拍识别与数拍](#1-节拍识别与数拍)
- [Beatgrid 校准](#2-beatgrid-校准)
- [对拍技巧](#3-对拍beatmatching)
- [EQ 混音技巧](#-eq-过渡技巧)
- [Looping 循环技巧](#1-looping循环)
- [和声混音](#2-harmonic-mixing和声混音)

**🛠️ 工具使用**
- [核心功能](#-核心功能)
- [开始使用](#-开始使用)
- [DJUCED 工作流](#-djuced-工作流)

**❓ 帮助**
- [常见问题 FAQ](#-常见问题-faq)
- [进阶技巧预览](#-进阶技巧预览)
- [文档资源](#-文档和资源)

---

## ⚡ 快速开始（30秒上手）

### 🎯 如果你是零基础（推荐从这里开始！）

#### 方式一：最简单（Windows 用户）
```powershell
双击运行：start.ps1
```

#### 方式二：所有人通用
```powershell
python -m pip install -r requirements.txt
python 13_tools/scripts/interactive_generator.py
```

### 📚 推荐学习路径

| 你的水平 | 推荐阅读 | 预计时间 |
|---------|----------|----------|
| 🔰 完全零基础 | [下面的完整教程](#-完整教程从零开始) | 30分钟 |
| 🎵 刚入门 | [阶段一 + 阶段二](#-阶段一基础入门1-2-周) | 1个月 |
| 🎧 想提高 | [阶段三 + 技巧库](#-阶段三进阶技巧5-8-周) | 持续学习 |

---

## 📖 完整教程（从零开始！）

> 💡 **提示**：本教程专为 **Hercules DJControl Inpulse 200 MK2** 设计，完全零基础友好！

### 🎛️ 第一步：认识你的 Hercules DJControl Inpulse 200 MK2

只需要记住这几个最重要的部分：

```
┌─────────────────────────────────────────────────────────────┐
│  █████████████████████████████████████████████████████████  │
│                                                             │
│   ┌─ Deck A ─┐      ┌── Mixer ──┐      ┌─ Deck B ─┐       │
│   │          │      │           │      │          │       │
│   │ 🎛️ 转盘  │      │ ↔️ 横推    │      │ 🎛️ 转盘  │       │
│   │ ▶️ 播放   │      │ 🔊 主音量  │      │ ▶️ 播放   │       │
│   │ 🎚️ 音量推子│     │ 🎧 耳机音量│      │ 🎚️ 音量推子│      │
│   │ 🎧 Cue    │      │ 🎚️ EQ    │      │ 🎧 Cue    │       │
│   │ 🔄 SYNC   │      │ L M H    │      │ 🔄 SYNC   │       │
│   │ 📊 Pitch  │      │           │      │ 📊 Pitch  │       │
│   └──────────┘      └───────────┘      └──────────┘       │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**左侧（Deck A）：**
- 🎛️ **大转盘 (Jog Wheel)** - 搓盘、找歌、调整位置
- ▶️ **播放/暂停按钮** - 开始/停止音乐
- 🎚️ **音量推子 (Channel Fader)** - 控制 Deck A 的声音大小
- 🎧 **Cue 按钮** - 耳机监听（只有你能听到！）
- 🔄 **SYNC 按钮** - 自动对齐两首歌的节拍 ⭐
- 📊 **音调滑块 (Pitch Fader)** - 调整速度（±10%）
- 🔴 **4个打击垫 (Pads)** - Hot Cues / 循环 / 采样

**中间（Mixer 混音台）：**
- ↔️ **横推 (Crossfader)** - 在 Deck A 和 Deck B 之间切换
- 🔊 **主音量旋钮 (Master Volume)** - 控制总输出音量
- 🎧 **耳机音量旋钮 (Cue Volume)** - 控制耳机声音大小
- 🎚️ **EQ 三段均衡器**：
  - **Low (左)** - 低音（底鼓、贝斯）🔉 20-250Hz
  - **Mid (中)** - 中音（人声、主旋律）🎤 250Hz-4kHz
  - **High (右)** - 高音（镲片、Hi-Hat）✨ 4kHz-20kHz

**右侧（Deck B）：**
- 和左侧 **一模一样**！

---

### ⏱️ 第二步：30分钟快速上手时间表

| 时间 | 内容 | 难度 |
|------|------|:----:|
| 0-5 分钟 | 认识设备 + 安装 DJUCED | ⭐ |
| 5-10 分钟 | 用 AI 生成第一首练习曲 + 导入 | ⭐ |
| 10-15 分钟 | 基础操作：播放、音量、耳机监听 | ⭐ |
| 15-20 分钟 | 对拍 + **第一次混音** | ⭐⭐ |
| 20-25 分钟 | EQ 基础："低切低"技巧 | ⭐⭐ |
| 25-30 分钟 | 自由练习 + 录制你的第一个 Mix | ⭐⭐ |

---

### 🎵 第三步：生成第一首练习曲

#### 方法一：使用交互式菜单（推荐新手！）

1. **双击运行** `start.ps1`
2. 选择菜单：
   ```
   1 → 1 → 输入参数 → Y → Y
   ```
3. 等待生成完成 ✅

#### 方法二：使用命令行

```powershell
python 13_tools/scripts/make_dj_track_minimax.py `
  --idea "新手练习，清晰底鼓，简单节奏" `
  --style "House" `
  --bpm 120 `
  --instrumental `
  --play
```

#### 导入到 DJUCED

1. 打开 DJUCED 软件
2. 左侧找到 **文件夹浏览器**
3. 导航到：`08_exports/dj_ready/`
4. 把生成的 MP3 文件 **拖到 Deck A**

---

### 🎮 第四步：基础操作（5分钟学会）

#### 1️⃣ 播放和暂停
```
操作：按 Deck A 的 ▶️ 按钮
结果：音乐开始播放！再按一次暂停
```

#### 2️⃣ 调整音量
```
操作：慢慢向上推 🎚️ 音量推子
结果：听声音变大，向下拉变小
```

#### 3️⃣ 使用耳机监听（重要技能！⭐）

```
操作步骤：
1. 插上耳机 🎧
2. 按 Deck A 的 Cue 按钮
3. 调整耳机音量旋钮
结果：只有你能听到，听众听不到！
```

**为什么要用耳机？**
- ✅ 准备下一首歌时听众看不到
- ✅ 专业 DJ 的必备技能
- ✅ 让混音更流畅自然

---

### 🎯 第五步：你的第一次混音！（超详细教程）

#### 准备工作

1. 在 **Deck A** 播放一首歌曲（用上面的方法导入的）
2. 再生成一首练习曲，加载到 **Deck B**
3. 确保两首歌风格相似、BPM 接近

#### 步骤详解（跟着做！）

##### 📍 第一步：耳机准备第二首歌

```
┌─────────────────┐         ┌─────────────────┐
│   Deck A        │         │   Deck B        │
│                 │         │                 │
│  🟢 正在播放     │    →    │  🔴 准备中       │
│  👂 听众能听到   │         │  🎧 只有你听到   │
└─────────────────┘         └─────────────────┘
```

**操作：**
1. 按 Deck B 的 **Cue 按钮** 🎧
2. 你会在耳机里听到 Deck B 的声音
3. 按 Deck B 的 **播放按钮** ▶️

##### 📍 第二步：对拍（使用 SYNC 魔法键！）

**操作：**
- 按 Deck B 的 **SYNC 按钮** 🔄
- 两首歌的速度会 **自动对齐**！
- 观察 Pitch 滑块会自动移动

**神奇吧？这就是现代 DJ 的秘密武器！** ✨

##### 📍 第三步：开始混音（激动人心的时刻！）

**方法一：使用音量推子**
```
时间轴：
0秒 ──────→ 10秒 ──────→ 20秒
  ↓              ↓              ↓
Deck A: 100%        50%            0%
Deck B:  0%         50%          100%
```

**操作：**
1. 慢慢向上推 Deck B 的 **音量推子** 📈
2. 同时慢慢向下拉 Deck A 的 **音量推子** 📉
3. 保持平滑，大约 15-20 秒完成过渡

**方法二：使用横推（更酷！）**
```
操作：把 ↔️ 横推从左边慢慢推到右边
效果：从 Deck A 平滑过渡到 Deck B
```

**🎉 恭喜！你完成了第一次 DJ 混音！**

---

### 🎛️ 第六步：EQ 的魔力（让你的混音更专业）

#### 什么是 EQ？

三个旋钮控制不同频率：

| 旋钮 | 频率范围 | 听起来像 | 图标 |
|------|----------|----------|------|
| **Low** | 20-250 Hz | 底鼓、贝斯（咚咚咚） | 🔉 |
| **Mid** | 250-4000 Hz | 人声、主要乐器 | 🎤 |
| **High** | 4000-20000 Hz | 镲片、Hi-Hat（次次次） | ✨ |

#### "低切低"技巧（最常用的专业技巧！⭐⭐⭐）

**为什么需要这个技巧？**
- 两首歌的低音叠加会让声音浑浊 ❌
- "低切低"让过渡干净清晰 ✅

**详细步骤：**

```
时间线：
T=0s        T=5s        T=10s       T=15s       T=20s
  ↓           ↓           ↓           ↓           ↓
Deck B Low:  -∞dB       -∞dB       -6dB        0dB         0dB
Deck A Low:   0dB        0dB       -6dB       -∞dB        -∞dB
Deck B Vol:   0%         25%        50%        75%        100%
Deck A Vol: 100%        75%        50%        25%          0%
```

**操作：**
1. **准备阶段**：Deck B 的 **Low** 旋钮完全转到左边（-∞）
2. **开始混音**：慢慢推起 Deck B 音量（此时没有低音）
3. **交换低频**：
   - 同时把 Deck A 的 **Low** 慢慢切掉
   - 同时把 Deck B 的 **Low** 慢慢打开
4. **完成**：完全拉下 Deck A 音量

**结果：完美的专业级混音，没有浑浊的低音！** 🎊

---

### 📅 第七步：第一周练习计划（每日任务清单）

#### 📅 周一：设备熟悉日
目标：认识每个按钮，不再害怕按错

- [ ] 认识每个按钮的名称（对照上面的图）
- [ ] 练习播放/暂停 **10 次**
- [ ] 练习音量推子上下移动（感受阻尼）
- [ ] 练习用耳机监听（按 Cue 按钮）
- [ ] **挑战**：闭着眼睛找到每个按钮

#### 📅 周二：节拍识别日
目标：培养"数拍子"的感觉

- [ ] 播放一首歌，大声数 **1-2-3-4**
- [ ] 跟着节拍点头或跺脚
- [ ] 在波形图上找底鼓的位置（大的凸起）
- [ ] 用 AI 生成一首简单的练习曲
- [ ] **挑战**：不看屏幕，只靠听觉数拍子

#### 📅 周三：第一次混音日
目标：完成一次完整的 SYNC 混音

- [ ] 加载两首相似的歌到 Deck A 和 B
- [ ] 使用 **SYNC** 对齐两首歌
- [ ] 完成一次完整的音量推子混音
- [ ] 尝试用横推再做一次
- [ ] **挑战**：录制下来，回放听听效果

#### 📅 周四：EQ 混音日
目标：掌握"低切低"技巧

- [ ] 练习 **"低切低"** 技巧 **5 次**
- [ ] 用横推配合 EQ 做过渡
- [ ] 完整混音两首歌（带 EQ）
- [ ] 对比有 EQ 和没 EQ 的区别
- [ ] **挑战**：尝试只调 Mid 或 High 的变化

#### 📅 周五：Hot Cues 日
目标：掌握提示点设置和使用

- [ ] 在一首歌上设置 **4 个 Cue 点**：
  - Cue 1：Intro 开始
  - Cue 2：First Drop（最嗨的部分）
  - Cue 3：Breakdown（安静的部分）
  - Cue 4：Outro 开始
- [ ] 从不同 Cue 开始播放
- [ ] 在 Cue 点之间快速跳转
- [ ] **挑战**：只用 Hot Cues 做 3 首歌的混音

#### 📅 周六-周日：综合练习日
目标：整合本周所学，享受过程！

- [ ] 回顾本周学到的所有技巧
- [ ] 完整混音 **3-4 首歌**（连续）
- [ ] 尝试不同的组合方式
- [ ] **最终挑战**：录制一个 15 分钟的 Mini Set！
- [ ] 🎉 庆祝你完成了第一周的 DJ 训练！

---

## 🎯 系统学习路径（完整版）

> 本学习路径结合 AI 生成的练习曲目，帮助你系统性地掌握 DJ 技能。

### 🎯 阶段一：基础入门（1-2 周）

#### 目标
- ✅ 熟悉 DJ 控制器和 DJUCED 软件
- ✅ 理解基础节拍和节奏
- ✅ 学会对拍（Beatmatching）

#### 第 1 天：设备熟悉
- [ ] 了解 Hercules 控制器各部分功能（参考上面的设备图）
- [ ] 安装并配置 DJUCED
- [ ] 导入一首练习曲目
- [ ] 播放、暂停、音量调节练习

**AI 练习曲目生成：**
```powershell
python 13_tools/scripts/make_dj_track_minimax.py `
  --idea "简单的 House 音乐，清晰的底鼓，适合新手" `
  --style "House" --bpm 120 --instrumental --play
```

#### 第 2-3 天：节拍识别
- [ ] 学习识别 **4/4 拍**
- [ ] 练习数拍（1-2-3-4）
- [ ] 在波形图上识别鼓点
- [ ] 使用 Beatgrid 工具

**4/4 拍结构：**
```
1 (强) - 2 (弱) - 3 (次强) - 4 (弱)
●     - ●     - ●      - ●
底鼓(Kick)通常在 1 和 3
拍手(Clap/Snare)通常在 2 和 4
```

#### 第 4-7 天：对拍入门
- [ ] 使用 **SYNC 功能**辅助对拍
- [ ] 手动调整 **Pitch 控制**
- [ ] 两首曲目的节拍对齐
- [ ] 理解 **Phrasing（乐句结构）**

**练习要点：**
- 选择两首 BPM 相近的曲目（±5 BPM）
- 先从相同 BPM 开始练习
- 练习听辨速度差异
- 保持同步至少 30 秒

---

### 🎯 阶段二：基础混音（3-4 周）

#### 目标
- ✅ 掌握基础混音技巧
- ✅ 学会使用 EQ（均衡器）
- ✅ 理解曲目结构
- ✅ 掌握 Hot Cue 的使用

#### 第 1-2 周：EQ 和过渡

**学习三频段 EQ：**
- **Low（低频）**：底鼓、贝斯，20-250Hz
- **Mid（中频）**：人声、乐器，250Hz-4kHz  
- **High（高频）**：镲片、Hi-Hat，4kHz-20kHz

**必须掌握的技巧：**

1. **Bass Swap（低切低）** - 最常用！
   ```
   曲目 A（播放中）    曲目 B（待混音）
   Low: 0dB    →    Low: -∞dB (完全切掉)
   Mid: 0dB          Mid: 0dB
   High: 0dB         High: 0dB
   ```

2. **渐进式过渡**
   ```
   时间 →
   曲目 A: Low ↓  Mid →  High ↓
   曲目 B: Low ↑  Mid →  High ↑
   ```

**AI 练习曲目生成（EQ 专用）：**
```powershell
# 生成两首风格相似的曲目
python 13_tools/scripts/make_dj_track_minimax.py `
  --idea "Tech House 练习曲 A，适合 EQ 过渡" `
  --style "Tech House" --bpm 126 --instrumental

python 13_tools/scripts/make_dj_track_minimax.py `
  --idea "Tech House 练习曲 B，适合 EQ 过渡" `
  --style "Tech House" --bpm 126 --instrumental
```

#### 第 3-4 周：曲目结构分析

**标准电子音乐结构：**
```
[Intro] → [Verse] → [Build Up] → [Drop] → [Breakdown] → [Drop] → [Outro]
  16拍      32拍      16拍        32拍      16拍        32拍      16拍
```

**必备 Hot Cue 设置：**
- **Cue 1**: Intro 开始
- **Cue 2**: First Drop（最嗨的部分）
- **Cue 3**: Breakdown（安静的部分）
- **Cue 4**: Outro 开始

**常见混音点：**
- **Intro → Intro**：适合开场
- **Verse → Drop**：能量提升
- **Drop → Drop**：保持能量
- **Breakdown → Build**：戏剧性过渡
- **Outro → Intro**：平滑过渡

**8/16/32 拍乐句：**
```
[8拍]  [8拍]  [8拍]  [8拍]
 Intro   Verse   Build   Drop
```
**混音时机**：通常在 **32 拍的边界处**开始混音

---

### 🎯 阶段三：进阶技巧（5-8 周）

#### 目标
- ✅ 掌握 Looping（循环）技巧
- ✅ 学习使用 Effects（效果器）
- ✅ 理解 Key 匹配
- ✅ 尝试 Scratching（搓盘）

#### Looping 技巧

**基础循环长度：**
- **4 拍循环**：适合快速填充
- **8 拍循环**：标准长度
- **16 拍循环**：更长的循环段落

**循环过渡步骤：**
1. 在曲目 A 的 Drop 开始 **8 拍循环**
2. 引入曲目 B
3. 当曲目 B 到达 Drop 时
4. 停止循环，切换到曲目 B

**半拍循环效果：**
- 创建紧张感
- 适合 Build-up 阶段
- 配合 Filter 效果更佳

#### Harmonic Mixing（和声混音）

**Camelot Wheel（骆驼轮）：**
```
大调 (Major) → 1B-12B
小调 (Minor) → 1A-12A
```

**基本规则：**
- 同一个数字可以混音（如 8A → 8B）
- 相邻数字可以混音（如 8A → 9A 或 7A）
- 这样能保证和声和谐

#### Effects 效果器

**常用效果器：**

| 效果器 | 英文名 | 用途 | 使用场景 |
|--------|--------|------|----------|
| **滤波器** | Filter LPF/HPF | 渐变声音 | 过渡、Build-up |
| **混响** | Reverb | 添加空间感 | Breakdown、结尾 |
| **延迟** | Delay | 回声效果 | 特殊段落 |
| **镶边** | Flanger | 金属感调制 | 创意效果 |

---

### 🎯 阶段四：风格探索与创作（9-12 周）

#### 电子音乐风格速览

| 风格 | BPM 范围 | 特点 | 代表艺人 |
|------|----------|------|----------|
| **Deep House** | 118-124 | 温暖、律动感强 | Kerri Chandler |
| **Tech House** | 125-128 | 机械感、重复性强 | Fisher, Camelphat |
| **Techno** | 130-140 | 工业、黑暗 | Charlotte de Witte |
| **Progressive House** | 126-132 | 渐进、史诗感 | Eric Prydz |
| **Trance** | 134-142 | 情感丰富、高能量 | Armin van Buuren |
| **Drum & Bass** | 174-180 | 快节奏、复杂鼓点 | Netsky, Sub Focus |

#### Set 构建

**能量曲线设计：**
```
能量 ↑
     │           ╱╲
     │         ╱    ╲
     │       ╱        ╲
     │     ╱            ╲_______
     │   ╱
     │ ╱
     └──────────────────────────→ 时间
     开场  升温  高潮  冷却  结尾
```

**Set 结构建议：**
1. **开场（Warm-up）**：Deep House / Tech House，BPM 较低
2. **升温（Ramp-up）**：逐渐提高 BPM 和能量
3. **高潮（Peak Time）**：Techno / Trance，最高能量
4. **冷却（Cool-down）**：降低 BPM，更旋律化
5. **结束（Closing）**：Outro 友好，方便下一 DJ 接手

---

## 🎨 DJ 技巧大全

### 1. 节拍识别与数拍

**4/4 拍结构：**
```
1 (强) - 2 (弱) - 3 (次强) - 4 (弱)
●     - ●     - ●      - ●
```

**练习方法：**
- 听音乐时数 1-2-3-4
- 重点关注底鼓（Kick）通常在 1 和 3
- 拍手（Clap/Snare）通常在 2 和 4
- 在波形图上寻找规律的峰值

### 2. Beatgrid 校准

**步骤：**
1. 在波形图找到第一个底鼓
2. 将 Beatgrid 第一条线对齐该点
3. 播放检查后续鼓点
4. 微调 BPM 使所有鼓点对齐

**常见问题：**
- AI 生成的曲目可能有 tempo drift（速度漂移）
- 必要时分段调整 Beatgrid
- 关闭 Snap to grid 进行微调

### 3. 对拍（Beatmatching）

#### 使用 SYNC 辅助
1. 加载两首曲目
2. 一首播放，一首暂停
3. 按 SYNC 自动对齐
4. 观察 Pitch 变化

#### 手动对拍（进阶）
1. 耳机监听待混音的曲目
2. 调整 Pitch 使两首速度接近
3. 在 Cue 点同时播放
4. 微调 Pitch 保持同步

**练习要点：**
- 先从相同 BPM 开始
- 逐步增加难度到 ±5 BPM
- 练习听辨速度差异
- 保持同步至少 30 秒

### EQ 过渡技巧

#### Bass Swap（低切低）- 详细版
1. 曲目 A 播放中，曲目 B 准备好
2. 曲目 B 的 Low 完全切掉 (-∞)
3. 慢慢推起曲目 B 的 fader
4. 同时慢慢降低曲目 A 的 Low
5. 同时提升曲目 B 的 Low
6. 完全拉下曲目 A 的 fader

#### 其他 EQ 技巧

| 技巧名称 | 适用场景 | 操作 |
|---------|----------|------|
| **High Swap** | 过渡时保持清晰度 | 交换高频而非低频 |
| **Mid Scoop** | 制造空间感 | 中间段稍微降低 |
| **Full Kill** | 戏剧性效果 | 同时切掉所有频率 |
| **Sweep** | 渐变效果 | 缓慢旋转一个 EQ 旋钮 |

### 1. Looping（循环）

**基础循环：**
- **4 拍循环**：适合快速填充
- **8 拍循环**：标准长度
- **16 拍循环**：更长的循环段落

**循环过渡：**
1. 在曲目 A 的 Drop 开始 8 拍循环
2. 引入曲目 B
3. 当曲目 B 到达 Drop 时
4. 停止循环，切换到曲目 B

**半拍循环效果：**
- 创建紧张感
- 适合 Build-up 阶段
- 配合 Filter 效果更佳

### 2. Harmonic Mixing（和声混音）

**Camelot Wheel 基础：**
```
大调 (Major) → 1B-12B
小调 (Minor) → 1A-12A
```

**基本规则：**
- 同一个数字可以混音（如 8A → 8B）
- 相邻数字可以混音（如 8A → 9A 或 7A）
- 对角线也可以（能量变化更大）

---

## 🌟 核心功能

### 🤖 AI 音乐生成

| 功能 | 云端 API | 本地模型 |
|------|----------|----------|
| **模型** | MiniMax Music 2.5 | MusicGen (Meta) |
| **质量** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ ~ ⭐⭐⭐⭐⭐ |
| **速度** | 快（~1分钟） | 取决于硬件（CPU/GPU） |
| **网络** | 需要联网 | 完全离线 |
| **成本** | 需要 API Key | 免费 |
| **适用场景** | 高质量曲目 | 批量生成/隐私需求 |

### 🎚️ DJ 友好特性

- ✅ 自动生成 `[Intro]` 和 `[Outro]` 段落
- ✅ 清晰的底鼓和节拍结构
- ✅ 支持 14+ 结构标签精准编排
- ✅ 320kbps MP3 或 WAV 高保真输出
- ✅ 44.1kHz 采样率（俱乐部标准）

### 📊 智能管理

- 📁 **自动元数据存档**：每首歌保存完整提示词和参数
- 🎨 **12+ 风格预设**：Deep House、Techno、Trance 等
- 📋 **个性化练习计划**：根据水平定制
- 🔍 **曲库筛选系统**：按风格/BPM/日期过滤
- 📝 **Set List 创建器**：组织表演曲目单

---

## 🚀 开始使用

### 1️⃣ 安装依赖

```powershell
git clone https://github.com/kevinten10/dj.git
cd dj
python -m pip install -r requirements.txt
```

### 2️⃣ 配置云端 API（可选）

如果要用 MiniMax 云端 API：

```powershell
# 复制配置模板
cp 13_tools/configs/minimax_env.example.ps1 13_tools/configs/minimax_env.ps1

# 编辑并添加你的 API Key
notepad 13_tools/configs/minimax_env.ps1

# 加载配置
. .\13_tools\configs\minimax_env.ps1
```

获取 API Key：[platform.minimax.io](https://platform.minimax.io/)

### 3️⃣ 生成音乐（多种方式）

#### 🎯 方式一：交互式菜单（强烈推荐新手！）

```powershell
.\start.ps1
# 或
python 13_tools/scripts/interactive_generator.py
```

**优点：** 无需记命令，菜单引导，适合所有水平！

#### ☁️ 方式二：云端 API（高质量）

```powershell
# 基本
python 13_tools/scripts/make_dj_track_minimax.py `
  --idea "Peak hour techno, industrial warehouse vibe" `
  --style "Techno" --bpm 128 --instrumental --play

# 高级（自定义结构）
python 13_tools/scripts/make_dj_track_minimax.py `
  --idea "Epic trance journey with emotional buildup" `
  --style "Trance" --bpm 138 --duration 180 `
  --structure "[Intro:8][BuildUp:16][Drop:32][Breakdown:16][Drop:32][Outro:8]" `
  --play
```

#### 🏠 方式三：本地模型（离线/免费）

```powershell
# Small 模型（快速，适合测试）
python 13_tools/scripts/make_dj_track_local.py `
  --idea "Deep house groove for late night" `
  --style "Deep House" --bpm 120 --duration 90 --play

# Large 模型 + GPU（最佳质量）
python 13_tools/scripts/make_dj_track_local.py `
  --idea "Melodic techno with atmospheric pads" `
  --style "Techno" --bpm 128 --model facebook/musicgen-large `
  --cuda --temperature 0.9 --play
```

详细说明：[本地模型指南](12_docs/local_models.md)

#### 🎨 方式四：风格预设（一键生成）

```powershell
# 查看所有预设
python 13_tools/scripts/generate_with_preset.py --list

# 使用预设
python 13_tools/scripts/generate_with_preset.py `
  --preset tech_house --idea "Friday night party" --instrumental --play
```

可用预设：`tech_house`, `deep_house`, `techno`, `progressive_house`, `trance`, `drum_and_bass` 等

### 4️⃣ 获取练习计划

```powershell
# 新手计划（第1-2周）
python 13_tools/scripts/practice_plan.py --level beginner --save

# 进阶计划（第3-8周）
python 13_tools/scripts/practice_plan.py --level intermediate --save

# 高级计划（第9周+）
python 13_tools/scripts/practice_plan.py --level advanced --save
```

### 5️⃣ 管理你的曲库

```powershell
# 列出所有曲目
python 13_tools/scripts/library_manager.py list

# 筛选：Techno 风格，BPM 125-135
python 13_tools/scripts/library_manager.py list --style "Techno" --bpm-min 125 --bpm-max 135

# 创建 Set List
python 13_tools/scripts/library_manager.py setlist --name "My First Set" --tracks 1,3,5,7
```

---

## 🎧 DJUCED 工作流 (2026)

### 标准流程

```
1️⃣ 生成曲目          2️⃣ 导入 DJUCED        3️⃣ 分析标记          4️⃣ 校准 Beatgrid
   ↓                    ↓                     ↓                    ↓
AI 生成 MP3        拖放到 Deck         Autohotcue 自动标记   手动微调网格
                                        
5️⃣ 设置 Hot Cues    6️⃣ 练习混音          7️⃣ 录制 Mix          8️⃣ 分享！
   ↓                    ↓                     ↓                    ↓
标记关键点          应用 EQ/SYNC        导出音频文件          发布/回顾
```

### 详细步骤

1. **导入**：从 `08_exports/dj_ready/` 拖放文件到 DJUCED
2. **分析**：使用 **DJUCED 6.5+ Autohotcue** 自动设置 Intro/Chorus/Outro 标记
3. **校准**：在 Prepare 模式检查 **Beatgrid**（AI 曲目可能需要细微调整）
4. **混音**：使用 **Stems 视图** 实时分离人声和鼓组（高级功能）

---

## ❓ 常见问题 FAQ

### 🚀 安装和运行

**Q: 我应该先安装什么？**
```
A: 顺序如下：
   1. Python 3.9+ (从 python.org 下载)
   2. 项目依赖：pip install -r requirements.txt
   3. DJUCED 软件 (从 hercules.com 下载)
   4. 连接你的 Hercules 控制器
```

**Q: 运行 start.ps1 时报错？**
```
A: 可能的原因：
   - PowerShell 执行策略限制
   解决方案：以管理员身份运行 PowerShell，执行：
   Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

**Q: 本地模型安装失败？**
```
A: MusicGen 需要较大的依赖：
   - PyTorch (~2GB)
   - Audiocraft (~500MB)
   
   解决方案：
   1. 确保 Python 版本 >= 3.9
   2. 先安装 PyTorch：pip install torch torchvision torchaudio
   3. 再安装 audiocraft：pip install audiocraft
   
   详细指南：12_docs/local_models.md
```

### 🎵 音乐生成

**Q: 云端 API vs 本地模型，选哪个？**
```
A: 推荐：

   场景                推荐选项        原因
   ──────────────────────────────────────────
   新手入门            云端 API        简单、高质量
   批量生成练习曲      本地模型        免费、无限制
   需要最高质量        云端 API        效果最好
   没有网络/隐私敏感   本地模型        完全离线
   GPU 显卡好          本地模型 Large  速度快且免费
```

**Q: 生成的音乐不好听？**
```
A: 改进方法：
   
   1. 优化提示词（更具体）：
      差："好音乐"
      好："Deep House, 118 BPM, warm bassline, crisp hi-hats, soulful vocal chops"
   
   2. 调整参数：
      - temperature: 0.7-1.2 （越低越保守）
      - 多次生成选择最好的
   
   3. 使用风格预设（已优化过）
   
   4. 选择合适的 BPM 和时长
```

**Q: 如何生成特定结构的歌曲？**
```
A: 使用 --structure 参数：
   
   示例：
   --structure "[Intro:16][Verse:32][Chorus:32][Bridge:16][Outro:16]"
   
   可用标签：
   [Intro], [Verse], [Chorus], [Bridge], [Drop],
   [Breakdown], [BuildUp], [Outro]
```

### 🎧 DJ 操作

**Q: SYNC 对齐后还是听起来不对？**
```
A: 可能的原因和解决方法：
   
   1. Beatgrid 不准
      → 进入 Prepare 模式手动调整
   
   2. 两首歌结构差异太大
      → 选择结构相似的歌曲
   
   3. Pitch 调整过大（超过 ±6%）
      → 选择 BPM 更接近的歌曲
```

**Q: EQ 调整后声音很奇怪？**
```
A: 常见错误：
   
   ❌ 所有 EQ 都调到最大 → 声音失真
   ❌ Low 切太多 → 声音单薄
   ✅ 微调 ±3dB 通常足够
   ✅ 一次只调一个频率
```

**Q: 耳机里听不到 Deck B？**
```
A: 检查清单：
   
   1. Cue 按钮是否按下（灯亮？）
   2. 耳机是否插好
   3. 耳机音量旋钮是否打开
   4. Cue Mix 旋钮位置（中间？）
```

### 💻 技术问题

**Q: 生成的文件在哪里？**
```
A: 
   原始文件：04_generations/audio/raw/
   DJ就绪：  08_exports/dj_ready/
   元数据：  04_generations/metadata/
```

**Q: 如何批量生成多首歌？**
```
A: 创建脚本 batch_generate.ps1：
   
   $ideas = @(
       "Tech House, driving beat",
       "Deep House, soulful",
       "Techno, industrial"
   )
   
   foreach ($idea in $ideas) {
       python make_dj_track_minimax.py --idea $idea --style House
   }
```

**Q: 内存不足错误 (OOM)？**
```
A: 解决方案：
   
   1. 使用更小的本地模型（small 而非 large）
   2. 减少生成时长（--duration 60）
   3. 关闭其他程序释放内存
   4. 使用 CPU 而非 GPU（移除 --cuda）
```

---

## 💡 进阶技巧预览

当你掌握了基础后，可以尝试这些进阶技巧：

### 🎯 第二周：手动对拍

不使用 SYNC，手动调整 Pitch 来对齐节拍！

**步骤：**
1. 在 Deck A 播放参考曲
2. 在 Deck B 按下 Cue 监听
3. 听两首歌的底鼓是否同步
4. 如果 Deck B 太快 → 向下拉 Pitch
5. 如果 Deck B 太慢 → 向上推 Pitch
6. 当完全对齐时 → 开始混音

**练习目标：** 误差 < 5ms（人类几乎听不出来）

### 🎨 第三周：高级 EQ 技巧

除了"低切低"，还有这些技巧：

| 技巧名称 | 适用场景 | 操作 |
|---------|----------|------|
| **High Swap** | 过渡时保持清晰度 | 交换高频而非低频 |
| **Mid Scoop** | 制造空间感 | 中间段稍微降低 |
| **Full Kill** | 戏剧性效果 | 同时切掉所有频率 |
| **Sweep** | 渐变效果 | 缓慢旋转一个 EQ 旋钮 |

### 🔥 第四周：Hot Cues 创意用法

- **Looping**: 在 Drop 部分设置 Loop，延长高潮
- **Jump Cut**: 在不同段落间快速跳转
- **Mashup**: 用不同歌曲的片段创造新组合

### 🎪 第五周及以后：效果器和创意

- **Filter**: 让声音渐入渐出
- **Reverb**: 添加空间感
- **Delay**: 回声效果
- **Flanger**: 金属感调制

查看完整进阶教程：[DJ 技巧库](12_docs/techniques_library.md)

---

## 📂 工作区结构

```text
dj/
├── 04_generations/              # 📦 曲目存档
│   ├── audio/raw/               # 原始生成的音频
│   └── metadata/                # 生成日志和元数据
│
├── 08_exports/                  # 🎵 DJ 曲库
│   ├── dj_ready/                # 已处理，可直接导入 DJUCED
│   └── set_lists/               # 创建的 Set List
│
├── 12_docs/                     # 📚 知识库
│   ├── quickstart_guide.md      # ⚡ 30分钟快速上手（必读！）
│   ├── hercules_inpulse_200_mk2_guide.md  # 🎛️ 设备专属指南
│   ├── learning_path.md         # 📖 完整学习路径
│   ├── techniques_library.md    # 🎯 DJ 技巧大全
│   ├── local_models.md          # 🏠 本地模型使用指南
│   └── checklists/              # ✅ 质量和合规检查
│
└── 13_tools/                    # 🛠️ 自动化工具
    ├── scripts/
    │   ├── interactive_generator.py    # 🎮 交互式菜单（推荐！）
    │   ├── make_dj_track_minimax.py    # ☁️ 云端生成器
    │   ├── make_dj_track_local.py      # 🏠 本地模型生成器
    │   ├── generate_with_preset.py     # 🎨 预设生成器
    │   ├── practice_plan.py            # 📋 练习计划生成器
    │   └── library_manager.py          # 📁 曲目库管理器
    │
    ├── presets/
    │   └── styles.json           # 12+ 风格预设
    │
    └── configs/
        └── minimax_env.*        # API 配置模板
```

---

## 📘 文档和资源

### 🚀 入门必读（按顺序）

1. **[本文档 (README_CN.md)]** ⭐ - **一站式完整指南！**
2. **[30分钟快速上手指南](12_docs/quickstart_guide.md)** - 零基础首选
3. **[Hercules 设备指南](12_docs/hercules_inpulse_200_mk2_guide.md)** - 你的控制器详解

### 📚 进阶学习

4. **[DJ 学习路径](12_docs/learning_path.md)** - 从入门到高级的系统课程
5. **[DJ 技巧库](12_docs/techniques_library.md)** - 全面技巧参考手册
6. **[本地模型指南](12_docs/local_models.md)** - 离线生成详细教程
7. **[AI-DJ 教程](12_docs/ai_djuced_tutorial.md)** - 从提示词到表演

### ✅ 合规和质量

8. **[质量检查清单](12_docs/release_checklist/dj_ready_checklist.md)** - 曲目发布前检查
9. **[许可指南](12_docs/licenses/terms_checklist.md)** - 2026 商业权利和 C2PA

---

## 🤝 贡献与许可证

### 贡献

欢迎贡献！无论是：
- ✨ 更好的提示词模板
- 🛠️ 改进的脚本或工具
- 📖 新教程或文档
- 🐛 Bug 修复

提交 Pull Request 即可！

### 许可证

本项目基于 **MIT 许可证** 开源。

详见 [LICENSE](LICENSE) 文件。

---

## 🎉 开始你的 DJ 之旅！

**记住这三句话：**

1. 😊 **享受过程** - DJ 是一门艺术，不是比赛
2. 📈 **每天进步一点点** - 30分钟 > 偶尔练几小时  
3. 🎵 **用 AI 作为工具** - 它是你的创作伙伴，不是替代品

**现在就开始吧！** 

```powershell
.\start.ps1
```

---

*用 ❤️ 为 AI-DJ 社区创建 | 专为 Hercules Inpulse 200 MK2 打造 | 2026*
