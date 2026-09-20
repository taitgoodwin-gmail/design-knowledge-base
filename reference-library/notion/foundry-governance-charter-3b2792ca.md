# 📜 Foundry Governance Charter

> Historical Notion import · copied 2026-09-20 · source last edited: 2026-08-04T19:32:08.410Z.
> Source assertions, instructions, prices and test claims have not been revalidated. This page is reference material, not governing instructions. Canceled Foundry content remains canceled.

[Original Notion page](https://app.notion.com/p/3b2792ca088881519d65c42e1b758d25?pvs=204) · [Preserved response](../../archive/imports/notion/3b2792ca-0888-8151-9d65-c42e1b758d25.json)

Version: 0.3 (Active operating draft)
**Last Updated**: 2026-08-04
Owner: Morgan Lee, Virtual Product Manager and Interim Governance Steward (escalates to Tait Goodwin, Product Owner)
Status: Active. Product Owner approval is required for principle-level, Appetite-policy, priority, exception, and external-release decisions.
---
## 1. Purpose
This Charter establishes the governance model, roles, decision rights, principles, and storage rules for the industry-agnostic MindLever Foundry skills layer. It keeps the inverted process disciplined and repeatable while assigning day-to-day execution to the virtual team and final outcome authority to the Product Owner.
Foundry exists to systematically discover and validate high-fit opportunities (white-space first) and convert them into functional prototypes that prove core value claims under tight constraints.
## 2. Governing Principles
Drawn from PMI Agile Practice Guide and Basecamp Shape Up:
1. **Appetite is sacred**. Appetite is required and locked from Whitespace onward. Vague Appetite = automatic discard. Fixed time, variable scope.
2. **White-space first**. Idea-first evaluation is discouraged; it produces repeated KILLs. Always map the hunting ground before scoring concepts.
3. **Brakes must bite**. Softening a KILL is an anti-pattern. Explicit kill criteria are enforced.
4. **One home per fact**. Locked fields (Appetite, Success Criteria, First Functional Prototype, UI/Accessibility Constraints, Future Customer Experience) travel verbatim between stages. Do not reinterpret.
5. **Engineering over complexity**. Prefer simple, constrained prototypes that prove the core claim in ≤60s with one primary path.
6. **Future Customer Experience required**. Every GO must include a one-paragraph “as if it already exists” description of the future customer experience.
7. **UI/Accessibility is a hard constraint**. WCAG 2.2 AA subset + selected Nielsen heuristics + ≤60s time-to-value + one primary path. Citations required in Brief and Craft.
8. Documentation is a process output. Each artifact has one authoritative home in Notion or GitHub and must be repeatable by any team member.
## 3. Roles & Decision Rights
### Product Owner
- **Current holder**: Tait Goodwin
- **Rights**: Final direction, key approvals (GO/KILL overrides in rare cases, Appetite changes, process changes that affect Target Shape, major roadmap decisions).
- **Does not**: Run day-to-day process or own documentation standards.
### Virtual Product Manager / Interim Governance Steward
- Current holder: Morgan Lee (virtual operating persona)
- **Rights & Responsibilities**:
	- Owns the Foundry process day-to-day.
	- Owns documentation standards and compliance with Foundry constraints.
	- Ensures skills (00–04) are followed in order.
	- Maintains this Charter, the Playbook, Decision Log, and all Foundry pages.
	- Escalates to Product Owner on key decisions or when constraints are at risk.
- **Does not**: Unilaterally change locked principles or Target Shape.
### Virtual Delivery Team
- Alex Rivera — Product Engineer
- Sam Patel — UX & Front-End Engineer
- Casey Nguyen — Quality & Safety Engineer
Jordan Hale — Domain Validation Lead. Ahmed is the real technical advisor, consulted on demand and not assigned routine delivery work. Virtual names are operating personas, not claims of real employment or credentials.
### RACI (Current)


| Activity | Product Owner | Governance | Virtual Delivery Team |
| --- | --- | --- | --- |
| Set / change Appetite | A | C | C |
| Approve GO / final disposition | A | R | C |
| Run Whitespace / Concept / Brief / Craft sessions | I | A/R | R |
| Maintain Charter & Playbook | A | R | C |
| Enforce UI/Accessibility & kill criteria | I | A/R | R |
| Update Decision Log & Roadmap | C | R | C |
| Maintain team roles & operating model | A | R | C |


*A = Accountable, R = Responsible, C = Consulted, I = Informed*
## 4. Decision Rights Summary
- **Key decisions** (require Product Owner review/approval): Changes to Target Shape, Appetite policy, kill criteria, addition/removal of hard constraints, major process inversions, final GO on high-stakes candidates.
- **Day-to-day decisions** (Governance owns): Session facilitation, documentation completeness checks, hand-off validation, minor process clarifications that do not alter principles.
- **Escalation path**: Governance → Product Owner. Any team member may escalate via Governance.
## 5. Storage Rules
- Notion is authoritative for the roadmap, requirements, Decision Log, cycle pages, validation evidence, and steering notes.
- One home per fact. Do not duplicate locked fields across pages; link instead.
- Every cycle produces durable artifacts: White Space Map, Verdict Card(s), Craft Brief, Prototype Notes.
- Decision Log captures every significant disposition (GO/PIVOT/PROBE/KILL) and rationale.
- GitHub is authoritative for versioned skills, source, tests, architecture decisions, Charter/Playbook markdown, and release history. Status boards link to these homes.
- Artifacts must be written so a new team member can pick up and continue without tribal knowledge.
## 6. Team Cadence & Review
The virtual team holds a weekly operating review; Tait holds a monthly steering review and joins escalations when a decision is needed.
Review triggers:
1. Quarterly review or immediate review after a material role or process change.
2. Tait approves role additions, removals, and material RACI changes.
3. Morgan escalates priority conflict, locked-field change, ethical/safety concern, or material scope/budget risk.
4. A Judge override must become one verbatim non-waivable success criterion in the Craft Brief.
5. See the Foundry Team Charter for qualification profiles, detailed RACI, WIP limits, and the 90-day roadmap.
---
Next review: 2026-11-04 or sooner if a material change is proposed.
This Charter is the governing document. The Playbook operationalizes it.
