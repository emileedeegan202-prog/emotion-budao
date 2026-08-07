# Load map

Paths are **optional**. Skill runs even if only one chapter file is open.

Assumes early pipeline already ran via **oh-story** (long-write / analyze / import) when those files exist.

## A. Prefer when present (relative to book root)

| Path patterns | Why |
|---------------|-----|
| `正文/` or `chapters/` (authoritative) | Canon text |
| `设定/文风.md`, `文风.md` | Voice + word band |
| `设定/**/角色*.md`, `设定/角色/` | Voice continuity |
| `追踪/上下文.md`, `进度.md` | Timeline |
| `追踪/伏笔.md`, `伏笔.md` | Do not spoil |
| `大纲/**` matching this chapter | Must-deliver beats |

## B. Never required

- Private “拆文库 / 对标库 / 情绪节拍库” outside the project  
- Any third-party novel corpus  
- Sibling draft trees (`正文2/`, `正文3/`, `draft_old/`) unless user points to them

## C. Conflict rule

1. User explicit instruction wins  
2. Project canon folder + outline anchors win for **plot**  
3. This skill’s emotion/prose gates win for **revision quality** when project style is silent  
4. If project `文风.md` conflicts with prose-gate on a soft preference, follow project; keep hard bans unless project explicitly overrides
