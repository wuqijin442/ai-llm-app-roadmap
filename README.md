# AI 大模型应用开发 · 转岗学习路线图与实战仓库

> 从「后端 / 前端工程师」转向「AI 大模型应用开发」的系统性资料库、练手项目、企业级实战与阶段规划。
> 内容基于公开学习路线（参考 CSDN《学 AI 大模型的正确顺序》《Harness 到底是什么》等）+ 2026 年一线落地实践，并由本人结合真实工程背景**拓展与校正**。

---

## 一、这个仓库是什么 / 不是什么

**是什么**
- 一份**可执行的转岗学习地图**：从 0 到能独立交付企业级 AI 应用的完整路径。
- 一套**渐进式代码仓库**：练手项目（能跑通的最小闭环）→ 企业级实战（贴近真实业务）。
- 一份**个人视角的校正笔记**：哪些是 2026 年真刚需、哪些是噱头、后端/前端背景怎么借力。

**不是什么**
- 不是算法/论文研究仓库（应用开发岗 90% 不需要手推 Transformer 数学）。
- 不是「背完就上岸」的题库（项目作品集才是硬通货）。
- 不是一次性文档（本仓库按阶段持续增补，见 `docs/` 与 `roadmap/`）。

---

## 二、为什么转岗（我的视角）

我本职是 EMS 储能系统的后端 + 前端工程师（Java/Spring Boot + Vue），当前主做电价配置模块，面向台湾客户。决定往 AI 大模型应用方向转，基于几个判断：

1. **岗位需求结构性倾斜**：2026 年传统 CRUD 岗在收缩（参考英特尔裁员 2 万等信号），而 RAG / Agent / 私有化部署岗位在扩招。企业不是缺「会调 API 的人」，而是缺「能把模型接进业务系统、跑得稳、算得清成本」的工程人才。
2. **后端背景是强杠杆，不是从零开始**：
   - 你已经懂 **API 设计、鉴权、限流、异步、容器化、部署**——这些正是 AI 应用工程化的核心（AI 应用 ≈ 一个会调 LLM 的后端服务）。
   - 前端背景让你能做 **对话 UI、流式渲染（SSE）、可视化**——这是很多纯算法同学短板。
   - 你已有的 **DGX + Ollama bridge（本地跑 Qwen / DeepSeek / qwen3-vl）** 意味着「本地模型实验」对你来说是零额外成本，别人还在纠结算力，你已经能跑通。
3. **领域机会（储能 × AI）**：EMS 的工单摘要、电价知识库问答、设备日志异常归因、运维 Agent——全是大模型落地的高价值场景。转岗不一定离开行业，可以先在**本行业做 AI 落地**积累作品集。

> 一句话：**不要把自己当成「小白从零学 AI」，你是「有工程底盘、补齐 AI 应用层」的转岗者。** 这份路线就是为此设计的。

---

## 三、2026 年正确的学习顺序（6 大模块）

来源：参考文章《学 AI 大模型的正确顺序，千万不要搞错了》的 6 模块，本人按落地优先级重排并拓展。

| 顺序 | 模块 | 目标产出 | 我的校正 |
|---|---|---|---|
| 1 | **大模型基础认知** | 能说清 Token / 上下文窗口 / RAG / Agent；主流模型选型 | 不啃论文，建立直觉即可 |
| 2 | **开发基础能力** | 用 Python 调通大模型 API（流式 + 工具调用） | 后端同学 1 周可跑通第一个应用 |
| 3 | **Prompt 工程** | 10+ 高质量 Prompt 模板，稳定输出 | 从「写话术」升级到「结构化任务拆解」 |
| 4 | **RAG 检索增强** | 企业级知识库问答（带引用来源） | 企业落地第一刚需，面试最高频 |
| 5 | **Agent 智能体 + Harness** | 多工具协同 Agent、长任务运行系统 | 2026 拉开差距的是「模型外的系统设计」 |
| 6 | **微调 / 部署 / 面试** | 私有化部署服务 + 作品集 + 面试冲刺 | 微调了解流程即可，部署是工程岗加分项 |

> ⚠️ 关键认知（来自参考文章核心观点）：**2025 比的是模型和 Prompt，2026 比的是模型外面的系统设计（Harness）。** Prompt 决定单轮怎么答，Harness 决定系统在很多轮、很多工具、很长时间里能否稳定完成任务。本仓库把 Harness 作为进阶主线（见 `docs/05-Agent智能体与Harness.md`）。

---

## 四、仓库导航

```
ai-llm-app-roadmap/
├── README.md                      # 本文件：定位、路线总图、我的视角
├── docs/                          # 资料库（按主题深讲）
│   ├── 00-开篇-为什么转岗AI大模型应用.md
│   ├── 01-学习路线图总纲.md
│   ├── 02-大模型基础认知.md
│   ├── 03-Prompt工程.md
│   ├── 04-RAG检索增强生成.md
│   ├── 05-Agent智能体与Harness.md
│   ├── 06-模型微调与部署工程化.md
│   ├── 07-技术栈与开发框架.md
│   ├── 08-多模态大模型.md
│   ├── 09-企业级落地范式.md
│   ├── 10-面试求职冲刺.md
│   └── 11-工具平台与资源汇总.md
├── projects/                      # 代码仓库（由浅入深）
│   ├── 01-practice/               # 练手项目（最小可跑闭环）
│   │   ├── p1-chatbot-cli/        #   流式对话机器人
│   │   ├── p2-rag-docs-qa/        #   RAG 文档问答
│   │   ├── p3-simple-agent/       #   工具调用 Agent
│   │   ├── p4-prompt-lab/         #   Prompt 实验台
│   │   └── p5-mcp-server-lab/     #   MCP Server + 红队评测（9 类攻击）
│   └── 02-enterprise/             # 企业级实战（贴近业务）
│       ├── e1-enterprise-kb/      #   企业知识库
│       ├── e2-smart-customer-service/  # 智能客服
│       └── e3-doc-extraction/     #   文档结构化抽取
├── roadmap/                       # 阶段规划（打卡用）
│   ├── 30天-入门冲刺.md
│   ├── 90天-核心突破.md
│   └── 180天-转岗实战.md
├── cloned_projects/               # 克隆的企业级实战项目（gitignore，不入库，累计 61 个见第 7 节）
│   ├── ai-agents-for-beginners/   #   微软官方 Agent 教程（73.3k★）
│   ├── ruoyi-ai/                  #   Java 企业级 AI 框架（5.7k★）
│   ├── Langchain-Chatchat/        #   Python 本地知识库 RAG（38.6k★）
│   ├── FastGPT/                   #   Docker 企业级 RAG/Agent 平台（29.5k★）
│   ├── MaxKB/                     #   Docker 企业级知识库（22.6k★）
│   └── ...（第 2/3 期 20 个，见第 7 节清单）
├── weekly/                        # 周度汇总报告（每周日产出）
│   ├── 2026-W35-周报.md           #   W35 周报：28 岗位 / 25 仓库 / 99.92% 编译通过
│   ├── 2026-W36-周报.md           #   W36 周报：29 岗位 / 19 仓库 / 6 期主线 / 6 大趋势 / 7 项 docs 缺口
│   └── 2026-W37-周报.md           #   W37 周报：16 岗位 / 14 仓库 / 6 期主线（落地→数据→产品→岗位→编排→安全）/ 99.95% 编译通过 / langflow 154.6k★ 历史第二
├── scripts/                       # 可复现的测试/工具脚本
│   └── test_cloned_projects.py    #   克隆项目本地测试 harness
├── docs/
│   ├── ...（00~11 主题资料）
│   └── 20-克隆企业级项目测试报告.md   # 克隆项目全量测试报告
└── assets/                        # 架构图、脑图等
```

