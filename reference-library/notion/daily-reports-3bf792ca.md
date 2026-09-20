# 📅 Daily reports

> Historical Notion import · copied 2026-09-20 · source last edited: 2026-08-17T06:38:09.352Z.
> Source assertions, instructions, prices and test claims have not been revalidated. This page is reference material, not governing instructions. Canceled Foundry content remains canceled.

[Original Notion page](https://app.notion.com/p/3bf792ca08888198a89bf3254997e7b6?pvs=204) · [Preserved response](../../archive/imports/notion/3bf792ca-0888-8198-a89b-f3254997e7b6.json)

One entry per sweep. Newest first. Each records what was checked, what was new, what changed, what failed, and what returned no material change.
# 2026-08-17 — first full sweep
**Result**: 149 sources verified across six topic areas. 20 failures, redirects and gaps recorded. Baseline established; no prior run to diff against, so everything is new by definition.
## Coverage


| Topic | Sources |
| --- | --- |
| API, Agents & MCP | 44 |
| Claude Code & Agent SDK | 38 |
| Security & Governance | 28 |
| Cowork | 21 |
| Prompting | 13 |
| Claude Design | 5 |


## Material changes written into hub pages
- **Models & prompting guide** — one dead source link corrected, Opus 5 thinking constraint at high effort added, Opus 4.1 retirement and Sonnet 5 price permanence recorded, documented knowledge cutoffs added.
- **Claude instructions & skills — setup reference** — commands/skills merge, `.claude/rules/`, `AGENTS.md` pattern, auto-memory load limit, and answers to two of the page's own open questions.
## Failures, redirects and honest gaps
- `docs.claude.com` and `docs.anthropic.com` 302-redirect their entire trees. Canonical hosts are now `code.claude.com` and `platform.claude.com`.
- `privacy.anthropic.com` redirects to `privacy.claude.com`.
- **Silent consolidation**: eleven prompt-engineering technique URLs still return HTTP 200 but serve the single consolidated best-practices page — `be-clear-and-direct`, `multishot-prompting`, `chain-of-thought`, `use-xml-tags`, `system-prompts`, `chain-prompts`, `long-context-tips`, `extended-thinking-tips`, `prompt-templates-and-variables`, `prompt-improver`, `prompt-generator`. `prefill-claudes-response` serves the overview page. A status-code-only link check would call all twelve healthy.
- `test-and-evaluate/eval-tool` is absent from the current docs index; `develop-tests` is the equivalent.
- `trust.anthropic.com/subprocessors` returns 200 but renders its content in JavaScript — the subprocessor list could not be verified without a browser.
- `github.com/anthropics/claude-code` and `claude-code-action` could not be fetched directly; both are cited by official docs but their contents are unverified here.
- `github.com/anthropics/knowledge-work-plugins/tree/main/design` is blocked by robots — the design plugin exists per the repo README but its skills are unverified.
- No Cowork or Claude Design documentation exists on `docs.claude.com` / `platform.claude.com`. All end-user material lives on `support.claude.com`. Recorded as a real gap rather than padded with adjacent Agent Skills pages.
## No material change
Claude Design remains a research preview with the same four-page corpus and no changelog beyond its single launch line. Its three support articles still show no dates.
