# 05 · Agent 智能体与 Harness 工程

> 2026 真正拉开差距的，不是模型本身，而是「模型外面的那层系统设计」——Harness。

## 1. Agent 基础

**ReAct 循环**：思考(Thought) → 行动(Act) → 观察(Observation) → 再思考 … → 输出。
Agent 能：规划任务、调用工具、迭代执行、自我反思。

**核心组件**
- 规划（Planner）：把「写行业报告」拆成 收集→大纲→撰写→润色。
- 记忆（Memory）：短期（对话缓存）/ 长期（向量库检索历史）。
- 工具（Tools）：代码解释器、API、数据库、文件系统、搜索。
- 反思（Reflection）：结果自评与修正。

## 2. 框架选型
- **LangChain / LangGraph**：主流，图式编排多步骤 Agent，岗位需求最大。
- **LlamaIndex**：RAG 向更强，轻量。
- **AutoGen / MetaGPT**：多 Agent 协作。
- **Dify / AnythingLLM**：可视化编排，快速搭原型（非代码）。

## 3. MCP（Model Context Protocol）
2026 Agent 与外部工具交互的**标准化协议**。掌握 MCP = 让 Agent 即插即用各种工具（数据库、浏览器、文件系统），是 Agent 开发必备技能。优先理解：MCP Server / Client 结构、如何暴露一个 tool。

## 4. Harness（重点拓展，来自参考文章核心观点）

**定义**：Harness = 围绕 LLM/Agent 的「执行与治理层」，不是模型、不是 Prompt、不是框架、也不只是 workflow。

**一个成熟 Harness 包含**
1. **Agent loop**：用户输入→思考→调工具→执行→观察→再思考 的循环。
2. **Tool layer**：给模型接 shell/代码/浏览器/DB/API/文件系统，并校验调用合法性。
3. **Memory / state**：保存中间状态、进度、摘要、检查点，解决长任务「做着做着就忘了」。
4. **Safety / permissions**：限制能访问什么、能改什么、什么需审批、怎么过滤 IO。
5. **Lifecycle / recovery**：崩了能否续跑、重启能否接着干、跨小时/天能否继续。
6. **Client/runtime integration**：对接 CLI / IDE / Web / 容器，以稳定协议暴露。

**Harness Engineering 的本质**：从「提示工程」升级到「智能体运行系统工程」——
- 怎么让仓库对 Agent 更可读
- 怎么把知识沉淀进 repo
- 怎么通过反馈回路让 Agent 持续纠错
- 怎么控制「熵增」与系统漂移
- 怎么让 humans steer, agents execute

> 我的视角：作为工程背景转岗者，**Harness 是你的主战场**。面试时讲「我设计的 Agent 失败能重试、长任务能续跑、工具有审批、有日志可观测、成本可控」，比讲「模型答得准」值钱得多。

## 5. 协议层岗位映射（MCP Engineer，2026 新增主线岗位）

> 来源：W36 周报 P1 修订 + 第 8 期 MCP Engineer 条目（llmhire.com 2026-04 / dev.to / secondtalent.com）。

- **岗位定义**：设计、构建、运营 MCP server——把企业「数据库 / API / 内部服务」标准化暴露给 AI Agent：server 开发（tools/resources/prompts）+ 安全权限模型 + 运营（schema 版本化 / 限流 / 审计）。
- **为何出现**：MCP 已入 Linux Foundation AAIF，月 SDK 下载 97M、10,000+ 生产 server，Orchestration Staff total $380K–$550K 为全 AI 岗类第二高；咨询/集成商 MCP 岗位 +410% 增长最快。
- **能力模型**：MCP 规范（tools/resources/prompts/sampling + stdio/SSE/HTTP 传输）、server 开发（TS-first + Python SDK）、工具 schema 设计（工具描述是 Agent 推理接口）、OAuth/OIDC 企业身份、prompt injection 威胁模型、eval-style 工具测试、A2A 互操作（agent→agent）、AP2（Agent Payments）。
- **学习路径**：精读 MCP 规范 → 自建 MCP server（Python SDK）→ 多模型 schema 测试 → 接入 e1 知识库 MCP 化。
- **对标**：`modelcontextprotocol/python-sdk`（24.1k★）、`typescript-sdk`（13.3k★）、`servers`（89.9k★）（均已克隆）；本期新增 `a2aproject/A2A`（25.7k★，Agent-to-Agent 协议，MCP 之上「agent→agent」互操作层）。
- **与 Harness 衔接**：MCP 是 Harness「Tool layer」的标准化协议——没有 MCP，Tool layer 退化为「每个 Agent 各自写一套工具接口」。

## 6. 交付物
- 练手：`projects/01-practice/p3-simple-agent`（工具调用 Agent）。
- 实战：`projects/02-enterprise/e2-smart-customer-service`（多工具客服 Agent + Harness 化）。
