# 🎛️ Models & prompting guide

> Historical Notion import · copied 2026-09-20 · source last edited: 2026-08-12T15:33:19.887Z.
> Source assertions, instructions, prices and test claims have not been revalidated. This page is reference material, not governing instructions. Canceled Foundry content remains canceled.

[Original Notion page](https://app.notion.com/p/3ba792ca08888152a723ca5a26e2cab4?pvs=204) · [Preserved response](../../archive/imports/notion/3ba792ca-0888-8152-a723-ca5a26e2cab4.json)

**Last verified: 2026-08-12.** This area changes faster than anything else in the hub — re-verify against the sources below before relying on it for a migration or a big build decision. Items marked *(inference)* are not stated in docs.
# 1. Current lineup


| Model | Tier | Best for (documented) | Context / max output | API price (in/out per MTok) |
| --- | --- | --- | --- | --- |
| **Claude Fable 5** | Flagship — most capable | "Next-generation intelligence for long-running agents"; deep reasoning, long-horizon agentic work, novel problem-solving | 1M / 128k | \$10 / \$50 |
| **Claude Opus 5** | High | Complex agentic coding & enterprise work; "multihour autonomous coding agents, large-scale refactoring, complex systems engineering" | 1M / 128k | \$5 / \$25 |
| **Claude Sonnet 5** | Balanced | "Best combination of speed and intelligence": code generation, data analysis, content creation, visual understanding, agentic tool use at scale | 1M / 128k | \$2 / \$10 |
| **Claude Haiku 4.5** | Fast/cheap | "Fastest model with near-frontier intelligence": real-time, high-volume, cost-sensitive, subagent tasks | 200k / 64k | \$1 / \$5 |
| Claude Mythos 5 / Preview | Invitation-only | Defensive cybersecurity (Project Glasswing); shares Fable 5 specs | 1M / 128k | \$10 / \$50 |


Opus 5 and 4.8 support **fast mode** (up to 2.5× output speed). Prior generation (Opus 4.8/4.7/4.6, Sonnet 4.6/4.5) remains available and documented. The Claude app's model picker shows display names; dated IDs like `claude-haiku-4-5-20251001` are API naming *(inference — picker composition isn't in developer docs)*.
# 2. Choosing a model
Anthropic's documented rule of thumb: **"Start with the most intelligent generally available model and use effort level to dial in performance and cost."** The alternative strategy is efficiency-first: start with Haiku 4.5 and move up only when quality demands it (prototyping, tight latency, high volume).
- Hardest reasoning, long-running agents, novel problems → **Fable 5**
- Multihour autonomous coding, large refactors, complex systems → **Opus 5**
- Everyday coding, analysis, content creation, tool use at scale → **Sonnet 5**
- Real-time, high-volume, cheap, subagent workers → **Haiku 4.5**
- Writing: no documented per-task recommendation; family positioning points to Fable/Opus for demanding writing *(inference)*
**Effort is the first dial, not model choice**, on the current generation: Opus 5 defaults to `high` (adjust from evals); on Opus 4.8/4.7, `xhigh` is documented as "the best setting for most coding and agentic use cases"; Sonnet 5 defaults to `high` (`xhigh` for the hardest work) — and Sonnet 5 at `medium` ≈ Sonnet 4.6 at `high`.
# 3. Prompting the current generation (applies to all)
- **Say what to do, not what to avoid.** Drop aggressive emphasis — "CRITICAL: You MUST use this tool" now over-triggers; "Use this tool when…" is enough. Remove old anti-laziness prompts when migrating.
- **Literal instruction following.** Current models don't silently generalize an instruction or infer requests you didn't make — state scope explicitly ("Apply this to every section, not just the first").
- **Less verbose by default**; may skip summaries unless prompted. Match your prompt's formatting to the output you want (markdown in → markdown out).
- **Distinguish "suggest" from "implement"** when tools or actions are involved.
- **Never instruct "show your internal thinking/reasoning"** — on Fable 5 this triggers refusals; read the structured thinking output instead.
- Golden rule (documented): if a colleague with minimal context would be confused by your prompt, Claude will be too.
# 4. Per-model prompting notes
## Fable 5
- Effort is the primary control; lower settings often exceed prior models' best. Expect longer turns — minutes per request at high effort.
- Can over-plan: "When you have enough information to act, act. Do not re-derive facts… give a recommendation, not an exhaustive survey."
- Tidies/refactors beyond the ask — if unwanted: "Don't add features, refactor, or introduce abstractions beyond what the task requires."
- On autonomous runs, can misstate progress — require grounding: "Before reporting progress, audit each claim against a tool result from this session; if tests fail, say so with the output."
- May take unrequested actions (drafting emails, backup branches) — set boundaries: "The deliverable is your assessment. Report your findings and stop."
- Performs notably better with memory/lesson files: one lesson per file, one-line summary on top, delete wrong notes.
- Give the reason, not only the request: "I'm working on \[larger task\] for \[who\]. They need \[what the output enables\]. With that in mind: \[request\]."
- Shown a token countdown, it may wrap up early — hide budget counts or reassure ("You have ample context remaining").
## Opus 5
- Effort controls how much it *thinks*, not how much it *says* — control response length by prompting for it explicitly; written deliverables run long ("do not pad with filler sections, redundant summaries, or boilerplate").
- **Remove verification instructions** — it self-verifies; explicit "double-check your work" prompts waste tokens with no quality gain.
- Watch scope expansion: "Deliver what was asked, at the scope intended — say so in a sentence rather than quietly widening."
- Delegates to subagents readily — constrain: only for large, independent, parallelizable work; never to check its own output.
- Narrates during agentic work — prescribe cadence: "Before your first tool call, one sentence on what you're about to do; lead with the outcome."
- Best when "given the complete task specification up front and left to run."
## Sonnet 5
- Adaptive thinking ON by default; `temperature`/`top_p`/`top_k` now return errors — steer variety via the prompt instead.
- New tokenizer uses \~30% more tokens for the same text — retune `max_tokens` and leave headroom at high effort or the answer gets truncated after thinking.
- More agentic by default; respects effort strictly at the low end — shallow reasoning means raise effort, not prompt harder.
- Settles into a fixed visual style in design work — fix with a fully specified brief, or ask for "4 distinct visual directions, then I pick."
- Code review: obeys severity bars literally — "Report every issue you find, including uncertain ones; a separate step will filter."
## Opus 4.8
- Thinking OFF unless you enable adaptive thinking — opposite default from Sonnet 5/Opus 5. `xhigh` is the sweet spot; `max` can overthink.
- Favors reasoning over tool calls — raise effort or explicitly instruct tool use when needed.
- Spawns FEWER subagents than Opus 5/Fable 5 (steerable both directions).
- Direct, opinionated tone with minimal validation — re-check voice prompts if warmth matters.
- Persistent design house style (cream backgrounds, serif display type, terracotta accents) — same fixes as Sonnet 5.
## Haiku 4.5
- No dedicated prompting page exists. Documented: 200k context (not 1M), extended thinking (not adaptive), context awareness, positioned for subagent/high-volume/real-time work. Treat further specifics as unverified.
# 5. Context engineering
- **Long inputs (20k+ tokens): documents at the TOP, query and instructions at the END** — documented up-to-30% response-quality improvement on multi-document tasks.
- Wrap documents in XML: `<document><source>…</source><document_content>…</document_content></document>`.
- Ask Claude to **quote relevant passages first**, then answer — grounds long-context work.
- Examples: 3–5, relevant and diverse, in `<example>` tags. Canonical cases, not edge-case stuffing.
- **Context rot is documented**: accuracy degrades as tokens grow — treat context as "a finite resource with diminishing marginal returns." Prefer just-in-time retrieval (keep identifiers, load data via tools) over pre-stuffing.
- Long-horizon work: structured note files / memory, subagents that return condensed summaries, git as state store.
- Prompt caching shapes ORDER: stable content first (tools → system → messages), changing content (timestamps, user input) last.
# 6. Sources


| Source | Covers |
| --- | --- |
| [Models overview](https://platform.claude.com/docs/en/about-claude/models/overview) | Lineup, specs, pricing |
| [Choosing a model](https://platform.claude.com/docs/en/about-claude/models/choosing-a-model) | Selection strategies, effort guidance |
| [Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices) | Generation-wide guidance |
| [Prompting Fable 5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5) | Fable 5 deltas |
| [Prompting Sonnet 5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5) | Sonnet 5 deltas |
| [Prompting Opus 5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5) | Opus 5 deltas |
| [Prompting Opus 4.8](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-4-8) | Opus 4.8 deltas |
| [Long context tips](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/long-context-tips) | Document placement, XML, quoting |
| [Context windows](https://platform.claude.com/docs/en/build-with-claude/context-windows) | What counts toward context |
| [Prompt caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) | Ordering for cache efficiency |
| [Effective context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) | Context rot, just-in-time retrieval, long-horizon patterns |
| [Models explained (blog, 2026-07-24)](https://claude.com/blog/claude-models-explained-choosing-the-best-model-for-your-use-case) | Family positioning — one stale claim flagged, cross-check with overview |
