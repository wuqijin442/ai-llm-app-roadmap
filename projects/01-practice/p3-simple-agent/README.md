# P3 · 简单工具调用 Agent（练手）

> 手写一个 **ReAct 循环**：模型思考 → 选工具 → 执行 → 观察 → 再思考，直到给出最终答案。
> 不依赖框架，帮你真正理解 Agent 的"大脑"是怎么转的。

## 运行
```bash
cd p3-simple-agent
python agent.py
```
示例问题：`帮我算一下 23 * 47，然后告诉我现在几点`。Agent 会先调计算器，再调时间工具。

## 你会学到
- ReAct 范式（Thought / Action / Observation）。
- 如何用 Prompt 约束模型输出"可解析的"工具调用指令。
- 工具注册表（name → function）与参数解析。
- 最大轮次限制（防止死循环，这正是 Harness 的"失败恢复"雏形）。

## 进阶
→ `e2-smart-customer-service`：把工具换成真实业务（查订单/退款政策/转人工），并加审批、重试、日志（Harness 化）。
