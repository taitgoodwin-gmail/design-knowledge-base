# 📘 Foundry Governance Playbook

> Historical Notion import · copied 2026-09-20 · source last edited: 2026-08-04T19:30:01.483Z.
> Source assertions, instructions, prices and test claims have not been revalidated. This page is reference material, not governing instructions. Canceled Foundry content remains canceled.

[Original Notion page](https://app.notion.com/p/3b2792ca088881488e15df03248b69ac?pvs=204) · [Preserved response](../../archive/imports/notion/3b2792ca-0888-8148-8e15-df03248b69ac.json)

Version: 0.3
**Companion to**: Foundry Governance Charter
**Purpose**: Make the inverted Foundry process fully repeatable by any team member. This is the operational manual.
---
## 1. Entry Point (Always)
Use the `00-foundry` orchestrator skill as the single entry point for any full cycle or continuation.
It will:
- Detect current artifact state
- Route to the correct next skill (01 → 02 → 03 → 04)
- Halt with precise missing requirements if brakes must bite
- Enforce locked-field hand-offs
Never start mid-pipeline without a valid upstream artifact.
## 2. Stage-by-Stage Operating Procedures
### 01 – Whitespace (Hunting Ground → Opportunity Candidates)
**Input**: Domain / segment / blank slate or prior White Space Map.
**Output**: White Space Map + ranked Opportunity Candidates that already fit Target Shape.
**Must include for every candidate**:
- Gap(s) identified
- Core mechanism
- Target Shape rationale
- First Functional Prototype sketch
- **Concrete Appetite** (locked from this point)
**Rules**:
- Appetite required and locked. Vague = discard.
- Prefer candidates that already fit Target Shape over idea-first invention.
- Document the map under the current cycle’s page in Notion.
### 02 – Concept (Candidate → Verdict Card)
**Input**: Opportunity Candidate from Whitespace (with Appetite).
**Output**: Verdict Card with disposition: GO / PIVOT / PROBE / KILL.
**Required on every GO**:
- Numeric scoring + Fit to Target Shape assessment
- Adversarial judgment
- **Future Customer Experience** paragraph (“as if it already exists”)
- Locked Success Criteria (verbatim)
- First Functional Prototype description
- Appetite (unchanged)
**Kill criteria**: Explicit. Softening a KILL is forbidden. Log the kill reason in Decision Log.
**Hand-off**: Only GO (or tightly reframed PIVOT with testable Success Criteria) proceeds to Brief.
### 03 – Brief (GO → Craft Brief)
**Input**: Valid GO Verdict Card.
**Output**: Craft Brief that locks:
- Success Criteria (verbatim)
- First Functional Prototype
- Appetite
- UI/Accessibility Constraints (WCAG 2.2 AA subset + selected Nielsen heuristics + ≤60s + one primary path)
- Forbidden list
- Time box
**Rules**: Citations required for UI/Accessibility choices. Brief must be ready-to-use so a Craft sitting can start immediately.
### 04 – Craft (Brief → Functional Prototype)
**Input**: Valid Craft Brief.
**Output**: Working prototype that proves the core value claim + Prototype Notes.
**Hard constraints**:
- ≤60s to value
- One primary path
- UI/Accessibility compliance as locked
- Prove the claim; do not expand scope
Document outcome (Success / Fail + learnings) under the cycle page and Decision Log.
## 3. Locked Fields That Travel Between Stages
These must pass verbatim and never be re-interpreted:


| Field | Locked From | Travels To |
| --- | --- | --- |
| Appetite | Whitespace | Concept → Brief → Craft |
| Success Criteria | Concept (GO) | Brief → Craft |
| First Functional Prototype | Concept / Brief | Craft |
| UI/Accessibility Constraints | Brief | Craft |
| Future Customer Experience | Concept (GO only) | Brief / Craft notes |


## 4. Cycle Documentation Template
For every Foundry cycle create a child page under MindLever Foundry named:
`Cycle YYYY-MM-DD – [Short Candidate Name]`
Contents:
1. Link to White Space Map / Candidate
2. Verdict Card (full)
3. Craft Brief (if GO)
4. Prototype Notes + link/demo
5. Decision Log entry (disposition + rationale)
6. Next action
## 5. Decision Log Protocol
Every significant disposition is logged in the live Decision Log database under MindLever Foundry:
<mention-page url="https://app.notion.com/p/860160b38a3c4dccb5b62a7643ccb480"/>
**Current schema (as of 2026-08-04)**:
- **Decision** (title) – short name of the decision or candidate
- **Date**
- **Disposition** – GO / PIVOT / PROBE / KILL / Other
- **Rationale** – key rationale (especially explicit kill reasons)
- **Owner** (person)
- **Related Artifacts** – links or references to White Space Map, Verdict Card, Craft Brief, Prototype, etc.
- **Tags** – Process, Roles, Target Shape, Appetite, UI/A11y, Cycle, Governance
- **Appetite** – the locked Appetite in force for that decision
- **Status** – Not started / In progress / Done / Archived (transitional)
Protocol:
1. Create a new row for every significant disposition or process decision.
2. Fill Disposition + Rationale + Appetite at minimum for cycle decisions.
3. Link Related Artifacts so the full chain is one click away.
4. Softening a KILL is forbidden; the Rationale must state the explicit kill criterion that was met.
This database is the single home for decision history.
## 6. Team Operation & Role Evolution
- Virtual team: Morgan Lee (Virtual Product Manager and Interim Governance Steward), Alex Rivera (Product Engineer), Sam Patel (UX/Front-End), Casey Nguyen (Quality/Safety), and Jordan Hale (Domain Validation). Ahmed is a real technical advisor consulted on demand.
- Morgan maintains the RACI and proposes updates; Tait approves all material role changes.
- Product Owner approves final role definitions.
- Update this Playbook and Charter after each material change.
## 7. Cadence Recommendations (Initial)
- The virtual team holds a weekly operating review for flow, blockers, risks, and the next gate.
- Tait holds a monthly steering review for priorities, roadmap changes, Appetite policy, and exceptions; escalations occur as needed.
- Review the Charter and Playbook quarterly, after a material role/process change, or after significant cycle evidence.
## 8. Anti-Patterns (Never Do)
- Softening a KILL
- Starting Concept without a White Space Map + Appetite
- Changing locked Success Criteria or Appetite mid-stream
- Expanding Craft beyond the Brief
- Storing process knowledge only in chat or personal notes
- Skipping the orchestrator for “speed”
---
**This Playbook is the how. The Charter is the why and who.**
Both must stay current. Governance owns currency; Product Owner owns direction.
