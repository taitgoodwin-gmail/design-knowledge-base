# MindLeverX — launch inspection and Codex handoff

Inspected 12 September 2026. **Not ready for a complete source handoff or launch.** This audit package is usable now, but contains a reference production build, not the editable source project. **Current scope: preserve the existing design.** The user explicitly cancelled the design-system replacement after this audit. Repair functional, content and accessibility defects within the existing design, then repeat affected checks.

No deployment, DNS changes, website edits, or live lead submissions were made.

## Evidence and scope

Read directly in the Claude project: `CLAUDE.md`, `docs/OPEN-ITEMS.md`, `docs/TECHNICAL.md`, `docs/TOKEN-INVENTORY.md`, `docs/LAUNCH.md`, `docs/CHANGELOG.md`, and `docs/RELEASE-NOTES.md`. All seven exist. The source folder inventory was inspected; the source homepage was rendered. Other source code files were not exported or exhaustively read.

Project: https://claude.ai/design/p/8aabc09f-69a6-4246-8790-6edbedef24da

The local archive `MindLeverX files render.zip`, already in Downloads and timestamped 12 Sep 2026 15:42, contains nine files, all under `site-v3.1/dist/`. Those files are included unchanged under `reference-build/` in this audit package. All six HTML files and three crawler files were inspected. `static-audit.json` records per-file hashes, metadata, schemas, inputs and link results. This is a dated snapshot; equality to the latest Claude source or latest remote dist is **unverified**.

The Share → Project HTML export action did not yield a verifiable new full-source download in this session. A download-event wait timed out. No full-source ZIP is claimed. Browser access to Chrome's downloads page was blocked by browser policy; no bypass was attempted.

## Verified structure and authorities

The source folder inventory and project documentation agree:

```text
CLAUDE.md                     standing project rules
README.md                     present; not inspected
docs/                         seven requested documents present/read
site/                         frozen v3.0 rollback, per CLAUDE.md
site-v3.1/                    authoritative editable source
  index.html
  what-is-geo.html
  research-hub.html
  answer-engine-index-q3-2026.html
  case-study.html
  about.html
  style-guide.html            old design system; not served
  head-schema.html            schema authority; not served
  token-lint.js               present; not exported or executed
  DEPLOY.md
  robots.txt
  sitemap.xml
  llms.txt
  dist/                      generated public files
uploads/                      present; contents not independently inventoried
```

The root also contains old platform/design explorations and `support.js`; they must not be mistaken for the six-page production website. No package manifest, lockfile or reusable build script appeared in the inspected root or v3.1 folder inventories. This is not proof of absence everywhere in the project.

Preserve: self-contained HTML, six-page shared-chrome sweeps, SAMPLE labels, no invented case-study measurements, empty `sameAs` until verified profiles exist, no invented schema URLs, honest endpoint gating. The user has not authorized publishing during this inspection.

## Commands and build gap

There is no package installation requirement for the reference build. Python 3 was used for preview and static checks; Node v26.7.0 for isolated form tests. From this audit package root:

```sh
python3 -m http.server 8765 --bind 127.0.0.1 --directory reference-build/site-v3.1/dist
python3 checks/audit_static.py
node checks/form-audit.cjs
```

Open `http://127.0.0.1:8765/index.html`.

For the eventual full project, the equivalent preview command is:

```sh
python3 -m http.server 8765 --bind 127.0.0.1 --directory site-v3.1/dist
```

**Exact v3.1 build command: unavailable/unverified.** TECHNICAL.md specifies stripping INTERNAL sentinel blocks, injecting canonical/Open Graph tags and JSON-LD, then copying crawler files. It refers to a one-off v3.1 script and to `site/strip-internal.sh` for v3.0. Recover the actual script or implement and verify a reproducible v3.1 build after inspecting source and schema authority. Never reverse-engineer editable source by treating dist as authoritative.

