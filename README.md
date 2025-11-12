# CIBC Agents Lab (Python + Microsoft Agent Framework + GitHub Models)

This repo contains a **90‑minute, Python‑first lab** for building **AI agents** using the **Microsoft Agent Framework** with **GitHub Models** (OpenAI‑compatible API).  
Supports restricted networks where egress is allowed **only** to the GitHub Models inference endpoint.

---

## What you’ll build
1. **Hello Agent** – a minimal agent, demonstrating instructions and a prompt loop  
2. **Agent + Tools** – a single agent that **invokes Python tools** via function‑calling  
3. **Multi‑Agent Handoff** – a triage agent that **routes** to specialists  
4. **Bonus** – **structured outputs** + creative extension tracks

> We use **GitHub Models** for inference. No Azure AI Foundry is required.  
> If you later adopt Foundry, you can swap the client layer with minimal changes.

---

## ✅ Prerequisites

- **Python 3.10–3.12** and **Git**
- A **GitHub token** with **Models** inference access
- **Egress allow‑list** for: `https://models.inference.ai.azure.com`
- If your org uses a TLS inspecting proxy:
  - Know your proxy URL and **root CA** path (set via env vars)

See **./PRE-LAB-CHECKLIST.md** for a concise checklist to share with participants.

---

## ✅ Setup & Run Instructions

> **Run all commands from the repo root** (where `requirements/` and `labs/` folders exist).

### **Linux / macOS**
```bash
cd /path/to/cibc-agents-lab
python3 -m venv .venv && source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements/requirements_full.txt
pip install "agent-framework==1.0.0b251105" --pre
cp env/.env.sample.github .env && nano .env
python scripts/verify_env.py
python labs/01_hello_agent/01_hello_agent.py