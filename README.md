# Cognition Intel

A Markdown-based intelligence system for learning and tracking **Cognition**, **Devin**, and the **AI coding-agent market**.

The system crawls selected sources weekly, detects what changed, summarizes important changes using OpenAI, and writes clean Markdown notes. The repo is also usable as an Obsidian vault.

---

## Structure

```
01 - Weekly Digests/       Weekly summary notes (auto-generated)
03 - Sources/              Source definitions (sources.yaml)
04 - Concepts/             Concept notes (Agent Harness, MCP, etc.)
05 - Battlecards/          Competitive battlecards (Devin vs X)
06 - Sales Narratives/     Sales positioning notes
07 - Questions to Validate/ Questions generated from changes
90 - Raw Snapshots/        Raw crawled Markdown snapshots
prompts/                   Prompt templates (future use)
src/                       Python pipeline code
tests/                     Test suite
```

## How it works

1. **Crawl** — `src/crawl.py` fetches pages from sources defined in `03 - Sources/sources.yaml` using [Firecrawl](https://firecrawl.dev) or [Tavily](https://tavily.com)
2. **Normalize** — `src/normalize.py` cleans Markdown for reliable diffing
3. **Diff** — `src/diff_engine.py` compares the latest snapshot with the previous one, scores changes 1–5, and keeps only score ≥ 3
4. **Summarize** — `src/summarize.py` sends significant changes to OpenAI for structured summaries
5. **Write** — `src/write_markdown.py` produces the weekly digest and questions-to-validate notes

## Required API keys

| Key | Purpose | Required? |
|---|---|---|
| `FIRECRAWL_API_KEY` | Crawl sources via Firecrawl | For Firecrawl sources |
| `TAVILY_API_KEY` | Crawl sources via Tavily | For Tavily sources |
| `OPENAI_API_KEY` | Summarize changes via OpenAI | For summarization |

## Setup

```bash
# Clone the repo
git clone https://github.com/nadavmapss-glitch/cognition-intel.git
cd cognition-intel

# Install dependencies
pip install -r requirements.txt

# Set API keys
export FIRECRAWL_API_KEY="your-key"
export TAVILY_API_KEY="your-key"
export OPENAI_API_KEY="your-key"
```

## Run locally

```bash
# Run the full weekly pipeline
python -m src.weekly_run

# Skip crawling (use existing snapshots for diff/summarize)
python -m src.weekly_run --skip-crawl

# Run tests
python -m pytest tests/ -v
```

## GitHub Actions

The repo includes two workflows:

- **Tests** (`tests.yml`) — runs on every push and PR to `main`
- **Weekly Intel Pipeline** (`weekly-intel.yml`) — runs every Monday at 08:00 UTC, or manually via `workflow_dispatch`

### Configure GitHub Secrets

Go to **Settings → Secrets and variables → Actions** and add:

- `FIRECRAWL_API_KEY`
- `TAVILY_API_KEY`
- `OPENAI_API_KEY`

## Use as an Obsidian vault

1. Open Obsidian
2. Choose **Open folder as vault**
3. Select the `cognition-intel` directory
4. The vault opens with `DASHBOARD.md` as the home note

Wiki-style links (`[[Agent Harness]]`, `[[Devin]]`, etc.) work natively. The `.obsidian/` folder contains minimal config — it will not override your Obsidian settings.

## Adding sources

Edit `03 - Sources/sources.yaml`:

```yaml
sources:
  - name: my-new-source
    url: https://example.com/docs
    crawl_method: firecrawl   # or tavily
    description: What this source is
    tags: [tag1, tag2]
```

## Conventions

| Convention | Example |
|---|---|
| File names | Readable names with spaces (Obsidian-friendly) |
| Internal links | `[[Agent Harness]]`, `[[Devin]]` |
| Tags | `#concept`, `#battlecard`, `#sales` |
| Dates | `YYYY-MM-DD` (ISO 8601) |
| Digest filenames | `YYYY-MM-DD - Weekly AI Coding Agents Digest.md` |

## License

Private repository. All rights reserved.
