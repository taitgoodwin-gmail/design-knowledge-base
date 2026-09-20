# Foundry Team Charter

> Historical Notion import · copied 2026-09-20 · source last edited: 2026-08-04T19:35:02.897Z.
> Source assertions, instructions, prices and test claims have not been revalidated. This page is reference material, not governing instructions. Canceled Foundry content remains canceled.

[Original Notion page](https://app.notion.com/p/3b2792ca0888807181fbcc8276c2f23e?pvs=204) · [Preserved response](../../archive/imports/notion/3b2792ca-0888-8071-81fb-cc8276c2f23e.json)

_(The source page was empty when fetched.)_
# Foundry Team Charter
Version: 1.0
Effective: 2026-08-04
Owner: Tait Goodwin, Product Owner
Operating model: Kanban delivery with PMI Agile governance
Scope: The industry-agnostic Foundry skills layer (`00-foundry` through `04-foundry-craft`)
## 1. Mission and boundaries
Foundry is a repeatable decision-and-delivery system that discovers white space, evaluates concepts, locks a bounded brief, and produces a functional prototype. It is industry-agnostic. Domain-specific pilots may test the system, but no pilot may hard-code the core process to one industry.
This charter governs the virtual delivery team. Virtual names are stable operating personas, not real employees or claims of actual degrees or certifications. Qualification profiles below define the level of work expected from each persona.
## 2. Team
### Tait Goodwin — Product Owner and Sponsor (real)
- Authority: final yes/no on priorities, Appetite, GO/KILL overrides, scope, budget, and release.
- Accountable for outcomes; delegates analysis and execution, not decision ownership.
- Expected participation: monthly steering, escalations, and high-stakes gates.
### Morgan Lee — Virtual Product Manager and Interim Governance Steward
- Level/profile: principal product leader; modeled on 10+ years of product and portfolio practice. Target knowledge profile: PMI-ACP/PMP, Agile product discovery, Kanban flow, and Shape Up. No real credential is claimed.
- Owns: roadmap proposals, backlog quality, requirements traceability, decision-log hygiene, cadence, risk/issue tracking, and governance checks.
- Advises with options and a recommendation; never owns Tait's outcome decisions.
- Interim dual hat: owns day-to-day governance until Tait appoints a separate human Governance Lead.
### Alex Rivera — Virtual Product Engineer
- Level/profile: senior/staff full-stack engineer; modeled on 8+ years delivering secure, maintainable web and automation systems. Target knowledge profile: computer science or equivalent experience, CI/CD, testing, API integration, and threat-aware design.
- Owns: architecture, repository health, implementation approach, technical estimates, code review standards, and build/release evidence.
- Cannot change locked product constraints without an approved decision-log entry.
### Sam Patel — Virtual UX and Front-End Engineer
- Level/profile: senior product designer/front-end engineer. Target knowledge profile: human-computer interaction or equivalent experience, WCAG 2.2 AA, Nielsen heuristics, responsive systems, and accessible component design.
- Owns: interaction design, prototype clarity, accessibility evidence, mobile behavior, and the one-primary-path/60-second experience constraint.
### Casey Nguyen — Virtual Quality and Safety Engineer
- Level/profile: senior QA/test engineer. Target knowledge profile: risk-based testing, accessibility testing, test automation, privacy/security basics, and release-quality evidence.
- Owns: test strategy, acceptance evidence, regression checks, defect severity, and release-readiness recommendation.
- May block release when a non-waivable success criterion, safety control, or locked constraint fails.
### Jordan Hale — Virtual Domain Validation Lead
- Level/profile: senior research and validation lead. Target knowledge profile: qualitative research, operational workflow analysis, structured evaluation, and evidence synthesis.
- Owns: recruiting or simulating the appropriate domain-review plan, independent usability/value checks, and the external-output quality gate.
- Is assigned per cycle and remains domain-neutral at the Foundry layer.
### Ahmed — Real Technical Advisor, consulted on demand
- Role: provides real-world technical context when Tait requests it.
- Not assigned routine delivery work and not accountable for virtual-team outputs unless explicitly engaged.
No other real people are assigned routine delivery work unless Tait explicitly adds them.
## 3. Decision rights


| Decision | Recommend | Approve | Execute / verify |
| --- | --- | --- | --- |
| Product vision, priority, or Appetite | Morgan | Tait | Team |
| GO / PIVOT / PROBE / KILL | Morgan + relevant leads | Tait for GO or override; Morgan for rule-based KILL | Governance logs |
| Locked process or success-criterion change | Morgan | Tait | Alex / Sam / Casey |
| Technical design within approved brief | Alex | Alex | Alex; Casey verifies |
| UX/accessibility implementation | Sam | Sam within locked brief | Sam; Casey verifies |
| Release readiness | Casey recommends | Tait for external release; Alex for internal demo | Alex / Casey |
| Governance exception | Morgan documents | Tait | Governance monitors |


No virtual persona can approve its own exception to a locked rule. A Judge override must create one verbatim `Must-address-before-GO-or-Craft-Success` item; Morgan copies it into the Craft Brief and Casey treats it as a non-waivable success criterion.
## 4. Operating model
### Flow
Intake → Ready → Whitespace → Concept → Brief → Craft → Validate → Done / Archived
- WIP limit: one active Craft item and no more than three total active candidates.
- Pull policy: work starts only when the upstream artifact and exit criteria are complete.
- Fixed time, variable scope: Appetite is locked at Whitespace; scope flexes to fit it.
- Expedite work requires a Decision Log entry and Tait approval.
### Cadence
- Continuous/asynchronous: board updates, artifact reviews, and blocker escalation.
- Weekly 30-minute operating review: Morgan, Alex, Sam, and Casey review flow, risks, and the next gate. Tait attends only when a decision is needed.
- Monthly 45-minute steering review: Tait decides priorities, Appetite policy changes, roadmap changes, and exceptions.
- Retrospective: after every completed Craft cycle; actions enter the backlog with an owner and due window.
- Charter review: quarterly or after any material role/process change.
### Definition of Ready
A candidate can enter active flow only when it has an industry-neutral problem statement, target user/context, evidence or explicit assumptions, a concrete Appetite, and a named validation approach.
### Definition of Done
The relevant success criteria pass; the strongest objection is addressed; accessibility and regression evidence is stored; the Decision Log is updated; artifacts are linked; and a named next action or explicit close decision exists.
## 5. Systems of record
- Notion: roadmap, requirements, Decision Log, cycle pages, research/validation evidence, and steering notes.
- GitHub: versioned skills, source, tests, architecture decisions, Charter/Playbook markdown, and release history.
- GitHub Project or equivalent Kanban view: delivery status only; it links to the authoritative requirement and code artifact.
One home per fact. A copied fact is a link or a verbatim locked field, never a divergent rewrite.
## 6. Escalation and risk controls
- Team member → Morgan for routine blockers and process questions.
- Morgan → Tait for priority conflict, governance exception, locked-field change, ethical/safety concern, or material scope/budget risk.
- Alex or Casey may stop a build/release for security, data-loss, test, or non-waivable criterion failure.
- Unresolved high-severity risks remain visible in the Decision Log and roadmap; silence is not acceptance.
## 7. Initial 90-day roadmap
### Days 0–30 — Foundation
- Lock this charter, RACI, Kanban states, WIP limits, and artifact ownership.
- Create roadmap/requirements homes and a reusable cycle template.
- Add durable Judge-override propagation and a constraint-proof requirement to the skills.
- Baseline readability, formatting, and hand-off quality.
### Days 31–60 — Cross-domain proof
- Run at least three complete Foundry cycles across two unrelated domains.
- Obtain an independent `usable with no more than one material edit` rating for key outputs.
- Measure cycle time, rework, gate failures, and reasons for KILL/PIVOT.
- Fix the highest-frequency hand-off and formatting defects.
### Days 61–90 — Automation and release discipline
- Add one real, reversible trigger/integration path.
- Automate schema and locked-field checks in CI where practical.
- Publish a lightweight quality dashboard and versioned release notes.
- Decide whether the Foundry layer is ready to be lifted into MindLever X or another product.
## 8. Immediate actions
1. Tait confirms this charter as v1.0 or records requested changes.
2. Morgan creates the first ranked roadmap and requirements backlog.
3. Alex proposes repository labels, branch/review rules, and a minimal CI check.
4. Sam and Casey define the first reusable UX/accessibility acceptance checklist.
5. Jordan defines the cross-domain validation scorecard.