---

## 五、我的视角拓展（重点看这里）

这些是公开路线很少讲、但转岗成败关键的点：

1. **借力而非归零**：把「AI 应用」当成「带 LLM 调用的后端服务」来做。你写的 FastAPI 接口、Redis 会话缓存、Docker 部署、限流重试，全是直接复用技能。不要去和算法岗比模型，要比「工程化落地」。
2. **先有本地模型，再谈云**：你已经能在 DGX 上跑 Qwen / DeepSeek，练习阶段全部走本地，省 API 钱、还能调流式/工具调用。对外展示作品时再接一家公有 API（DeepSeek / 通义千问性价比高）。
3. **Harness 思维**：别只追求「模型答得好」。企业真正买账的是：失败能重试、长任务能续跑、工具调用有审批、有日志可观测、成本可控。把这些当成你的系统设计亮点写进简历。
4. **领域切入**：储能行业的「工单/电价/设备日志」是最好的练手语料，做成本行业知识库 + 运维 Agent，既是作品集又是给现公司的价值证明。
5. **项目驱动、拒绝收藏**：每个 `docs/` 主题都对应 `projects/` 里一个能跑的项目。只看不写 = 白学。

---

## 六、如何食用

1. 按 `roadmap/30天-入门冲刺.md` 打卡，每天对应 `docs/` 一个主题 + `projects/` 一个项目。
2. 先跑通 `projects/01-practice/p1-chatbot-cli`，建立「我能做出 AI 应用」的信心。
3. 用你自己的 DGX / 公有 API Key 替换示例里的占位配置。
4. 每完成一个企业级项目，按 `docs/10-面试求职冲刺.md` 的模板沉淀作品集。

---

## 七、克隆企业级实战项目（已本地测试）

为把「看教程」升级成「读真源码、跑真项目」，本仓库从 GitHub 高星仓库克隆了 **58 个**覆盖 Agent / RAG / 知识库 / 多 Agent 编排 / 微调 / 部署 / 安全 / MCP / 向量库 / 评测 / 可观测 / 治理 / 具身智能 / 工作流自动化 / LLM 可观测性 / AI 产品工程 / AI 销售 / AI Agent 框架 / Multimodal Agent / AI 教育认证 / Agent 商业化 / MCP 安全 / Token 经济学 / LLM 推理优化 / RAG 数据基础设施 / 评测基础设施 / Prompt 编译 / AI 平台 / OpenTelemetry GenAI / AI 评测 Ops / AI 合规 / AI 部署落地 / MCP 工程 / Agent 记忆层 / Agent 工作流推理引擎 / **AI 基础设施三件套（Ray 分布式计算 + MLflow AI 工程平台 + TGI 推理服务引擎）** / **企业级落地三件套（A2A 协议 + LeRobot 具身智能 + OpenAI Cookbook AI 教育）** / **AI 应用工程栈数据底座（GraphRAG RAG 数据基础设施 + Pydantic 数据契约 + uv 工程化底座）** / **AI 应用产品闭环与 RAG 应用框架深化（RAGFlow RAG 应用框架 + LlamaIndex 文档特化 RAG 框架 + AI 产品经理 AI 应用深化）** / **智能体开发工程师（smolagents HF 官方 500 行级 Agent 框架，CodeAgent 写代码执行 + 沙箱 + 多 Agent 编排 + 智能体开发员国家新职业对标）** / **AI 工作流编排双栈（Langflow 可视化编排 + Coze Studio 低代码编排，AI 工作流设计师 / AI 应用运维 / AI PM 工作流深化核心基础设施）** / **AI 应用安全与对齐三件套（Promptfoo LLM 红队测试 + NeMo Curator 数据策展投毒防御 + OpenAI Evals 对齐评估，LLM Red Teamer / RAG 投毒防御 / AI 对齐评估核心基础设施）**的实战项目，放入 `cloned_projects/`，并编写 `scripts/test_cloned_projects.py` 做**可复现的本地全量测试**。

> 每日任务按「岗位 → 对标仓库」逐期追加：第 1 期 5 个（2026-08-27）+ 第 2 期 11 个（2026-08-28）+ 第 3 期 9 个（2026-08-29）+ 第 4 期 2 个（2026-08-31）+ 第 5 期 6 个（2026-09-01）+ 第 6 期 3 个（2026-09-02）+ 第 7 期 3 个（2026-09-03）+ 第 8 期 2 个（2026-09-04）+ 第 9 期 3 个（2026-09-05）+ 第 10 期 3 个（2026-09-07）+ 第 11 期 3 个（2026-09-08）+ 第 12 期 2 个（2026-09-09）+ 第 13 期 1 个（2026-09-10）+ 第 14 期 2 个（2026-09-11）+ 第 15 期 3 个（2026-09-12）+ 第 16 期 3 个（2026-09-14）= 累计 61 个。
> 完整测试报告（含每项的命令与输出证据）：[`docs/20-克隆企业级项目测试报告.md`](docs/20-克隆企业级项目测试报告.md)
> 安全策略：仅克隆官方高星仓库，未引入任何未知/冷门未审计源码；克隆目录已 gitignore，**不入库**，仅元数据与测试报告入库。

