# P2 · RAG 文档问答（练手）

> 把一个文件夹里的文档变成「能问答的知识库」：加载 → 分块 → 向量化 → 检索 → 生成。
> 进阶见企业级 `e1-enterprise-kb`（加混合检索、重排、引用来源）。

## 安装
```bash
pip install langchain langchain-community chromadb sentence-transformers
# 或本地 Ollama 提供 embedding：pip install langchain-ollama
```

## 运行
```bash
cd p2-rag-docs-qa
mkdir -p data && cp 你的文档.pdf data/   # 放几篇 Markdown/PDF
python rag.py
```

## 你会学到
- 文档加载（TextLoader / PyPDFLoader）、递归字符分块。
- Embedding 向量化 + Chroma 向量库入库与检索。
- Naive RAG 链路：检索 top-k → 拼 Prompt → 生成。
- 切换本地 embedding（bge/m3e）与本地 LLM（Ollama），零 API 成本。

## 调优方向（过渡到 e1）
- 混合检索（向量 + BM25）、Cross-Encoder 重排、上下文压缩、多轮记忆。
- 展示引用来源，让用户可信任、可审计。
