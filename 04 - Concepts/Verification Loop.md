# Verification Loop

#concept

A **verification loop** is the process by which an AI coding agent validates that its generated code actually works. This is a critical differentiator between agents that merely generate code and agents that deliver working software.

## Steps in a typical verification loop

1. **Write code** -- generate or modify source files
2. **Lint / type-check** -- run static analysis to catch obvious errors
3. **Build** -- compile or bundle the project
4. **Test** -- run the existing test suite (and sometimes write new tests)
5. **Manual check** -- (optional) visually inspect UI, check API responses
6. **Iterate** -- if any step fails, analyze the error and retry

## Implementation by product

| Product | Verification approach |
|---|---|
| [[Devin]] | Full loop in sandbox: lint, build, test, browser check, iterate |
| [[Claude Code]] | Terminal-based: runs commands, reads output, iterates |
| [[GitHub Copilot]] | Agent mode runs commands and iterates; user approves |
| [[Cursor]] | Composer can run terminal commands; user-in-the-loop |

## Why it matters

- Agents without a verification loop produce code that "looks right" but may not compile or pass tests
- The quality of the verification loop directly impacts user trust and adoption
- Enterprise buyers specifically evaluate this capability

## Related

- [[Agent Harness]]
- [[Devin Harness]]
- [[Enterprise Deployment]]