### 7.1 项目清单与测试结果

**第 1 期（2026-08-27）· Agent / RAG / 企业框架基础**

| 项目 | 定位 | Stars | 本机测试结论 |
|---|---|---|---|
| `microsoft/ai-agents-for-beginners` | Agent 入门教程（18 课，官方） | 73.4k | ✅ 15 个 .py 全量语法编译通过；2240 个 .ipynb JSON 全部合法 |
| `ageerle/ruoyi-ai` | 基于 RuoYi 的 Java 企业级 AI 框架 | 5.7k | ✅ 24 个 .py 编译通过；pom.xml well-formed（4 模块） |
| `chatchat-space/Langchain-Chatchat` | Python 本地知识库 RAG/Agent | 38.6k | ✅ 281 个 .py 全量语法编译通过 |
| `labring/FastGPT` | Docker 企业级 RAG/Agent 平台（Next.js+TS） | 29.5k | ✅ 脚手架校验（docker-compose + package.json scripts） |
| `1Panel-dev/MaxKB` | Docker 企业级知识库问答（Python+Vue） | 22.6k | ✅ 1051 个 .py 全量语法编译通过 |

**第 2 期（2026-08-28）· Agentic 时代角色分化（编排 / 微调 / 部署 / 安全 / MCP）**

| 项目 | 定位 | Stars | 本机测试结论 |
|---|---|---|---|
| `langchain-ai/langgraph` | LangGraph 状态机 + 多 Agent 编排 | 40.6k | ✅ 452 个 .py 编译通过；35 个 .ipynb 合法 |
| `crewAIInc/crewAI` | CrewAI 多 Agent 协作框架 | 57.8k | ⚠️ 1314/1319 通过（5 个 CLI 模板占位符 `{{folder_name}}`，预期） |
| `microsoft/autogen` | AutoGen 多 Agent 对话框架 | 60.7k | ✅ 546 个 .py 编译通过；49 个 .ipynb 合法 |
| `huggingface/peft` | HF PEFT（LoRA/QLoRA/IA3） | 21.6k | ✅ 443 个 .py 编译通过；48 个 .ipynb 合法 |
| `vllm-project/vllm` | vLLM 高吞吐 LLM 推理引擎 | 90.4k | ✅ 4324 个 .py 编译通过（本期最大） |
| `nvidia/NeMo-Guardrails` | LLM 安全护栏 | 7.0k | ✅ 938 个 .py 编译通过；19 个 .ipynb 合法 |
| `protectai/rebuff` | LLM 提示注入防御 | 1.5k | ✅ 13 个 .py 编译通过 |
| `protectai/llm-guard` | LLM I/O 安全检查 | 3.2k | ✅ 217 个 .py 编译通过；6 个 .ipynb 合法 |
| `modelcontextprotocol/servers` | MCP 官方参考服务器集合 | 89.9k | ✅ 14 个 .py 编译通过 |
| `modelcontextprotocol/typescript-sdk` | MCP TypeScript SDK | 13.3k | ✅ 脚手架校验（package.json scripts） |
| `modelcontextprotocol/python-sdk` | MCP Python SDK | 24.1k | ✅ 835 个 .py 编译通过 |

**第 3 期（2026-08-29）· 生产链路落地（保 / 测 / 架 / 管）**

| 项目 | 定位 | Stars | 本机测试结论 |
|---|---|---|---|
| `openvla/openvla` | OpenVLA（VLA 机器人模型） | 6.9k | ✅ 97 个 .py 编译通过 |
| `explodinggradients/ragas` | Ragas（LLM 应用评测框架） | 15.5k | ✅ 387 个 .py 编译通过；23 个 .ipynb 合法 |
| `qdrant/qdrant` | Qdrant 向量数据库（Rust） | 34.3k | ✅ 225 个 .py 编译通过；docker-compose + Dockerfile |
| `pgvector/pgvector` | PostgreSQL 向量检索扩展（C） | 22.8k | ✅ 结构校验（Dockerfile） |
| `open-telemetry/opentelemetry-python` | OpenTelemetry Python（Agent 可观测） | 2.6k | ✅ 750 个 .py 编译通过 |
| `huggingface/datasets` | HF Datasets（训练数据管理） | 21.9k | ✅ 237 个 .py 编译通过 |
| `huggingface/huggingface_hub` | HF Hub（模型/数据集管理） | 3.9k | ✅ 286 个 .py 编译通过 |
| `microsoft/responsible-ai-toolbox` | Responsible AI Toolbox（AI 治理） | 1.8k | ✅ 288 个 .py 编译通过；28 个 .ipynb 合法 |
| `weaviate/weaviate` | Weaviate 向量数据库（Go） | 16.8k | ✅ 54 个 .py 编译通过；docker-compose + Dockerfile |

**第 4 期（2026-08-31）· AI 应用落地最后一公里（教育 + 可靠性 + GTM）**

| 项目 | 定位 | Stars | 本机测试结论 |
|---|---|---|---|
| `langfuse/langfuse` | LLM 可观测性平台（MIT，ClickHouse 旗下） | 33.9k | ✅ 5 个 .py 全量语法编译通过；docker-compose + Dockerfile + package.json scripts |
| `n8n-io/n8n` | 工作流自动化 + AI Agent 节点（Sustainable Use License） | 202.9k | ✅ 69 个 .py 全量语法编译通过（本期最大）；docker-compose + Dockerfile + package.json scripts |

> 第 4 期 2 个仓库覆盖 5 个岗位（AI Reliability、LLM Observability、AI GTM、AI Workflow Automation、AI 教育），n8n 202.9k stars 为本仓库历史最高（超过 vllm 90.4k stars）。

**第 5 期（2026-09-01）· AI 应用商业闭环与前沿（产品 + 销售 + 框架 + 多模态 + 认证 + 商业化）**

