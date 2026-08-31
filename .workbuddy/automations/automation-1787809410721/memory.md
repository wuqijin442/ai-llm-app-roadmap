# 自动化任务执行记忆（automation-1787809410721）

> 任务：AI 大模型应用开发转岗 · 每日岗位学习 digest + 双通道同步（GitHub + ima 知识库 7498617266899781）

## 执行历史（倒序）

### 2026-08-31（周一，W36）· 补推 ima 过期累积文档
- 触发：老大指令「推」，新会话 ima-mcp 已生效（上一轮写入 `~/.workbuddy/mcp.json` 后重启会话生效）
- 先查 `get_knowledge_list`：已推 6 份全部最新（W35 三期 digest + W35 周报 + W36 第 4 期 digest），**但两份累积型文档停在 08-28**：
  - `W35-岗位全景与学习路径索引.md` 13758 B（20 岗）vs 本地 28322 B（34 岗/4 期）
  - `W35-克隆企业级项目测试报告.md` 11000 B（11 仓）vs 本地 17406 B（27 仓）
- 根因：自动化任务只规定「daily-digest 按 ISO 周推」，**未规定累积型文档何时重推** → 08-29/30/31 三期连续漏推
- 补推 2 份（W36 前缀，三步流程，全部 media_state=2 / parse_progress=100）：
  - `W36-岗位全景与学习路径索引.md`（28322 B）
  - `W36-克隆企业级项目测试报告.md`（17406 B）
  - 知识库条目 29 → 31
- 踩坑：**create_media 不可并行** —— 并行取两份凭证，第 2 份 COS 上传 403 `InvalidAccessKeyId`；sleep 8s 重试仍 403（排除同步延迟）；改串行重取凭证后 HTTP 200 成功
- 流程固化（已写入自动化任务 prompt B.1b / B.3 / B.5 / B.7）：
  1. 累积型文档（docs/30 + docs/20）每期必推，推送前用 file_size 比对判断是否过期
  2. 多文件推送必须串行，不可并行 create_media
  3. 403 报错不要 sleep 等待，直接串行重取
  4. ima MCP 无删除接口，旧周前缀版本残留须提示用户手动清理
- 遗留：知识库中 `W35-岗位全景与学习路径索引.md`、`W35-克隆企业级项目测试报告.md` 两份 08-28 旧版需人工删除

### 2026-08-31（周一，W36）· 第 4 期 · AI 应用落地最后一公里（自动化任务本体执行）
- 主线：教育 + 可靠性 + GTM（补前三期轻描淡写的三块拼图）
- 岗位 6 个：AI Reliability、AI GTM、AI Educator 深化、LLM Observability、AI Workflow Automation、AI Learning PM
- 对标仓库 2 个：langfuse/langfuse（33940★/5 .py）、n8n-io/n8n（202889★/69 .py，本仓库历史最高星，超 vllm 90.4k）
- 两仓库各克隆失败 1 次（网络抖动）→ 重试成功；测试全量重跑 27 仓库 33m49s exit 0
- GitHub commit 99995f6（6 文件 349 插入）push 成功；ima 推 W36-daily-digest-2026-08-31.md（31060 B）成功
- 累计：34 岗位 / 4 期 / 27 仓库

### 2026-08-30（周日，W35）· 周报汇总（自动化任务本体执行）
- 产出 `weekly/2026-W35-周报.md`（17586 B）：28 岗 / 25 仓 / 99.92% 编译通过 / 5 大趋势 / 7 项 docs 缺口 / 3 个 P1 修订建议
- GitHub commit f565c80 push 成功（94cd8f2..f565c80）
- ima 推 4 份（W35 前缀）：三期 digest + W35 周报，全部 media_state=2 / parse_progress=100

