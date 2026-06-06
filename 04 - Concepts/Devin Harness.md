# Devin Harness

#concept #devin

The **Devin Harness** is Cognition's implementation of the [[Agent Harness]] pattern. It is the orchestration and execution environment that makes Devin an autonomous software engineer rather than just a code-completion tool.

## Architecture

Devin's harness provides a full development environment ([[Devbox]]) for each session:

- **Shell/Terminal** -- full Linux environment for running commands
- **Code editor** -- embedded IDE for reading and writing code
- **Browser** -- Chrome instance (accessible via CDP) for web interactions and testing
- **Planner** -- breaks tasks into sub-steps with dependency tracking
- **Memory** -- maintains context across the session, including conversation history and file state

## Key differentiators

1. **Full autonomy** -- Devin operates independently, unlike IDE-embedded agents that require user presence
2. **Parallel sessions** -- multiple Devin instances can work on different tasks simultaneously
3. **Sub-task decomposition** -- complex tasks can be split into independent sub-tasks
4. **Persistent environment** -- the devbox persists state, so Devin can install dependencies, run servers, and test end-to-end
5. **Model-agnostic** -- supports multiple LLM backends (Claude, GPT, Gemini, SWE-1.6)

## Capabilities

Per Cognition's positioning: "If you can do it in three hours, Devin can most likely do it."

Strengths:
- Tackling many tasks in parallel
- Code migrations and refactors
- Repetitive engineering tasks (tests, docs, PR review)
- Building integrations with unfamiliar APIs

## Related

- [[Agent Harness]]
- [[Devbox]]
- [[Verification Loop]]
