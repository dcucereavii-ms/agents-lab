import asyncio
import os
from dotenv import load_dotenv

# Load .env so we don't rely on shell exports
load_dotenv()

from agent_framework.openai import OpenAIChatClient

async def main():
    # Initialize client with GitHub Models endpoint and token
    chat = OpenAIChatClient(
        api_key=os.getenv("OPENAI_API_KEY"),  # GitHub token
        base_url=os.getenv("OPENAI_BASE_URL"),  # https://models.inference.ai.azure.com
        model_id=os.getenv("OPENAI_CHAT_MODEL", "gpt-4o-mini"),  # ✅ GitHub model name
    )

    agent = chat.create_agent(
        name="hello_agent",
        instructions="You are concise and helpful. Reply in 2-3 sentences."
    )

    result = await agent.run("What is an AI agent and why does it matter?")
    print(result)

if __name__ == "__main__":
    asyncio.run(main())