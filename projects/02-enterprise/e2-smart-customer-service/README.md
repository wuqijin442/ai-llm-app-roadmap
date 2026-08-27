# E2 · 智能客服 Agent（实战 · Harness 化）

> 多工具客服 Agent：查订单、查退款政策、转人工。重点不是"答得准"，而是**工程化治理**——
> 这正是 `docs/05` 讲的 Harness：失败重试、长任务续跑、敏感动作审批、日志可观测。

## Harness 落地点（面试讲这些）
- **Tool layer**：给 Agent 接 `query_order / refund_policy / escalate` 三个工具，校验参数。
- **Safety/权限**：退款等敏感动作需"人工审批"才执行（不自动放行）。
- **Lifecycle/重试**：工具调用失败自动重试，超过次数转人工，绝不卡死。
- **日志观测**：每次（意图→工具→结果→最终回复）落日志，可追溯、可复盘成本。

## 运行
```bash
pip install langchain-ollama
python cs_agent.py
```
示例："查一下订单 A123 的状态，如果已发货就告诉我物流，否则走退款。"

## 交付价值（写进简历）
"设计客服 Agent 的 Harness 运行层：工具调用失败重试、敏感动作人工审批、全链路日志观测，
支撑日均 X 咨询稳定自动化，转人工率降至 Y%。"
