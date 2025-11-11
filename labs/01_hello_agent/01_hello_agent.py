#### `labs/01_hello_agent/01_hello_agent.py`

import asyncio, os
from agent_framework import ChatAgent
from agent_framework.openai import OpenAIChatClient

async def main():
    chat = OpenAIChatClient(
        api_key=os.getenv("OPENAI_API_KEY"),
        base_url=os.getenv("OPENAI_BASE_URL"),
        model=os.getenv("OPENAI_CHAT_MODEL", "gpt-4o-mini"),
    )
    agent = chat.create_agent(
        name="hello_agent",
        instructions="You are concise and helpful. Reply in 2-3 sentences."
    )
    print(await agent.run("What is an AI agent and why does it matter?"))

if __name__ == "__main__":
    asyncio.run(main())