# P1 · 流式对话机器人（练手）

> 最小可跑闭环：用 Python 调通大模型 API，实现**流式输出（打字机效果）**多轮对话。
> 默认走你本地的 **Ollama / DGX bridge（127.0.0.1:11434）**，零成本；也可一键切到 DeepSeek / OpenAI 等公有 API。

## 运行
```bash
cd p1-chatbot-cli
# 可选：切换到公有 API
# export LLM_BASE_URL="https://api.deepseek.com/v1"
# export LLM_API_KEY="sk-xxx"
# export LLM_MODEL="deepseek-chat"
python chat.py
```
输入 `exit` 退出。

## 你会学到
- OpenAI 兼容 `/v1/chat/completions` 协议（Ollama 也兼容，省一套代码）。
- SSE 流式解析（`data:` 分块、遇到 `[DONE]` 结束）。
- 多轮对话的 `messages` 历史管理。
- 用环境变量管理 Key（绝不硬编码）。

## 下一步
→ `p4-prompt-lab` 把 Prompt 模板化；→ `p2-rag-docs-qa` 接入你的文档。
