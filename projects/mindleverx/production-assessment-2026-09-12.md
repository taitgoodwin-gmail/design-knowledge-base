# MindLeverX GEO skills: production automation assessment

Reviewed 12 September 2026. Sources: the supplied Mindleverx-1.3.1-v3.zip and the current clean-slate requirements workbook. The example PDF is outside the assessment scope, following your clarification.

**Verdict: reusable guidance for an operator-assisted service; not a demonstrated unattended production system.** The skills can be part of an automated implementation. This package alone does not supply the execution, measurement, persistence, or enforcement needed for URL → payment → reliable delivered report.

This assessment is based on static package review, inspection of all five SKILL.md files and relevant supporting references/evaluation records, and workbook comparison. The three JSON files parsed successfully and all five skill files have delimited frontmatter. These are structural checks only. I did not install or invoke the plugin in Claude, run paid engine calls, rerun the client audit, validate historical website observations, or test concurrent customer jobs.

**What is present**

The archive has 23 files: 18 Markdown documents, three JSON files, one HTML template, and one CSS file. It includes a Claude plugin manifest and five skills:

| Component | Reusable contribution | First-sale treatment |
| --- | --- | --- |
| geo-audit | Website checks, explicit evidence labels, missing-data disclosure, spot-panel guidance | Keep and revise into a bounded audit-only workflow |
| client-deliverable | Branded HTML/CSS, report structure, owner/implementer distinction, rendering guidance | Keep; preapprove a shorter fixed report structure and supply structured evidence |
| gso-delivery-runbook | Scope, ownership, gate criteria, disclosure, client records | Simplify for a one-time report; keep operator release |
| geo-solution | Draft copy, schema, remediation artifacts, dependency ordering | Optional later service; exclude live changes from report fulfillment |
| geo-tracking | Frozen panels, provenance continuity, repeated observations | Defer recurring monitoring; reuse only the measurement concepts needed for the initial audit |

**Production blockers and supporting evidence**

