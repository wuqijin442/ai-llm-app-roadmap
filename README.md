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
│   │   └── p4-prompt-lab/         #   Prompt 实验台
│   └── 02-enterprise/             # 企业级实战（贴近业务）
│       ├── e1-enterprise-kb/      #   企业知识库
│       ├── e2-smart-customer-service/  # 智能客服
│       └── e3-doc-extraction/     #   文档结构化抽取
├── roadmap/                       # 阶段规划（打卡用）
│   ├── 30天-入门冲刺.md
│   ├── 90天-核心突破.md
│   └── 180天-转岗实战.md
├── cloned_projects/               # 克隆的企业级实战项目（gitignore，不入库）
│   ├── ai-agents-for-beginners/   #   微软官方 Agent 教程（73.3k★）
│   ├── ruoyi-ai/                  #   Java 企业级 AI 框架（5.7k★）
│   ├── Langchain-Chatchat/        #   Python 本地知识库 RAG（38.6k★）
│   ├── FastGPT/                   #   Docker 企业级 RAG/Agent 平台（29.5k★）
│   └── MaxKB/                     #   Docker 企业级知识库（22.6k★）
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

为把「看教程」升级成「读真源码、跑真项目」，本仓库从 GitHub 高星仓库克隆了 **25 个**覆盖 Agent / RAG / 知识库 / 多 Agent 编排 / 微调 / 部署 / 安全 / MCP / 向量库 / 评测 / 可观测 / 治理 / 具身智能的实战项目，放入 `cloned_projects/`，并编写 `scripts/test_cloned_projects.py` 做**可复现的本地全量测试**。

> 每日任务按「岗位 → 对标仓库」逐期追加：第 1 期 5 个（2026-08-27）+ 第 2 期 11 个（2026-08-28）+ 第 3 期 9 个（2026-08-29）= **累计 25 个**。
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
