# Google SEO foundations for project reuse

Selected official guidance checked **23 September 2026**. This complements the [Lighthouse playbook](lighthouse-audit-playbook.md); it is a foundational reference, not a complete SEO audit procedure for every site type.

## Source guidance and proposed project checks

| Official guidance | Our proposed application | Verification evidence |
| --- | --- | --- |
| Search Essentials separates technical requirements, spam policies and best practices | Track each separately in the project; preserve intentional exclusions from indexing | Actual response, rendered page, crawling/indexing controls and scope |
| Useful, reliable content; descriptive titles/headings; crawlable navigation | Give each public page a clear purpose, accurate information and understandable navigation | Content review, actual links and rendered output |
| Eligibility does not guarantee crawling, indexing or serving | Report readiness separately from observed Search performance | Search Console evidence with dates and scope |
| Structured data must follow applicable policies and describe the content accurately | Select supported markup for the actual page; do not invent claims or reviews | Applicable rich-result validation plus manual content comparison |
| Spam policies address manipulative practices, including scaled-content abuse | Review generated content for usefulness and accuracy; avoid ranking manipulation | Editorial review and provenance |
| Google's generative search guidance does not require `llms.txt` | Apply normal search foundations; do not sell that file as a Google visibility requirement | Source-backed claim review; separate evidence for other AI platforms |
| Good Core Web Vitals are recommended | Measure field LCP, INP and CLS when available; use lab diagnostics to investigate | Device/URL-or-origin/period-aware CrUX or RUM records |

Sources: [Search Essentials](https://developers.google.com/search/docs/essentials), [structured-data policies](https://developers.google.com/search/docs/appearance/structured-data/sd-policies), [spam policies](https://developers.google.com/search/docs/essentials/spam-policies), [generative AI Search guide](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide), [Core Web Vitals guidance](https://developers.google.com/search/docs/appearance/core-web-vitals).

## Keep measurements distinct

- **Lighthouse SEO:** selected technical checks on a tested page/state.
- **Search Console:** observed indexing and Google Search performance within its reporting scope. [Official introduction](https://developers.google.com/search/docs/monitor-debug/search-console-start).
- **CrUX / RUM:** real-user performance with stated population and collection windows.
- **Observed AI answers:** actual observations with platform, query, date, locale and method recorded.
- **Controlled model-API experiments:** experimental outputs with their own model/prompt/settings; not automatically representative of consumer search products.
- **Business outcomes:** actual leads, conversions and revenue, with attribution limits.

These are our evidence-design choices. A higher technical score alone does not demonstrate ranking, citation, lead or revenue improvement. Keep tested facts, expected effects and hypotheses visibly separate.

## Extend only for the project's needs

For a consequential implementation, retrieve and review the responsible current Google documentation for relevant areas such as canonicalization, robots directives, JavaScript rendering, sitemaps, internationalization, local search, commerce or migrations. Add a dated source record and meaningful verification. These topic areas are a future-review map, not a claim that this research covered each exhaustively.

Keep project-specific acceptance criteria and results in the project record, linked to this module and its exact repository commit. Follow the [official-source practice](../../governance/official-source-build-practice.md).
