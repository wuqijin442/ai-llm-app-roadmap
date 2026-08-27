#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
P4 Prompt 实验台：加载模板 -> 调模型 -> 打分对比 -> 导出最佳。
零三方依赖，使用本地 Ollama（可切公有 API）。
"""
import os
import json
import urllib.request

BASE_URL = os.getenv("LLM_BASE_URL", "http://127.0.0.1:11434/v1")
API_KEY = os.getenv("LLM_API_KEY", "ollama")
MODEL = os.getenv("LLM_MODEL", "qwen3:latest")

# 内置模板：{question} 为占位符
TEMPLATES = {
    "客服友好版": "你是耐心友好的客服，用通俗语言回答用户问题：{question}",
    "专业精简版": "你是资深工程师，只给要点，不超过3条：{question}",
    "结构化版": "请严格按 JSON 输出 {\"answer\": \"\", \"confidence\": 0-1}：{question}",
}

QUESTION = "储能系统一天充放电两次，怎么向客户解释收益？"


def llm(prompt: str) -> str:
    url = f"{BASE_URL.rstrip('/')}/chat/completions"
    body = {"model": MODEL, "messages": [{"role": "user", "content": prompt}], "stream": False}
    req = urllib.request.Request(
        url, data=json.dumps(body).encode(),
        headers={"Content-Type": "application/json", "Authorization": f"Bearer {API_KEY}"},
    )
    with urllib.request.urlopen(req, timeout=120) as r:
        return json.loads(r.read().decode())["choices"][0]["message"]["content"]


def score(out: str) -> int:
    # 简单 rubric：长度适中(20-300字) + 含"收益"关键词 给高分
    s = 0
    if 20 <= len(out) <= 300:
        s += 3
    if "收益" in out:
        s += 2
    return s


def main():
    results = {}
    for name, tpl in TEMPLATES.items():
        out = llm(tpl.format(question=QUESTION))
        sc = score(out)
        results[name] = {"output": out, "score": sc}
        print(f"\n=== {name} (评分 {sc}) ===\n{out}")
    best = max(results, key=lambda k: results[k]["score"])
    print(f"\n🏆 最佳模板：{best}（评分 {results[best]['score']}）")
    with open("best_prompt.json", "w", encoding="utf-8") as f:
        json.dump({"best": best, "template": TEMPLATES[best]}, f, ensure_ascii=False, indent=2)
    print("已导出 best_prompt.json")


if __name__ == "__main__":
    main()
