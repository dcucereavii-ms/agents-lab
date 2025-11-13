# Agents Lab (Python + Microsoft Agent Framework + GitHub Models)

This repo contains a **90-minute, Python-first lab** for building **AI agents** using the **Microsoft Agent Framework** with **GitHub Models** (OpenAI-compatible API).  
Designed for restricted networks where egress is allowed **only** to the GitHub Models inference endpoint.

---

## ✅ What You’ll Build
1. **Lab 01 – Hello Agent:** Minimal agent with instructions and a prompt loop  
2. **Lab 02 – Agent + Tools:** Single agent that invokes Python tools via function calling  
3. **Lab 03 – Multi-Agent Handoff:** Triage agent that routes to specialists  
4. **Bonus – Structured Outputs:** Return validated JSON using `pydantic`

> We use **GitHub Models** for inference. **No Azure AI Foundry required.**  
> If you later adopt Foundry, you can swap the client layer with minimal changes.

---

## ✅ Prerequisites
- **Python 3.10 – 3.12** and **Git**
- A **GitHub token** with **Models inference** access
- **Egress allow-list** for:  
  `https://models.inference.ai.azure.com`
- If your org uses a TLS-inspecting proxy, have your **proxy URL** and **root CA path** ready

---

## ✅ Environment Variables

Create a `.env` in the repo root (you can start from `env/.env.sample.github`).

| Variable | Required | Example / Notes |
|---|---|---|
| `OPENAI_API_KEY` | ✅ | Your **GitHub token** (used as the OpenAI key) |
| `OPENAI_BASE_URL` | ✅ | `https://models.inference.ai.azure.com` |
| `MODEL` | ➖ | e.g., `gpt-4o-mini` (or another GitHub Models name used in the labs) |
| `HTTPS_PROXY` / `HTTP_PROXY` | ➖ | e.g., `http://user:pass@proxy.company:8080` |
| `REQUESTS_CA_BUNDLE` or `SSL_CERT_FILE` | ➖ | Path to org root CA (for TLS-inspection) |

> The labs and helper scripts read from `.env`—no code edits needed.

---

## ✅ Environment Setup

> **Run all commands from the repo root** (where `requirements.txt` and `labs/` live).  
> Avoid installing under OneDrive or `/mnt/c` in WSL—use a non-synced path like `C:\dev\Agents-Lab` or `~/work/Agents-Lab`.

### Linux / macOS

```bash
# Navigate to repo root
cd /path/to/Agents-Lab

# Fresh virtual environment
rm -rf .venv
python3 -m venv .venv
source .venv/bin/activate

# Upgrade pip and install deps
python -m pip install --upgrade pip
pip install --no-cache-dir -r requirements.txt

# Configure environment
cp env/.env.sample.github .env
${EDITOR:-nano} .env

# Verify environment variables and network access
python scripts/verify_env.py

# Run labs
python labs/01_hello_agent/01_hello_agent.py
python labs/02_tools_single_agent/02_agent_with_tool.py
python labs/03_multiagent_handoff/03_multi_agent_handoff.py
python labs/99_bonus_paths/99a_structured_outputs.py
```

### Windows (PowerShell)

```powershell
# Navigate to repo root
cd "C:\path\to\Agents-Lab"

# Fresh virtual environment
Remove-Item -Recurse -Force .venv -ErrorAction SilentlyContinue
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# (If activation is blocked) Temporarily relax policy for this session:
# Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

# Upgrade pip and install deps
python -m pip install --upgrade pip
pip install --no-cache-dir -r requirements.txt

# Configure environment
Copy-Item env\.env.sample.github .env
notepad .env

# Verify environment variables and network access
python scripts\verify_env.py

# Run labs
python labs\01_hello_agent\01_hello_agent.py
python labs\02_tools_single_agent\02_agent_with_tool.py
python labs\03_multiagent_handoff\03_multi_agent_handoff.py
python labs\99_bonus_paths\99a_structured_outputs.py
```

---

## 🤪 Troubleshooting

- **401/403**: Ensure your GitHub token has **Models inference** permissions and is placed in `OPENAI_API_KEY`.  
- **Proxy/SSL errors**: Set `HTTPS_PROXY` and `REQUESTS_CA_BUNDLE`/`SSL_CERT_FILE` to your org CA bundle.  
- **Model not found**: Confirm the model name in `.env` matches one available via **GitHub Models** for your org.  
- **WSL paths**: Prefer a native Linux path (e.g., `~/work/...`) rather than `/mnt/c/...` to avoid file-watcher quirks.

---

### Notes on Minimal Client Changes
Swapping from GitHub Models (OpenAI-compatible) to Azure AI Foundry typically only requires changing:
- Base URL / client construction
- API key / credential
- (Sometimes) model name

Your agent logic and tool wiring remain the same.

---

