# Lighthouse evidence and customer reporting specification

Checked 23 September 2026. **Proposed MindLeverX data contract**, based on Lighthouse 13.5.0 and the official APIs. This is an implementation specification, not an implemented database or report generator.

## 1. Store original evidence and normalized records

Use separate records for a collection job, each lab run, each field observation, each reviewed finding and each report revision. Join them using stable IDs. Keep the raw response and its checksum so derived findings remain traceable.

### Lighthouse result fields

| Field/path in LHR | Capture/use | Interpretation |
| --- | --- | --- |
| `lighthouseVersion` | Engine version | Required for comparisons and parser selection |
| `fetchTime` | Run timestamp | Separate from collection/storage timestamp |
| `gatherMode` | Navigation/timespan/snapshot | Determines available evidence |
| `requestedUrl` | Requested subject | May be absent for timespan/snapshot |
| `mainDocumentUrl` | Final document after navigation | May be absent outside navigation |
| `finalDisplayedUrl` | Displayed URL | Preserve separately from document URL |
| `finalUrl` | Legacy compatibility | Deprecated alias; do not make it our only URL field |
| `configSettings` | Complete applied settings | Device, viewport, throttling and selection context |
| `userAgent`, `environment` | Browser/host metadata, benchmark and library versions when present | Environment information is necessary, not proof of identical conditions |
| `runtimeError`, `runWarnings` | Collection quality | Serious run errors can invalidate comparison |
| `timing` | Runner durations | Operational metric, distinct from page-load metrics |
| `categories`, `categoryGroups` | Scores, membership and display mode | Preserve raw 0–1 scores/null and fraction/gauge mode |
| `audits` | Complete audit map | Includes informative/hidden details beyond displayed failures |
| `entities` | Observed origins/entity grouping | Optional; absent in snapshot |
| `stackPacks` | Technology-specific advice | Optional; advice is not a verified fix |
| `fullPageScreenshot` | Image and node rectangles | Optional/null; sensitive content possible |