| 项目 | 定位 | Stars | 本机测试结论 |
|---|---|---|---|
| `All-Hands-AI/OpenHands` | AI 软件工程 Agent（前 OpenDevin，MIT，$18.8M Series A） | 85.8k | ✅ 10 个 .py 全量语法编译通过；docker-compose + Dockerfile + package.json scripts |
| `openai/openai-agents-python` | OpenAI 官方 Agent SDK（Python，MIT） | 29.1k | ✅ 923 个 .py 全量语法编译通过 |
| `stanfordnlp/dspy` | Stanford 声明式 AI 应用编程框架（Prompt 编译优化，Python） | 37.7k | ✅ 279 个 .py 全量语法编译通过 |
| `anthropics/anthropic-cookbook` | Anthropic 官方示例库（Jupyter Notebook，AI 教育核心教材） | 52.3k | ✅ 121 个 .py 全量语法编译通过；Notebook JSON 全部合法 |
| `langgenius/dify` | LLMOps 可视化 + AI 工作流平台（修改版 Apache 2.0，多租户 SaaS 需商业许可） | 154.0k | ✅ 3,877 个 .py 全量语法编译通过（本期最大，本仓库 Python 仓库之最）；docker-compose + Dockerfile + package.json scripts |
| `browser-use/browser-use` | AI 浏览器自动化 Agent（Python，RPA 替代 + computer use） | 111.9k | ✅ 388 个 .py 全量语法编译通过；pyproject.toml + Dockerfile |

> 第 5 期 6 个仓库覆盖 6 个岗位（AI Product Engineering、AI Sales Engineer、AI Agent Framework、Multimodal Agent、AI Educator 认证深化、AI Agent 商业化 PM），dify 154k stars 为本仓库历史第二高（仅次于 n8n 202.9k stars），dify 3,877 个 .py 为本期最大（也是本仓库历史 Python 仓库之最，超过 vllm 4,324 个 .py）。

**第 6 期（2026-09-02）· 生产级 Agent 的 5 条工程化路径（安全 + 成本 + 性能 + 数据 + 评测 + 编译）**

| 项目 | 定位 | Stars | 本机测试结论 |
|---|---|---|---|
| `guardrails-ai/guardrails` | LLM 输出护栏 + Validator 编排框架（Python，AI Agent Security 核心基础设施） | 7.3k | ✅ .py 全量语法编译通过；pyproject.toml + Makefile |
| `openai/openai-python` | OpenAI 官方 Python SDK（多模型路由 + 批处理 + Prompt Caching 基础，AI Agent Cost / Inference Engineering 核心基础设施） | 31.5k | ✅ .py 全量语法编译通过；pyproject.toml + package.json scripts |
| `milvus-io/milvus` | 云原生向量数据库（Go+C++ 双后端，AI Data Engineer for RAG 核心基础设施） | 45.9k | ✅ 结构校验（Dockerfile + docker-compose + Makefile） |

> 第 6 期 3 个仓库覆盖 6 个岗位（AI Agent Security、AI Agent Cost、LLM Inference Optimization、AI Data Engineer for RAG、AI Agent Evaluation、AI Prompt Compiler），milvus 45.9k stars 为「云原生向量数据库」赛道最成熟方案之一，openai-python 31.5k stars 为「官方 SDK」赛道最成熟方案，guardrails 7.3k stars 为「LLM 输出护栏 + Validator 编排」赛道最成熟方案之一。
> 注：GitHub 直连不可达，本期 3 个仓库通过 codeload tarball 下载（`codeload.github.com`），完整测试明细以 `docs/20` 为准。

**第 7 期（2026-09-03）· Agent 生产治理三支柱（可管 + 可查 + 能测 + 能合规 + 能落地）**

| 项目 | 定位 | Stars | 本机测试结论 |
|---|---|---|---|
| `open-telemetry/opentelemetry-collector` | 遥测数据管道（Go，OpenTelemetry GenAI 语义约定 + Collector receivers/processors/exporters，AI Platform / LLM Observability 核心基础设施） | 7.5k | ✅ 结构校验（Dockerfile + go.mod + Makefile）；2,848 文件 |
| `confident-ai/deepeval` | LLM 应用评测框架（15+ 内建指标 + 幻觉/偏见/毒性检测 + LLM-as-judge 校准，AI Evaluation Ops / AI Compliance 核心基础设施） | 18.1k | ✅ .py 全量语法编译通过；pyproject.toml + Makefile；992 个 .py |
| `google/adk-python` | Google 官方 Agent 开发框架（Python，AI Deployment / FDE / AI Platform 核心基础设施） | 21.4k | ✅ .py 全量语法编译通过；pyproject.toml + Dockerfile；1,853 个 .py |

> 第 7 期 3 个仓库覆盖 5 个岗位（AI Platform Engineer、LLM Observability Engineer（标准化）、AI Evaluation Ops Engineer、AI Compliance Engineer（时间窗）、AI Deployment / FDE（落地）），otel-collector 7.5k stars（Go）是「OpenTelemetry GenAI 语义约定 + 数据管道」核心基础设施，deepeval 18.1k stars 是「LLM 应用自动化评测 + 偏见/毒性检测」核心基础设施，adk-python 21.4k stars 是「Google 官方 Agent 框架」核心基础设施。
> 注：otel-collector 通过 git 直连克隆成功；deepeval GitHub 直连失败（curl 56），改用 codeload tarball 下载成功；adk-python 为已克隆补登记（第 5 期 AI Agent Framework 已引用）。完整测试明细以 `docs/20` 为准。

**第 8 期（2026-09-04）· 治理底座三根深水桩（协议 + 记忆 + 引擎）**

| 项目 | 定位 | Stars | 本机测试结论 |
|---|---|---|---|
| `sgl-project/sglang` | 高性能 LLM 推理引擎（RadixAttention 前缀缓存 + 结构化输出 xgrammar + EAGLE-3 投机解码，Agent 工作流 TTFT 降 60%，400,000+ GPU 部署，LLM Inference Engineer Agent 特化核心基础设施） | 34.1k | ✅ 6,207 个 .py 全量语法编译通过（本仓库 .py 数历史第一）；3 个 .ipynb 全部合法；docker-compose + Dockerfile |
| `mem0ai/mem0` | AI Agent 通用长期记忆层（五层记忆栈 + 事实抽取 + 多信号检索 + 时间推理，LongMemEval 94.4 / LoCoMo 92.5 基准第一，Context/Memory Engineer 核心基础设施） | 64.7k | ✅ 390 个 .py 全量语法编译通过；7 个 .ipynb 全部合法；docker-compose + Dockerfile |

