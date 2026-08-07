# human-writing 对接（轻洗，不整章重写）

本技能**不内嵌** [human-writing](https://github.com/KKKKhazix/human-writing) 全文。  
改章推荐链（**不含 story 融合**）：

```text
已有正文草稿（来源不限：story 日更 / 手写 / 其它）
    ↓
① human-writing（轻量）—— 表层活人感 / 硬禁令
    ↓
② emotion-budao（本技能）—— 情绪结构补刀 + 本包 prose-gate + 字数
```

## ① 何时跑、跑多重

| 情况 | 做法 |
|------|------|
| 已安装 `human-writing`，用户未说跳过 | **先**按其 `fiction.md` + `revision.md` 做**轻改**，再进本技能 Step 1 |
| 用户说「跳过活人感 / 只用情绪补刀」 | 直接本技能 |
| 未安装 human-writing | 跳过 ①；本包 `prose-gate.md` 仍覆盖重叠硬禁令 |

**轻改定义（硬）：**

- 只清：`——` / `—`、叙述里滥用的 `：`、翻案句（不是A而是B 等）、空洞解释腔  
- **不**整章重写结构、**不**削反应层起哄、**不**把口语/感叹号洗成散文平句  
- **不**为「更像长帖」加作者说教尾巴  
- 网文项目有 `设定/文风.md` 时：**文风优先于** human-writing 的散文默认（短句连斩、吐槽分段保留）

若 ① 把番茄吵闹感洗没了，② 必须按 emotion-gate / platform-oral **补回**，不要顺着平稿结束。

## ② 与本包分工

| 层 | 谁管 |
|----|------|
| 句子禁令、材料别灌水、活人叙述 | human-writing（①） |
| 六拍、微赢再撕、代价物件、反检查单、口语反应 | **emotion-budao（②）** |
| 重叠禁令（破折号/冒号/翻案） | ① 清一轮；② `prose-gate` 再扫一轮 |

## 脚本（可选）

若本机有 human-writing 的 `scripts/check_prose.py`，① 结束后可跑一次；② 仍以本包 `count_chars.py` + `prose-gate` 为准。
