# DJ Ready Checklist（导入 DJUCED 前检查）

适用场景：你用 AI 生成了音频，想要“好混/好练”，并且尽量避免现场/练习时的坑。

## 1) 文件与格式

- 文件能被 DJUCED 识别（优先 MP3/WAV/AIFF/FLAC）。
- 命名清晰：`YYYYMMDD_风格_idea_128bpm.ext`（至少含日期 + 风格/关键词 + BPM）。
- 统一保存到：`08_exports/dj_ready/`（方便在 DJ 软件里批量导入）。

## 2) 音量与动态（练习优先“稳定”）

- 主观听感不要忽大忽小（AI 生成常见问题）。
- 避免爆音/削波（失真会严重影响练习和后期处理）。
- 如果你后续要做混音/母带，建议保留一份无损版本（WAV/AIFF）。

## 3) 结构是否“好混”

- Intro / Outro 至少有一段“鼓点较干净”的区域（便于混入/混出）。
- Drop/Break/Build-up 分段清晰（Hot Cue 好打点）。
- 如果全曲都很花/一直有人声：考虑重新生成（`--instrumental`）或后期做 DJ Edit（加长 intro/outro）。

## 4) Beatgrid（核心）

AI 生成经常出现 tempo drift（越放越快/慢）：
- 在 DJUCED 的 Prepare 模式里检查 beatgrid 是否跟得上鼓点。
- 如果漂移严重：优先把它当“练手曲”，不要强求用它练纯手动对拍；先用 SYNC + loop 练结构/换歌。

## 5) Hot Cue（最少 4 个）

建议每首歌至少打 4 个点：
- Intro 起点
- Break 起点
- Drop 起点
- Outro 起点

## 6) 最终检查（30 秒）

- 用耳机和音箱各试听一次（尤其是低频）。
- DJUCED 里加载后能正常分析、能放、波形正常、Cue/Loop 工作正常。