### 2026-08-29（周六，W35）· 第 3 期 · 生产链路落地（保/测/架/管）
- 产出：`daily-digest/2026-08-29.md`（8 岗位，与第 1/2 期 20 岗不重叠）+ `docs/30-岗位全景与学习路径索引.md` 追加第 3 期 8 条目（累计 28 岗/3 期）+ `logs/automation-2026-08-29.log`
- 主线：「保（AgentOps）+ 测（AI QA）+ 架（基础设施/平台）+ 管（治理/红队）」——Agentic 系统从 Demo 走向生产后的四个岗位簇
- 岗位：具身智能/多模态算法(3/5)、AI 测试/质量(5/5)、AgentOps(5/5)、AI Governance 深化(4/5)、Agent/RAG 基础设施(5/5)、AI 数据工程(4/5)、AI 平台(5/5)、AI 安全红队(4/5)
- 新增观察：AI 智能体开发 +244%（智联/CSDN）、需供比 2.62:1、具身智能多模态算法 60-150W / 具身智能最高 200W / VLA 80-120W、AI 训练师 +2250%、AgentOps base $168K-$220K（The Hartford）/ +280% YoY（LinkedIn）、AI Governance 中位 $158,750（Axial）、RAG Infra $170K-$240K / Agent Infra $180K-$275K、AI Safety $287.5K 最高（AI Market Pulse）
- 合规侧时间窗：EU AI Act Article 50 透明度 2026-08-02 生效；高风险义务经 Digital Omnibus（2026-07-08）延迟至 2027-12
- GitHub：commit 9a2a19b [2026-08-29] 每日AI岗位学习内容获取（4 文件，281 插入）→ push **失败**（exit 128 网络不可达）→ **09:00 补推成功**（39aeada..9a2a19b，exit 0）
- **补做对标仓库（老大指令「企业级项目没有看到」）**：第 3 期 8 岗位需 clone+test+报告入库，原定 12 仓库
  - 成功 9 个：openvla(6912★/97.py) / ragas(15524★/387.py) / qdrant(34250★/225.py) / pgvector(22805★/C) / opentelemetry-python(2603★/750.py) / datasets(21874★/237.py) / huggingface-hub(3852★/286.py) / responsible-ai-toolbox(1826★/288.py) / weaviate(16759★/54.py)
  - 失败 3 个（仓库路径不存在，非网络）：portainer/llm-gateway、labelbox/labelbox（正确名 labelbox-python-sdk 亦失败）、owasp/www-project-llm-top-10
  - 网络抖动 4 个（openvla/ragas/qdrant/huggingface-hub）→ 重试后成功
  - 测试：scripts/test_cloned_projects.py 跑 25 仓库全量，43m32s，exit 0 → docs/20 重写 15643 B；第 3 期 .py 全量编译通过 2259/2259
  - 更新：daily-digest/2026-08-29.md 加「三·补」小节、scripts/test_cloned_projects.py 追加 9 仓库、docs/30 累计统计加「对标仓库 25」
  - GitHub：commit 75f65c6 [2026-08-29] 补做第3期对标仓库 clone+test（9仓库/25累计），6 文件 166 插入 → push 成功（9a2a19b..75f65c6，exit 0）✓
- ima 推送：**两次均未执行**（凭证缺失：~/.config/ima/ 不存在 + 无 IMA_CLIENT_ID/IMA_API_KEY 环境变量 + 无 ima MCP 工具——ToolSearch 确认 mcp__ima-mcp__* 不存在），待配置 ima 凭证后补推 W35-daily-digest-2026-08-29.md + W35-岗位全景与学习路径索引.md
- 数据源（新增）：CSDN 163335325/163919604、toutiao 7647847862449062400、tencent 2685549、qaskills.sh、aliyun 1752547、aicoding.csdn.net、joinnextdev.com、notify.careers、agenticcareers.co、danilchenko.dev、themoneyzoo.com、aitechconnect.in、orbit.reconn.io、cogitodaily.com、f5hiringsolutions.com、llmhire.com、theaimarketpulse.com、aitrendshub.net、crmcurator.com、artificialintelligencemax、practical-devsecops、securitycareers.help、ogwilliam.com
- ISO 周：W35（2026-08-24 ~ 08-30）
- 教训：GitHub push 网络抖动 exit 128 为已知问题（2026-08-28 曾出现，重试成功）；本次连续两次失败判为网络不可达，未继续重试；ima 凭证需在 ~/.config/ima/ 配置 client_id + api_key（来源 https://ima.qq.com/agent-interface）