TECHNICAL.md's lint command points at `node token-lint.js site-v3.1/*.html`, while the inventory locates the script inside `site-v3.1/`. Inspect its argument contract before establishing the corrected command; do not claim it passed.

## Findings ordered by launch impact

Locations below are in the audited `site-v3.1/dist/` snapshot unless explicitly marked as documentation. Port fixes to matching source locations, then rebuild. P1 = launch-blocking; P2 = repair before acceptance; P3 = follow-up/documentation.

| ID | Severity | Location and evidence | Impact and recommended action |
|---|---|---|---|
| F1 | P1 | All four forms read `window.MLX_AUDIT_ENDPOINT`, unset in the snapshot. `index.html:594,628`; OPEN-ITEMS L1. | No lead capture. Preserve the gate until a real receiving service is validated. |
| F2 | P1 | `index.html:421,446,498` claims daily tracking, a live measured score and continuous monitoring; `what-is-geo.html` FAQ Q3–Q5 claims daily monitoring and movement from day one. OPEN-ITEMS U1–U5 says scoring, scorecards and monitoring are unbuilt. | Visitors may buy on unsupported capability claims. Sweep visible copy, metadata, JSON-LD and llms.txt against the capability register. SAMPLE footnotes do not cure contradictory live-service prose. |
| F3 | P1 | `research-hub.html:364,371,443` promises monthly email, including after endpoint configuration. U6 says newsletter is deferred. | Wiring intake enables another unsupported schedule promise. Remove cadence and unsubscribe-function claims until actually implemented; distinguish subscription interest from an audit request in downstream routing. |
| F4 | P1 | `about.html:256` and `case-study.html:232` label static sample tickers LIVE. Their pause labels also say live. | Shared chrome misrepresents measurements. Apply consistent sample wording including accessible names on all six pages. Keep actual historical case-study measurements separate. |
| F5 | P1 | `index.html:639`, `what-is-geo.html:651`, `research-hub.html:457`, `answer-engine-index-q3-2026.html:458` check only `r.ok`. Four isolated tests reproduced success with a 202 response whose body is `{ok:false}`. | Success can contradict the documented acceptance contract. Parse and validate the agreed response; define durable acceptance and downstream error handling. |
| F6 | P1 | LAUNCH §4 recommends a direct Zapier Catch Hook, while TECHNICAL.md requires custom 202/400/429 JSON including `lead_id`; browser config injection is unspecified. | Catch Hook is not a drop-in implementation of that contract. Choose an adapter or explicitly revise and test the contract. A same-origin receiving function with a server-side webhook secret is a recommendation, not existing functionality. |
| F7 | Closed by scope change | The user cancelled the design-system replacement. | Keep the existing design. Replacement and wholesale token mapping are not launch dependencies. |
| F8 | P1 | Source export and reproducible v3.1 build are missing from this package. | Cannot prove source/dist parity or safely complete source edits. Export the complete project and compare a clean build to committed output. |
| F9 | P1 | OPEN-ITEMS L2 requires www→apex. Actual Vercel/Cloudflare settings were not inspected. | Domain behavior is unverified. At authorized launch, retain Cloudflare DNS and existing mail records, use Vercel's account-specific values, and verify permanent redirects and TLS. |
| F10 | P2 | `what-is-geo.html:558`, `research-hub.html:371`, `answer-engine-index-q3-2026.html:378`: `fnote` lacks status/live-region semantics. Homepage has both. | Screen-reader users may miss submission outcomes. Add a suitable status region and test announcements; TECHNICAL.md overstates four-page coverage. |
| F11 | P2 | All six pages declare `--muted:#75787d` near the start of CSS. Calculated contrast is 4.43:1 on white and 4.14:1 on `#f7f7f8`. | Insufficient for normal-size text under WCAG AA. Resolve through the existing design tokens and measure actual uses in both themes. |
| F12 | P2 | `answer-engine-index-q3-2026.html:233` JSON-LD describes benchmark findings without the visible sample qualification. Its description meta includes Sample data. | Crawlers receive less-qualified claims than visitors. Preserve sample provenance in every machine-readable description. |
| F13 | P2 | `case-study.html:346` retains the dated historical 0/6 JSON-LD finding; the audited build now embeds schema on all six pages. | Historical evidence must remain dated, not treated as current. Re-measure the corrected build and later the live origin separately; never invent updated numbers. |
| F14 | P2 | All form fetch chains lack a request deadline; secondary audit forms derive a company domain from every email, unlike the homepage's free-mail follow-up field. | A stalled request can leave Sending indefinitely; free-mail leads yield unsuitable company domains. Add a timeout and align data collection/validation across audit forms, retaining newsletter-specific semantics. |
| F15 | P3 | `index.html:546`, other footers and `sitemap.xml` retain internal decision comments, including an unverified deployed-date comment. `llms.txt` links homepage via /index.html while canonical is /. | Sentinel count zero does not mean all internal notes are stripped. Review public artifacts, remove internal-only comments, and align canonical links. No credential was identified in inspected text; a full repository secret scan remains outstanding. |

