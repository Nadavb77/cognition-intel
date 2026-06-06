# Devbox

#concept #devin

A **devbox** (in the Devin context) is the isolated, ephemeral development environment that Devin uses for each session. It provides a complete Linux machine with:

- Shell access
- File system
- Package managers
- Browser (Chrome via CDP)
- Network access
- Persistent state within the session

## Purpose

The devbox ensures that Devin can:

1. Install any dependencies needed for the task
2. Run builds, tests, and servers
3. Interact with web UIs for testing
4. Access external APIs and services
5. Operate without affecting the user's local environment

## Comparison

| Feature | Devin Devbox | GitHub Codespace | Replit |
|---|---|---|---|
| Purpose | Agent execution | Developer workspace | Cloud IDE |
| Autonomy | Fully autonomous | User-driven | Mixed |
| Browser | Built-in Chrome | Not included | Not included |
| Persistence | Per-session + snapshots | Persistent | Persistent |

## Related

- [[Devin Harness]]
- [[Agent Harness]]