### 2026-08-28（周五，W35）· 第 2 期 · 补做对标仓库 clone+test
- 老大指出第 2 期漏走仓库既有纪律（对标仓库必须 clone + test + 报告入库）
- 补做 11 个对标仓库：langgraph / crewAI / autogen / peft / vllm / NeMo-Guardrails / rebuff / llm-guard / mcp-servers / mcp-typescript-sdk / mcp-python-sdk
- 全部 `git clone --depth 1` 到 `cloned_projects/`（gitignore，不入库）
- 跑 `scripts/test_cloned_projects.py`（41m59s，Python 3.13.12 托管）
- 测试结论：9401 个 .py 编译通过 9393（crewAI CLI 模板占位符 8 个失败，预期）→ 有效通过率 99.92%
- 关键发现：vllm 90250★ 是本期最高星仓库（4324 个 .py 全量编译通过）；MCP 三件套（servers 89915★ / typescript-sdk 13262★ / python-sdk 24138★）全部克隆并验证
- 更新文件：`daily-digest/2026-08-28.md`（21496 → 24971 B，加「三·补、对标开源仓库 · 本地 clone + 测试」小节）+ `docs/20-克隆企业级项目测试报告.md`（重写，16 仓库全量明细）+ `scripts/test_cloned_projects.py`（REPOS 追加 11 仓库）+ `logs/automation-2026-08-28.log`
- GitHub：commit 39aeada [2026-08-28] 补做对标仓库 clone+test → push origin main 退出码 0 ✓（首次网络抖动 128，重试成功）
- ima（REPLACE 策略）：W35-daily-digest-2026-08-28.md（24971 B，media_state=2 parse_progress=100）+ W35-克隆企业级项目测试报告.md（11000 B，media_state=1 parse_progress=75 解析中）+ W35-岗位全景与学习路径索引.md（13758 B，media_state=2 parse_progress=100）
- 教训：每日任务必须把「对标仓库 clone + test + 报告」纳入产出闭环，不能只列仓库不测试

### 2026-08-28（周五，W35）· 第 2 期
- 产出：`daily-digest/2026-08-28.md`（21496 B）+ `docs/30-岗位全景与学习路径索引.md` 追加第 2 期 10 条目（13758 B，累计 20 岗）
- 主线：「Agentic 时代角色分化 + 中国应用层爆发」（与第 1 期「岗位市场全景」互补，不重叠）
- 岗位：Agentic AI Architect(5/5)、LLM Fine-tuning(4/5)、AI Security(4/5)、MCP Auditor(4/5)、AI Integration(5/5)、AI Ops(4/5)、AI BA(4/5)、CAIO(2/5)、LLMOps(5/5)、RAG Engineer(5/5)
- 新增观察：Agentic 岗位 +280%（90K 量级，US）vs 传统 developer -27.5%（Stanford AI Index 2026）；CAIO 采用率 11%→26%→76%（3 年，IBM CEO Study 2026）；MCP 安全岗位「供给近零」（$130K-$175K）；AI 安全工程师 $152K-$210K（OpenClaw Claw Hub 供应链攻击 230+ 恶意扩展案例）
- 关键分化信号：「AI Engineer」标签下实际是 5 个不同 reqs（Applied / ML / MLOps / Prompt / Applied AI），增速各不相同
- GitHub：commit 1701510 [2026-08-28] 每日AI岗位学习内容获取 → push origin main 退出码 0 ✓
- ima（REPLACE 策略）：W35-daily-digest-2026-08-28.md（21496 B，media_state=2 parse_progress=100）+ W35-岗位全景与学习路径索引.md（13758 B，media_state=1 parse_progress=74 解析中）
- 数据源（新增）：frontiernews.ai / whatsthebigdata / artificialintelligencemax.com / practical-devsecops.com / securitycareers.help / blog.ogwilliam.com / agenticcareers.co / iternal.ai / techjacksolutions / futureproofing.dev / shawnkanungo / usaii.org / CSDN 163919604 / aitrendshub.net / crmcurator.com / jobzonerisk.com / daily.dev/recruiter / llmhire.com / signalhire.com
- ISO 周：W35（2026-08-24 ~ 08-30）

