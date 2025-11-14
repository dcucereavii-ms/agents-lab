<div align="center" style="border: 2px solid #ccc; border-radius: 10px; padding: 10px 15px; background-color: #f9f9f9;">

<table>
<tr>
<td style="width: 200px; text-align: center; vertical-align: middle;">
  <img src="images/lab04-readme.png" alt="Lab 01 – Hello Agent" width="200"/>
</td>
<td style="text-align: left; vertical-align: middle;">
  <h1>Lab 04 — Structured Outputs</h1>
  <em>Bonus — Advanced & Creative Tracks</em>
</td>
</tr>
</table>

</div>

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