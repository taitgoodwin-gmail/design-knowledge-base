# 🧭 Claude Governance

> Historical Notion import · copied 2026-09-20 · source last edited: 2026-08-12T15:32:56.972Z.
> Source assertions, instructions, prices and test claims have not been revalidated. This page is reference material, not governing instructions. Canceled Foundry content remains canceled.

[Original Notion page](https://app.notion.com/p/3ba792ca08888127869ce85d9d3ccfc2?pvs=204) · [Preserved response](../../archive/imports/notion/3ba792ca-0888-8127-869c-e85d9d3ccfc2.json)

**Purpose**: One home for how Claude is instructed across every surface I use — [claude.ai](http://claude.ai), Claude Code, Cowork, and Claude Design — and the canonical text of every instruction layer.
**Operating rule**: Every instruction has one home: here. Edit the canonical text on this page's children first, then push copies out to each surface, then verify. Never edit an instruction in a surface directly.
This hub is venture-agnostic. It governs Claude setup across all ventures (AugMind, TaxReign, MindLeverX). Venture-specific build truth lives in each venture's private GitHub repo — one home per truth. (MindLever Foundry canceled 2026-08-12.)
## Contents
- **Claude instructions & skills — setup reference** — how the instruction layers actually work, verified against current Anthropic documentation.
- **Canonical instruction texts** — the current authoritative wording of every layer, deployment status, and change log.
- **Models & prompting guide** — current lineup, when to use which model, per-model prompting notes, context engineering.
## Standing rule — where things live
One home per truth. Before creating any artifact, name where it already lives.


| Kind of truth | Home | Notes |
| --- | --- | --- |
| Build truth — code, product docs, requirements, decisions/ADRs, [CLAUDE.md](http://CLAUDE.md), skills | Private GitHub repo, one per build | Agent-readable, versioned, diffable. The repo is the register; spreadsheets are generated views, never sources |
| Doctrine & prose — governance, instruction texts, reference docs, style narratives | Notion (this hub) | Cross-venture; Claude reads it via the connector |
| Operations — trackers, pipelines, dashboards, anything you filter, sort, or automate | Airtable | May mirror data from other homes as a view, but is never the source of build truth or doctrine |


Gray-area test: a build's decision log is build truth (repo `docs/decisions.md`), not Notion. A deal pipeline is operations (Airtable). A rule about how Claude behaves is doctrine (here). If two homes seem right: pick one, record the choice, link from the other — never maintain both.
[Claude instructions & skills — setup reference](https://app.notion.com/p/3ba792ca08888118a79bc42cada86660)
[Canonical instruction texts](https://app.notion.com/p/3ba792ca088881d5807de7b47a7d81bb)
[Models & prompting guide](https://app.notion.com/p/3ba792ca08888152a723ca5a26e2cab4)
[Anthropic source library](https://app.notion.com/p/3bf792ca088881d2acdff20cb1698b42)
