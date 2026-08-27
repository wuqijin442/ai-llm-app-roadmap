#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
E2 智能客服 Agent（Harness 化骨架）。
体现：工具层 / 权限审批 / 失败重试 / 日志观测 —— 这正是 2026 拉开差距的"模型外系统设计"。
"""
import os
import json
import urllib.request
import datetime

BASE_URL = os.getenv("LLM_BASE_URL", "http://127.0.0.1:11434/v1")
API_KEY = os.getenv("LLM_API_KEY", "ollama")
MODEL = os.getenv("LLM_MODEL", "qwen3:latest")
LOG_FILE = "cs_agent.log"

SYSTEM = """你是电商客服 Agent。可用工具：
- query_order(order_id)：查订单状态
- refund_policy()：查退款政策
- escalate(reason)：转人工（仅在无法自动处理时调用）
涉及"退款/取消"等敏感动作，先调用 refund_policy 并告知用户，不要擅自执行资金操作。
输出格式：
Thought: ...
Action: 工具名(参数)
或 Final: 给客户的回复
"""


# ===== 业务工具（真实场景接数据库/API）=====
def query_order(order_id: str) -> str:
    # 模拟：真实场景查 DB
    return f"订单 {order_id} 状态：已发货，物流：顺丰 SF123"


def refund_policy() -> str:
    return "7天无理由退款；已发货需拒收后退款。"


def escalate(reason: str) -> str:
    return f"已转人工，原因：{reason}"


TOOLS = {"query_order": query_order, "refund_policy": refund_policy, "escalate": escalate}


# ===== Harness: 带重试 + 审批 + 日志 =====
def call_tool(name, arg, retries=2):
    for i in range(retries + 1):
        try:
            if name == "escalate":  # 敏感动作：模拟人工审批
                print(f"[审批] 即将执行敏感动作 {name}，需人工确认（演示中自动通过）")
            return TOOLS[name](arg)
        except Exception as e:
            if i == retries:
                return f"工具 {name} 执行失败且重试耗尽，转人工"
            print(f"[重试] {name} 第{i+1}次失败：{e}")


def log(event: dict):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps({"ts": datetime.datetime.now().isoformat(), **event}, ensure_ascii=False) + "\n")


def llm(messages):
    url = f"{BASE_URL.rstrip('/')}/chat/completions"
    body = {"model": MODEL, "messages": messages, "stream": False}
    req = urllib.request.Request(url, data=json.dumps(body).encode(),
        headers={"Content-Type": "application/json", "Authorization": f"Bearer {API_KEY}"})
    with urllib.request.urlopen(req, timeout=120) as r:
        return json.loads(r.read().decode())["choices"][0]["message"]["content"]


import re
def run(task):
    messages = [{"role": "system", "content": SYSTEM}, {"role": "user", "content": task}]
    for _ in range(5):
        out = llm(messages)
        log({"intent": task[:30], "model_out": out[:100]})
        if "Final:" in out:
            return out.split("Final:")[-1].strip()
        m = re.search(r"Action:\s*(\w+)\((.*?)\)", out, re.S)
        if not m:
            break
        name, arg = m.group(1).strip(), m.group(2).strip()
        obs = call_tool(name, arg)
        log({"tool": name, "arg": arg, "obs": obs[:80]})
        messages.append({"role": "assistant", "content": out})
        messages.append({"role": "user", "content": f"Observation: {obs}"})
    return "未能自动处理，已转人工"


if __name__ == "__main__":
    task = input("客户> ").strip() or "查一下订单 A123 的状态"
    print("\n=== 客服 Agent ===\n" + run(task))
