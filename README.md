# CIBC Agents Lab (Python + Microsoft Agent Framework + GitHub Models)

This repo contains a **90‑minute, Python‑first lab** for building **AI agents** using the **Microsoft Agent Framework** with **GitHub Models** (OpenAI‑compatible API).  
Supports restricted networks where egress is allowed **only** to the GitHub Models inference endpoint.

---

## What you’ll build
1. **Hello Agent** – a minimal agent demonstrating instructions and a prompt loop  
2. **Agent + Tools** – a single agent that **invokes Python tools** via function‑calling  
3. **Multi‑Agent Handoff** – a triage agent that **routes** to specialists  
4. **Bonus** – **structured outputs** + creative extension tracks

> We use **GitHub Models** for inference. No Azure AI Foundry is required.  
> If you later adopt Foundry, you can swap the client layer with minimal changes.

---

## ✅ Prerequisites

- **Python 3.10–3.12** and **Git**
- A **GitHub token** with **Models** inference access
- **Egress allow‑list** for:  
  `https://models.inference.ai.azure.com`
- If your org uses a TLS-inspecting proxy:
  - Know your proxy URL and **root CA** path (set via env vars)

See **./PRE-LAB-CHECKLIST.md** for a concise checklist to share with participants.

---

## ✅ Setup & Run Instructions

> **Run all commands from the repo root** (where `requirements.txt` and `labs/` folders exist).  
> Avoid installing under OneDrive or `/mnt/c` in WSL—use a non-synced path like `C:\dev\CIBC-Agents-Lab` or `~/work/CIBC-Agents-Lab`.

---

### **Linux / macOS**
```bash
cd /path/to/cibc-agents-lab
rm -rf .venv
python3 -m venv .venv && source .venv/bin/activate

# Install dependencies from single requirements file
pip install --no-cache-dir -r requirements.txt

# Configure environment
cp env/.env.sample.github .env && nano .env

# Verify environment variables
python scripts/verify_env.py

# Run first lab
python labs/01_hello_agent/01_hello_agent.py