---
name: emotion-budao
description: >-
  Emotion revision for Chinese web-novel chapters after a full human-writing pass:
  soft-win-then-tear, cost-as-object, anti-checklist, oral reactions, prose gate,
  word-count without merging paragraphs. Chain: human-writing (full revision) →
  emotion-budao. Triggers: /emotion-budao, /情绪补刀, /改章情绪, /回炉第X章.
---

# emotion-budao（情绪补刀）

独立改章技能。与 **human-writing** 串联；**不融合 story**。

```text
正文草稿
  → ① human-writing 完整改稿（fiction + revision + check_prose）
  → ② 本技能：情绪补刀 + prose-gate + 字数
```

对接（力度说明）：[references/human-writing-handoff.md](references/human-writing-handoff.md)

- ① **按改正文实操跑满**，不是轻扫标点  
- 有 `设定/文风.md` → 番茄口吻优先于 human-writing 长帖默认  
- 不内嵌 human-writing 全文；不建工程树；不写第三方书名

## When to use

- 草稿要「先活人感改稿，再情绪补刀」  
- 或用户只要情绪层（可声明跳过①）

## Pipeline (strict order)

```
0 human-writing 完整改稿（可选，默认有则跑）
→ 1 Locate → 2 Load → 3 Emotion gate
→ 4 Revise → 5 Prose gate → 6 Word count → 7 Log
```

Details: [references/pipeline.md](references/pipeline.md)  
Handoff: [references/human-writing-handoff.md](references/human-writing-handoff.md)  
Emotion: [references/emotion-gate.md](references/emotion-gate.md)  
Oral: [references/platform-oral.md](references/platform-oral.md)  
Prose: [references/prose-gate.md](references/prose-gate.md)

---

## Step 0 — human-writing（完整改稿）

1. 已安装且未跳过：读 **fiction.md** + **revision.md**，按七遍改稿认真改。  
2. 跑 **check_prose.py**（若有），硬禁令清零。  
3. 保留项目文风的短句/吐槽/反应层；拆的是表演腔和注水，不是番茄热度。  
4. 未安装 / 用户跳过 → Step 1。

## Step 1 — Locate

Chapter under `正文/`（忽略 `*_原稿_*`）。多章逐文件跑 0–6。

## Step 2 — Load project context

| If present | Use for |
|------------|---------|
| prev/next 章 | Continuity |
| `设定/文风.md` | Voice（优先） |
| `追踪/*` / 细纲 / 角色卡 | Lock plot |

## Step 3 — Emotion gate

[emotion-gate.md](references/emotion-gate.md)。缺 build/wound/cost/warmth → 必须补。

## Step 4 — Revise

1. Soft-win then tear  
2. Cost as object  
3. Touchable objects  
4. Body-first + self-contradiction；气氛多停一拍  
5. Multi-reaction  
6. People over meters  
7. Misread comedy + [platform-oral.md](references/platform-oral.md)  
8. Anti-checklist（§E）

若①改平了，本步按门禁**补回**情绪与口语，不顺着平稿结束。

## Step 5–7

Prose-gate → `count_chars.py`（删词不并段，默认 1700–2100）→ 追踪记一行（含是否跑过①）。

## Anti-patterns

| Bad | Good |
|-----|------|
| ①只改标点叫「跑过 human-writing」 | ①按 revision 七遍 + check_prose |
| ①洗成知乎散文再假装完稿 | 文风优先；②补情绪/口语 |
| ②后再整章 human-writing | 情绪收尾；最多禁令复扫 |

## Triggers

`/emotion-budao` · `/情绪补刀` · `/改章情绪` · 「回炉第X章」· 「按之前改稿手法」