| Priority | Finding | Evidence in supplied material | Required resolution |
| --- | --- | --- | --- |
| Before unattended execution | No shipped execution/measurement integration | README explicitly defers a measurement connector in .mcp.json. No .mcp.json, application entrypoint, dependency manifest, or executable audit scripts are included. geo-tracking relies on an available tracker or browser. | Configure and test a controlled worker with an explicit fetch/search instrument and one named answer-engine integration. Record actual exposed metadata; do not invent unavailable fields. |
| Before accepting automated orders | No order-to-report application | No checkout handler, payment verification, durable queue, customer storage implementation, retry controller, or delivery implementation is included. | Connect an order ID to confirmed payment, customer authorization, run ID, evidence, and report; support duplicate notifications, failure handling, and controlled delivery. Initially these operations can be operator-assisted. |
| Before publication | Scoring is underdefined | geo-audit specifies four 0–100 dimensions and their mean, but no per-check scoring function. evals/brightwater/EXISTING-BAND-SCALE.md explicitly acknowledges missing dimension-specific anchors. | Prefer separate findings for the first release, following the workbook. If a score is retained, define and validate an explicit rubric before publishing it. |
| Before choosing the audit method | Skills conflict with workbook | Skills require a composite; workbook MLX3-MEA-013 prohibits it. geo-audit uses 5–10 prompts and available engines; workbook specifies 10–15 prompts and one named engine. geo-tracking calls for 20–40 prompts, multiple engines and 2–3 samples; workbook requires at least three attempts when the approved method calls for them. | Choose one authoritative first-sale method. These are alternative product specifications, not interchangeable implementations. |
| Before unattended release | Provenance rules are advisory and inconsistent | README defers the Stop hook and provenance-verifier. geo-audit/client-deliverable preserve NOT MEASURED; geo-solution maps an unmeasured finding to an UNVALIDATED fix and omits an explicit STATED mapping. The manifest says provenance is enforced end to end, but no enforcement implementation is shipped. | Store structured observations and claims with stable evidence references. Programmatically reject unsupported numbers, missing evidence, ambiguous entities, and inappropriate claims. Keep evidence status separate from recommendation status. |
| Before measuring reliability | No runnable end-to-end evaluation harness | JSON files contain prompts, assertions, and reported results; no runner or raw model/tool transcripts are included. Brightwater records 23/24 with skills and 13/24 without, but those figures are historical summaries, not results reproduced in this review. | Add repeatable fixtures, executable assertions, pinned inputs/configuration and retained execution logs. Test repeatability, negative cases, failure recovery, and output validation. |
| Before unattended collection | No demonstrated security boundary | Markdown instructions do not implement customer isolation, URL/redirect restrictions, prompt-injection containment, secret protection, or enforceable permission limits. | Implement these in the worker and storage layer. Test that page content cannot change tools, customer scope, or release behavior. |
| Before unattended operation | Workflow expects human input and external systems | Runbook assumes a buyer conversation, three competitors, signed SOW, Airtable, Linear, Drive, and sometimes Fireflies. client-deliverable requests outline approval, a reply route, and reader checks. | Define fixed intake fields, a preapproved template, and explicit hold states. Choose only the systems needed for one paid report. Do not silently skip missing inputs. |
| Before repeatable rendering | Rendering depends on environment | Rendering instructions use a versioned Linux Chromium path; fonts are named but not bundled or loaded by the stylesheet. Instructions acknowledge substitutions. | Pin a renderer and package fonts/dependencies. Validate generated HTML and rendered PDFs. Do not treat a successful export alone as report acceptance. |
| Before method release | Version and research-reference drift | plugin.json is 1.3.1, while README incorrectly says it is 1.1.2 and multiple files say Methodology V1.0. geo-tracking marks its variance study unverified yet retains a precise 0.0003 claim later. | Separate package and method versions explicitly, then reference them consistently. Verify or remove unsupported research claims; do not use them to choose sampling depth. |

**Recommended first-sale architecture**

URL + email + authorization → confirmed one-time payment → durable job → bounded evidence collection → one named engine/panel → structured findings → skills draft the narrative → deterministic checks → owner review → private delivery.

Preserve the GEO skills as editable methodology and writing guidance. Put collection, durable state, arithmetic, validation and delivery controls in code. There is no demonstrated reason yet to rewrite the package for a different model provider. Anthropic documents filesystem skills in the Agent SDK, which provides a viable route to test reuse with the original ecosystem. Actual compatibility and reliability must be tested, not inferred from the existence of that route.

An upload to the Claude Skills API is a different deployment path: Anthropic says its skill code-execution containers have no network access. Live collection must be supplied through the surrounding tools/integrations or an external worker, rather than assumed to work from arbitrary network calls inside that container.

Official references checked:
- [Claude Agent SDK skills](https://code.claude.com/docs/en/agent-sdk/skills)
- [Claude Agent Skills overview and environment limits](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
- [MindLeverX requirements workbook](https://docs.google.com/spreadsheets/d/1UQ6t-KJyF7d91ap23n_If8NsFV9plRV_dNU1aZT2c5w/edit)

**The next proof to build**

Create one fixed-input audit-to-report test before implementing a storefront. Give it captured pages, engine responses, and an expected set of findings. Run it repeatedly in fresh sessions and require preserved evidence, consistent metrics, explicit unknowns, and a valid report. Include an unreachable site, an entity/address conflict, absent engine access, a malicious instruction embedded in page content, a duplicate job, and a provider timeout. Then run the same workflow on one authorized live target to measure real fulfillment time, model/tool cost, and review effort. Fixed-input tests evaluate pipeline repeatability; live-engine variability is a separate measurement problem.

For the first sale, retain owner review even after those tests pass. Expand automation only where observed failures and delivery volume justify it.
