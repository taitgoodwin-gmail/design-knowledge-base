# Component lab plan — 20 September 2026

Run `component-lab-20260920`. Scope E04/E05/E06, in the existing private draft file. This is a teaching fixture, not an approved MindLeverX brand system or a production replacement.

## Discovery and reuse

No active application token source exists under tools/figma. The existing imported site has 166 variables, 51 text styles and no local components across the two observed pages. Its variables remain unchanged. Compact discovery is saved in the lab evidence directory; the initial larger result was truncated and is not a complete inventory.

get_libraries reported eight subscribed community libraries and no additional page. Evidence-card search scoped to Simple Design System and Material 3 returned general cards, including Card (Slot); no match was established for the exact state/property contract. The exercise requires editable local main components to verify propagation and overrides, so create a separate lab family instead of modifying remote community masters.

## Locked fixture scope

- Lab primitives, one Value mode: paper #F7F7FC, ink #11142B, blue #2448FF, blue-light #A8B7FF, error #A52639, error-light #FFADBB; padding 24, gap 12, radius 16, true, false. Eleven primitives, intentionally hidden from property pickers where supported.
- Lab semantics, Light/Dark modes: surface, text, accent, error, padding, gap, radius, show-source. Eight variables; values alias primitives. Appearance colors switch by mode; spacing stays constant; show-source true in Light, false in Dark for the diagnostic, not a production coupling.
- CSS syntax uses var(--lab-...). Boolean CSS names are descriptive mapping metadata, not a claim that CSS custom properties implement component booleans.
- Text style LAB / Body, Inter Regular 16 / 150%; no shadow style needed for this exercise.
- Local Evidence card family: State=Default/Open/Error; editable title; optional source indicator; variable-length source content slot.
- Boolean variant probe: Visible=True/False, used only to compare BOOLEAN-property and VARIANT-property bindings.
- Preserve original page and current lab. Add focused documentation and component pages, with a cover/getting-started/foundations/components/utilities organization through named sections rather than empty separator pages; this is a bounded lab extension, not a full product library.

## Acceptance

E04: customize an instance, update the main, compare unchanged and overridden fields, then change variants. E05: add/reorder variable-length slot content and change variants while preserving the instance link. E06: record exact BOOLEAN and VARIANT binding acceptance/rejection, resulting visibility and both appearance modes. Preserve failures, actual IDs, source dates and screenshots. Do not equate API acceptance with UI entitlement or deployed application behavior.
