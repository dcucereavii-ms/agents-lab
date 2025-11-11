#### `labs/03_multiagent_handoff/03_multi_agent_handoff.py`

import asyncio, os
from collections.abc import AsyncIterable
from typing import cast
from agent_framework import (
    ChatAgent, ChatMessage, HandoffBuilder, HandoffUserInputRequest,
    RequestInfoEvent, WorkflowEvent, WorkflowOutputEvent, WorkflowRunState, WorkflowStatusEvent
)
from agent_framework.openai import OpenAIChatClient

def create_agents(chat):
    triage = chat.create_agent(
        name="triage_agent",
        instructions=("Read the latest user message and decide whether to hand off to "
                      "refund_agent, order_agent, or support_agent. Use the handoff tools.")
    )
    refund  = chat.create_agent(name="refund_agent",  instructions="You process refunds.")
    order   = chat.create_agent(name="order_agent",   instructions="You resolve delivery issues.")
    support = chat.create_agent(name="support_agent", instructions="You handle general inquiries.")
    return triage, refund, order, support

async def drain(stream: AsyncIterable[WorkflowEvent]): return [e async for e in stream]

def handle(events):
    reqs=[]
    for e in events:
        if isinstance(e, WorkflowStatusEvent) and e.state in {WorkflowRunState.IDLE, WorkflowRunState.IDLE_WITH_PENDING_REQUESTS}:
            print(f"[status] {e.state.name}")
        elif isinstance(e, WorkflowOutputEvent):
            convo = cast(list[ChatMessage], e.data)
            print("\n=== Final Conversation Snapshot ===")
            for m in convo: print(f"- {(m.author_name or m.role.value)}: {m.text}")
        elif isinstance(e, RequestInfoEvent) and isinstance(e.data, HandoffUserInputRequest):
            print("\n=== User Input Requested ===")
            for m in e.data.conversation: print(f"- {(m.author_name or m.role.value)}: {m.text}")
            reqs.append(e)
    return reqs

async def main():
    chat = OpenAIChatClient(
        api_key=os.getenv("OPENAI_API_KEY"),
        base_url=os.getenv("OPENAI_BASE_URL"),
        model=os.getenv("OPENAI_CHAT_MODEL")
    )
    triage, refund, order, support = create_agents(chat)
    wf = (HandoffBuilder(name="customer_support", participants=[triage, refund, order, support])
          .set_coordinator("triage_agent")
          .with_termination_condition(lambda conv: sum(1 for m in conv if m.role.value=="user") >= 4)
          .build())
    scripted = [
        "My order 1234 arrived damaged and the packaging was destroyed.",
        "Yes, I'd like a refund if that's possible.",
        "Thanks for resolving this."
    ]
    events = await drain(wf.run_stream("Hello, I need assistance with my recent purchase."))
    pending = handle(events)
    while pending and scripted:
        reply = scripted.pop(0)
        print(f"\n[User responding: {reply}]")
        events = await drain(wf.send_responses_streaming({r.request_id: reply for r in pending}))
        pending = handle(events)

if __name__ == "__main__":
    asyncio.run(main())