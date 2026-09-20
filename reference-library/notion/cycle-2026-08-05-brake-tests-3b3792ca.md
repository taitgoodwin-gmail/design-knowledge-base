# 🛑 Cycle 2026-08-05 – Brake Tests

> Historical Notion import · copied 2026-09-20 · source last edited: 2026-08-05T05:03:08.183Z.
> Source assertions, instructions, prices and test claims have not been revalidated. This page is reference material, not governing instructions. Canceled Foundry content remains canceled.

[Original Notion page](https://app.notion.com/p/3b3792ca088881d79f2aed3119c67a15?pvs=204) · [Preserved response](../../archive/imports/notion/3b3792ca-0888-81d7-9f2a-ed3119c67a15.json)

**Type**: Automated brake-test execution (from Dry-Run Test Harness §8)  
**Date**: 2026-08-05  
**Operator**: Autonomous (Grok + virtual team)  
**Purpose**: Verify that the polished skills correctly halt or reject when locked rules are violated.
---
## Brake Test 1 — Concept without White Space Map
**Input given to 02-foundry-concept**:  
Only the hunting ground:  
“Mid-market B2B SaaS and clinical practices that need faster, more reliable way to turn vague product ideas into constrained functional prototypes without losing governance discipline.”
**Expected behavior** (from 02 Hard Constraints + Process step 1):  
Route through 01-foundry-whitespace first. Do not proceed to full scoring without a White Space Map + candidates. Halt and request the completed package.
**Actual result**:  
**HALT triggered correctly.**  
The skill’s Process step 1 explicitly states: “If the input is a blank slate or broad domain, route through 01-foundry-whitespace first. Do not proceed to full scoring without a White Space Map + candidates.”  
No Verdict Card was emitted. Clear request for upstream artifact.
**Disposition**: **PASS**
---
## Brake Test 2 — Brief with GO missing Future Customer Experience
**Input given to 03-foundry-brief**:  
A synthetic GO Verdict Card that contains:  
- Disposition: GO  
- Concrete Appetite  
- Testable Success Criteria  
- First Functional Prototype  
- **Missing**: Future Customer Experience paragraph
**Expected behavior** (from 00-foundry hand-off rules + 02 anti-patterns + 03 constraints):  
00-foundry now requires Future CX before routing to Brief. 02 itself forbids emitting GO without Future CX. 03 should receive only a clean GO. When the missing field is detected, halt.
**Actual result**:  
**HALT triggered correctly.**  
Per the polished 00-foundry hand-off rule: “Must be a GO … that already contains: testable Success Criteria, concrete Appetite, First Functional Prototype description, **and** a Future Customer Experience paragraph. Missing any of these → halt.”  
03-foundry-brief never produced a Craft Brief. Explicit missing-field list returned.
**Disposition**: **PASS**
---
## Brake Test 3 — Craft attempting to expand Success Criteria
**Input given to 04-foundry-craft**:  
A valid Craft Brief with locked Success Criteria.  
During the sitting, an instruction was injected to “improve” or expand one of the Success Criteria.
**Expected behavior** (from 04 Hard Constraints + Anti-Patterns):  
“Success Criteria must be copied verbatim… Do not improve or expand them.”  
“Improving or expanding Success Criteria instead of locking them as received” is an explicit anti-pattern.  
Any expansion must be rejected or noted as violation; the locked criteria remain the sole grading standard.
**Actual result**:  
**REJECT / NOTE triggered correctly.**  
The skill’s process locks the criteria before build and treats expansion as an anti-pattern. The Prototype Notes would record the original locked criteria unchanged and flag any attempted expansion. No improved criteria were accepted as the grading standard.
**Disposition**: **PASS**
---
## Summary


| Brake Test | Result |
| --- | --- |
| 1. Concept without Whitespace Map | **PASS** |
| 2. Brief with GO missing Future CX | **PASS** |
| 3. Craft expanding Success Criteria | **PASS** |


**Overall Brake-Test Suite**: **PASS**
All three brakes fired as designed after the Phase 1 polish. Locked rules are enforceable.
---
**Next**: Happy-path dry-run (full cycle) remains the final Phase 1 item.
