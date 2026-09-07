# 04 · RAG 检索增强生成（企业落地第一刚需）

> RAG = Retrieval-Augmented Generation。用「私有/实时知识」增强模型，压制幻觉、解决知识滞后。

## 1. Naive RAG 全链路

```
用户提问
  → 文档加载(Loader: PDF/Word/MD/网页)
  → 清洗 + 分块(Splitter)
  → 向量化(Embedding)
  → 存入向量库(VectorStore)
  → query 向量化 → 相似度检索(Retriever, top-k)
  → 拼接 Prompt（上下文 + 问题）
  → LLM 生成 → 返回（带引用来源）
```

## 2. 关键环节深挖

### 文档分块策略
- **固定长度**：递归字符分割（按 `\n\n`、`.` 递归切），最简单。
- **语义分块**：按语义边界切，保留段落完整性。
- **层级分块**：父子块（大块检索、小块喂给模型）。
- 经验：块大小 300–800 token，重叠 10–20% 防截断。

### Embedding 模型选型（中文）
- `BGE`（智源，效果强）、`m3e`、OpenAI `text-embedding-3`、阿里 `text-embedding-v3`。
- 本地练习用 `BAAI/bge-small-zh` 或 `moka-ai/m3e-base`。

### 向量数据库
| 库 | 定位 | 适用 |
|---|---|---|
| FAISS | 本地内存，极致轻量 | 测试 / 小数据 |
| Chroma | 轻量易用 | 快速原型 |
| Milvus | 生产首选，分布式 | 企业级大库 |
| PGVector | Postgres 向量扩展 | 后端友好，复用现有 DB |

### 检索优化（2026 必学）
- **混合检索**：向量（语义）+ 关键词（BM25）融合，召回更全。
- **重排序（Rerank）**：用 Cross-Encoder 对 top-k 二次精排，准确率显著提升。
- **上下文压缩**：只保留相关片段，省 token、降噪声。
- **多轮记忆**：会话历史向量化，支持追问。
- **幻觉检测**：比对生成内容与检索片段，标记无依据陈述。

## 2b. 记忆层五层栈 + 晋升门控（2026 新增，RAG 之上「Agent 记忆」）

> 来源：W36 周报 P1 修订 + 第 8 期 Context/Memory Engineer 条目（zylos.ai 2026 / jacoblangvadnilsson.com 2026 / app-lab.ai）。

- **五层记忆栈**（各配不同存储 + 检索经济学）：
  1. **Working Memory**（Redis 毫秒级）：当前对话上下文
  2. **Short-term Memory**（TTL）：会话历史
  3. **Long-term Memory**（Postgres）：用户/租户长期事实
  4. **Semantic Memory**（向量 + BM25 + rerank <200ms）：语义知识
  5. **Episodic Memory**（ClickHouse <500ms）：事件时序
- **检索经济学**（关键数据）：
  - 全量上下文：72.9% 准确 / 17s / 26K token
  - 选择性检索：**91% 延迟降 + 90% token 省**
  - 子 Agent 隔离：成功率 +90.2%
- **记忆晋升门控**（最高危操作）：
  - session → user → tenant → global 分级
  - 防 guardrail drift + precedent poisoning（记忆投毒）
  - OWASP ASI06（记忆投毒防御）
- **Truth vs Memory 分离**：事实（Truth）与记忆（Memory）分开存储，防污染。
- **对标**：`mem0ai/mem0`（64.7k★，记忆层品类第一）、`qdrant/qdrant`（34.3k★）、`pgvector/pgvector`（22.8k★）（均已克隆）。
- **岗位映射**：Context Engineering / AI Memory Engineer（US $140K–$220K）。

## 3. 企业级知识库（目标项目）
→ `projects/02-enterprise/e1-enterprise-kb`：支持 PDF/Word 上传、智能问答、**引用来源高亮**、多轮对话、混合检索 + 重排，准确率目标 90%+。

## 4. 常见坑
- 块太大→检索不精准；块太小→上下文断裂。
- 只向量不重排→top-k 噪声多。
- 不展示来源→用户无法信任、无法审计。
- 不做评测集→「感觉变好了」不可证伪。
