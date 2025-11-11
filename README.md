# CIBC Agents Lab (Python + Microsoft Agent Framework + GitHub Models)

This repo contains a **90‑minute, Python‑first lab** for building **AI agents** using the **Microsoft Agent Framework** with **GitHub Models** (OpenAI‑compatible API). It supports a restricted network posture where egress is allowed **only** to the GitHub Models inference endpoint.

## What you’ll build
1. **Hello Agent** – a minimal agent, demonstrating instructions and a prompt loop  
2. **Agent + Tools** – a single agent that **invokes Python tools** via function‑calling  
3. **Multi‑Agent Handoff** – a triage agent that **routes** to specialists  
4. **Bonus** – **structured outputs** + creative extension tracks

> We use **GitHub Models** for inference. No Azure AI Foundry is required.  
> If you later adopt Foundry, you can swap the client layer with minimal changes.

---

## Prerequisites

- **Python 3.10–3.12** and **Git**
- A **GitHub token** with **Models** inference access (enterprise policy permitting)
- **Egress allow‑list** for: `https://models.inference.ai.azure.com`
- If your org uses a TLS inspecting proxy:
  - Know your proxy URL and **root CA** path (set via env vars)

See **./PRE-LAB-CHECKLIST.md** for a concise checklist to share with participants.

---

## Install & run

> You can use any workflow you like (pip, uv, conda). Shown below: standard `pip`+venv.

1) Create a virtual environment
```bash
python -m venv .venv
# macOS/Linux:
source .venv/bin/activate
# Windows (PowerShell):
# .\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
