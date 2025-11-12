import asyncio
import os
from dotenv import load_dotenv

# Load .env so we don't rely on shell exports
load_dotenv()

from agent_framework.openai import OpenAIChatClient

# -----------------------------
# 1) Python implementations
# -----------------------------
def get_quote(symbol: str) -> float:
    quotes = {"MSFT": 425.20, "CIBC": 58.40, "CM": 58.40}
    return quotes.get(symbol.upper(), 100.00)

def place_order(symbol: str, quantity: int) -> dict:
    return {
        "status": "filled",
        "symbol": symbol.upper(),
        "qty": quantity,
        "avg_price": get_quote(symbol),
    }

# -----------------------------
# 2) Tool specs (JSON ONLY)
#    DO NOT put Python functions in these dicts
# -----------------------------
TOOL_SPECS = [
    {
        "type": "function",
        "function": {
            "name": "get_quote",
            "description": "Get the latest quote for a symbol.",
            "parameters": {
                "type": "object",
                "properties": {"symbol": {"type": "string"}},
                "required": ["symbol"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "place_order",
            "description": "Place a simulated market order.",
            "parameters": {
                "type": "object",
                "properties": {
                    "symbol": {"type": "string"},
                    "quantity": {"type": "integer"},
                },
                "required": ["symbol", "quantity"],
            },
        },
    },
]

async def main():
    # IMPORTANT for this AF build: pass model_id (not model) at client init
    chat = OpenAIChatClient(
        api_key=os.getenv("OPENAI_API_KEY"),           # GitHub token
        base_url=os.getenv("OPENAI_BASE_URL"),         # https://models.inference.ai.azure.com
        model_id=os.getenv("OPENAI_CHAT_MODEL", "gpt-4o-mini"),
    )

    # Option A (preferred on recent AF core): pass specs + implementations separately
    trader = chat.create_agent(
        name="capital_markets_trader",
        instructions=(
            "Educational only. Use tools to get quotes and place paper trades when asked. "
            "Never provide financial advice; remind users of risks."
        ),
        tools=TOOL_SPECS,
        # Map function name -> Python callable
        tool_implementations={
            "get_quote": get_quote,
            "place_order": place_order,
        },
    )

    # If your AF build doesn't accept 'tool_implementations', try Option B below.

    prompt = "Buy 10 shares of MSFT if the price is under $500. Confirm the simulated fill."
    result = await trader.run(prompt)
    print(result)

if __name__ == "__main__":
    asyncio.run(main())