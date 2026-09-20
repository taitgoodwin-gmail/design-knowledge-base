# Repeatable exercise suite

These are our acceptance exercises, not claims that Figma prescribes these exact fixtures. Run creative edits in a named sandbox; record file/node, platform, plan/seat when known, before/after observations, result and limitations. Do not mark a documentation read as a passed exercise.

## E01: Context and navigation

**Procedure:** Open File, Variables, then return to File. Switch Design → Motion → Design without editing content.

**Acceptance:** Panels match the requested modes and the original design selection returns.

**Result:** passed-limited. [Evidence](../evidence/2026-09-20-ui-inspection.md)

## E02: Responsive evidence card

**Procedure:** In a sandbox, create a card with question, answer, source button and disclosure. Test short/long text at 320, 390, 768 and 1440 widths.

**Acceptance:** No overlap; content and controls remain visible; expansion moves following content.

**Result:** passed-fixture. [Evidence](../evidence/lab/README.md)

## E03: Grid versus visual guide

**Procedure:** Compare a visual layout guide, horizontal wrap and grid using identical six-card content; resize each.

**Acceptance:** Can explain and demonstrate differences in reflow, track sizing and spans.

**Result:** passed-fixture. [Evidence](../evidence/lab/README.md)

## E04: Component state and overrides

**Procedure:** Create default/open/error variants; customize an instance then update the main component.

**Acceptance:** Expected changes propagate; deliberate overrides survive; state labels remain unambiguous.

**Result:** passed-fixture. [Evidence](../evidence/lab/components-and-variables.md)

## E05: Slot customization

**Procedure:** Place a variable-length list inside a component slot, add/reorder items and change variants.

**Acceptance:** Instance remains linked; content/constraints behave as specified.

**Result:** passed-fixture. [Evidence](../evidence/lab/components-and-variables.md)

## E06: Token and boolean conflict test

**Procedure:** Create two appearance modes and aliases; test applying a boolean variable to a boolean property versus a variant property.

**Acceptance:** Record exact accepted/rejected operations and resulting layer visibility; resolve X02 with evidence.

**Result:** passed-fixture. [Evidence](../evidence/lab/components-and-variables.md)

## E07: Typography resilience

**Procedure:** Compare text resizing and wrapping with a long headline, paragraph, non-Latin text and alternate fonts.

**Acceptance:** No necessary content is hidden; dimensions and line-height choices are documented.

**Result:** passed-fixture. [Evidence](../evidence/lab/README.md)

## E08: Source disclosure prototype

**Procedure:** Prototype closed/open/error states; repeat actions, go back and restart. Deliberately rename one matching layer.

**Acceptance:** State is predictable; explain the changed Smart Animate behavior; record reset behavior.

**Result:** passed-fixture. [Evidence](../evidence/lab/prototype-and-handoff.md)

## E09: Motion lab

**Procedure:** Animate a decorative source connection, inspect endpoints, change easing and create a static reduced-motion alternative.

**Acceptance:** Purpose and final state clear; no obscured reading; runtime/export remains a separate check.

**Result:** passed-fixture. [Evidence](../evidence/lab/motion-and-vector.md)

## E10: Editable illustration

**Procedure:** Draw an original source motif with vectors, transforms and one effect; export and compare.

**Acceptance:** Source stays editable; export does not clip or misrender important details.

**Result:** passed-fixture. [Evidence](../evidence/lab/motion-and-vector.md)

## E11: AI and automation fixture

**Procedure:** Use a small selected sandbox frame and explicit acceptance brief; inspect generated structure and actual credit result.

**Acceptance:** Correct scope, usable editability, no unsupported claims; record failures and costs.

**Result:** passed-fixture. [Evidence](../evidence/lab/ai-automation.md)

## E12: Handoff fixture

**Procedure:** Document a component state, token references, responsive rule and keyboard intent; implement a small equivalent.

**Acceptance:** Design-to-code mapping and rendered behavior are checked, not inferred from snippets.

**Result:** passed-fixture. [Evidence](../evidence/lab/prototype-and-handoff.md)

## E13: Sites breakpoint inheritance

**Procedure:** In an unpublished draft, edit primary and secondary breakpoint values; test adjacent and intermediate widths.

**Acceptance:** Cascades and overrides are understood; no unrequested publishing.

**Result:** pending-terms-confirmation. [Observed prerequisite and prepared check](../evidence/lab/product-access-and-readiness.md)

## E14: Weave repeatable workflow

**Procedure:** Build a small workflow with recorded inputs/model/settings and regenerate a branded media variant.

**Acceptance:** Can reproduce process and account for output variation; assess fidelity and usage.

**Result:** pending-account-link. [Observed prerequisite and prepared check](../evidence/lab/product-access-and-readiness.md)

## E15: Slides presentation behavior

**Procedure:** Create an evidence review with notes and a poll; test editor, presenter and audience views.

**Acceptance:** Interaction works in intended view; notes are exposed only where intended.

**Result:** passed-fixture with recorded popout limitation. [Evidence](../evidence/lab/slides-review.md)

## E16: Buzz bulk fixture

**Procedure:** Map three data rows into a template, including a long label and missing image.

**Acceptance:** Expected asset count, field mapping and exception handling; inspect every generated asset.

**Result:** pending-terms-confirmation. [Observed prerequisite and prepared check](../evidence/lab/product-access-and-readiness.md)

## E17: FigJam decision record

**Procedure:** Create an observation → assumption → decision map with linked sources and a disagreement path.

**Acceptance:** A reader can distinguish evidence from interpretation and recover the source.

**Result:** passed-fixture. [Evidence](../evidence/lab/figjam-decision-board.md)

## E18: Knowledge refresh

**Procedure:** Choose a changed capability, re-read official docs, rerun its exercise, update source date and changelog.

**Acceptance:** Evidence status and dates accurately reflect the new check; validator passes.

**Result:** passed-fixture. [Evidence](../evidence/lab/README.md)