## Verification performed

- Six pages: one h1 and one apex canonical each; JSON-LD parses; zero missing local linked files/fragments; zero `href="#"`; zero INTERNAL sentinel strings. Forms occur only on the four documented pages. See static-audit.json.
- All six pages rendered at 375, 960 and 1280 in both light and dark: no document-width horizontal overflow. Navigation was hidden/mobile at 375 and 960 and desktop at 1280. These are DOM/layout checks, not a full visual or accessibility certification.
- What-is-GEO menu opened at 960; dark mode switched; the disconnected form displayed honest unavailability using synthetic `audit@example.com`, with no live endpoint configured.
- Twenty-four isolated JavaScript tests: four forms × absent endpoint, accepted response, false body with successful HTTP status, 429, 500, and network rejection. All four reject the absent endpoint without a request, handle HTTP/network errors, and restore busy state after settled requests. All four incorrectly accept the false-body case. These mocks do not test actual Zapier/Airtable/email delivery or browser CORS. See form-audit.json.
- Source-to-dist equality, full keyboard/screen-reader traversal, every visual section, no-JS/reduced-motion rendering, external source claims, font availability under failure, real provider permissions/configuration, production headers, DNS/TLS and end-to-end delivery remain **unverified**. Motion CSS and JS gates were inspected but not fully exercised.

## Design scope — current user decision

Keep the current website design. The separate 1b design exploration is historical context and is not authorized for implementation. Do not import its palette, typography, wordmark or dashboard components.

D1–D6 in OPEN-ITEMS remain documented design debt, not blanket launch blockers. Resolve only what is necessary to repair verified accessibility defects or preserve the existing pages. Correct the muted-text contrast and form status semantics; avoid a redesign. Keep the current self-contained HTML architecture and six-page consistency checks.

## Integrations and configuration

Existing browser configuration: `window.MLX_AUDIT_ENDPOINT` (a JavaScript global, not a verified environment variable). No host injection mechanism or existing server-side environment-variable names were verified.

Proposed adapter configuration, only if implemented: `ZAPIER_WEBHOOK_URL` stored server-side. Keep the public browser endpoint a same-origin route such as `/api/audit`. Never put the private Catch Hook URL, Airtable credentials or mailbox credentials into HTML or exported docs. This proposal adds server-side handling and must be reconciled with the static hosting notes.

Intended workflow: validate input/spam server-side → accept durably → Zapier → Airtable lead record + internal notification to tait@augmind.ai. Expected payload fields are email, domain, website (honeypot), ts, and source. A client-provided timestamp alone cannot establish trustworthy dwell time. Rate limiting/deduplication must be server-side. Define audit versus newsletter-interest routing.

Keep prospect auto-replies disabled. The MindLeverX mailbox is deferred; the internal notification address must not become a prospect-facing sender. No mailbox decision needs to block this audit handoff.

