# 🧾 Change log

> Historical Notion import · copied 2026-09-20 · source last edited: 2026-08-17T06:38:09.352Z.
> Source assertions, instructions, prices and test claims have not been revalidated. This page is reference material, not governing instructions. Canceled Foundry content remains canceled.

[Original Notion page](https://app.notion.com/p/3bf792ca088881d598acf453f743d399?pvs=204) · [Preserved response](../../archive/imports/notion/3bf792ca-0888-81d5-98ac-f453f743d399.json)

Material additions, revisions, deprecations and removals. Append-only; newest first.
## 2026-08-17
**Added** — Anthropic source library created under the Claude Governance hub: this change log, the source register (149 entries), and daily reports.
**Added** — Baseline register of 149 verified official sources across Claude Code & Agent SDK, Cowork, Claude Design, prompting, API/agents/MCP, and security & governance.
**Revised** — Canonical documentation hosts. `docs.claude.com` and `docs.anthropic.com` now redirect wholesale to `code.claude.com` (Claude Code, Agent SDK) and `platform.claude.com` (API, models, prompting). `privacy.anthropic.com` now redirects to `privacy.claude.com`.
**Deprecated** — Eleven standalone prompt-engineering technique pages have been folded into a single *Prompting best practices* page. Their URLs still resolve with HTTP 200 but no longer serve distinct content. The *Models & prompting guide* source table cited one of them (`long-context-tips`) and has been corrected.
**Deprecated** — *Extended thinking* is now labelled legacy. Adaptive thinking plus the `effort` parameter is the current control surface; `thinking.type: "enabled"` is unsupported on Fable 5, Opus 5 and Sonnet 5.
**Deprecated** — MCP specification 2025-06-18 superseded by 2026-07-28, which is stateless: the `initialize` handshake and session IDs are removed, Sampling and Roots leave the core client feature set, and Tasks, Skills-over-MCP and MCP Apps become opt-in Extensions.
**Removed** — Claude Opus 4.1 retired 2026-08-05.
**Noted** — The planned 2026-09-01 Claude Sonnet 5 price increase to \$3/\$15 per MTok will not occur; \$2/\$10 became the standard rate on 2026-08-10.
