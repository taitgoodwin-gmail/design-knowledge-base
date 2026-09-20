# E15 — Slides editor, presenter and audience fixture

Checked 20 September 2026. **Passed in the bounded fixture; popout navigation limitation retained.** [Open the editable three-slide deck](https://www.figma.com/slides/8O9jPYugwpM8pt4OEJRi40?node-id=3-2). New draft, single returned team, reported Professional/Full seat.

## Design and construction

The deck reviews evidence, not marketing outcomes. A cobalt opening, ivory measured baseline and dark practice-poll slide use one bracket/line motif. Manrope ExtraBold titles contrast with readable Inter body text. Theme colors and type styles were deliberately updated. The three spatial compositions serve statement, measurement and decision respectively; no animation is needed to interpret the evidence.

The [construction script](../../exercises/scripts/e15-build-review.js) creates native editable text and shapes with append-before-position helpers. Speaker notes contain an explicit `E15-NOTE-ONLY` test marker. The poll was added through the editor's Live interaction control because the Plugin API cannot create it. Design mode X/Y fields positioned it at 1050,300, size 720×402. [Final audit](84-slides-final-audit.json) verifies three 1920×1080 slides, notes, one native POLL, no missing fonts, text/interaction overlap or bounds errors. Editor normalized slide names to their ordinal numbers; stable IDs remain the references.

## Actual behavior checked

| View | Observed result |
|---|---|
| Editor | Notes visible; poll question/options editable. Voting controls were not presented. After the live vote, the result persisted as 100% and “You voted.” |
| Presenter | Notes marker visible; audience vote synchronized. Previous moved to slide two and Restart to slide one after closing the popout. |
| Audience | Poll visible and usable; one synthetic vote for Assistive technology changed the result to 100%. The notes marker/block was absent from the visible tree and screenshot. |

[Browser observations](e15-browser-observations.json) record the same-account test and its limits. Initial automatic popout was blocked; explicitly clicking Open audience view worked without a settings change. With that popout open, a presenter Previous action briefly changed the URL then reverted. Do not certify cross-window navigation from this run. The native slide PNG omitted the poll; visual verification therefore used the actual audience view. No real stakeholder feedback, independent viewer-account permission test or accessibility conformance is claimed.

## Official guidance and interpretation

Relevant sections checked 20 September 2026:

- [Slides overview](https://help.figma.com/hc/en-us/articles/24170630629911-Explore-Figma-Slides): editor modes and review context.
- [Live interactions](https://help.figma.com/hc/en-us/articles/24246820870807-Add-live-interactions-to-slides): interactions operate in presentation views, require an authenticated viewer with access, and retain results.
- [Presenter notes](https://help.figma.com/hc/en-us/articles/24245848829847-Add-and-view-presenter-notes): notes and audience use separate views. **Anyone with can-view access can open presenter view.** Hidden from the audience screen does not mean confidential from file viewers.

Our practice: put evidence caveats in notes, keep sensitive information outside a shared deck, and verify the actual audience surface. The latter is an implementation choice, not a claim that every export preserves live widgets.

## Repeat

Create a new Slides draft; inspect its empty grid/theme; adapt the saved construction script; add the native poll through Live interaction → Poll; set fields and position in Design mode. Compare notes in editor/Presenter with audience output; cast a clearly labeled test vote and verify retention. Record popout, permission and export limits beside results. Never substitute a static mock poll for the native interaction.
