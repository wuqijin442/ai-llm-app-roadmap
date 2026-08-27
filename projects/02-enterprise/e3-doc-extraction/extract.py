#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
E3 文档结构化抽取：把文本抽成受约束的 JSON。
关键技巧：系统提示强制 JSON + 字段 schema + 输出后校验。
"""
import os
import json
import urllib.request

BASE_URL = os.getenv("LLM_BASE_URL", "http://127.0.0.1:11434/v1")
API_KEY = os.getenv("LLM_API_KEY", "ollama")
MODEL = os.getenv("LLM_MODEL", "qwen3:latest")

# 期望的字段 schema（真实场景按业务定义）
SCHEMA = {
    "order_id": "字符串，订单号",
    "customer": "字符串，客户名",
    "amount": "数字，金额（元）",
    "date": "字符串，YYYY-MM-DD",
    "items": "数组，商品名列表",
}

SYSTEM = (
    "你是信息抽取引擎。只输出一个 JSON 对象，字段如下：\n"
    + json.dumps(SCHEMA, ensure_ascii=False, indent=2)
    + "\n不要输出任何解释性文字，只输出可被 json.loads 解析的 JSON。"
)


def llm(prompt: str) -> str:
    url = f"{BASE_URL.rstrip('/')}/chat/completions"
    body = {"model": MODEL, "messages": [{"role": "user", "content": prompt}], "stream": False}
    req = urllib.request.Request(url, data=json.dumps(body).encode(),
        headers={"Content-Type": "application/json", "Authorization": f"Bearer {API_KEY}"})
    with urllib.request.urlopen(req, timeout=120) as r:
        return json.loads(r.read().decode())["choices"][0]["message"]["content"]


def extract(text: str, retries=2):
    prompt = f"{SYSTEM}\n\n待抽取文本：\n{text}"
    for i in range(retries + 1):
        try:
            raw = llm(prompt)
            # 容错：截取第一个 { 到最后一个 }
            start, end = raw.find("{"), raw.rfind("}")
            obj = json.loads(raw[start:end + 1])
            # 校验必填字段
            missing = [k for k in SCHEMA if k not in obj]
            if missing:
                raise ValueError(f"缺字段: {missing}")
            return obj
        except Exception as e:
            if i == retries:
                return {"error": str(e), "raw": raw[:200]}
            print(f"[重试] 抽取第{i+1}次失败：{e}")
    return {"error": "未知"}


def main():
    text = ""
    if os.path.exists("sample.txt"):
        text = open("sample.txt", encoding="utf-8").read()
    else:
        text = input("粘贴待抽取文本> ").strip()
    result = extract(text)
    print("\n=== 抽取结果 ===")
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
