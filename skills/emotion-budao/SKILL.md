---
name: emotion-budao
description: >-
  Post-draft emotion revision for Chinese web novels (oh-story companion, not a fork):
  soft-win-then-tear, cost-as-object, anti-checklist voice, oral reaction layers,
  prose gate, word-count without merging paragraphs. Triggers: /emotion-budao,
  /情绪补刀, /改章情绪, /回炉第X章, hollow payoff chapters. Not for outlining or day-writing.
---

# emotion-budao（情绪补刀）

独立技能，**不是** oh-story 的一部分。前期用 oh-story（`story-long-write` / `analyze` / `import`）走开书与日更；正文草稿出来后，用本技能做**情绪加厚**。

- **不替代** story 的拆文、落盘、日更、去AI味  
- **不建** `设定/大纲/追踪`  
- **不抽** `文风.md`  
- **不写** 第三方书名；手法全在 `references/`

有 `设定/文风.md` / `追踪/` / 细纲 → 只读它们锁剧情与口吻；本技能只管情绪结构 + 文笔门 + 改序。

## When to use

- 已有章节要「情绪补刀 / 回炉」
- 只有爽点+笑话，缺疼 / 代价 / 温度
- 批量按同一情绪标准改 1–N 章

**不要**用本技能：选题、开书、写细纲、从零日更（走 oh-story）。

## Pipeline (strict order)

```
1 Locate → 2 Load project (optional) → 3 Emotion gate
→ 4 Revise → 5 Prose gate → 6 Word count (delete words, never merge paragraphs)
→ 7 Log (if project has tracking)
```

Details: [references/pipeline.md](references/pipeline.md)  
Load rules: [references/load-map.md](references/load-map.md)  
Emotion gate: [references/emotion-gate.md](references/emotion-gate.md)（**微赢再撕**、**反检查单腔**）  
Oral cadence: [references/platform-oral.md](references/platform-oral.md)（吐槽分段 / 反应层；文风优先）  
Prose gate: [references/prose-gate.md](references/prose-gate.md)

---

## Step 1 — Locate

1. Find the chapter file (common: `正文/第00X章_*.md`). Ignore `*_原稿_*`, `*.bak`.
2. Optional version banner; bump a short note after revise.
3. Multi-chapter: finish Steps 2–6 per file; no mega-paste.

## Step 2 — Load project context (optional, best-effort)

Read what exists; **skip missing** (still works on a lone `.md`):

| If present | Use for |
|------------|---------|
| Target + prev + next chapter | Continuity |
| `设定/文风.md` | Voice, punctuation, word band |
| `追踪/上下文.md` / `追踪/伏笔.md` | Progress; spoilers to avoid |
| Outline for this chapter | Must-deliver plot beats |
| Character sheets on-page | Voice drift |

**Canon:** project 正文 folder wins over sibling draft folders unless user says otherwise.  
**Plot anchors locked** (scores, names, hooks, timeline) unless user asks to change setting.

## Step 3 — Emotion gate (before editing)

Score with [emotion-gate.md](references/emotion-gate.md).

Hard fail: only **release + comedy**, missing **build / wound / cost / warmth**.

## Step 4 — Revise

Patch order (highest ROI first):

1. **Soft-win then tear** on opening/build  
2. **Cost** after payoff — object contrast, not slogan  
3. **Touchable objects** before action  
4. **Body-first** + **self-contradiction**; atmosphere lingers one beat before kinship  
5. **Multi-reaction contrast** (≥2 unlike reactions)  
6. **People over meters** — show, don’t thesis  
7. **Misread comedy** + oral asides per [platform-oral.md](references/platform-oral.md)  
8. Strip **checklist voice** (emotion-gate §E)

Voice: follow `设定/文风.md` if any; else keep chapter person/tense + oral rhythm（dense emotion ≤1–2 spans / chapter）.

## Step 5 — Prose gate

Run [prose-gate.md](references/prose-gate.md) on the full chapter.

After this skill, optional: oh-story `/story-deslop`（本门 ≠ deslop 全流程）.

## Step 6 — Word count & paragraphs

- Default band: **1700–2100** non-whitespace（override via 文风 or `--min/--max`）.
- Count: [scripts/count_chars.py](scripts/count_chars.py). Not `wc -w`.
- **Shorten: delete words only. Never merge paragraphs / collapse blank lines.**

## Step 7 — Log

If `追踪/上下文.md` exists, append one decision line（chapter + which emotion patches）.  
Checklist labels ≠ progress.

## Anti-patterns

| Bad | Good |
|-----|------|
| Use this skill to scaffold a new book | Use oh-story long-write / import |
| Paste emotion **labels** into prose | Body + object + glance |
| Payoff → instant system joke | Cost / warmth between |
| Merge paragraphs to hit quota | Delete wording, keep breaks |

## Triggers

`/emotion-budao` · `/情绪补刀` · `/改章情绪` · 「回炉第X章」· 「这章情绪不够」