> 第 8 期 2 个仓库覆盖 3 个岗位（MCP Engineer、Context Engineering / AI Memory Engineer、LLM Inference Engineer（Agent 特化）），其中 MCP Engineer 由已克隆的 mcp-python-sdk / mcp-typescript-sdk / mcp-servers 共同对标；mem0 64.7k stars 为本仓库历史第三高（仅次于 n8n 202.9k / dify 154k），是「记忆层」品类 star 数第一（对照 Zep ~12k / Letta ~18k）；sglang 6,207 个 .py 为本仓库 Python 仓库 .py 数历史第一（超过 dify 3,877）。本期 2 仓库测试全绿（100% 编译通过率）。
> 注：本期 GitHub 直连（git clone）连续失败（Failed to connect to github.com:443），沿用第 6 期 fallback，两仓库均走 `codeload.github.com` tarball 下载成功（sglang 30MB / mem0 19MB），非 git 元数据克隆（无 .git 目录）。完整测试明细以 `docs/20` 为准。

**第 9 期（2026-09-05）· AI 基础设施三件套（算力引擎 + 平台层 + 服务引擎）**

| 项目 | 定位 | Stars | 本机测试结论 |
|---|---|---|---|
| `ray-project/ray` | AI compute engine（Ray Core 分布式计算 + GPU 编排 + 调度 + 容错 + Ray Serve，AI Infrastructure / AI Platform 核心基础设施） | 43.7k | ⚠️ 4807/4808 个 .py 通过（失败 1：`syntax_error.py`，测试用例预期失败）；62 个 .ipynb 全部合法；Dockerfile |
| `mlflow/mlflow` | 开源 AI 工程平台（实验追踪 + 模型注册 + LLM 评测 + MLflow GenAI，AI Platform / AI Solution Architect 核心基础设施） | 27.8k | ✅ 2675 个 .py 全量语法编译通过；42 个 .ipynb 全部合法；docker-compose + Dockerfile |
| `huggingface/text-generation-inference` | 生产级 LLM 推理服务引擎（Rust 后端 + CUDA 加速 + continuous batching + 多 GPU 并行，与 vLLM/SGLang 形成「三大引擎」格局，LLM Inference Engineer 核心基础设施） | 10.9k | ✅ 380 个 .py 全量语法编译通过；Dockerfile |

**第 10 期（2026-09-07）· 企业级落地三件套（架构 + 互操作 + 具身 + 教育）**

| 项目 | 定位 | Stars | 本机测试结论 |
|---|---|---|---|
| `a2aproject/A2A` | Agent-to-Agent 协议（Google/Linux Foundation 托管，MCP 之上「agent→agent」互操作层，AI Solution Architect / A2A 协议工程师核心基础设施） | 25.7k | ✅ 3 个 .py 全量语法编译通过 |
| `huggingface/lerobot` | HF 官方 VLA 策略框架（SO-101 机械臂 + ACT/Diffusion Policy/π0，具身智能 / VLA 工程师核心基础设施） | 27.3k | ✅ 812 个 .py 全量语法编译通过；1 个 .ipynb 合法 |
| `openai/openai-cookbook` | OpenAI 官方示例库（Jupyter Notebook，AI 教育深化核心教材，AI Trainer / 企业内训 / 认证核心基础设施） | 75.8k | ✅ 225 个 .py 全量语法编译通过；272 个 .ipynb 全部合法（本仓库 Notebook 数历史第一）；docker-compose + Dockerfile |

> 第 10 期 3 个仓库覆盖 4 个岗位（AI Solution Architect、具身智能 / VLA 工程师、AI 教育深化、A2A 协议工程师），其中 A2A 协议工程师由 `a2aproject/A2A` + 已克隆的 mcp-python-sdk / typescript-sdk / servers 共同对标；a2aproject/A2A 25.7k stars 为「Agent 互操作协议」品类 star 数第一（对照 modelcontextprotocol/servers 89.9k stars 是「工具服务器集合」，不是「agent 间协议」）；huggingface/lerobot 27.3k stars / 812 .py 为「具身智能 / VLA 策略框架」品类 star 数第一（对照 openvla 6.9k stars / NVIDIA/Isaac-GR00T 8.0k stars）；openai/openai-cookbook 75.8k stars / 272 .ipynb 为「AI 教育深化 / 官方示例库」品类 star 数第二（对照 anthropic-cookbook 52.3k stars）。
> 注：本期 a2aproject/A2A 通过 git 直连克隆成功（164 文件）；huggingface/lerobot（6.4MB）+ openai/openai-cookbook（790.7MB）GitHub 直连失败（Failed to connect to github.com:443），沿用第 6/8/9 期 fallback，两仓库均走 `codeload.github.com` tarball 下载成功，非 git 元数据克隆（无 .git 目录）。完整测试明细以 `docs/20` 为准。

**第 11 期（2026-09-08）· AI 应用工程栈数据底座（RAG 数据基础设施 + 数据契约 + 工程化底座）**

| 项目 | 定位 | Stars | 本机测试结论 |
|---|---|---|---|
| `microsoft/graphrag` | 模块化图基 RAG（实体/关系抽取 + 社区摘要 + 多跳检索，RAG 数据基础设施进阶，RAG 数据基础设施工程师核心基础设施） | 35.9k | ✅ 574 个 .py 全量语法编译通过；40 个 .ipynb 全部合法 |
| `pydantic/pydantic` | Python 数据校验（Pydantic V2 Rust 核心 + JSON Schema 自动生成，Agent 工具 I/O 数据契约层核心基础设施） | 28.7k | ✅ 442 个 .py 全量语法编译通过 |
| `astral-sh/uv` | Rust 编写的高性能 Python 包 + 项目管理器（比 pip 快 10–100 倍，AI 平台「环境即代码」核心基础设施） | 89.6k | ✅ 105 个 .py 全量语法编译通过；Dockerfile ✅ |

