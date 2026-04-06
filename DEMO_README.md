# 🎵 AI DJ Demo 音乐

## 快速获取 Demo 音乐的方法

### 方法一：使用预生成的 Demo（推荐）

我们已经为你准备了示例 Demo 音乐，可以直接下载：

**下载链接：** [点击下载 Demo MP3](https://github.com/kevinten10/dj/releases/download/demo/ai_dj_demo.mp3)

### 方法二：使用云端 API 生成（需要 API Key）

1. 获取 MiniMax API Key：[platform.minimax.io](https://platform.minimax.io/)
2. 配置环境变量：
   ```powershell
   cp 13_tools/configs/minimax_env.example.ps1 13_tools/configs/minimax_env.ps1
   # 编辑文件添加你的 API Key
   . .\13_tools\configs\minimax_env.ps1
   ```
3. 生成音乐：
   ```powershell
   python generate_and_play.py "你的想法"
   ```

### 方法三：使用本地模型生成（无需 API Key）

1. 安装依赖：
   ```powershell
   pip install torch audiocraft
   ```

2. 运行本地生成脚本：
   ```powershell
   python generate_demo_local.py
   ```

3. 首次运行会下载模型（约1GB），之后就可以离线使用了！

---

## Demo 音乐特点

我们的 Demo 音乐具有以下特点，非常适合 DJ 练习：

- ✅ **清晰的节拍** - 底鼓明显，容易对拍
- ✅ **标准结构** - 有 Intro、Verse、Drop、Outro
- ✅ **适合混音** - 有清晰的 32 拍段落
- ✅ **多种风格** - House、Techno、Trance 等

---

## 如何使用 Demo 音乐

### 1. 直接播放
双击 MP3 文件即可用默认播放器播放

### 2. 导入 DJUCED 软件
1. 打开 DJUCED
2. 将 MP3 文件拖到 Deck A
3. 开始练习混音！

### 3. 练习建议
- 先用一首 Demo 练习播放/暂停
- 用两首 Demo 练习混音
- 尝试使用 SYNC 和手动对拍
- 练习 EQ 过渡技巧

---

## 示例提示词

如果你想自己生成音乐，可以使用这些提示词：

```
"清晰的 House 节拍，适合练习混音，120bpm"
"高能 Techno，强烈的底鼓，适合派对，130bpm"
"放松的 Deep House，温暖的感觉，适合日落，118bpm"
"史诗 Trance，情感丰富，适合高潮部分，138bpm"
```

---

享受你的 AI DJ 之旅！🎧✨
