# Google Lighthouse research for MindLeverX

Checked: 2026-09-23. Research only; no website audit was run and no code or Figma design was changed.

## Findings and source record

| Source checked | Documented finding |
| --- | --- |
| [Lighthouse overview](https://developer.chrome.com/docs/lighthouse/overview) | Open-source page auditing tool. Available through DevTools, CLI, Node, and PageSpeed Insights. Supports authenticated-page testing through appropriate local workflows. |
| [DevTools Lighthouse guide](https://developer.chrome.com/docs/devtools/lighthouse) | Standard categories: Performance, Accessibility, Best Practices, SEO. Navigation, Timespan, and Snapshot modes serve different testing needs. Google recommends the Performance panel for detailed performance debugging. |
| [Performance scoring](https://developer.chrome.com/docs/lighthouse/performance/performance-scoring) | Scores depend on measured metrics and test conditions. 90–100 is the good range; 100 is not expected. Hardware, network, and extensions can change results. |
| [Accessibility scoring](https://developer.chrome.com/docs/lighthouse/accessibility/scoring) | Automated audits contribute to the score; manual audits do not. A perfect score cannot establish full accessibility conformance. |
| [PageSpeed Insights](https://developers.google.com/speed/docs/insights/v5/about) | Combines Lighthouse lab diagnostics with available CrUX field data from a trailing 28-day period. Low-traffic pages or origins may have insufficient field data. |
| [Lighthouse CI](https://github.com/GoogleChrome/lighthouse-ci/blob/main/docs/getting-started.md) | Can collect reports on commits, compare results, and enforce selected assertions. Documentation advises gradual adoption. |
| [Agentic browsing audits](https://developer.chrome.com/docs/lighthouse/agentic-browsing/scoring) | Experimental category based on proposed standards. Documentation specifies Chrome 150+; WebMCP audits require origin-trial registration. Uses audit pass ratios, not a conventional weighted 0–100 score. |

## Recommended MindLeverX use — implementation choices

1. Establish mobile and desktop baselines for the seven implemented public pages. Audit production builds or deployed pages, not the Figma editor or prototype.
2. Use consistent Lighthouse/Chrome versions, device and network settings, and multiple runs. Preserve HTML/JSON reports, timestamp, tested URL, commit identifier, and environment details.
3. Prioritize concrete failures and user impact. A 90+ performance target is reasonable, but avoid a blanket 100 requirement. Combine automated accessibility checks with keyboard, focus, screen-reader, zoom, and content reviews.
4. Compare lab results with real-user Core Web Vitals when field data exists. Missing field data remains “unavailable”; do not substitute a Lighthouse score for it.
5. Add Lighthouse CI after a stable baseline is understood. Begin by collecting reports, then introduce specific regression checks. Store private application reports in an appropriate private location.
6. Consider experimental agentic audits separately after confirming tool availability. They could inform interface usability for agents; they do not establish ChatGPT recommendation visibility or validate a GEO outcome claim.

## Limits and unresolved questions

- Lighthouse evaluates running web pages. It cannot score the unimplemented MindLeverX design as a website.
- Actual MindLeverX results, exact release thresholds, and CI integration have not been measured or implemented in this research task.
- The current CLI README lists the four standard categories, while Chrome documentation also describes experimental agentic audits. Verify the installed version and supported configuration before relying on that category.
- Search ranking, business outcomes, and AI answer inclusion require their own evidence; do not present Lighthouse results as proof of those outcomes.
