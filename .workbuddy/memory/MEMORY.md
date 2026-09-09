# ai-llm-app-roadmap 项目长期记忆

## 仓库定位

「AI 大模型应用开发转岗学习」仓库。视角：EMS 后端/前端工程师（Java + MyBatis-Plus + Vue）转岗 AI 应用开发。
主线：**Harness（执行与治理层）** + 工程能力杠杆。每日自动化采集岗位 → 克隆对标仓库 → 测试入库。

## 纪律（历史返工教训，不可跳过）

1. **对标仓库只列名字不算完成**，必须真实 clone + 真实测试 + 报告入库（第 2、3 期因漏做被返工）。
2. **README 第 7 节项目总数必须与 docs/20 一致**（docs/20 已 25 个时 README 还写 5 个，文档互相矛盾）。
3. **累积型文档每期必推 ima**：docs/30、docs/20 每期原地追加，只推 daily-digest 会让知识库持续落后
   （08-29/30/31 连漏 3 期，知识库停在 20 岗/11 仓库，本地已 34 岗/27 仓库）。
4. **git push 成功判定必须以退出码为准**，禁止 `git push | tail`（管道退出码恒 0，会把失败误报成功）。
5. **不凭印象猜 GitHub 仓库路径**，先用 API 校验（portainer/llm-gateway、labelbox/labelbox、
   owasp/www-project-llm-top-10 等均不存在）。

## 环境

- GitHub 直连 443 常不可达。push 走 Clash 代理：
  `git -c http.proxy=http://127.0.0.1:7890 -c https.proxy=http://127.0.0.1:7890 push origin main`
  clone 走 `codeload.github.com` tarball fallback（副作用：无 .git 目录）。
- Ollama 本地 127.0.0.1:11434 可用，模型 qwen3.8:27b（主用）/ qwen3-coder:30b / bge-m3（embedding）。
- 托管 Python：`C:/Users/Administrator/.workbuddy/binaries/python/versions/3.13.12/python.exe`
- `/tmp` 在 Windows Git Bash + 托管 Python 下不可靠，用当前目录 `.tmp_automation/`。
- ima 推送必须**串行**（create_media → COS 上传 → add_knowledge 走完一个再下一个），
  并行取凭证会导致第二个 secret_id 与 token 不匹配 → COS 403，且 sleep 重试无效。

## 通用工程原则（本项目沉淀，可跨项目复用）

### LLM 评测/红队：判定器比被测对象更容易写错

用**全文关键词匹配**判定模型是否被攻破，会把「正确拒绝」误判为「已被攻破」——
模型在复述攻击内容以示拒绝时，会原样引用 `exec_sql` / `DROP TABLE` 等危险词。

正确做法：只解析模型**声明的动作行**（如 `ACTION:` 行）来判定，不看全文。
且修判定器时**必须全局搜一遍所有遗留的匹配逻辑**，改一处不够
（p5 项目里这个坑踩了两轮：先修 `llm_was_hijacked()`，用例 6 残留的独立条件又误判一次）。

**评测器的可信度不会高于被测对象。**

### 选型看依赖边界，不看 star 数

B 级 Python 编译通过率不是「代码质量指标」，而是「**依赖隔离度指标**」：
- llama_index 99.97%（160+ 集成包做成 namespace package，核心零外部耦合）→ 适合嵌入现有 Java/Spring
- ragflow 94.21%（失败集中在 agent/、admin/client/，Python 层是 Go 主服务胶水层）→ 适合独立部署

### Agent 安全的投入顺序

实测（qwen3.8:27b）：hardened 与 naive 两组提示词都是 9/9 通过 →
**权限模型 > 输入隔离 > 审计 > 提示词**。别把安全感建立在 system prompt 上。
