# DJ 学习路径：从零入门到专业

## 📚 学习路径概览

本学习路径专为新手设计，结合 AI 生成的练习曲目，帮助你系统性地掌握 DJ 技能。

---

## 🎯 阶段一：基础入门（1-2 周）

### 目标
- 熟悉 DJ 控制器和 DJUCED 软件
- 理解基础节拍和节奏
- 学会对拍（Beatmatching）

### 第 1 天：设备熟悉
- [ ] 了解 Hercules 控制器各部分功能
- [ ] 安装并配置 DJUCED
- [ ] 导入一首练习曲目
- [ ] 播放、暂停、音量调节练习

**练习建议**：
```
使用 AI 生成一首简单的 120BPM 4/4 拍 House 曲目
python 13_tools/scripts/make_dj_track_minimax.py --idea "简单的 House 音乐，清晰的底鼓，适合新手" --style "House" --bpm 120 --instrumental --play
```

### 第 2-3 天：节拍识别
- [ ] 学习识别 4/4 拍
- [ ] 练习数拍（1-2-3-4）
- [ ] 在波形图上识别鼓点
- [ ] 使用 Beatgrid 工具

**练习曲目**：使用 AI 生成鼓点清晰的 Tech House

### 第 4-7 天：对拍入门
- [ ] 使用 SYNC 功能辅助
- [ ] 手动调整 pitch 控制
- [ ] 两首曲目的节拍对齐
- [ ] 理解 phrasing（乐句结构）

**练习建议**：
- 选择两首 BPM 相近的曲目（±5 BPM）
- 先从相同 BPM 开始练习

---

## 🎯 阶段二：基础混音（3-4 周）

### 目标
- 掌握基础混音技巧
- 学会使用 EQ（均衡器）
- 理解曲目结构
- 掌握 Hot Cue 的使用

### 第 1-2 周：EQ 和过渡
- [ ] 学习低频（Bass）、中频（Mid）、高频（Hi）的作用
- [ ] 练习用 EQ 做平滑过渡
- [ ] "低切低"（Bass Swap）技巧
- [ ] 理解频率避让

**练习曲目**：
```
生成两首风格相似的曲目，重点练习低频过渡
python 13_tools/scripts/make_dj_track_minimax.py --idea "Tech House 练习曲 A，适合 EQ 过渡" --style "Tech House" --bpm 126 --instrumental
python 13_tools/scripts/make_dj_track_minimax.py --idea "Tech House 练习曲 B，适合 EQ 过渡" --style "Tech House" --bpm 126 --instrumental
```

### 第 3-4 周：曲目结构分析
- [ ] 识别 Intro → Verse → Build → Drop → Break → Outro
- [ ] 设置 Hot Cue 标记点
- [ ] 在结构点处进行混音
- [ ] 理解 8/16/32 拍乐句

**必备 Hot Cue 设置**：
- Cue 1: Intro 开始
- Cue 2: First Drop
- Cue 3: Breakdown
- Cue 4: Outro 开始

---

## 🎯 阶段三：进阶技巧（5-8 周）

### 目标
- 掌握 Looping（循环）技巧
- 学习使用 Effects（效果器）
- 理解 Key 匹配
- 练习 Scratching（搓盘）

### Looping 技巧
- [ ] 基础 4/8/16 拍循环
- [ ] 半拍循环效果
- [ ] 循环叠加
- [ ] 用循环做过渡

### Effects 效果器
- [ ] Filter（滤波器）LPF/HPF
- [ ] Reverb（混响）
- [ ] Delay（延迟）
- [ ] Flanger/Phaser
- [ ] 效果器组合使用

### Harmonic Mixing（和声混音）
- [ ] 理解 Camelot Wheel
- [ ] 识别曲目的 Key
- [ ] 同 Key 或相邻 Key 混音
- [ ] Energy Boost 技巧

**Camelot Wheel 快速参考**：
```
1A - 8A - 3A - 10A - 5A - 12A - 7A - 2A - 9A - 4A - 11A - 6A
1B - 8B - 3B - 10B - 5B - 12B - 7B - 2B - 9B - 4B - 11B - 6B
```

### Scratching（搓盘）入门
- [ ] Baby Scratch
- [ ] Forward Scratch
- [ ] Chirp Scratch
- [ ] Transformer Scratch

---

## 🎯 阶段四：表演准备（9-12 周）

### 目标
- 构建 Set List（曲目列表）
- 掌握曲目编排
- 理解情绪曲线
- 准备完整的演出 Set

### Set 构建原则
1. **开场（Intro）**：低能量，渐入佳境
2. **建立（Build）**：能量逐步提升
3. **高潮（Peak）**：最高能量点
4. **维持（Maintain）**：保持热度
5. **收尾（Outro）**：能量逐渐降低

**Set 能量曲线示例**：
```
时间 →
能量
  ↑
  ●     ●
 ● ●   ● ●
●   ● ●   ●
●     ●     ●
────────────────→
```

### 练习 Set 构建
- [ ] 选择 8-12 首曲目
- [ ] 规划能量曲线
- [ ] 确保 Key 和 BPM 兼容
- [ ] 完整排练整个 Set
- [ ] 录制并复盘

---

## 🎯 阶段五：风格探索（持续学习）

### 主要电子音乐风格

#### House 家族
- **Deep House**：110-125 BPM，灵魂感，柔和
- **Tech House**：120-130 BPM，科技感，节奏感强
- **Progressive House**：125-135 BPM，旋律化，渐进式
- **Funky House**：118-128 BPM，采样 Funk，律动强

#### Techno 家族
- **Techno**：120-140 BPM，极简，工业感
- **Industrial Techno**：125-145 BPM，硬核，噪音元素
- **Melodic Techno**：120-130 BPM，旋律化，情感丰富
- **Acid Techno**：125-140 BPM，TB-303，酸性音色

#### Bass 家族
- **Dubstep**：140 BPM，半拍，重 Bass
- **Drum & Bass**：160-180 BPM，快速鼓点，重低音
- **Trap**：140 BPM，808 鼓组，三连音
- **House/Bass**：125-135 BPM，Wobble Bass

#### Trance 家族
- **Trance**：128-140 BPM， uplifting，旋律化
- **Psytrance**：135-150 BPM，迷幻，快速节奏
- **Progressive Trance**：125-135 BPM，渐进式

---

## 📋 每周练习计划表

### 第一周（基础）
```
周一：设备熟悉 + 播放控制
周二：节拍识别 + 数拍
周三：Beatgrid 校准
周四：Pitch 控制练习
周五：对拍练习（SYNC 辅助）
周六：手动对拍练习
周日：复盘 + 自由练习
```

### 第二周（基础混音）
```
周一：EQ 入门 + 低频控制
周二：中频和高频 EQ
周三：EQ 过渡练习
周四：Hot Cue 设置
周五：结构识别
周六：基础混音练习
周日：完整 2 首曲目的混音
```

---

## 🎓 学习资源推荐

### 视频教程
- DJUCED 官方教程
- YouTube DJ 教学频道
- Hercules 控制器使用指南

### 书籍
- 《DJing for Dummies》
- 《How to DJ Right》

### 社区
- DJ 论坛
- Reddit r/DJs
- 本地 DJ 社群

---

## 📊 进度跟踪表

每周完成后在相应位置打勾：

- [ ] 阶段一完成
- [ ] 阶段二完成
- [ ] 阶段三完成
- [ ] 阶段四完成
- [ ] 首次公开演出

---

*记住：DJ 是一门需要持续练习的艺术，享受过程比追求完美更重要！* 🎧