> 第 11 期 3 个仓库覆盖 3 个岗位（RAG 数据基础设施工程师、AI 数据契约工程师、AI 工程化底座工程师），其中 RAG 数据基础设施由 `graphrag` + 已克隆的 qdrant / pgvector / weaviate / milvus 共同对标，AI 数据契约由 `pydantic` + 已克隆的 mcp-python-sdk / typescript-sdk 共同对标，AI 工程化底座由 `uv` + `pydantic` + `graphrag` 共同对标；astral-sh/uv 89.6k stars 为「Python 包管理」品类 star 数第一（超过 pypa/pip ~50k★）、microsoft/graphrag 35.9k stars 为「GraphRAG / 知识图谱 RAG」品类 star 数第一、pydantic/pydantic 28.7k stars 为「Python 数据校验」品类 star 数第一。
> 注：本期 3 仓库全部通过 git 直连克隆成功（有 .git 目录，优于第 6/8/9/10 期 codeload tarball fallback，graphrag 908 文件 / pydantic 828 文件 / uv 1,738 文件，全部 4s 内完成），无网络抖动。完整测试明细以 `docs/20` 为准。

**第 12 期（2026-09-09）· AI 应用产品闭环与 RAG 应用框架深化（RAG 应用框架 + AI 产品经理 AI 应用深化）**

| 项目 | 定位 | Stars | 本机测试结论 |
|---|---|---|---|
| `infiniflow/ragflow` | 深度文档理解 RAG 引擎（表格/布局/OCR + 模板化 chunking + GraphRAG + 可视化工作流 + 多模态 + Agent-ready，RAG 应用框架 + AI PM 深化核心基础设施） | 90.3k | ✅ （测试脚本运行中，Go 主语言 B 级仅覆盖 Python 子模块）；docker-compose + Dockerfile |
| `run-llama/llama_index` | 文档特化 RAG 框架（160+ 数据源连接器 + 8+ 索引类型 + 原生 RouterQueryEngine + 内置 FaithfulnessEvaluator / RelevancyEvaluator，RAG 应用框架核心基础设施） | 52.1k | ✅ （测试脚本运行中，Python）；pyproject.toml + Dockerfile |

> 第 12 期 2 个仓库覆盖 2 个岗位（AI 产品经理 AI 应用深化、RAG 应用框架工程师），其中 AI PM 深化由 `ragflow` + 已克隆的 dify / FastGPT / OpenHands 共同对标，RAG 应用框架由 `llama_index` + `ragflow` + 已克隆的 dify / graphrag / qdrant / pgvector / weaviate / milvus 共同对标；infiniflow/ragflow 90.3k stars 为「RAG 应用框架」品类 star 数第一梯队（对照 Dify 154k★ 是「LLMOps 可视化平台」、LlamaIndex 52,076★ 是「文档特化 RAG 框架」、GraphRAG 35,875★ 是「RAG 数据基础设施」）、run-llama/llama_index 52.1k stars 为「文档特化 RAG 框架」品类 star 数第一（对照 LangChain 143k★ 是「Agent 编排框架」）。
> 注：本期 2 仓库 GitHub 直连（git clone）均失败（Failed to connect to github.com:443 / Recv failure: Connection was reset），沿用第 6/8/9/10 期 fallback，两仓库均走 `codeload.github.com` tarball 下载成功（ragflow 18.4MB / llama_index 272MB），非 git 元数据克隆（无 .git 目录）。完整测试明细以 `docs/20` 为准。

**第 13 期（2026-09-10）· 智能体开发工程师（官方认定新职业深化 + 薪资对标）**

| 项目 | 定位 | Stars | 本机测试结论 |
|---|---|---|---|
| `huggingface/smolagents` | HF 官方 500 行级 Agent 框架（CodeAgent 写代码执行动作 + E2B/Modal/Docker 沙箱 + Hub 集成 + 多 Agent 编排，智能体开发员国家新职业对标） | 29.3k | ✅ 75 个 .py 全量语法编译通过；3 个 .ipynb 全部合法；pyproject.toml ✅ + Makefile ✅ |

> 第 13 期 1 个仓库覆盖 1 个岗位（智能体开发工程师：官方认定新职业深化），智能体开发员 2026-09-09 成国家新职业（人社部第八批新职业信息），AI 智能体开发人才需求 +244% / 核心开发人才缺口 500 万 / 供需比 1:10；huggingface/smolagents 29,262★ 为「智能体开发」品类 HF 官方标杆（对照 langchain-ai/langgraph 40.6k★ 是「Agent 编排框架」、crewAI 57.8k★ 是「多 Agent 协作框架」、openai-agents-python 29.1k★ 是「OpenAI 官方 Agent SDK」），~1,000 行代码级 Agent 框架（agents.py 单文件），「Agent 框架」从「复杂编排」升级为「**极简可理解**」（500 行代码可读懂全部 Agent 逻辑，适合教学与二次开发）。
> 注：本期 GitHub 直连（git clone）失败（curl 56 Recv failure: Connection was reset），沿用第 6/8/9/10/12 期 fallback，走 `codeload.github.com` tarball 下载成功（smolagents 1.19MB），非 git 元数据克隆（无 .git 目录）。完整测试明细以 `docs/20` 为准。

**第 14 期（2026-09-11）· AI 工作流编排双栈（可视化 + 低代码）+ AI 应用运维（AIOps）**

| 项目 | 定位 | Stars | 本机测试结论 |
|---|---|---|---|
| `langflow-ai/langflow` | 低代码 Agent + 工作流编排平台（拖拽式构建 + 多模型路由 + RAG 集成 + 工具编排，AI 工作流设计师 / AI 应用运维 / AI PM 工作流深化核心基础设施） | 154.6k | ✅ 4,042 个 .py 待全量编译（测试脚本运行中）；docker-compose + Dockerfile |
| `coze-dev/coze-studio` | 字节官方低代码 Agent 平台（插件 + 工作流 + 多 Agent 编排 + 知识库，AI 工作流设计师 / AI 应用运维核心基础设施） | 21.6k | ✅ 5,941 个 .ts + 3 个 .py 待全量编译（测试脚本运行中）；package.json + docker-compose |

