#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
P1 流式对话机器人（零三方依赖，仅用标准库）。
默认连本地 Ollama（你的 DGX bridge），可通过环境变量切换到 DeepSeek/OpenAI 等。
"""
import os
import sys
import json
import urllib.request

# ===== 配置（用环境变量，绝不硬编码 Key）=====
BASE_URL = os.getenv("LLM_BASE_URL", "http://127.0.0.1:11434/v1")
API_KEY = os.getenv("LLM_API_KEY", "ollama")          # 本地无需真实 key
MODEL = os.getenv("LLM_MODEL", "qwen3:latest")        # 可改 deepseek-r1:32b / qwen3-coder:30b

SYSTEM_PROMPT = "你是一个简洁、专业的中文助手，回答尽量条理清晰。"


def stream_chat(messages):
    """调用模型并流式打印，返回完整回复文本。"""
    url = f"{BASE_URL.rstrip('/')}/chat/completions"
    body = {"model": MODEL, "messages": messages, "stream": True}
    req = urllib.request.Request(
        url,
        data=json.dumps(body).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {API_KEY}",
        },
    )
    full = []
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            for raw in resp:
                line = raw.decode("utf-8").strip()
                if not line.startswith("data:"):
                    continue
                data = line[5:].strip()
                if data == "[DONE]":
                    break
                try:
                    delta = json.loads(data)["choices"][0]["delta"].get("content", "")
                except Exception:
                    continue
                if delta:
                    print(delta, end="", flush=True)
                    full.append(delta)
    except Exception as e:
        print(f"\n[调用失败] {e}", file=sys.stderr)
        return ""
    return "".join(full)


def main():
    print(f"💬 本地模型对话（model={MODEL}），输入 exit 退出\n")
    history = [{"role": "system", "content": SYSTEM_PROMPT}]
    while True:
        try:
            user_input = input("你> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n再见")
            break
        if user_input.lower() in ("exit", "quit"):
            print("再见")
            break
        if not user_input:
            continue
        history.append({"role": "user", "content": user_input})
        print("AI> ", end="", flush=True)
        reply = stream_chat(history)
        print()  # 换行
        if reply:
            history.append({"role": "assistant", "content": reply})


if __name__ == "__main__":
    main()
