# MCP (Model Context Protocol)

#concept #protocol

**MCP** (Model Context Protocol) is an open protocol created by Anthropic for connecting LLMs to external tools, data sources, and services. It has become a de facto standard in the AI coding-agent ecosystem.

## What it does

MCP provides a standardized way for AI agents to:

- Read from and write to external systems (databases, APIs, file systems)
- Use tools (search, code execution, browser automation)
- Access context from third-party services (project management, documentation)

## Adoption

| Product | MCP support |
|---|---|
| [[Claude Code]] | Native (creator of MCP) |
| [[Devin]] | Supported |
| [[GitHub Copilot]] | Supported (with auto-approve) |
| [[Cursor]] | Supported |

## Why it matters

- **Ecosystem lock-in** -- tools built for MCP work across all supporting agents
- **Extensibility** -- users can connect agents to their internal tools
- **Competitive moat** -- Anthropic benefits from ecosystem effects as the protocol creator
- **Enterprise adoption** -- MCP reduces integration cost for enterprise deployments

## Related

- [[Agent Harness]]
- [[Enterprise Deployment]]
- [[Claude Code]]
