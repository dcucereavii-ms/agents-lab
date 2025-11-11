#### `labs/02_tools_single_agent/02_agent_with_tool.py`

import asyncio, os
from agent_framework.openai import OpenAIChatClient

def get_quote(symbol: str) -> float:
    quotes = {"MSFT": 425.20, "CIBC": 58.40, "CM": 58.40}
    return quotes.get(symbol.upper(), 100.00)

def place_order(symbol: str, quantity: int) -> dict:
    return {"status": "filled", "symbol": symbol.upper(), "qty": quantity, "avg_price": get_quote(symbol)}

async def main():
    chat = OpenAIChatClient(
        api_key=os.getenv("OPENAI_API_KEY"),
        base_url=os.getenv("OPENAI_BASE_URL"),
        model=os.getenv("OPENAI_CHAT_MODEL"),
    )
    trader = chat.create_agent(
        name="capital_markets_trader",
        instructions=("Educational only. Use tools to get quotes and place paper trades when asked. "
                      "Never provide financial advice; remind users of risks."),
        tools=[
            {"type": "function", "function": {
                "name": "get_quote",
                "description": "Get latest quote for a symbol.",
                "parameters": {"type": "object","properties": {"symbol": {"type": "string"}}, "required": ["symbol"]},
                "implementation": get_quote
            }},
            {"type": "function", "function": {
                "name": "place_order",
                "description": "Place a simulated market order.",
                "parameters": {"type": "object","properties": {
                    "symbol": {"type": "string"}, "quantity": {"type": "integer"}}, "required": ["symbol","quantity"]},
                "implementation": place_order
            }},
        ],
    )
    print(await trader.run("Buy 10 shares of MSFT if the price is under $500. Confirm the simulated fill."))

if __name__ == "__main__":
    asyncio.run(main())