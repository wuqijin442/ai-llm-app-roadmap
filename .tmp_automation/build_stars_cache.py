#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""重建 stars 缓存：git HEAD 旧报告提取 + GitHub API 实测（走代理）"""
import os, sys, json, re, subprocess, urllib.request

BASE = r"E:/ai-llm-app-roadmap"
CACHE = os.path.join(BASE, ".tmp_automation", "stars_cache.json")

REPOS = []
# 从测试脚本 REPOS 列表解析 (full, local)
src = open(os.path.join(BASE, "scripts", "test_cloned_projects.py"), encoding="utf-8").read()
for m in re.finditer(r'\("([\w.-]+/[\w.-]+)",\s*"([\w-]+)",', src):
    REPOS.append((m.group(1), m.group(2)))
print("repos parsed:", len(REPOS))

cache = {}
try:
    cache = json.load(open(CACHE, encoding="utf-8"))
except Exception:
    pass

# 1) git HEAD 旧报告提取
try:
    old = subprocess.run(
        ["git", "-C", BASE, "show", "HEAD:docs/20-克隆企业级项目测试报告.md"],
        capture_output=True).stdout.decode("utf-8")
    cur = None
    for line in old.splitlines():
        m = re.match(r"^###\s+([\w.-]+/[\w.-]+)\s+→", line)
        if m:
            cur = m.group(1)
            continue
        m2 = re.search(r"GitHub：stars=(\d+)，主语言=(\S+)", line)
        if m2 and cur:
            cache[cur] = [int(m2.group(1)), m2.group(2), ""]
            cur = None
    print("extracted from git HEAD:", sum(1 for f, _ in REPOS if f in cache))
except Exception as e:
    print("git show failed:", e)

# 2) API 实测缺失项（走 Clash 代理）
os.environ["HTTPS_PROXY"] = "http://127.0.0.1:7890"
os.environ["HTTP_PROXY"] = "http://127.0.0.1:7890"
need = [f for f, _ in REPOS if f not in cache]
print("need API:", need)
for full in need:
    try:
        req = urllib.request.Request(f"https://api.github.com/repos/{full}",
                                     headers={"User-Agent": "test-harness",
                                              "Accept": "application/vnd.github+json"})
        with urllib.request.urlopen(req, timeout=15) as r:
            d = json.load(r)
        cache[full] = [d.get("stargazers_count"), d.get("language"), d.get("description", "")]
        print("API OK:", full, cache[full][:2])
    except Exception as e:
        print("API FAIL:", full, e)

with open(CACHE, "w", encoding="utf-8") as f:
    json.dump(cache, f, ensure_ascii=False, indent=1)
missing = [f for f, _ in REPOS if f not in cache]
print("cache saved, still missing:", missing)
