#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
P2 Naive RAG 文档问答（LangChain + Chroma）。
演示：加载文档 -> 分块 -> 向量化 -> 检索 -> 拼 Prompt -> 生成。
"""
import os
from langchain_community.document_loaders import TextLoader, PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# 本地优先：用 Ollama 提供 embedding 与 LLM（零 API 成本）
from langchain_ollama import OllamaEmbeddings, ChatOllama

EMBED_MODEL = os.getenv("EMBED_MODEL", "bge-m3")          # 或 nomic-embed-text
LLM_MODEL = os.getenv("LLM_MODEL", "qwen3:latest")
DATA_DIR = "data"

PROMPT = ChatPromptTemplate.from_messages([
    ("system", "你只能根据下面的「参考上下文」回答问题，不知道就说不知道，不要编造。"),
    ("human", "参考上下文：\n{context}\n\n问题：{question}"),
])


def load_docs():
    docs = []
    for name in os.listdir(DATA_DIR):
        path = os.path.join(DATA_DIR, name)
        if name.lower().endswith(".pdf"):
            docs += PyPDFLoader(path).load()
        elif name.lower().endswith((".md", ".txt")):
            docs += TextLoader(path, encoding="utf-8").load()
    return docs


def build_chain():
    raw = load_docs()
    splits = RecursiveCharacterTextSplitter(
        chunk_size=500, chunk_overlap=80
    ).split_documents(raw)
    vectordb = Chroma.from_documents(
        splits, OllamaEmbeddings(model=EMBED_MODEL),
        persist_directory="./chroma_db",
    )
    retriever = vectordb.as_retriever(search_kwargs={"k": 4})
    llm = ChatOllama(model=LLM_MODEL, base_url="http://127.0.0.1:11434")
    chain = (
        {"context": retriever, "question": lambda x: x["question"]}
        | PROMPT
        | llm
        | StrOutputParser()
    )
    return chain, retriever


def main():
    chain, retriever = build_chain()
    print("📚 RAG 问答已就绪，输入问题（exit 退出）")
    while True:
        q = input("\n问题> ").strip()
        if q.lower() in ("exit", "quit"):
            break
        if not q:
            continue
        answer = chain.invoke({"question": q})
        print("\n回答>", answer)
        # 展示检索到的来源片段（便于过渡到 e1 的"引用高亮"）
        print("\n— 检索来源 —")
        for i, d in enumerate(retriever.invoke(q), 1):
            print(f"[{i}] {d.page_content[:120]}...")


if __name__ == "__main__":
    main()
