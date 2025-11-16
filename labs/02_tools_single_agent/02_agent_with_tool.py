import os
import json
import requests
from dotenv import load_dotenv

# Load .env and override any shell vars
load_dotenv(override=True)

# Force GitHub Models endpoint
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY") or ""
BASE_URL = "https://models.github.ai/inference"
MODEL = os.getenv("OPENAI_CHAT_MODEL") or "gpt-4o-mini"

# -----------------------------
# 1) Tools with logging
# -----------------------------
def get_quote(symbol: str) -> float:
    print(f"[Tool Called] get_quote(symbol={symbol})")
    quotes = {"EXCALIBUR": 100.0, "MSFT": 425.20, "CIBC": 58.40, "CM": 58.40}
    return quotes.get(symbol.upper(), 100.0)

def place_order(symbol: str, quantity: int) -> dict:
    print(f"[Tool Called] place_order(symbol={symbol}, quantity={quantity})")
    return {
        "status": "filled" if quantity > 0 else "rejected",
        "symbol": symbol.upper(),
        "qty": quantity,
        "avg_price": get_quote(symbol),
        "note": "fantasy/classroom simulation"
    }

# -----------------------------
# 2) Local simulation logic
# -----------------------------
symbol = "EXCALIBUR"
power = get_quote(symbol)
order_result = None
if power < 500:
    order_result = place_order(symbol, 10)

# -----------------------------
# 3) Prompt for model summary
# -----------------------------
summary_prompt = (
    f"Fantasy quest simulation:\n"
    f"Power level of {symbol}: {power}\n"
    f"Order result: {json.dumps(order_result)}\n"
    f"Write a short, fun summary of the quest outcome."
)

# -----------------------------
# 4) Call GitHub Models API
# -----------------------------
def chat_completions(prompt):
    url = f"{BASE_URL}/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json",
    }
    body = {
        "model": MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7,
    }
    resp = requests.post(url, headers=headers, data=json.dumps(body), timeout=60)
    resp.raise_for_status()
    return resp.json()

# -----------------------------
# 5) Entrypoint
# -----------------------------
def main():
    print("\n=== Environment ===")
    print("OPENAI_BASE_URL =", BASE_URL)
    print("OPENAI_CHAT_MODEL =", MODEL)
    print("====================\n")

    response = chat_completions(summary_prompt)
    content = (response.get("choices") or [{}])[0].get("message", {}).get("content")

    print("\n--- Simulation Output ---")
    print(content)

    # Tools summary
    print("\n--- Tools Used ---")
    print(f"get_quote called for: {symbol}")
    if order_result:
        print(f"place_order called for: {symbol}, qty=10")
    else:
        print("place_order was NOT called")

if __name__ == "__main__":
    main()