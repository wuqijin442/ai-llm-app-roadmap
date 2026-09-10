import json, urllib.request
CANDS = [
    "pydantic/pydantic",
    "astral-sh/uv",
    "microsoft/graphrag",
    "microsoft/semantic-kernel",
    "pydantic/pydantic-ai",
    "run-llama/llama_index",
    "openai/openai-agents-python",
]
def get(fn):
    url = f"https://api.github.com/repos/{fn}"
    try:
        req = urllib.request.Request(url, headers={"User-Agent":"test-harness","Accept":"application/vnd.github+json"})
        with urllib.request.urlopen(req, timeout=15) as r:
            d = json.load(r)
        return d.get("stargazers_count"), d.get("language"), d.get("archived"), (d.get("description") or "")[:90]
    except urllib.error.HTTPError as e:
        return None, None, None, f"HTTP {e.code}"
    except Exception as e:
        return None, None, None, f"ERR {e}"
for c in CANDS:
    s,l,a,desc = get(c)
    print(f"{c:45s} stars={s} lang={l} archived={a} | {desc}")
