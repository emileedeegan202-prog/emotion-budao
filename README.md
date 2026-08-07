# emotion-budao

独立网文 **情绪补刀** skill（oh-story 后置伴侣，不是 oh-story 分叉）。

| 前期 | 后期 |
|------|------|
| [oh-story-claudecode](https://github.com/worldwonderer/oh-story-claudecode) 扫榜/拆文/开书/日更 | **本仓库** `/emotion-budao` 情绪加厚 |

特有手法：微赢再撕 · 代价=物件对比 · 反检查单腔 · 口语反应层 · 删词不并段。

## Install

### Cursor / Claude Code（拷贝）

```text
skills/emotion-budao/  →  ~/.cursor/skills/emotion-budao/
                       或  ~/.claude/skills/emotion-budao/
                       或  {书}/.cursor/skills/emotion-budao/
```

### skills CLI（若已配置）

```bash
npx skills add <你的GitHub用户名>/emotion-budao -y -g
```

把仓库推到 GitHub 后，把上面的 `<你的GitHub用户名>` 换成真实路径。

## Usage

```text
/写长篇 …（oh-story 日出草稿）
/emotion-budao 回炉第3章
/情绪补刀 第6–10章
```

## Layout

```text
skills/emotion-budao/
  SKILL.md
  README.md
  references/
    emotion-gate.md
    platform-oral.md
    prose-gate.md
    load-map.md
    pipeline.md
  scripts/
    count_chars.py
功能说明.md
README.md
```

## License

MIT（可自由改、可商用写作工作流）。与 oh-story 许可证独立；请勿声称本包为官方插件。
