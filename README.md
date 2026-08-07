# emotion-budao

独立网文 **情绪补刀** skill。与 **human-writing** 串联；不融合 oh-story。

```text
草稿 → human-writing（轻洗）→ emotion-budao（情绪）
```

| 层 | 工具 |
|----|------|
| 表层禁令 / 活人感轻改 | [human-writing](https://github.com/KKKKhazix/human-writing)（需自装） |
| 微赢再撕 · 代价物件 · 反检查单 · 口语反应 | **本仓库** |

## Install

```bash
npx skills add emileedeegan202-prog/emotion-budao -y -g
```

另装 human-writing（可选但推荐）：

```bash
npx skills add KKKKhazix/human-writing -y -g
```

或拷贝 `skills/emotion-budao/` → `~/.cursor/skills/` / `~/.claude/skills/`。

仓库：https://github.com/emileedeegan202-prog/emotion-budao

## Usage

```text
/emotion-budao 回炉第3章
# 默认：若已装 human-writing，先轻洗再补情绪
/情绪补刀 第6章（跳过活人感）
```

## Layout

```text
skills/emotion-budao/
  SKILL.md
  references/
    human-writing-handoff.md
    emotion-gate.md
    platform-oral.md
    prose-gate.md
    ...
  scripts/count_chars.py
```

## License

MIT。勿声称本包为 oh-story / human-writing 官方插件。