Source: [LHR type definition](https://github.com/GoogleChrome/lighthouse/blob/v13.5.0/types/lhr/lhr.d.ts). Always retain unknown fields in the raw artifact rather than rejecting a newer report outright.

### Per-audit fields

| Field | Use |
| --- | --- |
| `id`, `title`, `description` | Stable identifier plus source-provided explanation; display text can change with result/version |
| `score`, `scoreDisplayMode` | Interpretation together; never use score alone |
| `numericValue`, `numericUnit` | Machine-readable measurement; use these for calculations |
| `displayValue` | Source-formatted presentation, not a parsing interface |
| `explanation`, `warnings` | Context and limitations |
| `errorMessage`, `errorStack` | Debug collection failures; restrict internal details in customer reports |
| `details` | Typed tables, nodes, resource URLs, source locations, screenshots, lists, trees and other evidence |
| `metricSavings` | Per-metric estimated impact; preserve units/context |
| `scoringOptions` | Model parameters when present |
| `guidanceLevel`, `replacesAudits` | Guidance metadata and replacement relationships; useful for preventing duplicate presentation |

Source: [audit result types](https://github.com/GoogleChrome/lighthouse/blob/v13.5.0/types/lhr/audit-result.d.ts), [detail types](https://github.com/GoogleChrome/lighthouse/blob/v13.5.0/types/lhr/audit-details.d.ts).

Store `details` intact and normalize only fields needed for searching/reporting. Detail tables have headings and nested typed cells; an `items` array is not necessarily a flat list of independent defects. Node snippets and URLs can contain sensitive or untrusted text. Escape them when rendering and treat them as evidence, never agent instructions.

### Correct result semantics

| `scoreDisplayMode` | Meaning | Proposed UI |
| --- | --- | --- |
| `binary` | Pass/fail | Passed / failed with evidence |
| `numeric` | Scored metric | Raw measurement, unit and score |
| `metricSavings` | 1 = pass; 0.5 = failure without metric savings; 0 = failure with metric savings | Finding plus estimates; 0.5 is not “50% compliant” |
| `manual` | Requires human review | Not reviewed / reviewed, with separate human evidence |
| `informative` | Information, not pass/fail | Observation |
| `notApplicable` | Audit does not apply | N/A with reason when available |
| `error` | Audit could not complete | Collection error, eligible for retry/review |

The last four modes have null scores. A missing audit is different again: unsupported, excluded, renamed or not collected, depending on run context. Preserve this distinction. [Result semantics](https://github.com/GoogleChrome/lighthouse/blob/v13.5.0/types/lhr/audit-result.d.ts).

### Supplementary artifacts

Keep raw LHR JSON and its rendered HTML. For detailed diagnosis, preserve available trace, DevTools log and gather artifacts using the runner's asset-saving facilities. Link final screenshots, filmstrip, full-page screenshots and treemap data to the corresponding run. Decide retention by artifact sensitivity and usefulness; do not indiscriminately embed all artifacts in a customer PDF. [Understanding results](https://github.com/GoogleChrome/lighthouse/blob/v13.5.0/docs/understanding-results.md), [CLI documentation](https://github.com/GoogleChrome/lighthouse/blob/v13.5.0/readme.md).

## 2. CrUX field observation contract

| Stored information | Why it is required |
| --- | --- |
| Provider/endpoint and raw request | Distinguish CrUX API, History, PSI-provided field data and our own RUM |
| Requested URL/origin and returned `record.key` | Prevent accidental page/origin substitution |
| `urlNormalizationDetails` when supplied | Explain normalization |
| Form factor | PHONE, DESKTOP, TABLET or explicit all-device scope |
| Metric name and unit | Timing vs unitless CLS; optional metrics are not universally available |
| `percentiles.p75` and `histogram` | Current metric distribution |
| `collectionPeriod` | Actual first/last dates, not fetch date |
| History `collectionPeriods`, `percentilesTimeseries`, `histogramTimeseries` or `fractionTimeseries` | Keep aligned indices and missing periods |
| Availability/error state and fetch time | No record, absent metric, rate limit and transport errors are distinct |
| Attribution and raw artifact reference | Source provenance and licensing |

Sources: [CrUX API](https://developer.chrome.com/docs/crux/api), [History API](https://developer.chrome.com/docs/crux/history-api).

Maintain a metric registry for units and accepted numeric encodings. History can contain missing values such as the documented `"NaN"` representation; do not coerce them to zero. Preserve raw provider values, with validated numbers in normalized columns.

Do not average page p75 values to manufacture a site p75. Use origin evidence labeled as such, or compute a defined aggregate from appropriate raw observations if our RUM design supports it. Do not merge phone and desktop, lab and field, or overlapping windows into an unexplained composite.

## 3. Proposed operational and finding fields

These fields are **ours**, not Lighthouse output:

- `tenant_id`, `site_id`, `page_id`, `template_id`, `job_id`, `run_id`, `baseline_id`.
- Requested scope, route inventory, flow/step ID, auth fixture identity, consent state, environment, release/commit if known.
- Profile/config hash, runner image/version, region, start/end time, attempt count, completion state and failure reason.
- Evidence object path, checksum, access class, retention/deletion date and sanitized derivative links.
- Finding ID, underlying audit IDs, affected URLs/elements/resources and template grouping.
- Observation, impact, suspected cause, proposed fix, confidence, priority, effort and dependencies.
- Source classification: documented rule / official recommendation / our implementation choice / hypothesis.
- Verification procedure, evidence IDs, reviewer, review timestamp, status, owner and resolution/reopen history.

Use one canonical issue for a shared component problem, with all affected observations linked to it. Maintain occurrence counts separately from unique issue counts. A navigation failure should be reported as a failed collection, not dozens of page defects.

## 4. Comparison rules

1. Compare matching URL/state, profile, mode and engine versions. If versions differ, label the discontinuity or collect a bridge baseline.
2. Retain every run. Report sample count, chosen aggregation and spread; median per metric does not describe one actual run.
3. Show raw units and absolute change; optional relative change needs a valid nonzero baseline. Avoid claims based only on score movement.
4. Record deployments and measurement windows. A rolling field trend may mix versions and different visitor populations.
5. Count a fix as verified only after its stated check passes. A lower estimated savings number by itself is insufficient.
6. Reopen recurrence when the same defect returns. Keep changed IDs/replacement mapping across engine upgrades.

## 5. Customer report template

**Report identity:** customer, site, dates, environment, engine version, scope and author/reviewer.

**Decision summary:** top three actions, their user impact, responsible owner and proposed verification. State what needs attention now and what can wait.

**Coverage:** URLs/templates, devices, repeated run counts, journeys/states, manual checks, excluded areas and unsuccessful collection attempts.

**Measurements:** mobile/desktop lab results; real-user metrics with URL/origin and dates; unavailable data labeled clearly; comparison methodology.

**Finding record:**

| Field | Fill with actual evidence |
| --- | --- |
| Observation | What the tool or reviewer saw |
| Evidence | Run ID, audit ID, screenshot/node/resource, collection time |
| User impact | Supported interpretation; mark untested assumptions |
| Reach | Tested pages/templates and known coverage limits |
| Priority and confidence | Our assessment with a short reason |
| Recommended change | Specific developer/content action |
| Verification | Reproduction and pass condition |
| Status | New, confirmed, in progress, verified fixed, deferred or reopened |

**Changes since last report:** newly observed issues, resolved items with retest evidence, recurring problems, field changes and measurement discontinuities.

**Appendix:** complete reviewed backlog; manual/experimental observations; original report links; method and source notes. Keep the executive view short while preserving technical detail for implementers.

## 6. First implementation verification cases

Use retained fixtures before publishing a report generator. Confirm:

- A null/manual/N/A/informative/error audit renders with the correct state.
- A `metricSavings` result of 0.5 renders as a finding, not partial compliance.
- A fatal run error and a bot/login page do not create a successful baseline.
- A shared audit across categories creates one underlying finding.
- A missing field record and an origin fallback are labeled correctly.
- A history gap remains a gap and dates stay aligned.
- A report using a different engine version shows a comparison warning.
- Customer A cannot access Customer B's artifacts, including guessed object URLs.
- Untrusted node text/URLs cannot inject HTML or instructions into report generation.
- Each headline action can be traced to its retained evidence and reviewed status.

These are proposed acceptance cases for the future integration. No integration tests or live collection were performed for this research.