## Provider guidance requiring correction or verification

Zapier documents non-customizable Catch Hook responses, possible delayed handling, and a delay before disabled hooks stop returning 200. Therefore HTTP 200 alone is not proof that Airtable and email actions completed. Its webhook feature also requires a supported paid plan; account eligibility was not checked. [Zapier webhook documentation](https://help.zapier.com/hc/en-us/articles/8496288690317-Trigger-Zap-workflows-from-webhooks).

At launch use the records Vercel reports for the actual project. Retain external DNS management at Cloudflare. A repo containing the full source needs its actual generated output path, not blindly `.` or `dist`; the current tree nests it at `site-v3.1/dist`. [Vercel domain setup](https://vercel.com/docs/domains/set-up-custom-domain).

LAUNCH's blanket claim that Cloudflare proxying necessarily causes a redirect loop is too broad; DNS-only is a simple intended setup, while proxy behavior depends on TLS/origin settings. Do not change nameservers or remove MX/SPF/DKIM/DMARC records. Verify the current provider instructions on deployment day. [Cloudflare encryption modes](https://developers.cloudflare.com/ssl/origin-configuration/ssl-modes/).

Contrast and status recommendations above use [WCAG 2.2](https://www.w3.org/TR/WCAG22/) and [W3C ARIA22](https://www.w3.org/WAI/WCAG22/Techniques/aria/ARIA22.html). No full conformance claim is made.

## Dependency-ordered next work

1. Export the complete current editable Claude project, including source, docs, schema authority, lint and build scripts. Preserve the audited snapshot. In parallel, identify the target Vercel project and existing Zapier/Airtable connections without changing them.
2. Read source rules; inventory files; recover or implement the repeatable generator; establish source/dist parity and the correct lint command. Preserve the existing design.
3. Repair unsupported service/newsletter/live-label claims, sample schema descriptions, form status accessibility and muted-text contrast. Re-measure current artifact facts with dated evidence.
4. Implement and validate receiving/acceptance semantics, server validation, timeouts, rate limiting, deduplication, source routing and secret handling. Wire authorized Zapier/Airtable/internal email connections. Keep prospect auto-replies off.
5. Run clean build, lint, link/schema checks, endpoint acceptance/rejection tests, full keyboard and screen-reader checks, reduced-motion/no-JS checks, and visual checks at 375/960/1280 in both themes.
6. When preview deployment is authorized, deploy a Vercel preview and repeat realistic browser/CORS/network tests. Verify an approved synthetic submission through storage and internal notification.
7. Present the checked preview and exact intended domain changes for production authorization. Then publish, verify TLS/redirects/canonical and crawler files, test live intake, re-measure live case-study facts, and record rollback steps. Current inspection authorization excludes deployment and DNS changes.

## Export steps and remaining user inputs

The UI path observed is **Share → Project HTML (.zip or standalone) → Download**; extra export options may appear after opening **More formats and apps**. Verify the resulting archive contents. The existing nine-file dist archive is insufficient.

If that export omits editable/internal files, paste this into the Claude project:

> Package the complete MindLeverX project for Codex as a downloadable ZIP. Include CLAUDE.md, README, docs, editable site-v3.1 source, head-schema.html, current style guide and assets, token-lint.js, all build/strip scripts, generated dist, and the decision records needed to interpret them. Preserve relative paths. Include manifests/lockfiles only if they exist. Exclude credentials, .env values, caches and installed dependencies. Include a file manifest, exact reproducible build/test commands, and explain any missing generator. This must not be a dist-only export. Do not deploy or change DNS.

Only immediate missing input: the full current editable source export (or its local path). No new design bundle is needed. For the subsequent integration stage: the target Vercel project/account, intended Airtable base/table and approved connected workflow; provide secrets through secure configuration, not this document. The operator identity for About remains an optional content input, not a reason to invent a name.

