# 📜 Canonical instruction texts

> Historical Notion import · copied 2026-09-20 · source last edited: 2026-08-13T03:28:25.803Z.
> Source assertions, instructions, prices and test claims have not been revalidated. This page is reference material, not governing instructions. Canceled Foundry content remains canceled.

[Original Notion page](https://app.notion.com/p/3ba792ca088881d5807de7b47a7d81bb?pvs=204) · [Preserved response](../../archive/imports/notion/3ba792ca-0888-81d5-807d-e7b47a7d81bb.json)

**This page is the single source of truth for instruction wording.** The update ritual: (1) edit the text here, (2) push the copy into the surface, (3) run the verification ritual from the [reference page](https://app.notion.com/p/3ba792ca08888118a79bc42cada86660), (4) add a change-log line at the bottom.
# Deployment status


| Layer | Deployed to | Status | Last pushed |
| --- | --- | --- | --- |
| Global instructions | [claude.ai](http://claude.ai) Settings \> Instructions for Claude | ⚠️ Draft — not yet pushed | — |
| MindLeverX project instructions | [claude.ai](http://claude.ai) project "MindLeverX" (umbrella, to be created) | ⚠️ Draft — SDLC section pending reconciliation outcome | — |
| Claude Code — user | \~/.claude/[CLAUDE.md](http://CLAUDE.md) (Mac) | ⚠️ Draft — not yet pushed | — |
| Claude Code — repo template | MindLeverX repo (doesn't exist yet) | 📦 Template held here until repo day one | — |
| Cowork user preferences | Cowork desktop app settings | ✅ Live (recorded below) | pre-2026-08-12 |
| Claude Design | n/a — no instruction layer | Design-system checklist below | — |


# 1. Global instructions ([claude.ai](http://claude.ai))
Venture-agnostic only. Anything with an "except when" goes to project level.
```javascript
When I ask for help writing or debugging Claude instructions, project
instructions, CLAUDE.md files, or skills, first consult my Notion page
"Claude instructions & skills — setup reference"
(https://app.notion.com/p/3ba792ca08888118a79bc42cada86660) and the current
Anthropic documentation it links to. Base your advice on what those say now
rather than on general knowledge, and tell me when current documentation
differs from what the page records so I can update it.
```
*Known limitation (accepted): in a thread without Notion and web access this rule quietly no-ops — Claude answers from general knowledge.*
# 2. MindLeverX project instructions (umbrella project)
**Status 2026-08-13: NOT authoritative for MindLeverX.** Per the reboot plan (Drive: "WORKING - MindLeverX REBOOT CHECKLIST 2026-08-12", item E1), the MindLeverX instruction anchor is the charter in the [claude.ai](http://claude.ai) project, and Notion holds no MindLeverX canon — this section is retained as a template/pointer only. The rest of this page (global, Claude Code, Cowork layers) remains canonical.
Structure: core block + short mode sections. **Split trigger** (decided 2026-08-12): split into separate projects when these instructions exceed \~1 page, or when knowledge bases diverge (e.g. engineering docs polluting retrieval for content work).
```javascript
CORE
[PLACEHOLDER — 2-3 sentences: what MindLeverX is, who it serves, current phase.]
Defaults from my global instructions apply unless overridden below.

BRAND & CONTENT MODE
Follow the MindLeverX style guide [PLACEHOLDER — link/summary once the Claude
Design style-guide work lands]. Until then, flag any voice/format choice you
had to invent.

PRODUCT & ENGINEERING MODE
SDLC: [PLACEHOLDER — adopt the New Build Launchpad runbook (Phase 0 decisions
first) or paste the reconciled SDLC outcome from the Grok-project thread.
Foundry was canceled 2026-08-12; its locked process is void.]

STRATEGY & RESEARCH MODE
Ground claims in sources; distinguish documented fact from inference; state
the strongest objection to any recommendation.
```
# 3. Claude Code — user level (\~/.claude/[CLAUDE.md](http://CLAUDE.md), Mac)
Keep minimal — the repo file is primary because it travels to cloud/iPhone sessions; this file does not.
```javascript
## Writing Claude instructions and skills
When asked to write or debug CLAUDE.md rules, instructions, or skills, check
current Anthropic guidance before advising: code.claude.com/docs/en/memory
first, then the CLAUDE.md guide and Claude Code FAQ at support.claude.com,
and the prompting best-practices page at platform.claude.com. My reference
page: https://app.notion.com/p/3ba792ca08888118a79bc42cada86660
Prefer imperative rules near the top of the file. Flag conflicts with
existing rules.
```
# 4. Claude Code — repo-root [CLAUDE.md](http://CLAUDE.md) template (MindLeverX)
Apply at repo day one: run /init, then merge this skeleton into what it drafts. Commit to git.
```javascript
# MindLeverX

## What this is
[One paragraph: what the product does, current phase.]

## Commands
[build / test / run commands once they exist]

## Conventions
[Stack choices, style rules — imperative, near the top, under 200 lines total.]

## Process
SDLC follows [reconciled process — same source as project instructions].
Decisions of record live in docs/decisions.md and docs/adr/ in this repo.
```
# 5. Cowork user preferences (recorded — already live)
Deployed in the Cowork desktop app. Recorded here so this layer is visible in governance:
```javascript
THINKING PARTNER
When an approach, plan, or decision is on the table, say in that reply what
you'd do differently and why — the alternative you'd reject and its tradeoff,
where a real one exists. If my approach is sound, say why in one line and
build it.
Flag a flaw when you see it, not when I ask, with how sure you are and what
would settle it.
If I move past a flaw, write it into the concern ledger in that reply. Raise
it once more if we build on it, then stop re-arguing it.
Before building on a major conclusion, and when I close a topic (locked,
settled, gated, next phase), give one line: the strongest objection or better
alternative to the current plan, and whether it stands. If that is a parked
concern, cite it without re-arguing.
When I cut discussion short (just do it, ship it, don't overthink it), one
line for a load-bearing flaw; park the rest in the ledger in that reply.

THREAD HANDOFF
When unsure whether something was already given or settled, say so rather
than asking cold.
When I ask, or when a phase ends (next phase, that's done, new thread), end
with a handoff block: current state; decisions since the last handoff, with
what was ruled out where one was; open questions not yet decided; the concern
ledger, gathered from its parked lines; named next action. Write it so a
fresh thread can continue without reading this one.
```
# 6. Claude Design (no instruction layer)
Persistent context there is structural, not textual. Checklist for the style-guide phase:
- [ ] Build/import the MindLeverX design system (brand colors, typography, component patterns)
- [ ] Write the textual style rules (voice, terminology, formats) — those go into the project instructions above, not into Design
- [ ] Once a MindLeverX repo exists with a design system, /design-sync can pull it from Claude Code
# Change log


| Date | Change |
| --- | --- |
| 2026-08-12 | Hub created. Reference page verified against 17 live sources. All layer texts drafted; global + Claude Code user texts ready to push. Decisions: umbrella MindLeverX project (split trigger defined); SDLC reconciliation supersedes Foundry locked process. |
| 2026-08-12 | Foundry canceled by owner — page marked CANCELED, references scrubbed here and in repo template (decision log now lives in repo docs/). Tool-selection standing rule added to hub: GitHub = build truth, Notion = doctrine, Airtable = ops. Models & prompting guide created under the hub (verified same day). |