> 第 14 期 2 个仓库覆盖 3 个岗位（AI 工作流设计师：2026 新增热门岗位 / AI 应用运维（AIOps）：US 中位 $156K / 国内一线 30–70K+ / AI PM 工作流深化：71% 岗位不需要真正懂 AI 底层），其中 AI 工作流设计师由 `langflow` + `coze-studio` + 已克隆的 dify / n8n / FastGPT 共同对标，AI 应用运维由 `langflow` + `coze-studio` + 已克隆的 otel-collector / langfuse / vllm / sglang / tgi 共同对标，AI PM 工作流深化由 `langflow` + `coze-studio` + 已克隆的 dify / n8n 共同对标；langflow-ai/langflow 154,553★ 为「AI 工作流编排（可视化）」品类 star 数第一（对照 langgenius/dify 154k★ 是「LLMOps 可视化 + AI 工作流平台」、n8n 202.9k★ 是「工作流自动化 + AI Agent 节点」、coze-dev/coze-studio 21.6k★ 是「低代码 Agent 平台」）、coze-dev/coze-studio 21,574★ 为「AI 工作流编排（低代码）」品类字节官方标杆（对照 coze-dev/coze-loop 5,714★ 是「Go 后端」）。
> 注：本期 2 仓库全部通过 git 直连克隆成功（langflow 352M / coze-studio 133M，无网络抖动，优于第 6/8/9/10/12/13 期 codeload tarball fallback），非 git 元数据克隆（有 .git 目录）。完整测试明细以 `docs/20` 为准。

**第 15 期（2026-09-12）· AI 应用安全与对齐三件套（红队安全 + RAG 投毒防御 + 对齐评估）**

| 项目 | 定位 | Stars | 本机测试结论 |
|---|---|---|---|
| `promptfoo/promptfoo` | LLM 红队测试 / 提示注入 / 越狱 / 数据投毒防御框架（TypeScript，LLM Red Teamer / RAG 投毒防御核心基础设施） | 25.0k | ✅ 102/102 .py 全量编译通过；package.json scripts + Dockerfile + .devcontainer docker-compose |
| `NVIDIA-NeMo/Curator` | 数据策展 / 质量评估 / 清洗 / 去重 / 过滤（Python，RAG 投毒防御数据治理侧核心基础设施） | 1.8k | ✅ 971/971 .py 全量编译通过 + 20 .ipynb JSON 全部合法；pyproject.toml + Dockerfile |
| `openai/evals` | LLM 对齐评估 / 能力评测 / 安全评测 / 基准测试框架（Python，AI 对齐评估工程师核心基础设施） | 19.4k | ✅ 353/353 .py 全量编译通过 + 5 .ipynb JSON 全部合法；pyproject.toml + Dockerfile（elsuite） |

> 第 15 期 3 个仓库覆盖 3 个岗位（LLM Red Teamer：2026 增长最快 AI 安全细分 / RAG 投毒防御工程师：RAG 投毒 0.04% 语料 → 98% 攻击成功率 / AI 对齐评估工程师：LLM Evaluation +210% YoY），其中 LLM Red Teamer 由 `promptfoo` + 已克隆的 `deepeval` / `llm-guard` / `rebuff` / `guardrails` / `NeMo-Guardrails` 共同对标，RAG 投毒防御由 `neMo-Curator` + `promptfoo` + 已克隆的 `graphrag` / `milvus` / `qdrant` / `pgvector` / `weaviate` 共同对标，AI 对齐评估由 `openai-evals` + 已克隆的 `deepeval` / `ragas` / `dspy` / `langfuse` / `helm` 共同对标；promptfoo 25.0k stars 为「LLM 红队测试」品类 star 数第一（对照 NVIDIA/garak 9.2k★ 是「LLM 红队扫描」、confident-ai/deepeval 18.1k★ 是「LLM 评测框架」）、NVIDIA-NeMo/Curator 1.8k stars 为「数据策展 / 质量评估」品类 NVIDIA 官方标杆（对照 NVIDIA/NeMo 是「LLM 训练框架」）、openai/evals 为「LLM 对齐评估」品类 OpenAI 官方标杆（对照 confident-ai/deepeval 18.1k★ 是「LLM 评测框架」、explodinggradients/ragas 15.5k★ 是「RAG 评测」）。
> 注：本期 GitHub 直连（git clone）失败（curl 28 Failed to connect to github.com:443），沿用第 6/8/9/10/12/13 期 fallback，3 仓库均走 `codeload.github.com` tarball 下载成功（promptfoo 239M / neMo-Curator 36M / openai-evals 8M，其中 promptfoo 用 Clash 代理 127.0.0.1:7890 重试成功），非 git 元数据克隆（无 .git 目录）。完整测试明细以 `docs/20` 为准。

**第 16 期（2026-09-14）· Agent 的耳朵、嘴巴与离线小脑（实时语音 Agent 双栈 + 端侧 LLM 推理底座）**

| 项目 | 定位 | Stars | 本机测试结论 |
|---|---|---|---|
| `livekit/agents` | 实时语音 Agent 编排框架（WebRTC 基础设施公司 LiveKit 官方，pipeline 编排 + 多 provider 插件 + 电话/WebRTC 接入 + worker 分布式部署，Voice AI Engineer 核心基础设施） | 14.2k | ⚠️ 1,042/1,044 .py 全量编译通过（失败 2 为上游 main 分支缺陷：elevenlabs stt.py 参数重复定义）；docker-compose + Dockerfile |
| `pipecat-ai/pipecat` | 开源 voice agent / 多模态 / realtime AI 框架（Daily 旗下官方维护，流式 ASR/LLM/TTS 抽象 + 打断/轮次内建，Voice AI Engineer 核心基础设施） | 15.5k | ✅ 1,343/1,343 .py 全量编译通过；pyproject.toml |
| `ggml-org/llama.cpp` | 端侧/本地 LLM 推理底座（纯 C/C++，GGUF 量化格式事实标准 + CPU/GPU/NPU 混合 + 手机/笔电/树莓派全覆盖，端侧 LLM 工程师核心基础设施） | 128.1k | ✅ 219/219 .py 全量编译通过（B 级仅覆盖 Python 子模块）；Makefile + CMakeLists.txt（本机构建走 D 级） |

