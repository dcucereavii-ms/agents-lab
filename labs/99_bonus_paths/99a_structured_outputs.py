import asyncio, os, json
from typing import List, Optional
from pydantic import BaseModel, ValidationError
from agent_framework.openai import OpenAIChatClient

class TradeConfirmation(BaseModel):
    symbol: str
    quantity: int
    avg_price: float
    warnings: Optional[List[str]] = []

SYSTEM_INSTRUCTIONS = """
You must return ONLY a valid JSON object with fields:
- symbol (string), quantity (integer), avg_price (number), warnings (array of strings, optional)

Validate inputs logically; if anything is uncertain, include a warning.
No prose, no backticks—JSON ONLY.
"""

async def main():
    chat = OpenAIChatClient(
        api_key=os.getenv("OPENAI_API_KEY"),
        base_url=os.getenv("OPENAI_BASE_URL"),
        model=os.getenv("OPENAI_CHAT_MODEL"),
    )
    agent = chat.create_agent(
        name="json_conf_agent",
        instructions=SYSTEM_INSTRUCTIONS
    )
    raw = await agent.run("Confirm a simulated buy for 5 shares of CM at market; summarize any risks.")
    try:
        # If the SDK returns a string, parse to dict; if it returns dict, this is a no-op
        data = json.loads(raw) if isinstance(raw, str) else raw
        conf = TradeConfirmation.model_validate(data)
        print(json.dumps(conf.model_dump(), indent=2))
    except (json.JSONDecodeError, ValidationError) as e:
        print("❌ Output failed validation:")
        print(e)

if __name__ == "__main__":
    asyncio.run(main())