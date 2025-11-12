# Bonus — Advanced & Creative Tracks

Pick one (or more) and experiment:

1. **Structured outputs with validation**  
   - Use `pydantic` to validate JSON returned by the agent (`99a_structured_outputs.py`).  
   - Funnel the validated dict into a mini “risk check” function.

2. **MCP concept (filesystem / Git)**  
   - Draft how you'd expose a read-only filesystem or Git repo via MCP (`99b_mcp_creative_ideas.md`).  
   - Define what the agent must request, and what is returned.

3. **AI Search concept**  
   - Design how you’d add an “enterprise docs” retrieval tool (`99c_ai_search_creative_ideas.md`).  
   - Define filters and security constraints (no PII in prompts, etc.).

4. **Add an agent role**  
   - Insert a **Compliance** or **Risk** specialist that must approve any refund/tool call.

5. **Blue/Red prompt hardening**  
   - Try to break the instructions, then improve them. Track improvements and results.

There’s no single “right” solution—optimize for clarity, testability, and safe behavior.