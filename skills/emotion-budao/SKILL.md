---
name: emotion-budao
description: >-
  Emotion revision for Chinese web-novel chapters, after a light human-writing pass:
  soft-win-then-tear, cost-as-object, anti-checklist, oral reactions, prose gate,
  word-count without merging paragraphs. Chain: human-writing (light) → emotion-budao.
  Triggers: /emotion-budao, /情绪补刀, /改章情绪, /回炉第X章. Not for outlining or day-writing.
---

# emotion-budao（情绪补刀）

独立改章技能。与 **human-writing** 串联使用；**不融合 story**（story 只是草稿常见来源之一）。

```text
正文草稿（任意来源）
  → ① human-writing 轻洗（若已安装）
  → ② 本技能：情绪补刀 + prose-gate + 字数
```

对接细则：[references/human-writing-handoff.md](references/human-writing-handoff.md)

- **不替代** story 开书/日更；不内嵌 human-writing 全文  
- **不建** `设定/大纲/追踪`；**不抽** `文风.md`  
- **不写** 第三方小说书名；情绪手法在 `references/`

有 `设定/文风.md` → 口吻以它为准（压过 human-writing 散文默认）。

## When to use

- 草稿已有，要「先洗表层再补情绪」或直接「情绪补刀」
- 只有爽+笑话，缺疼 / 代价 / 温度

**不要**用本技能：选题、开书、写细纲、从零日更。

## Pipeline (strict order)

```
0 human-writing light（可选，见 handoff）
→ 1 Locate → 2 Load project → 3 Emotion gate
→ 4 Revise → 5 Prose gate → 6 Word count（删词不并段）
→ 7 Log
```

Details: [references/pipeline.md](references/pipeline.md)  
Handoff: [references/human-writing-handoff.md](references/human-writing-handoff.md)  
Load: [references/load-map.md](references/load-map.md)  
Emotion: [references/emotion-gate.md](references/emotion-gate.md)  
Oral: [references/platform-oral.md](references/platform-oral.md)  
Prose: [references/prose-gate.md](references/prose-gate.md)

---

## Step 0 — human-writing（轻量，可选）

1. 若环境有 `human-writing` 且用户未要求跳过：按其 **fiction + revision** 做**轻改**（禁令与灌水），**禁止整章重写**。  
2. 网文保留吐槽分段、反应层、感叹号；项目 `文风.md` 优先。  
3. 未安装 / 用户跳过 → 直接 Step 1。

## Step 1 — Locate

1. Chapter file（常见 `正文/第00X章_*.md`）。忽略 `*_原稿_*`。  
2. 可改版本条。多章则逐文件跑完 0–6。

## Step 2 — Load project context（可选）

| If present | Use for |
|------------|---------|
| Target + prev + next | Continuity |
| `设定/文风.md` | Voice / word band（优先） |
| `追踪/上下文.md` / `伏笔.md` | Progress |
| Outline / 角色卡 | Plot lock / voice |

Plot anchors locked unless user changes setting.

## Step 3 — Emotion gate

Score [emotion-gate.md](references/emotion-gate.md).  
Hard fail: only **release + comedy**.

## Step 4 — Revise

1. Soft-win then tear  
2. Cost as object contrast  
3. Touchable objects  
4. Body-first + self-contradiction；气氛多停一拍  
5. Multi-reaction  
6. People over meters  
7. Misread comedy + [platform-oral.md](references/platform-oral.md)  
8. Strip checklist voice（§E）

若 Step 0 洗平了口语，本步按 oral / emotion-gate **补回**，不要顺着平稿收工。

## Step 5 — Prose gate

[prose-gate.md](references/prose-gate.md) 全章再扫（与 human-writing 硬禁令对齐的一层保险）。

## Step 6 — Word count

- Default **1700–2100** non-whitespace（`count_chars.py`）  
- **删词不并段**

## Step 7 — Log

`追踪/上下文.md` 可记一行：本章情绪补丁 + 是否跑过 human-writing 轻洗。

## Anti-patterns

| Bad | Good |
|-----|------|
| 把 human-writing 当整章重写再交给本技能 | ① 只轻洗 → ② 补情绪 |
| ② 之后再重度 human-writing | 情绪放最后；需要的话只做禁令复扫 |
| 融进 story 开书流程 | story 保持外挂，本包只管改章链 |

## Triggers

`/emotion-budao` · `/情绪补刀` · `/改章情绪` · 「回炉第X章」· 「先活人感再补情绪」
