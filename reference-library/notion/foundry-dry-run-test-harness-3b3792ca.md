# 🧪 Foundry Dry-Run Test Harness

> Historical Notion import · copied 2026-09-20 · source last edited: 2026-08-05T05:14:11.017Z.
> Source assertions, instructions, prices and test claims have not been revalidated. This page is reference material, not governing instructions. Canceled Foundry content remains canceled.

[Original Notion page](https://app.notion.com/p/3b3792ca088881b1a008c2573a270459?pvs=204) · [Preserved response](../../archive/imports/notion/3b3792ca-0888-81b1-a008-c2573a270459.json)

**Purpose**: Prove that the polished 00–04 skills produce a complete, correctly structured cycle under the locked rules.  
**Status**: Design complete. Brake-test suite → PASS. Happy-path dry-run executed 2026-08-05 → **PASS**. Phase 1 exit criteria met.  
**Owner**: Engineering + Interim Governance  
**Appetite**: One focused sitting (target ≤ 90 minutes total human + agent time)
---
## 1. Goal of the Dry-Run
Execute one synthetic end-to-end cycle and verify:
1. Order is enforced (no skipped steps).
2. Locked fields travel verbatim (Appetite, Success Criteria, Future Customer Experience, UI/A11y constraints).
3. Brakes bite (missing required fields cause a halt).
4. Output structures match the mandatory templates.
5. A new operator could follow the artifacts without tribal knowledge.
Success = all five checks pass and a complete set of artifacts is produced.
---
## 2. Synthetic Hunting Ground (Fixed Input)
**Hunting ground**:  
“Mid-market B2B SaaS and clinical practices that need faster, more reliable way to turn vague product ideas into constrained functional prototypes without losing governance discipline.”
This is deliberately close to Foundry’s own domain so the cycle feels realistic while remaining synthetic.
**Seed constraint**: Do **not** start with a pre-formed product idea. Begin only with the hunting ground above.
---
## 3. Execution Sequence


| Step | Skill | Required Input | Required Output | Max Attention |
| --- | --- | --- | --- | --- |
| 0 | 00-foundry | Hunting ground only | Routes to 01 | \< 2 min |
| 1 | 01-foundry-whitespace | Hunting ground | White Space Map + 1–2 recommended Candidates (with locked Appetite) | 10–12 min |
| 2 | 02-foundry-concept | Top candidate from Whitespace | Verdict Card (aim for GO or clean PIVOT) | \~10 min |
| 3 | 03-foundry-brief | GO / reframed PIVOT Verdict Card | Craft Brief (verbatim locks) | \< 5 min |
| 4 | 04-foundry-craft | Craft Brief (preferred) | Prototype Notes + (optional) minimal runnable sketch | ≤ 2 h or locked Appetite |


**Orchestrator rule**: Always invoke via `00-foundry` first. Do not call numbered skills directly unless testing a brake.
---
## 4. Validation Checklist (Pass / Fail)
### 4.1 Order & Brakes
- [ ] 00-foundry correctly detected blank state and routed to 01
- [ ] Attempting to jump to Concept/Brief/Craft without upstream artifact produces an explicit halt
- [ ] No skill re-interpreted a locked field
### 4.2 Whitespace (01)
- [ ] Output uses the exact WHITE SPACE MAP structure
- [ ] Every Opportunity Candidate has a **concrete Appetite** (not vague)
- [ ] Weak-fit or Appetite-less candidates are discarded with reason
- [ ] Evidence claims carry citations or clear sources
- [ ] Only top 1–2 candidates recommended for Concept
### 4.3 Concept (02)
- [ ] Output uses the exact VERDICT CARD structure (decision-first)
- [ ] Scoring legend shows hard cap at 9.0 and thresholds applied to capped score
- [ ] If disposition = GO or reframed PIVOT → **Future Customer Experience paragraph is present**
- [ ] Success Criteria are testable and concrete
- [ ] Appetite is locked and carried forward
- [ ] Judge override answered explicitly
- [ ] Soft KILL or soft GO is absent
### 4.4 Brief (03)
- [ ] Output uses the exact CRAFT BRIEF structure
- [ ] Success Criteria copied **verbatim** (no restatement)
- [ ] Appetite and Time box respect the upstream lock
- [ ] UI/Accessibility Constraints block is present and complete
- [ ] Forbidden list is present
### 4.5 Craft (04)
- [ ] Preferred input path (Craft Brief) was used, or fallback was explicitly noted
- [ ] Output uses the exact PROTOTYPE NOTES structure
- [ ] Success Criteria remain locked (not improved)
- [ ] UI/A11y check section completed
- [ ] Disposition is one of: Craft Success \| Craft Failed \| Needs Human Gate
- [ ] Time box / Appetite respected
### 4.6 Cycle-Level
- [ ] All artifacts can be read by a new team member without additional explanation
- [ ] Decision Log entry created for the cycle disposition
- [ ] Cycle page created under MindLever Foundry parent: `Cycle YYYY-MM-DD – Dry-Run Harness`
---
## 5. Expected Artifact Set (Minimum)
1. White Space Map (from 01)
2. Verdict Card (from 02)
3. Craft Brief (from 03)
4. Prototype Notes (from 04)
5. Decision Log entry
6. Cycle page linking the above
Optional but valuable: a minimal runnable sketch or screenshot if Craft produces one.
---
## 6. Pass / Fail Criteria for the Harness Itself


| Result | Definition |
| --- | --- |
| **Harness Pass** | All checklist items above are checked. No locked rule was violated. Artifacts are complete and correctly structured. |
| **Harness Partial** | Core cycle completed but 1–2 minor structural deviations exist (document them). |
| **Harness Fail** | Order broken, locked field re-interpreted, or required Future CX / Appetite / Success Criteria missing on a GO path. |


---
## 7. How to Record Results
1. Create Cycle page: `Cycle 2026-08-XX – Dry-Run Harness`
2. Paste or link each artifact in order.
3. Fill the Validation Checklist on that page (copy from section 4).
4. Log overall disposition in Decision Log.
5. Update Backlog item “Create one end-to-end dry-run cycle” → Done (or Partial with notes).
---
## 8. Brake Tests (Optional but Recommended)
After the happy-path cycle, deliberately probe the brakes:
- Call 02-foundry-concept with only a hunting ground (no White Space Map) → must halt.
- Feed a GO Verdict Card missing Future Customer Experience into 03 → must halt.
- Attempt to expand Success Criteria inside 04 → must be rejected / noted as anti-pattern.
Record brake-test results on the same Cycle page.
---
## 9. Exit Criteria for Phase 1
- Harness Pass (or documented Partial with no locked-rule violations)
- All P0 Backlog items closed
- Skills + harness ready to be handed to a new operator or lifted into a larger project
---
**Next action**: Execute the dry-run using this harness (start with `00-foundry` + the synthetic hunting ground above).
