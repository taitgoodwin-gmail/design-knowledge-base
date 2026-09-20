# Figma practice evidence — 20 September 2026

[Open the editable lab](https://www.figma.com/design/UgtCQvjyZpBQVOxhZAK4sk/MindLeverX?node-id=34-8). File `UgtCQvjyZpBQVOxhZAK4sk`, page `34:8`, editor `figma`. The lab is a separate page in the existing draft file. The observed tool could edit this file; the exact paid plan/seat is not established by that fact.

Each numbered JSON file contains the actual MCP response, including failures. PNGs are downloaded Figma renders, visually inspected during this run. Early records are API-and-render checks; E08/E12 add bounded presentation/browser and keyboard evidence. No full screen-reader, conversion or customer-outcome assurance is claimed. Scripts are in [the exercise scripts directory](../../exercises/scripts/README.md).

## E02 — responsive evidence card: passed in the recorded fixture

Node `35:8` was tested with short/long text, closed/open disclosure and widths 320, 390, 768 and 1440: 16 combinations. All recorded visible children stayed inside the padded card, with no overlap. Disclosure expansion moved following content by its height plus the 16px gap. The button stayed 48px tall. Editable long/open display copies are nodes `43:8`, `43:15`, `43:22`.

| Width | Long/closed height | Long/open height | Following-content movement |
|---|---:|---:|---:|
| 320 | 561 | 640 | 79 |
| 390 | 477 | 535 | 58 |
| 768 | 333 | 370 | 37 |
| 1440 | 249 | 286 | 37 |

The 1440px example deliberately tests an extreme container; its long reading lines are not a recommended production measure. The disclosure is toggled through the API here, not through an implemented prototype button. E08 covers actual prototype interaction separately.

Evidence: [320](02-e02-320.json), [390](02-e02-390.json), [768](02-e02-768.json), [1440](02-e02-1440.json). All four long/open renders were inspected: [320](e02-320-long-open.png), [390](e02-390-long-open.png), [768](e02-768-long-open.png), [1440](e02-1440-long-open.png).

## E03 — guide, wrap and grid: passed in the recorded fixture

Three frames used identical six-card content at 600, 390 and 840px. Wrap produced 3, 2 and 4 cards on the first row respectively. Grid retained three columns while their equal flexible widths changed to about 173.33, 103.33 and 253.33px. Grid child Fill was accepted in this API context. A later mixed-track example used a 120px first column, two 200px columns, and a 336px card spanning the first two columns plus the gap.

The stretch-guide control did not wrap. It repositioned constrained cards and allowed overlap/overflow at 390px; that is a diagnostic result, not a production layout pass. The lab was restored to a readable 600px width afterward. The span example intentionally places card 2 in a later row to demonstrate explicit cell placement, not a recommended reading order.

Evidence: [resize measurements](06-e03-resize.json), [fill result](05-e03-grid-fill.json), [track/span measurements](07-e03-span.json), [wrap render](e03-wrap.png), [grid render](e03-grid-span.png), [narrow guide diagnostic](e03-guide-390-control.png).

## E07 — typography resilience: passed in the recorded fixture

Node `39:8` contains a long headline, paragraph, Japanese text, and a long unbroken source identifier. Inter and Noto Sans were tested at 320, 390 and 768px; Japanese used Noto Sans JP throughout. All six geometry cases reported no missing font and no overlap or container-bound violations. The narrow Noto render visibly preserved all four samples.

The headline used 28px/140% line-height; paragraph 16px/150%; Japanese 16px/160%; identifier 14px/150%. These are fixture choices, not universal typography requirements. Auto-width made the headline 892px wide in a 320px frame. A fixed 272×39 box understated its required height; restoring auto-height yielded 272×156. That final layout was retained. This does not test every script, font, localization or browser font renderer.

Evidence: [font/width cases](09-e07-width-fonts.json), [resizing comparison](10-e07-resizing-modes.json), [render](e07-320-noto.png).

## E18 — knowledge refresh: passed in this bounded refresh

Refreshed the renamed layout-guide capability and its relationship to grid auto layout. After the first E03 measurements revealed position changes, read the official guide/constraint article and reran the comparison with a no-guide control. With left/top constraints, no-guide positions stayed 24/200/376; the stretch guide moved them to 24/130/306 at 390px. Updated the containers module, source records and changelog; validation result is recorded in this directory.

An attempted fixed-guide test supplied `sectionSize`, which the installed tool rejected as an unrecognized key even though local API typings list it. The failure is preserved in [11-e18-guide-refresh.json](11-e18-guide-refresh.json). The completed control run is [12-e18-guide-control.json](12-e18-guide-control.json). Fixed-guide creation through this route remains unverified.

## Official sources reviewed for this wave

Checked 2026-09-20. Review scope is the relevant article sections, not every linked page or video.

- [Auto layout](https://help.figma.com/hc/en-us/articles/360040451373-Guide-to-auto-layout): content-driven arrangements and parent/child sizing informed E02.
- [Grid flow](https://help.figma.com/hc/en-us/articles/31289469907863-Use-the-grid-auto-layout-flow): tracks, sizing and spans informed E03.
- [Text properties](https://help.figma.com/hc/en-us/articles/360039956634-Explore-text-properties): type controls and font-specific features informed E07.
- [Text dimensions](https://help.figma.com/hc/en-us/articles/27378154668951-Adjust-text-dimensions-and-resizing): resizing and font size are separate controls; tested their resulting bounds.
- [Guides with constraints](https://help.figma.com/hc/en-us/articles/360039957934-Combine-layout-guides-and-constraints): stretch guides make constraints relative to nearby tracks. Layout guides were renamed from layout grids in May 2025.

## Remaining work

E09 and E10 now have separate [motion and vector results](motion-and-vector.md), including a native MP4 export. Three exercises remain pending: E13, E14 and E16. E01 retains its earlier limited navigation evidence. The 183-article Design inventory establishes public API retrieval scope, not exhaustive capability knowledge or article review. [Whole-goal audit](../../../../evidence/full-goal-audit.md).

Saved-observation verification: [result](validation-observations.json). Repository integrity: [result](validation-integrity.json). [Latest live lab readback](28-final-lab-after-motion.json) contains 118 nodes; [original-page readback](17-original-page-check.json) matches the nine top-level node IDs and geometry observed before this wave. This comparison does not claim a byte-for-byte export of the entire Figma file.

Component-wave results: [E04/E05/E06](components-and-variables.md), with separate foundations and component pages and actual boolean-conflict resolution.

Prototype/handoff results: [E08/E12](prototype-and-handoff.md), with presentation navigation, reset caveats and a responsive keyboard-operable browser fixture.

FigJam result: [E17 decision board](figjam-decision-board.md), with evidence/assumption labels, linked sources and a disagreement/revisit path.

Slides result: [E15 review deck](slides-review.md), with native poll, presenter/audience note checks and explicit popout/export limitations.

AI result: [E11 scoped rewrite](ai-automation.md), with native-layer, content, layout/style and actual credit checks.
