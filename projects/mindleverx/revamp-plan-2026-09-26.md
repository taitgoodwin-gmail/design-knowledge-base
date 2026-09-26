# MindLeverX site revamp plan

Date: 26 September 2026. Status: proposed execution plan requested by the owner. The owner selected MindLeverX first, with learning from that work before doing more on the Augmind AI site. This authorizes planning; it does not claim the redesign is implemented, approved, or published.

Basis: [six winning Figma Makes study](../../learning/figma-make-winners-2026-09-26.md). Existing [design rationale](mindleverx-design-rationale.md) and [September 23 audit](audits/2026-09-23/report.md) are dated context. Recent local 25–26 September notes report later design revisions; reconcile them with the actual current file before editing. Preserve the separate unresolved Levarum naming exploration.

## Outcome

Make it easy for a visitor to understand the offer, experience how an AI answer can be examined against evidence, understand the limits of an example, and choose a relevant next step. Treat better comprehension and inquiry quality as hypotheses to test, not promised results.

The signature experience is a claim-to-source evidence explorer. It should demonstrate the service's reasoning in a small, understandable interaction. Other article features—3D, drawing, audio, AR—are options only if a real user task warrants them.

## Proposed site structure

| Area | Visitor question | Proposed content/behavior |
|---|---|---|
| Home | What is this, and why should I care? | Plain proposition, concise offer explanation, readable miniature evidence example, primary Explore an example action, and a secondary conversation path consistent with the approved offer. |
| Interactive example | What does examining an answer actually look like? | Fictional example initially; selectable claims; corresponding source excerpts; explicit supported/unresolved labels; explanation of limits; path to method and inquiry. |
| How it works | What would you do for us? | Verified service steps and deliverables, what information is needed, where human review happens, and limitations. Do not infer commitments from visual concepts. |
| Evidence/research content | Why should I trust this? | Only real, attributable research or clearly labeled illustrations. Preserve useful existing pages after inventory; do not invent client results or replace them with demo metrics. |
| Inquiry | What happens next? | Clear next step, minimum useful intake, explanation of follow-up, and an actual usable confirmation state once implemented. |

This is a proposed information structure, not an instruction to delete existing routes. Use the route/content inventory to map existing pages, retain useful content, and plan any eventual redirects.

## Delivery sequence and checkpoints

| Phase | Work | Concrete output | Completion evidence |
|---|---|---|---|
| 1 — Establish the baseline | Inspect current live routes and latest Figma frames; reconcile the September 23 audit with September 25–26 revisions; verify offer, audience, primary action, evidence, and implemented behavior. | Short current-state map; content inventory; explicit keep/change decisions; unresolved business questions. | Every proposed change points to the current page/frame or a recorded gap; no stale concept treated as current truth. |
| 2 — Shape the experience | Sketch Home → example → method → inquiry. Define claim/source relationships, statuses, navigation, and mobile layout before detailed polish. | One storyboard, a state map, and a bounded example dataset using approved fictional content. | All claims map to matching excerpts or explicit unresolved status. Labels distinguish illustration from measured findings. |
| 3 — Establish the visual system | Refine the first screen and evidence workspace together. Use the latest readable direction as a starting point; verify rather than resurrect rejected oversized/cobalt typography. Align type, spacing, buttons, cards, focus, and status labels. | Editable desktop/mobile key screens and a small shared component/token set. | Offer and action are readable; example content fits; colors are accompanied by status text; mobile is designed rather than merely shrunk. |
| 4 — Build the first working slice | Prototype the evidence explorer in Make using the approved design. Keep components/data separate, refine in small prompts, and preserve checkpoints. | Home → example → selected claim/source → unresolved claim → method → inquiry handoff. | Keyboard, touch, back/edit behavior, narrow layouts, and long text work. Every control has a defined purpose; simulated actions are labeled. |
| 5 — Learn and refine | Observe a small formative round with representative visitors. Ask them to explain the offer, find supporting evidence, identify an unresolved claim, and find the next step. Revise the largest misunderstandings first. | Observations, severity-ranked changes, prompt/version log, and a short learning memo. | Report what participants actually did and misunderstood; do not infer conversion lift from a small test. Recheck changed behaviors after fixes. |
| 6 — Extend and prepare delivery | Apply the successful pattern to remaining pages. Decide which interactions stay curated and which need real data. Review generated code and current platform documentation before choosing a production path. | Complete site design/prototype, implementation handoff, content/source ledger, route mapping, and release checklist with owners. | Verify real integrations separately; test complete inquiry flow, accessibility target, mobile behavior, performance, and affected search requirements before release. Record remaining gaps. |

These are dependency-ordered phases, not time or cost commitments. Resolve uncertainties during the phase where they matter. First review checkpoint: one complete homepage and evidence-explorer flow, not isolated decorative hero options or a whole untested site.

## Evidence explorer behavior

1. Show the question and a clearly labeled fictional answer immediately.
2. Selecting a claim opens its matching source excerpt without losing the surrounding answer.
3. Explain what the source supports; distinguish lack of evidence from a demonstrated falsehood.
4. Show an unresolved claim with a plain explanation of missing or inadequate support.
5. Let visitors switch claims, return to the full answer, and continue to the method.
6. Preserve source identifiers and honest provenance. A real observation should retain engine, question, date, collection method, and relevant conditions; a fictional record must not pretend those were measured.
7. Provide understandable initial, selected, unavailable/missing, and return states. Only add loading/retry/cancel states if actual asynchronous requests exist.

The first slice uses curated content. No fabricated live analysis, confidence percentage, spinning scanner, outcome promise, or auto-published recommendation. Missing evidence is not a positive checkmark. An attractive source explanation is not proof that the claim is correct.

## Design and engineering working rules

- Use a clear initial brief plus short refinement prompts; record what each change is intended to improve.
- Sketch ambiguous interactions; attach the actual intended frames rather than relying on broad style adjectives.
- Keep one coherent visual system and shared components. Show useful evidence as the main visual material.
- Preserve versions and revert when a failed approach becomes harder to reason about.
- Use the repository's WCAG 2.2 AA target proportionately; verify relevant criteria rather than claiming compliance from a screenshot or color check.
- Before production decisions, recheck official Figma, hosting, framework, data/API, and applicable Google Search guidance. Retain source URL, date, decision, and verification evidence.
- Keep the knowledge base as research/decision history; active implementation and backlog belong in the product repository.

## Learning handoff to Augmind

After the MindLeverX slice is tested, record which preparation, prompting, components, interactions, and checks helped—and which failed. Separate reusable methods from evidence-domain-specific design.

Then use those lessons to plan Augmind's opportunity configurator and Art of the Possible experience. Do not start a parallel Augmind rebuild or copy the MindLeverX evidence interface wholesale. The owner explicitly selected learning from MindLeverX before doing more on Augmind.

## Verification status

This document is a plan, not a fresh audit or product test. Article review and demo-inspection limits are retained in the linked study. No product implementation, external form submission, live integration, or website publication occurred as part of this planning task.
