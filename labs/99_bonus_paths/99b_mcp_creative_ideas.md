# MCP (Model Context Protocol) — Creative Ideas

**Goal:** Sketch how you’d let an agent read files safely using MCP.

- **Scope**: Read-only filesystem connector that exposes a curated folder
- **Tool surface**:
  - `list_files(path, pattern?) -> [str]`
  - `read_text(path) -> { "path": str, "content": str }`
- **Security**:
  - Enforce a root and extension allow-list (`.md`, `.txt`, `.csv`)
  - Max payload size, chunking large files
- **Agent contract**:
  - The agent must cite filename + line numbers when quoting
  - The agent must summarize **before** verbatim quotes
- **Test plan**:
  - Adversarial queries: path traversal (`../`), binary files, excessive file count