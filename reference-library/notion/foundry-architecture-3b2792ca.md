# 🏗️ Foundry Architecture

> Historical Notion import · copied 2026-09-20 · source last edited: 2026-08-04T23:07:16.838Z.
> Source assertions, instructions, prices and test claims have not been revalidated. This page is reference material, not governing instructions. Canceled Foundry content remains canceled.

[Original Notion page](https://app.notion.com/p/3b2792ca0888810f92e1dc8eb3d2be6e?pvs=204) · [Preserved response](../../archive/imports/notion/3b2792ca-0888-810f-92e1-dc8eb3d2be6e.json)

**Status**: Living document – first version 2026-08-04  
**Owner**: Engineering (Alex Rivera) + Interim Governance (Morgan Lee)  
**Purpose**: Define the technical and process architecture of the Foundry skills layer so it is clear, repeatable, and ready to hand off into larger projects (e.g. MindLever X + Claude).
---
## 1. High-Level System View
Foundry is a **skills-based orchestration layer**, not a full product.  
It provides a disciplined, inverted (white-space first) process for discovering, evaluating, briefing, and prototyping opportunities under tight constraints.
```javascript
Hunting Ground / Domain
        ↓
00-foundry (Orchestrator)          ← single entry point
        ↓
01-foundry-whitespace              ← Appetite locked here
        ↓
02-foundry-concept                 ← GO / PIVOT / PROBE / KILL
        ↓ (GO only)
03-foundry-brief                   ← Craft Brief locked
        ↓
04-foundry-craft                   ← Functional prototype
```
---
## 2. Core Components


| Component | Responsibility | Authoritative Home |
| --- | --- | --- |
| **00-foundry** | Detect state, enforce order, halt on missing artifacts | Skill + GitHub |
| **01-foundry-whitespace** | Map white space → ranked Opportunity Candidates with locked Appetite | Skill + Cycle pages |
| **02-foundry-concept** | Score candidate → Verdict Card (explicit disposition) | Skill + Cycle pages |
| **03-foundry-brief** | Turn GO into ready-to-use Craft Brief | Skill + Cycle pages |
| **04-foundry-craft** | Produce constrained functional prototype | Skill + Prototype Notes |
| **Decision Log** | Single home for every significant disposition + rationale | Notion database |
| **Governance docs** | Charter, Playbook, Team Charter, Roadmap | Notion + GitHub mirrors |


---
## 3. Locked Fields (Travel Verbatim)
These fields are never reinterpreted once set:
- **Appetite** (locked in Whitespace)
- **Success Criteria** (locked on GO)
- **First Functional Prototype** description
- **UI / Accessibility Constraints** (WCAG 2.2 AA subset + selected Nielsen + ≤60s + one primary path)
- **Future Customer Experience** paragraph (required on every GO)
---
## 4. Data & Artifact Flow
1. Every cycle creates a child page under MindLever Foundry:  
	`Cycle YYYY-MM-DD – [Short Candidate Name]`
2. Artifacts produced: White Space Map → Verdict Card → Craft Brief → Prototype Notes
3. Every disposition is also written to the Decision Log (one home for history)
4. GitHub holds versioned skill source + governance markdown mirrors
---
## 5. External Integration Points (Future)
- **Claude / Claude Code / Claude Design**: Hand-off of Craft Briefs and prototypes. GitHub is the shared coordination surface.
- **GitHub**: Authoritative source for skill code, tests, and governance markdown.
- **Larger projects (MindLever X)**: Foundry is designed to be lifted as a complete, repeatable process unit.
---
## 6. Non-Goals (Current Scope)
- Full product UI / multi-tenant SaaS
- Persistent multi-user collaboration features beyond Notion + GitHub
- Automated scoring engines (human + skill judgment remains primary)
- Production deployment infrastructure
---
## 7. Open Architecture Questions
- Exact interface contract between 04-foundry-craft output and Claude hand-off
- How test harness / dry-run cycles will be stored and versioned
- Whether Requirements and Backlog become formal databases or linked views
---
**Next action**: Review with Engineering (Alex) and Interim Governance, then lock any open questions before Phase 1 skill polish begins.
