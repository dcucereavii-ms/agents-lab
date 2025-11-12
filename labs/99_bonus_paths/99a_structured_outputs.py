import asyncio
import json
import os
from typing import List, Optional, Tuple

from dotenv import load_dotenv
from pydantic import BaseModel, ValidationError, field_validator

# Load .env from the repo root (no shell exports needed)
load_dotenv()

from agent_framework.openai import OpenAIChatClient


# ---------- Domain model (what we expect from the LLM) ----------
class TradeConfirmation(BaseModel):
    symbol: str
    quantity: int
    avg_price: Optional[float] = None
    warnings: Optional[List[str]] = []

    @field_validator("symbol")
    @classmethod
    def normalize_symbol(cls, v: str) -> str:
        return (v or "").strip().upper()


# ---------- Prompt & helpers ----------
SYSTEM_INSTRUCTIONS = """
Return ONLY a valid JSON object with the following fields:
- symbol (string, e.g., "CM" for CIBC)
- quantity (integer, e.g., 5)
- avg_price (number; if unknown, provide a reasonable estimated numeric value; do NOT return null)
- warnings (array of strings, optional)

Strict rules:
- Output must be a single JSON object, no markdown fences, no extra text.
- Keys must match exactly: "symbol", "quantity", "avg_price", "warnings".
- If any field is uncertain, include an explanation in "warnings", but do not leave fields null.
"""

USER_PROMPT = "Confirm a simulated buy for 5 shares of CM at market; summarize any risks."

# Simple price fallback for demonstration (you could call a real tool here)
FALLBACK_PRICES = {"CM": 58.40, "CIBC": 58.40, "MSFT": 425.20}


def to_text(response) -> str:
    """
    Agent Framework returns an AgentRunResponse object.
    We need the plain text payload (JSON string).
    """
    return getattr(response, "text", str(response))


def repair_payload_if_needed(data: dict) -> Tuple[dict, List[str]]:
    """
    If the model leaves 'avg_price' as None/null (or missing), supply a sensible fallback and
    append a warning so the object remains valid and honest.
    """
    warnings = list(data.get("warnings") or [])
    symbol = (data.get("symbol") or "").strip().upper()

    # Ensure required keys exist
    if "avg_price" not in data or data.get("avg_price") is None:
        fallback = FALLBACK_PRICES.get(symbol, 0.0)
        data["avg_price"] = float(fallback)
        warnings.append(
            "avg_price estimated due to uncertainty; using fallback price for demonstration."
        )
        data["warnings"] = warnings

    # Coerce quantity if it came as string
    if isinstance(data.get("quantity"), str) and data["quantity"].isdigit():
        data["quantity"] = int(data["quantity"])

    return data, warnings


# ---------- Main flow ----------
async def main():
    # IMPORTANT: use model_id (GitHub Models via OpenAI-compatible API)
    chat = OpenAIChatClient(
        api_key=os.getenv("OPENAI_API_KEY"),                  # GitHub token
        base_url=os.getenv("OPENAI_BASE_URL"),                # https://models.inference.ai.azure.com
        model_id=os.getenv("OPENAI_CHAT_MODEL", "gpt-4o-mini")
    )

    agent = chat.create_agent(
        name="json_conf_agent",
        instructions=SYSTEM_INSTRUCTIONS
    )

    # 1) Ask the model
    response = await agent.run(USER_PROMPT)
    raw_text = to_text(response)

    # 2) Try to parse as JSON
    try:
        data = json.loads(raw_text)
    except json.JSONDecodeError:
        print("❌ Model did not return valid JSON.\nRaw response:")
        print(raw_text)
        return

    # 3) First validation attempt
    try:
        conf = TradeConfirmation.model_validate(data)
        print("✅ Validated structured output:")
        print(json.dumps(conf.model_dump(), indent=2))
        return
    except ValidationError as e:
        # 4) Attempt a light repair (e.g., fill missing avg_price) and validate again
        repaired_data, _ = repair_payload_if_needed(data)
        try:
            conf = TradeConfirmation.model_validate(repaired_data)
            print("⚠️  Output needed minor repair, now valid:")
            print(json.dumps(conf.model_dump(), indent=2))
            return
        except ValidationError as e2:
            print("❌ Output failed validation, even after repair.")
            print("Raw response:")
            print(raw_text)
            print("\nFirst validation error:")
            print(e)
            print("\nSecond validation error (after repair):")
            print(e2)


if __name__ == "__main__":
    asyncio.run(main())