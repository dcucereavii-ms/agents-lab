# Azure AI Search — Creative Ideas

**Goal:** Draft a retrieval tool the agent can call when enterprise docs are available.

- **Inputs**: `query`, `top_k`, optional filters (department, date range)
- **Outputs**: list of `{ title, url, snippet, score }`
- **Guardrails**:
  - Disallow queries with PII patterns
  - Always show citations in final answers
- **Ranking**:
  - Blend semantic score + freshness + department boost
- **Offline simulation**:
  - Use a local JSON index; the tool returns filtered items
- **Upgrade path**:
  - Replace local JSON with Azure AI Search SDK + connection