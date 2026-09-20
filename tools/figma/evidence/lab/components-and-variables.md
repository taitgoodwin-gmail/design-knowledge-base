# Component, slot and variable exercises — 20 September 2026

[Open the component lab](https://www.figma.com/design/UgtCQvjyZpBQVOxhZAK4sk/MindLeverX?node-id=57-8) · [Foundations](https://www.figma.com/design/UgtCQvjyZpBQVOxhZAK4sk/MindLeverX?node-id=55-8) · [Final render](e04-e05-e06-final.png) · [Locked plan](../../exercises/component-lab-plan.md)

E04, E05 and E06 passed their bounded API-and-render fixtures. They do not establish prototype interaction, keyboard behavior, screen-reader behavior, browser implementation, plan-wide entitlement or production brand approval. All source labels are fictional. The current file accepted these edits; exact paid plan and seat remain unspecified.

## What was built

Two isolated collections contain 11 primitives and 8 semantic aliases. Semantics have Light/Dark modes, with scoped colors, spacing and radius, WEB code names, and one Inter Regular body style. Boolean scopes cannot be assigned through this API; their returned ALL_SCOPES is an observed exception, not a recommendation for other types. The two new pages contain 14 foundation descendants and 73 component descendants. The existing 118-node exercise page was not edited in this wave.

The family `57:32` has Default/Open/Error variants; `58:49` has True/False variants for the variable probe. The original imported collection still has 166 variables, and the nine original page-level nodes retain their recorded names and geometry. That comparison is bounded, not a byte-for-byte file comparison. [Readback](55-original-after-components.json).

## E04 — state and overrides

Customized instance `57:34` received its own question and a false Show source property. Control instance `57:41` kept defaults. Changing the family's question default updated the control while preserving the customized question. Updating the Default main component's explanatory text propagated to both Default instances. Other variants keep their own explanatory copy; changing one variant does not imply updating every variant.

The customized question and hidden source indicator survived Error → Default → Open. Instances remained linked to the appropriate main variants. [Before](43-e04-before-main-update.json), [after main update](44-e04-after-main-update.json), [state switches](46-e05-state-switches.json).

## E05 — native slot content

The Open instance received three source rows, reordered 3 → 1 → 2. Their measured heights were 24/48/72px with 12px gaps inside a 312×168px slot. The long row wrapped. The card measured 360×372px with the slot visible and 360×192px with it hidden. Content and order survived all three state switches; no detachment or slot-limit violation was observed. [Customization](45-e05-slot-customization.json), [switches](46-e05-state-switches.json), [render](e05-slot-open.png).

Slot item IDs changed as Figma remapped variant contents. Re-find the active slot and its descendants after switching states; do not reuse old instance-child IDs. Limits were set to 1–3 but exceeding them was not tested here.

## E06 — aliases, modes and the boolean conflict

| Route | Light: variable true | Dark: variable false | Result |
|---|---|---|---|
| BOOLEAN property on instance `58:21` | Indicator visible; height 204px | Indicator hidden; height 168px | Alias accepted and resolved correctly |
| VARIANT property on instance `58:50` | Main `58:35`, Visible=True, indicator visible | Main `58:42`, Visible=False, indicator hidden | Alias accepted and variant switched correctly |

Evidence: [boolean route](47-e06-boolean-binding.json), [variant route](52-e06-variant-binding.json), [appearance resolutions](35-component-foundations.json), [boolean Dark render](e06-boolean-dark.png), [variant Dark render](e06-variant-dark.png).

X02 is resolved **for this MCP/file context**: both routes work. The mode article still says boolean properties cannot receive boolean variables, while the component-property article describes assigning one as a default. Preserve that source discrepancy rather than presenting either sentence as universally authoritative. Coupling visibility to appearance modes is a diagnostic convenience; production features need their own state model.

## Verification and reproducibility

[Compact final audit](54-component-final-compact.json): nine component/instance roots, no visible-child overlap or bounds issues, no missing fonts, and all inspected component text fills token-bound. [Contrast calculation](56-component-contrast.json): six opaque text/background pairs all exceed 4.5:1; the lowest is Light accent at 5.707:1. This is not a full accessibility-conformance claim. The fixture's source labels are text, not implemented interactive controls.

Scripts in [the script directory](../../exercises/scripts/README.md) preserve actual operations and returned IDs. Creation scripts must not be rerun blindly. Inspect the current state ledger and reuse existing objects; for a new file, substitute IDs returned by each preceding step. The automated verifier checks saved observations and artifact hashes, not a fresh live Figma run.

Failures remain preserved: assigning boolean scopes, using zero instead of null for unset minHeight, referencing pre-combination property IDs, and assigning null instead of an empty property-reference object. `combineAsVariants` changed property suffixes; read the set's resulting definitions before further edits. Responses 29 and 53 were truncated; complete narrower responses 30 and 54 are authoritative for their stated scope.

## Sources checked

Relevant sections reviewed 2026-09-20; no exhaustive article/video review claimed.

- [Component properties](https://help.figma.com/hc/en-us/articles/5579474826519-Explore-component-properties): editable text/visibility controls and documentation of variable assignment.
- [Slots](https://help.figma.com/hc/en-us/articles/38231200344599-Use-slots-to-build-flexible-components-in-Figma): flexible nested instance content, settings and guidance limits.
- [Variable modes](https://help.figma.com/hc/en-us/articles/15343816063383-Modes-for-variables): inheritance, variant mapping and the conflicting boolean statement.
- [W3C contrast explanation](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html): normal text threshold and the contrast calculation basis.
