#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
P3 简单工具调用 Agent（手写 ReAct 循环，零三方依赖）。
理解：模型不是直接给答案，而是"思考 -> 调工具 -> 看结果 -> 再思考"。
"""
import os
import re
import json
import urllib.request
import datetime

BASE_URL = os.getenv("LLM_BASE_URL", "http://127.0.0.1:11434/v1")
API_KEY = os.getenv("LLM_API_KEY", "ollama")
MODEL = os.getenv("LLM_MODEL", "qwen3:latest")
MAX_TURNS = 5

SYSTEM = """你是一个会调用工具的助手。
当需要计算或查时间时，必须按如下格式输出（一次一个 Action）：
Thought: 你的思考
Action: 工具名(参数)
可用工具：
- calculator(expr)：计算数学表达式，如 calculator(23*47)
- now()：返回当前时间
当你能直接回答时，输出：
Final: 你的最终答案
"""

# ===== 工具注册表 =====
def calculator(expr: str) -> str:
    try:
        return str(eval(expr, {"__builtins__": {}}, {}))
    except Exception as e:
        return f"计算错误: {e}"

def now() -> str:
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

TOOLS = {"calculator": calculator, "now": now}


def llm(messages):
    url = f"{BASE_URL.rstrip('/')}/chat/completions"
    body = {"model": MODEL, "messages": messages, "stream": False}
    req = urllib.request.Request(
        url, data=json.dumps(body).encode(),
        headers={"Content-Type": "application/json", "Authorization": f"Bearer {API_KEY}"},
    )
    with urllib.request.urlopen(req, timeout=120) as r:
        return json.loads(r.read().decode())["choices"][0]["message"]["content"]


def run(task: str):
    messages = [{"role": "system", "content": SYSTEM}, {"role": "user", "content": task}]
    for turn in range(MAX_TURNS):
        out = llm(messages)
        print(f"\n[模型输出 #{turn+1}]\n{out}")
        if "Final:" in out:
            return out.split("Final:")[-1].strip()
        m = re.search(r"Action:\s*(\w+)\((.*?)\)", out, re.S)
        if not m:
            messages.append({"role": "assistant", "content": out})
            messages.append({"role": "user", "content": "请按格式输出 Action 或 Final。"})
            continue
        tool, arg = m.group(1).strip(), m.group(2).strip()
        obs = TOOLS.get(tool, lambda a: f"未知工具: {tool}")(arg)
        print(f"[工具执行] {tool}({arg}) -> {obs}")
        messages.append({"role": "assistant", "content": out})
        messages.append({"role": "user", "content": f"Observation: {obs}"})
    return "（达到最大轮次，未能得出最终答案）"


if __name__ == "__main__":
    task = input("任务> ").strip() or "帮我算 23*47，并告诉我现在几点"
    print("\n=== Agent 结果 ===")
    print(run(task))
