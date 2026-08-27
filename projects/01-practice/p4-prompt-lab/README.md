# P4 · Prompt 实验台（练手）

> 把 Prompt 当成"可版本化、可对比、可评测"的资产。加载模板 → 跑模型 → 对比效果 → 导出最佳。
> 对应 `docs/03-Prompt工程.md` 的"A/B 测试 + 评分标准"。

## 运行
```bash
cd p4-prompt-lab
python prompt_lab.py
```
默认内置 3 个模板（客服/抽取/摘要），对同一问题跑出结果并打分对比。

## 你会学到
- 模板化 Prompt（占位符 `{question}`）。
- 固定 rubric 评分（准确性/格式/简洁度），而非"凭感觉"。
- 把胜出 Prompt 沉淀成可复用资产。

## 模板扩展
在 `templates.json` 里加一条即可，无需改代码。
