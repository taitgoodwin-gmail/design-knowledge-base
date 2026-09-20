# MindLeverX homepage design benchmark evidence

Checked 2026-09-19. Scope: expert review of rendered homepage in connected Chrome; current viewport 1122 × 922, plus earlier desktop observations. No site edits. No mobile, dark-theme, full keyboard, screen-reader, form-submission or user-outcome test. No project docs/build-guidance.md or AGENTS.md found under current workspace. Standing official-source guidance read earlier in this thread.

## Observations and recommendations

1. Hero has large serif heading and a filled primary audit action beside a lower-emphasis scorecard link. Preserve relative emphasis; visual hierarchy and primary-action guidance support this judgment, not a measured conversion claim.
2. At viewport width 1122, main navigation and header audit action are hidden behind a hamburger. DOM exposes an Open menu accessible name. Consider a compact visible navigation with important destinations and a labeled overflow menu. This is an expert recommendation based on research, not an observed task failure.
3. Hero board displays engine names with 42%, 38%, 33%, 27% and deltas. No adjacent definition of those per-engine percentages, denominator, comparison period or delta units. Add metric name and measurement context; keep sample status. Contextual-help and recognition heuristic applies.
4. Method says Five moves, ranked by leverage; Off-site citations is fourth while described as the biggest lever. Resolve label/order inconsistency; do not invent a researched ranking.
5. Computed small caption color rgb(99,102,107), 12px, 400 weight, opacity 1. Sample note on white has calculated WCAG contrast 5.763869717053734:1; equivalent color on rgb(247,247,248) yields 5.383618800076339:1. These sampled pairs exceed 4.5:1. Larger important explanatory copy is a readability recommendation, not a WCAG font-size requirement. Not full accessibility conformance.
6. Ticker CSS scroll animation duration 38s. Pause sample ticker changes accessible name to Play sample ticker and computed animation-play-state to paused. Restored running state afterward. Consider static presentation of sample values because motion should serve user understanding. Pause behavior checked for ticker only; other animation/reduced-motion behavior not evaluated.

## Sources inspected (web retrieval on 2026-09-19)

- Nielsen Norman Group, 10 Usability Heuristics: https://www.nngroup.com/articles/ten-usability-heuristics/ — consistency, recognition, contextual information. Broad heuristics; site-specific recommendations are reviewer interpretations.
- Nielsen Norman Group, 5 Principles of Visual Design in UX: https://www.nngroup.com/articles/principles-visual-design/ — scale, hierarchy, balance, contrast, Gestalt.
- Nielsen Norman Group, Hamburger Menus and Hidden Navigation Hurt UX Metrics: https://www.nngroup.com/articles/hamburger-menus/ — hidden/visible navigation study, 2016; supports discoverability risk, does not measure this site.
- IBM Carbon button usage: https://carbondesignsystem.com/components/button/usage/ — principal action should have stronger emphasis than other actions. Applied as design-system guidance, not mandatory adoption of Carbon.
- IBM Carbon motion: https://carbondesignsystem.com/elements/motion/overview/ — purposeful, unobtrusive movement, static alternatives. Initial obsolete guidelines/motion URL failed; actual elements/motion source inspected successfully.
- W3C WCAG 2.2 Understanding SC 1.4.3: https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html — normal text 4.5:1, large text 3:1; computed foreground/background rather than screenshot anti-aliasing. Calculated via standard sRGB linearization and relative-luminance formula.
- W3C WCAG 2.2 Understanding SC 2.2.2: https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide.html — automatic moving/scrolling content longer than five seconds alongside other content requires pause/stop/hide unless essential. This record does not establish whole-page compliance.
- Design Council Double Diamond: https://www.designcouncil.org.uk/resources/the-double-diamond/ — discover with affected people, define problem, develop alternatives, test and improve at small scale. Proposed next step: target-user tasks asking who site is for, what an audit delivers, what scores mean, and where supporting evidence can be found; compare variants using completion and interpretation errors. This is proposed research, not performed testing.

The user invoked prompt-coach; its assessment exception permits direct discussion without a six-question coaching sequence. Core skill and verification module read. Optional audience-priority question sent; no answer received at time of this record. Review proceeds provisionally with prospective-client clarity while reporting audience-independent findings.
