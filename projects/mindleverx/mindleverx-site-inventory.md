# MindLeverX — Figma import inventory

Checked: 20 September 2026.

**Seven publicly linked routes have 14 editable baseline frames together on [LIVE SITE / Seven pages / Desktop + mobile](https://www.figma.com/design/UgtCQvjyZpBQVOxhZAK4sk/?node-id=82-8).** Six routes were added in this continuation. The second, non-auto-layout homepage import was copied into this page; the original Page 1 and its concepts/imports remain intact.

| Page | Live source | Desktop frame (1440px) | Mobile frame (390px) |
|---|---|---|---|
| Home | [Home](https://mindleverx.com/) | [85:9](https://www.figma.com/design/UgtCQvjyZpBQVOxhZAK4sk/?node-id=85-9) | [85:280](https://www.figma.com/design/UgtCQvjyZpBQVOxhZAK4sk/?node-id=85-280) |
| Method | [Method](https://mindleverx.com/method.html) | [81:12](https://www.figma.com/design/UgtCQvjyZpBQVOxhZAK4sk/?node-id=81-12) | [81:124](https://www.figma.com/design/UgtCQvjyZpBQVOxhZAK4sk/?node-id=81-124) |
| GEO | [GEO](https://mindleverx.com/what-is-geo.html) | [81:220](https://www.figma.com/design/UgtCQvjyZpBQVOxhZAK4sk/?node-id=81-220) | [81:576](https://www.figma.com/design/UgtCQvjyZpBQVOxhZAK4sk/?node-id=81-576) |
| Research | [Research](https://mindleverx.com/research-hub.html) | [81:882](https://www.figma.com/design/UgtCQvjyZpBQVOxhZAK4sk/?node-id=81-882) | [81:1034](https://www.figma.com/design/UgtCQvjyZpBQVOxhZAK4sk/?node-id=81-1034) |
| Case Study | [Case Study](https://mindleverx.com/case-study.html) | [81:1165](https://www.figma.com/design/UgtCQvjyZpBQVOxhZAK4sk/?node-id=81-1165) | [81:1563](https://www.figma.com/design/UgtCQvjyZpBQVOxhZAK4sk/?node-id=81-1563) |
| About | [About](https://mindleverx.com/about.html) | [81:1954](https://www.figma.com/design/UgtCQvjyZpBQVOxhZAK4sk/?node-id=81-1954) | [81:2197](https://www.figma.com/design/UgtCQvjyZpBQVOxhZAK4sk/?node-id=81-2197) |
| Sample Index | [Sample Index](https://mindleverx.com/answer-engine-index-q3-2026.html) | [81:2427](https://www.figma.com/design/UgtCQvjyZpBQVOxhZAK4sk/?node-id=81-2427) | [81:2612](https://www.figma.com/design/UgtCQvjyZpBQVOxhZAK4sk/?node-id=81-2612) |

## What was verified

- All fourteen frames have native text and layout layers: 1,850 text nodes in total, zero missing-font flags.
- Native headings, main content and copyright/footer were checked across all seven routes at both widths against fresh live Chrome reads. Main-region heights differed by less than four pixels in this bounded comparison; that is not a pixel-perfect comparison.
- The Method page received live desktop/mobile screenshot and native full-page render inspection: its seven stages and footer are present.
- Each new plugin import reported completion and no missing fonts. Auto-layout was disabled to preserve source positioning; hyperlinks were enabled. No purchase or upgrade was made.
- Sections have route names and separate non-overlapping canvas positions. The copied homepage is first spatially; its source capture was at 02:22 GMT-4 and its headings were rechecked against the current live homepage.

Machine-readable IDs, geometry, font counts, source comparison and limitations are in the [import audit](figma-import-audit-2026-09-20.json).

## Known representation limits

The animated sample ticker imports as a taller static wrapped block, adding approximately 44px on desktop and 165px on mobile before the main content. It does not preserve scrolling or its Pause behavior. The native screenshot exporter also included an off-canvas skip-link region. These captures are editable source baselines, not exact browser emulations.

The mobile navigation was opened on the live sample-index page: Services, Method, Example scorecard, What is GEO, Research, Audit availability and a dark-theme control. The baselines show the closed menu. Alternate dark themes, expanded menu states, ticker/topic explanations and all expanded FAQ combinations have not been captured as separate frames. The GEO page has five FAQs; its default first-open state was observed. These missing interaction states are explicitly tracked, not implied to be included by the fourteen-frame count.

Services, scorecard, engagement options and audit availability are homepage sections. Contact is part of About; `/index.html` is the homepage. The inventory covers discovered public linked routes, not undiscovered, unlinked or authenticated content. Working links, prototypes and production behavior require separate verification.

## Historical correction

An earlier maintained note said no pages had been imported and that the plugin awaited permission. That was stale: two homepage imports already existed. The first used auto-layout and showed footer displacement; the second disabled auto-layout. The current inventory replaces that stale status using observed file contents and the six completed new captures. Earlier archived research remains unchanged.
