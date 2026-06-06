# 🎵 ACE-Step 本地歌词生成部署报告

> 部署日期：2026年4月19日 | 目标：本地生成带歌词的DJ音乐

---

## 📋 部署总结

### 版本控制策略

`13_tools/ace_step/` 是第三方 ACE-Step 仓库的本地 clone，不直接纳入本仓库提交。主仓库只保留集成脚本、文档和菜单入口；本地 clone 通过 `.gitignore` 忽略，避免把第三方仓库和其中的本地测试改动误提交到 `kevinten10/dj`。

轻量检查命令：

```powershell
python 13_tools/scripts/make_dj_track_ace_step.py --check
```

参数预览命令（不会加载模型）：

```powershell
python 13_tools/scripts/make_dj_track_ace_step.py --prompt "Electronic House music, upbeat, 120 BPM" --dry-run
```

如果本地没有 ACE-Step clone，可按需安装：

```powershell
git clone https://github.com/ace-step/ACE-Step.git 13_tools/ace_step
python -m pip install torchcodec
```

### ✅ 已完成的步骤

1. **✅ 克隆仓库** - ACE-Step 仓库已成功克隆到 `13_tools/ace_step/`
2. **⚠️ 安装依赖** - PyTorch 2.12 + CUDA 13.0 可用；当前 `torchaudio.save` 还需要 `torchcodec`
3. **✅ 下载模型** - ACE-Step-v1-3.5B 模型 (~8GB) 已下载到缓存
4. **✅ 创建集成脚本** - `make_dj_track_ace_step.py` 已创建
5. **✅ 修复 Gradio 问题** - Web UI 兼容性问题已修复

### ⚠️ 遇到的问题

**缺少 TorchCodec 保存后端**

新版 `torchaudio.save` 会调用 TorchCodec。若短生成在保存阶段报 `No module named 'torchcodec'`，先安装：

```powershell
python -m pip install torchcodec
```

**RTX 5060 Ti 兼容性问题**

| 问题 | 详情 |
|------|------|
| **显卡** | NVIDIA GeForce RTX 5060 Ti (16GB) |
| **架构** | Blackwell (2026年最新) |
| **PyTorch** | 2.12.0.dev + CUDA 13.0 |
| **错误码** | -1073741819 (0xC0000005 - 内存访问违规) |
| **原因** | RTX 50xx 系列是最新架构，PyTorch 支持尚不完善 |

**崩溃位置：**
```text
正在加载管道... ✅ 管道加载成功
开始生成...
⚠️ Checkpoint not loaded, loading checkpoint...
[崩溃] - 模型权重加载到 GPU 时发生内存访问错误
```

---

## 🔍 问题分析

ACE-Step 是一个 3.5B 参数的大型扩散模型，需要：
1. 加载 Transformer 模型 (~6.6GB)
2. 加载 DCAE 解码器 (~314MB)
3. 加载 Vocoder (~206MB)
4. 加载文本编码器 (~1.1GB)

总共有 ~8GB 模型需要加载。即使使用 CPU offload，初始加载仍然需要经过 GPU，导致在 RTX 5060 Ti 上崩溃。

---

## 💡 解决方案

### 方案 A：等待 PyTorch 更新（推荐）

**步骤：**
1. 关注 PyTorch 更新：https://pytorch.org/
2. 等待支持 RTX 50xx 系列的稳定版本
3. 更新后重新运行测试

**预计时间：** 1-2 周

### 方案 B：使用 Web UI 通过浏览器测试

**虽然命令行崩溃，但 Web UI 可能有更好的错误处理：**

```powershell
cd d:\projects\dj\13_tools\ace_step
acestep --port 7865 --cpu_offload true --overlapped_decode true --bf16 true
```

然后访问：http://localhost:7865

### 方案 C：使用云端 API 临时替代

在本地部署稳定之前，可以使用现有的 MiniMax 云端 API：

```powershell
python 13_tools/scripts/make_dj_track_with_lyrics.py --theme "DJ派对" --style "House"
```

### 方案 D：尝试其他本地模型

根据之前的调研，还可以尝试：

| 模型 | 复杂度 | 可能兼容性 |
|------|--------|-----------|
| **MusicGen** | 低 | ✅ 已测试可用 |
| **SongGeneration** | 中 | 可能有问题 |
| **HeartMuLa** | 高 | 需要 ComfyUI |

---

## 📁 已创建的文件

| 文件 | 用途 |
|------|------|
| `13_tools/ace_step/` | ACE-Step 仓库 |
| `13_tools/scripts/make_dj_track_ace_step.py` | 集成脚本 |
| `12_docs/local_lyrics_models.md` | 模型对比文档 |
| `13_tools/ace_step/test_*.py` | 测试脚本 |

---

## 🎯 下一步建议

### 立即可用

1. **使用云端 API** - 稳定可靠，中文支持好
   ```powershell
   python 13_tools/scripts/make_dj_track_with_lyrics.py
   ```

2. **使用 MusicGen 本地生成** - 纯音乐，无歌词
   ```powershell
   python 13_tools/scripts/make_dj_track_local.py --idea "House music" --cuda
   ```

### 等待 GPU 兼容后

1. **运行 ACE-Step 测试**
   ```powershell
   python 13_tools/ace_step/test_final.py
   ```

2. **使用集成脚本**
   ```powershell
   python 13_tools/scripts/make_dj_track_ace_step.py --theme "DJ派对" --style "House"
   ```

3. **启动 Web UI**
   ```powershell
   cd 13_tools/ace_step
   acestep --port 7865 --cpu_offload true
   ```

---

## 🔗 相关链接

- [ACE-Step GitHub](https://github.com/ace-step/ACE-Step)
- [ACE-Step HuggingFace](https://huggingface.co/ACE-Step/ACE-Step-v1-3.5B)
- [PyTorch 下载](https://pytorch.org/get-started/locally/)
- [模型缓存位置](C:\Users\PC\.cache\ace-step\checkpoints)

---

*报告生成时间：2026年4月19日*
*PyTorch 版本：2.12.0.dev20260405+cu130*
*CUDA 版本：13.0*
*GPU：NVIDIA GeForce RTX 5060 Ti (16GB)*
