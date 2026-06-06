# Cognition Intel

A Markdown-based intelligence system for learning and tracking **Cognition**, **Devin**, and the **AI coding-agent market**.

The system monitors selected sources, detects what changed, summarizes important changes using OpenAI, and writes clean Markdown notes. The repo is also usable as an Obsidian vault.

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

The pipeline supports two modes for tracking sources:

### Firecrawl Monitoring (preferred for official docs/blogs)

For sources with `mode: monitor`, the system uses [Firecrawl Monitoring](https://firecrawl.dev) — a recurring crawl/scrape service that:
- Compares against retained snapshots automatically
- Detects same/new/changed/removed/error pages
- Returns markdown diffs with built-in judging (AI-powered meaningfulness scoring)
- Supports webhook or polling notification

The local `diff_engine.py` **does not duplicate** Firecrawl's diffing. Instead, it:
1. **Scores** the importance of Firecrawl-reported changes (1–5)
2. **Classifies** them into categories: `product`, `pricing`, `security`, `deployment`, `integration`, `competitor`, `docs-only`, `minor wording`, `unknown`

### Local crawl + diff (fallback for non-monitored sources)

For sources with `mode: crawl` or `mode: scrape`, the pipeline:
1. **Crawl** — `src/crawl.py` fetches pages via [Firecrawl](https://firecrawl.dev) or [Tavily](https://tavily.com)
2. **Normalize** — `src/normalize.py` cleans Markdown for reliable diffing
3. **Diff** — `src/diff_engine.py` compares latest vs previous snapshot, scores changes 1–5, keeps only score ≥ 3
4. **Summarize** — `src/summarize.py` sends significant changes to OpenAI for structured summaries
5. **Write** — `src/write_markdown.py` produces the weekly digest and questions-to-validate notes

### When to use which mode

| Mode | Best for | How it works |
|------|----------|-------------|
| `monitor` | Official docs, blogs, changelogs | Firecrawl runs recurring crawls, detects and diffs changes, provides AI judgment |
| `crawl` | External sources, community docs | Local crawler fetches + local diff engine compares snapshots |
| `scrape` | Single-page sources | Same as crawl but for explicit URLs only |

## Required API keys

| Key | Purpose | Required? |
|---|---|---|
| `FIRECRAWL_API_KEY` | Firecrawl crawling and monitoring | For Firecrawl/monitor sources |
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

## Firecrawl Monitoring

### Creating monitors

Monitors are defined in `03 - Sources/sources.yaml` with `mode: monitor`:

```yaml
- name: devin-docs
  url: https://docs.devin.ai
  mode: monitor
  monitor:
    target_type: crawl        # crawl (discovery) or scrape (explicit URLs)
    schedule:
      cron: "0 8 * * 1"      # Every Monday 8am, or use text: "every monday at 8am"
      timezone: UTC
    goal: >-
      Notify when docs pages add, remove, or materially change
      API behavior, features, or deployment instructions.
    crawl_limit: 100
    max_discovery_depth: 3
    notification: none        # none, webhook, or email
```

To create a monitor via the API:

```python
from src.firecrawl_monitoring import create_monitor
from src.crawl import load_sources

sources = load_sources()
monitor_source = next(s for s in sources if s["name"] == "devin-docs")
result = create_monitor(monitor_source)
# Save the returned monitor ID back to sources.yaml as monitor_id
```

### Webhooks vs weekly polling

| Approach | Pros | Cons |
|----------|------|------|
| **Weekly polling** (default) | Simple, no infra needed, runs during weekly pipeline | Delayed — changes detected only at poll time |
| **Webhook** | Real-time notifications | Requires a publicly-accessible endpoint |

For webhook mode, set `notification: webhook` and add `webhook_url` in the source config. The webhook receives `monitor.page` events with page-level diffs and judgments.

### How monitor results flow through the pipeline

1. `weekly_run.py` calls `fetch_monitor_results()` for all `mode: monitor` sources
2. Each source's latest check is parsed into `MonitorCheckResult` objects
3. `build_monitor_diff_report()` scores and classifies Firecrawl-reported changes
4. Results merge with local crawl diffs before summarization
5. The weekly digest separates changes into sections:
   - **Firecrawl Monitored Changes**
   - **Tavily-Discovered Updates**
   - **Crawl-Based Changes**

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
  # Firecrawl Monitoring (preferred for official docs)
  - name: my-monitored-source
    url: https://example.com/docs
    mode: monitor
    monitor:
      target_type: crawl
      schedule:
        cron: "0 8 * * 1"
        timezone: UTC
      goal: "Track documentation changes"
      crawl_limit: 50
      notification: none

  # Local crawl fallback
  - name: my-crawled-source
    url: https://example.com/docs
    mode: crawl
    crawl_method: tavily
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
