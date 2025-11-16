<div style="border: 2px solid #ccc; border-radius: 10px; padding: 10px 15px; background-color: #f9f9f9;">

<table>
<tr>
<td style="width: 200px; text-align: center; vertical-align: middle;">
  <img src="../../images/lab02-readme.png" alt="Lab 01 – Hello Agent" width="200"/>
</td>
<td style="text-align: left; vertical-align: middle;">
  <h1>Lab 02 — Agent with Tools</h1>
  <em>Teach an agent to work with tools.</em>
</td>
</tr>
</table>

</div>


> **Note:** In this lab, we simulate tool calls locally and then use the model to summarize the outcome because GitHub Models currently does not support OpenAI-style tool calling.

---

**What you’ll learn**
- Declaring tools with **names, descriptions, and JSON schemas**
- Implementing Python functions for tools
- Simulating tool calls locally and passing results to the model for summarization


**Run**
```bash
**Windows**
python 02_agent_with_tool.py

**Linux / macOS***
python3 02_agent_with_tool.py