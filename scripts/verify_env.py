import os, sys
required = ["OPENAI_API_KEY", "OPENAI_BASE_URL", "OPENAI_CHAT_MODEL"]
missing = [k for k in required if not os.getenv(k)]
if missing:
    print("❌ Missing env vars:", ", ".join(missing)); sys.exit(1)
print("✅ Env OK")