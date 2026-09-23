# Lighthouse and Google web quality source register

Checked: **23 September 2026**. Original summaries and selected source review; no claim of crawling all Google documentation or exercising all features.

Lighthouse implementation pinned to 13.5.0, commit `cb853a38a6410617518b363590c967b3fe211949`. Web documentation was checked on the date above; pages on moving branches can change. Recheck before consequential implementation or publication.

| Source ID | Source | Status | Reviewed scope and implication |
| --- | --- | --- | --- |
| REF-6ebd51fc204d | [Lighthouse overview](https://developer.chrome.com/docs/lighthouse/overview) | Reviewed documentation | Available collection paths and page-audit scope |
| REF-26bf3bacc401 | [DevTools Lighthouse](https://developer.chrome.com/docs/devtools/lighthouse) | Reviewed documentation | Modes and performance-debugging workflow |
| REF-d0ebf6fbc20d | [Performance scoring](https://developer.chrome.com/docs/lighthouse/performance/performance-scoring) | Reviewed documentation | Score interpretation and variability |
| REF-9207a20ae1aa | [Accessibility scoring](https://developer.chrome.com/docs/lighthouse/accessibility/scoring) | Reviewed documentation | Weighted automated checks; manual review separate |
| REF-5ef9b113fd32 | [Agentic browsing scoring](https://developer.chrome.com/docs/lighthouse/agentic-browsing/scoring) | Reviewed documentation | Experimental status and prerequisites; runtime availability untested |
| REF-9e01f0ace364 | [PSI interpretation](https://developers.google.com/speed/docs/insights/v5/about) | Reviewed documentation | Lab versus field, thresholds, missing data and assessment |
| REF-5bea86da45f8 | [PSI API guide](https://developers.google.com/speed/docs/insights/v5/get-started) | Reviewed documentation | Planned removal of bundled CrUX; use separate adapter |
| REF-2b7961629c90 | [PSI API reference](https://developers.google.com/speed/docs/insights/v5/reference/pagespeedapi/runpagespeed) | Reviewed documentation | Desktop/performance defaults; explicitly request categories and device |
| REF-c4356c56a04d | [CrUX API](https://developer.chrome.com/docs/crux/api) | Reviewed documentation | URL/origin query, metrics, period, quota; no live API request |
| REF-ad4709d3a749 | [CrUX History API](https://developer.chrome.com/docs/crux/history-api) | Reviewed documentation | Up to 40 overlapping periods and missing values |
| REF-35f5625620db | [CrUX methodology](https://developer.chrome.com/docs/crux/methodology) | Reviewed documentation | Eligibility, sample coverage, URL normalization and attribution |
| REF-74bf827a2002 | [CrUX BigQuery](https://developer.chrome.com/docs/crux/bigquery) | Reviewed documentation | Monthly history and optional broader benchmarking |
| REF-35ef629bf731 | [CrUX Vis](https://developer.chrome.com/docs/crux/vis) | Reviewed documentation | Existing historical dashboard and scope limits |
| REF-93d5c4474009 | [Web Vitals library](https://github.com/GoogleChrome/web-vitals) | Reviewed documentation | RUM and attribution option; not installed |
| REF-62c18319cdd3 | [Lighthouse CI getting started](https://github.com/GoogleChrome/lighthouse-ci/blob/main/docs/getting-started.md) | Reviewed documentation | Gradual CI adoption and artifact storage |
| REF-de2882326300 | [Lighthouse CI configuration](https://github.com/GoogleChrome/lighthouse-ci/blob/main/docs/configuration.md) | Reviewed documentation | Optimistic default, explicit aggregation, assertions and storage |
| REF-f1d657ab28c1 | [Lighthouse 13.5.0 release](https://github.com/GoogleChrome/lighthouse/releases/tag/v13.5.0) | Reviewed release metadata | Published September 18; channel rollout expectation is not runtime verification |
| REF-cc224bed75fe | [Google Search Essentials](https://developers.google.com/search/docs/essentials) | Reviewed documentation | Eligibility and content/navigation guidance; no ranking guarantee |
| REF-0a1c82c044ac | [Google spam policies](https://developers.google.com/search/docs/essentials/spam-policies) | Reviewed relevant policy sections | Search manipulation and scaled-content limits; not an exhaustive policy audit |
| REF-d76e3db85ca0 | [Structured-data policies](https://developers.google.com/search/docs/appearance/structured-data/sd-policies) | Reviewed relevant policy sections | Visible-content accuracy and eligibility; no rich-result guarantee |
| REF-6fe2317039f5 | [Google generative AI Search guide](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide) | Reviewed documentation | Search guidance and llms.txt claim boundary; not evidence about other AI products |
| REF-ef7e77b36286 | [Core Web Vitals and Search](https://developers.google.com/search/docs/appearance/core-web-vitals) | Reviewed documentation | Recommended field metrics and search claim limits |
| REF-3c7581b70ad6 | [Search Console guide](https://developers.google.com/search/docs/monitor-debug/search-console-start) | Reviewed documentation | Separate indexing/performance evidence |
| REF-c6f932c89131 | [W3C evaluation tools](https://www.w3.org/WAI/test-evaluate/tools/selecting/) | Reviewed documentation | Human review needed; automated tools cannot establish accessibility |
| REF-784435bb1b94 | [WCAG overview](https://www.w3.org/WAI/standards-guidelines/wcag/) | Reviewed overview | Standards context; this research is not a criterion-by-criterion conformance review |
| REF-7eb820e1e53b | [OWASP SSRF prevention](https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html) | Reviewed relevant guidance | Future untrusted-URL scanner isolation and request validation |
| REF-962af928dfaa | [Lighthouse package](https://github.com/GoogleChrome/lighthouse/blob/v13.5.0/package.json) | Inspected pinned source/docs | Version, Node engine and license metadata |
| REF-1f7dc78601d8 | [Default configuration](https://github.com/GoogleChrome/lighthouse/blob/v13.5.0/core/config/default-config.js) | Inspected pinned source/docs | Extracted all category references and weights; not runtime execution |
| REF-04fbf88226ca | [Agentic configuration](https://github.com/GoogleChrome/lighthouse/blob/v13.5.0/core/config/agentic-browsing-config.js) | Inspected pinned source/docs | Seven references and fraction display |
| REF-8aca5bf16fb5 | [LHR types](https://github.com/GoogleChrome/lighthouse/blob/v13.5.0/types/lhr/lhr.d.ts) | Inspected pinned source/docs | Metadata, category and environment fields |
| REF-ebdc4aba3aa9 | [Audit result types](https://github.com/GoogleChrome/lighthouse/blob/v13.5.0/types/lhr/audit-result.d.ts) | Inspected pinned source/docs | Score modes and per-audit fields |
| REF-1c6eecb4daaf | [Audit detail types](https://github.com/GoogleChrome/lighthouse/blob/v13.5.0/types/lhr/audit-details.d.ts) | Inspected pinned source/docs | Typed details and estimated savings representation |
| REF-627df4cbbea0 | [INP audit](https://github.com/GoogleChrome/lighthouse/blob/v13.5.0/core/audits/metrics/interaction-to-next-paint.js) | Inspected pinned source/docs | Timespan and non-simulated restrictions |
| REF-a67418871c85 | [llms.txt audit](https://github.com/GoogleChrome/lighthouse/blob/v13.5.0/core/audits/agentic/llms-txt.js) | Inspected pinned source/docs | Missing-file N/A and basic validation |
| REF-a0ef2e44df11 | [ARD audit](https://github.com/GoogleChrome/lighthouse/blob/v13.5.0/core/audits/agentic/ard-schema.js) | Inspected pinned source/docs | Discovery signals, absence and validation behavior |
| REF-45c2617f9ac6 | [Agent accessibility audit](https://github.com/GoogleChrome/lighthouse/blob/v13.5.0/core/audits/agentic/agent-accessibility-tree.js) | Inspected pinned source/docs | Subset of axe rules and evidence limits |
| REF-2dd047497063 | [WebMCP form coverage](https://github.com/GoogleChrome/lighthouse/blob/v13.5.0/core/audits/webmcp-form-coverage.js) | Inspected pinned source/docs | Conditional pass, informative and N/A states |
| REF-4197a91c0b05 | [WebMCP tools](https://github.com/GoogleChrome/lighthouse/blob/v13.5.0/core/audits/webmcp-registered-tools.js) | Inspected pinned source/docs | Informative inventory and tool-count warning |
| REF-b0ff8e28184c | [WebMCP schema audit](https://github.com/GoogleChrome/lighthouse/blob/v13.5.0/core/audits/webmcp-schema-validity.js) | Inspected pinned source/docs | Browser support, errors and warnings |
| REF-b466a0abc72a | [Run variability](https://github.com/GoogleChrome/lighthouse/blob/v13.5.0/docs/variability.md) | Inspected pinned source/docs | Repeated controlled runs; worker contention |
| REF-1e393eb392a6 | [Throttling](https://github.com/GoogleChrome/lighthouse/blob/v13.5.0/docs/throttling.md) | Inspected pinned source/docs | Simulation versus applied trace measurements |
| REF-7f5e04e2154f | [User flows](https://github.com/GoogleChrome/lighthouse/blob/v13.5.0/docs/user-flows.md) | Inspected pinned source/docs | Navigation, timespan and snapshot scope |
| REF-53d29cb88df5 | [Authenticated pages](https://github.com/GoogleChrome/lighthouse/blob/v13.5.0/docs/authenticated-pages.md) | Inspected pinned source/docs | Local/authenticated collection patterns |
| REF-e274c29a4dbe | [Understanding results](https://github.com/GoogleChrome/lighthouse/blob/v13.5.0/docs/understanding-results.md) | Inspected pinned source/docs | Artifacts and report structure |
| REF-03d5b8cd3c0f | [Plugin handbook](https://github.com/GoogleChrome/lighthouse/blob/v13.5.0/docs/plugins.md) | Inspected pinned source/docs | Extension capabilities and limits |
| REF-ba2c7577e026 | [Lighthouse CLI](https://github.com/GoogleChrome/lighthouse/blob/v13.5.0/readme.md) | Inspected pinned source/docs | CLI reports/assets; category help can lag implementation |

## Verification boundary

The audit inventory was extracted from the pinned default configuration: 165 references / 162 distinct audit IDs, with every ID resolving to one implementation file. This verifies inventory coverage, not successful execution on a website. The playbook identifies proposed practices separately from source behavior. Live API quotas, deployed engine versions, customer-site results, commercial outcomes and integration security remain untested.
