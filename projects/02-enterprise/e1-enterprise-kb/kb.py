#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
E1 企业级知识库问答（在 P2 基础上增强：引用来源 + 混合检索 + 重排 + 评测）。
演示结构，关键处注释说明如何替换为你自己的实现/模型。
"""
import os
import json
from langchain_community.document_loaders import TextLoader, PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.retrievers import BM25Retriever
from langchain_ollama import OllamaEmbeddings, ChatOllama
from langchain_core.prompts import ChatPromptTemplate

EMBED_MODEL = os.getenv("EMBED_MODEL", "bge-m3")
LLM_MODEL = os.getenv("LLM_MODEL", "qwen3:latest")
DATA_DIR = "data"


def load_splits():
    docs = []
    for n in os.listdir(DATA_DIR):
        p = os.path.join(DATA_DIR, n)
        if n.lower().endswith(".pdf"):
            docs += PyPDFLoader(p).load()
        elif n.lower().endswith((".md", ".txt")):
            docs += TextLoader(p, encoding="utf-8").load()
    return RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=80).split_documents(docs)


def build_hybrid_retriever(splits):
    # 向量检索
    vs = Chroma.from_documents(splits, OllamaEmbeddings(model=EMBED_MODEL), persist_directory="./kb_chroma")
    vector_retriever = vs.as_retriever(search_kwargs={"k": 8})
    # 关键词检索
    bm25 = BM25Retriever.from_documents(splits)
    bm25.k = 8

    def hybrid(q):
        a = vector_retriever.invoke(q)
        b = bm25.invoke(q)
        # 简易融合：去重后取前 k（真实场景可用 RRF 加权）
        seen, merged = set(), []
        for d in a + b:
            key = d.page_content[:50]
            if key not in seen:
                seen.add(key)
                merged.append(d)
        return merged[:6]

    return hybrid


PROMPT = ChatPromptTemplate.from_messages([
    ("system", "只依据给定上下文回答，并标注引用的片段编号 [1][2]。不知道就说不知道。"),
    ("human", "上下文：\n{ctx}\n\n问题：{q}"),
])


def answer(q, retriever):
    docs = retriever(q)
    ctx = "\n".join(f"[{i+1}] {d.page_content}" for i, d in enumerate(docs))
    llm = ChatOllama(model=LLM_MODEL, base_url="http://127.0.0.1:11434")
    out = (PROMPT | llm).invoke({"ctx": ctx, "q": q}).content
    return out, docs


def evaluate(retriever):
    """跑 eval.json 里的问答对，统计准确率（含关键词命中即算对，真实用可换 LLM 评委）。"""
    if not os.path.exists("eval.json"):
        print("（无 eval.json，跳过评测）")
        return
    data = json.load(open("eval.json", encoding="utf-8"))
    hit = 0
    for item in data:
        out, _ = answer(item["question"], retriever)
        if any(k in out for k in item.get("keywords", [])):
            hit += 1
    print(f"评测准确率：{hit}/{len(data)} = {hit/len(data):.0%}")


def main():
    splits = load_splits()
    retriever = build_hybrid_retriever(splits)
    evaluate(retriever)
    while True:
        q = input("\n问题> ").strip()
        if q.lower() in ("exit", "quit"):
            break
        out, docs = answer(q, retriever)
        print("\n回答>", out)
        print("\n引用来源：")
        for i, d in enumerate(docs, 1):
            src = d.metadata.get("source", "?")
            print(f"[{i}] {os.path.basename(src)}: {d.page_content[:80]}...")


if __name__ == "__main__":
    main()