### 2026-08-27（周四，W35）· 第 1 期 · 重跑（去储能版）
- 产出：`daily-digest/2026-08-27.md`（19.3 KB，重写）+ `docs/30-岗位全景与学习路径索引.md`（7.7 KB，重写）
- 岗位：AI Agent Dev(5/5)、LLM App Dev(5/5)、FDE(5/5)、AI PM(4/5)、Prompt Eng(4/5)、MLOps(4/5)、AI Architect(4/5)、AI Trainer(3/5)、AI Safety(3/5)、AI Educator(2/5，补充)
- 新增观察：PwC 56% 技能溢价、AI Agent +244%（CSDN）、Prompt hype trap（需求 -19% YoY）、MLOps +27% YoY、H2 新兴岗（Eval/Reliability/GTM/Junior 压缩）
- 关键变更：用户指令「自动化任务不应带储能视角」→ 已删除任务指令中「储能×AI 行业切入点」；digest/索引全部去储能；行业视角由仓库 README 与 docs/00 承载
- GitHub：commit bf59916 [2026-08-27] 每日AI岗位学习内容获取（去储能重跑版）→ push origin main 退出码 0
- ima（REPLACE 策略覆盖旧版）：W35-daily-digest-2026-08-27.md（19297 B，media_state=2 parse_progress=100）+ W35-岗位全景与学习路径索引.md（7720 B，media_state=1 parse_progress=75 解析中）
- 数据源（新增）：bitsfrombytes（PwC 56%）/ CSDN 163919604（Agent +244%）/ mlai.work（Prompt hype trap）/ bilgisam（MLOps +27%）/ careerindia（AI Gov +45%）/ theaimarketpulse（H2 新兴岗）/ trendflash / k12.careers / stanmoreuk（AI Educator）/ masaischool / dev.to / supercareer / techweek
- ISO 周：W35（2026-08-24 ~ 08-30）

### 2026-08-27（周四，W35）· 第 1 期 · 初版（含储能，已被重跑覆盖）
- 产出：`daily-digest/2026-08-27.md`（15.7 KB）+ `docs/30-岗位全景与学习路径索引.md`（6.9 KB）
- 岗位：9 岗（AI Agent Dev、LLM App Dev、FDE、AI PM、Prompt Eng、MLOps、AI Architect、AI Trainer、AI Safety）
- 储能×AI 作品集方向 5 个（电价知识库 RAG / 设备运维 Agent / 能耗预测 / 碳资产 / 算电协同）
- GitHub：commit ae5cd93 [2026-08-27] 每日AI岗位学习内容获取 → push origin main 退出码 0
- ima：W35-daily-digest-2026-08-27.md + W35-岗位全景与学习路径索引.md，均 media_state=2 parse_progress=100
- 数据源：LLMHire / aibusiness.vc / jobply.ai / signalhire / yochana / neuronhire / getperspective / aitalentreport / agenticcareers / aireplacedmyjob / jobdescription / gsdcouncil / hirevane / wjpps / toutiao
- ISO 周：W35（2026-08-24 ~ 08-30）

## 维护规则
1. 每日任务（周一至周六）追加 1 期（daily-digest/YYYY-MM-DD.md + 索引条目）
2. 周日任务汇总进 `weekly/YYYY-Www-周报.md`，并对过时条目标 `~已修订~`
3. 双通道同步必做：GitHub push（退出码判定）+ ima 知识库 W{ww}- 前缀推送
4. 所有数据必须附来源 URL；未验证数据标「来源：未交叉验证」
5. 禁止 emoji 作图标；禁止删除既有条目，只可追加/修订
6. ima 推送 3 步：create_media → COS 上传（Windows 路径 E:/...）→ add_knowledge REPLACE
7. 自动化记忆文件只记摘要，不放全文
