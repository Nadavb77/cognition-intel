# Agent Harness

#concept

An **agent harness** is the runtime environment and orchestration layer that wraps an LLM to turn it into a functional coding agent. It handles:

- **Sandboxed execution** -- running code safely in an isolated environment
- **Tool use** -- giving the LLM access to terminal, browser, file system, and APIs
- **Memory and context management** -- maintaining state across multi-step tasks
- **Planning and iteration** -- breaking tasks into sub-steps and retrying on failure
- **Verification** -- checking that generated code compiles, passes tests, and meets requirements (see [[Verification Loop]])

## Why it matters

The harness is where most of the differentiation happens between coding agents. The underlying LLM is often the same (Claude, GPT-4, Gemini), but the harness determines how effectively the model is applied to real engineering tasks.

## Key implementations

| Product | Harness approach |
|---|---|
| [[Devin]] | Full VM with browser, terminal, editor ([[Devbox]]) -- see [[Devin Harness]] |
| [[Claude Code]] | Terminal-native CLI with file system access |
| [[GitHub Copilot]] | IDE-embedded with terminal integration |
| [[Cursor]] | IDE-embedded with inline diffs and multi-file editing |

## Related

- [[Devin Harness]]
- [[Verification Loop]]
- [[Devbox]]