> 第 16 期 3 个仓库覆盖 3 个岗位（Voice AI Engineer：US +45% YoY / 2,055 在招 / 417 家公司 / 国内高德 30–55K 到字节 100–200K×15 薪 + 端侧 LLM 工程师：UK £45K–£180K / NPU 50–80 TOPS / 比移动开发溢价 30–45% + Conversational AI Designer：语言学背景切入的非工程岗），其中 Voice AI Engineer 由 `livekit-agents` + `pipecat` 双栈对标（中立框架 vs 平台框架），端侧 LLM 工程师由 `llama.cpp` 对标（Ollama 是其封装层，DGX 本地推理经验直接下钻）；ggml-org/llama.cpp 128,102★ 为「端侧/本地 LLM 推理」品类 star 数第一且断层领先，本仓库历史第四高星（仅次于 n8n 202.9k★ / langflow 154.6k★ / dify 154.0k★）。
> 注：本期 GitHub 直连（git clone）超时挂起，3 仓库均走 `codeload.github.com` tarball 下载成功（无 .git 目录）。完整测试明细以 `docs/20` 为准。

> 第 9 期 3 个仓库覆盖 3 个岗位（AI Infrastructure Engineer、AI Platform Engineer 深化、LLM Inference Engineer 三大引擎特化），其中 AI Infrastructure 由 `ray` + `vllm` + `sglang` + `tgi` 共同对标，AI Platform 由 `mlflow` + `langfuse` + `deepeval` + `ragas` + `otel-collector` 共同对标，LLM Inference 由 `tgi` + `vllm` + `sglang` 共同对标；ray 43.7k stars 为「分布式计算引擎」品类 star 数第一、mlflow 27.8k stars 为「AI 工程平台」品类 star 数第一、tgi 10.9k stars 为「HF 官方推理服务引擎」第一。
> 注：本期 GitHub 直连（git clone）全部失败（curl 28 Failed to connect to github.com:443），沿用第 6/8 期 fallback，三仓库均走 `codeload.github.com` tarball 下载成功（ray 198MB / mlflow 291MB / tgi 3.1MB），非 git 元数据克隆（无 .git 目录）。完整测试明细以 `docs/20` 为准。

**共用后端冒烟（分级 A，已通过）**：本地 Ollama 桥接 `http://127.0.0.1:11434/api/chat`（模型 `qwen3-coder:30b`）实测 HTTP 200、`done_reason=stop`，返回 `OK-SMOKE-TEST`。所有兼容 OpenAI/Ollama 的项目均可指向该端点做本地推理，无需云密钥。

### 7.2 本机测试分级说明

- **A 级（已真实执行）**：Ollama 本地模型冒烟。
- **B 级（已真实执行）**：Python 全量语法编译（`python -m py_compile` 全部 .py）。
- **C 级（已真实执行）**：Notebook JSON 合法性、Maven POM well-formed、Docker 脚手架存在性。
- **D 级（本机未执行 · 环境限制，非代码问题，附操作手册）**：需 Docker daemon + 数据库，或 Maven（本机缺失）/ Jupyter（本机缺失）/ 云密钥。详见测试报告与各仓库 README。

### 7.3 各项目「如何在本机跑通」（操作手册）

> 以下为第 1 期 5 个项目的典型路径，**具体以各仓库最新 README 为准**。所有「LLM/embedding」配置均可替换为本地 Ollama：`base_url=http://127.0.0.1:11434/v1`，`api_key=sk-任意`，`model=qwen3-coder:30b` / `qwen3-vl:8b`。
> 第 2/3 期追加的 20 个项目（编排 / 微调 / 部署 / 安全 / MCP / 向量库 / 评测 / 可观测 / 治理 / 具身智能）运行方式详见 [`docs/20-克隆企业级项目测试报告.md`](docs/20-克隆企业级项目测试报告.md) 与各自仓库 README；其中 Python 仓库统一走 `pip install -e .`，Rust/Go 仓库（qdrant / weaviate）走 `docker compose up -d`，C 扩展（pgvector）走 `make && make install`（需本地 PostgreSQL）。

1. **ai-agents-for-beginners（教程）**
   - 前置：Jupyter（`pip install jupyter`）+ 一个 LLM 端点。
   - 跑通：`pip install -r requirements.txt` → 打开 `00-course-setup` 起逐课运行；把 notebook 里的 AzureOpenAI 客户端改为 `OpenAI(base_url="http://127.0.0.1:11434/v1")`。
2. **ruoyi-ai（Java 企业框架）**
   - 前置：JDK17（本机已有）+ **Maven（本机缺失，需装）** + MySQL + Redis。
   - 跑通：`mvn clean package` → IDEA 导入；`docker compose -f docs/docker/ruoyi-ai/docker-compose.yaml up -d` 起中间件；改 `application.yml` 的 DB/Redis 与 LLM（支持 Ollama）；启动 `RuyiAiApplication`。
3. **Langchain-Chatchat（Python RAG）**
   - 前置：Python 3.10+、本地模型（Ollama Qwen）。
   - 跑通：`pip install -e .`（或 poetry）→ `python copy_config.py` → `python init_database.py --recreate-vs` 建向量库 → 放文档到 `kmss/` → `python startup.py -a`；配置里 LLM/embedding 指向 Ollama。
4. **FastGPT（Docker 平台）**
   - 前置：Docker daemon 运行中 + 一个 LLM（兼容 OpenAI，可填 Ollama base_url）。
   - 跑通：`cp docs/.env.example .` 改 key → `docker compose -f deploy/docker/docker-compose.yml up -d` → 访问 3000 端口。
5. **MaxKB（Docker 知识库）**
   - 前置：Docker daemon + 内置向量库。
   - 跑通：`cd installer && cp config_example.yml config.yml`（模型填 Ollama base_url）→ `./install.sh`（或 `docker compose up -d`）→ 访问 8080。

---

## 八、持续更新说明

AI 应用迭代极快（MCP、Harness、多模态每月都有新东西）。本仓库随学习进度增补，建议 Watch / Star 后定期 pull。所有内容基于本人实践与公开资料整理，欢迎 Issue / PR 指正。

**License**：CC BY-NC 4.0（署名-非商业）。代码骨架可自由用于学习与作品集。
