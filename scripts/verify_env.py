import os
import sys
from dotenv import load_dotenv

# Load .env file from repo root
load_dotenv()

required_vars = [
    "OPENAI_API_KEY",
    "OPENAI_BASE_URL",
    "OPENAI_CHAT_MODEL",
    "OPENAI_EMBEDDING_MODEL"
]

missing = [var for var in required_vars if not os.getenv(var)]

if missing:
    print(f"❌ Missing environment variables: {', '.join(missing)}")
    print("Please check your .env file in the repo root. Example:")
    print("""
OPENAI_API_KEY=<your_github_token>
OPENAI_BASE_URL=https://models.inference.ai.azure.com
OPENAI_CHAT_MODEL=gpt-4o-mini
OPENAI_EMBEDDING_MODEL=text-embedding-3-small
""")
    sys.exit(1)
else:
    print("✅ All required environment variables are set:")
    for var in required_vars:
        print(f"{var} = {os.getenv(var)}")