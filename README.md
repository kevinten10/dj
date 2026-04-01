# dj 工作目录（AI 生成 + DJUCED 练习）

这是一个把「灵感 → 生成音频 → 导入 DJ 软件练习」串起来的工作目录结构。当前已提供：
- 新手教程：`12_docs/ai_djuced_tutorial.md`
- 一键生成脚本（MiniMax）：`13_tools/scripts/make_dj_track_minimax.py`

## 快速开始（MiniMax）

1) 安装依赖：

```powershell
python -m pip install -r requirements.txt
```

2) 配置环境变量（二选一）：

- 直接在 PowerShell 里设置：

```powershell
$env:MINIMAX_API_KEY = "你的key"
# 可选：如果你需要走其他域名
$env:MINIMAX_API_BASE = "https://api.minimax.io"
```

- 或复制模板并执行：
  - 复制 `13_tools/configs/minimax_env.example.ps1` → `13_tools/configs/minimax_env.ps1`
  - 填好 Key 后运行：`. .\13_tools\configs\minimax_env.ps1`

3) 生成并导出一首可练习的曲子：

```powershell
python 13_tools/scripts/make_dj_track_minimax.py --idea "赛博朋克夜店，霓虹雨夜，128BPM，鼓点清晰，适合新手练习混音" --instrumental --play
```

输出位置：
- DJ 可用导出：`08_exports/dj_ready/`
- 原始音频：`04_generations/audio/raw/`
- 元数据：`04_generations/metadata/`

## 下一步建议

- 在 DJUCED 的 Prepare 模式做：beatgrid 校准 + Hot Cue（Intro/Break/Drop/Outro）。
- 需要更“好混”的结构时：参考 `12_docs/release_checklist/dj_ready_checklist.md` 做成 Extended Mix / DJ Edit。

## 许可与合规（重要）

如果你计划公开发布/商用，请先阅读并维护：
- `12_docs/licenses/README.md`

