# MindLeverX design and web-quality audit

**Checked 23 September 2026 · Read-only audit · 24 findings**

## Assessment

**The Figma concept needs another design and content pass before implementation. The live site has a sound technical baseline, with specific accessibility and credibility defects to fix.** A blanket claim that everything fails Google quality would be inaccurate.

The most urgent live issues are clipped mobile tables, a low-contrast link, a chart labeled both measured and fictional, and unsupported GEO claims. The most urgent Figma issues are exposed internal instructions, low-contrast essential labels, overflowing report labels and unwired links.

This is an evidence-based review, not a Figma certification, Google ranking prediction, security penetration test or full WCAG conformance assessment. Design-quality judgments are marked as recommendations; measured failures and verification gaps are identified separately.

## What was reviewed

- **Figma:** two pages, all 23 top-level frames, 2,127 unique nodes and 1,179 text layers. All 23 frame screenshots were visually inspected. Geometry, text styles, variables, components and prototype wiring were inspected without changing the design.
- **Production:** all seven public HTML routes, plus robots.txt, sitemap.xml and llms.txt. Each returned HTTP 200. Captured HTML, headings, metadata, internal links, fragments and JSON-LD were inspected, alongside the relevant shared CSS, JavaScript and build transformations.
- **Browser:** all seven routes at 320, 390, 768 and 1440 CSS pixels; targeted table-container inspection; homepage disclosure-menu keyboard behavior and ticker pause. Temporary viewport emulation and ticker changes were restored.
- **Lighthouse:** one mobile and one desktop result per route through Google PageSpeed Insights, Lighthouse 13.5.0, HeadlessChromium 153.0.8010.36. Runs were captured between 5:20 and 5:33 PM EDT. These are single-run samples, not repeat-run medians. Full Lighthouse JSON/traces were not exported; the visible report text and report URLs are preserved.
- **Code reference:** public MindLeverX repository at `4dfbeb6ff8c0ca2db62a6458eecae8c12249b940`. Captured deployed HTML is the runtime evidence; a source commit alone does not prove deployment identity.
- **Reference library:** design-knowledge-base at `1332a7f3dc3aeaf1c4d144f30b81918669b532c3`; Figma modules 02–06 and 10, project Figma record, build guidance and Google web-quality module. Applicable official sources were refreshed on the audit date.

The current Figma file is the Z2-inspired concept `OTfzO4cl4mosafK3Y74ayI`. The older file recorded in the library is a separate design direction and was not substituted for this one. Private operator-app screens, customer data, account flows and backend collection were outside this public-site audit.

## What is already working

- Seven live routes have descriptive unique titles, descriptions, self-referencing canonical URLs, one H1 each and parseable Organization plus WebPage/CollectionPage JSON-LD. No missing local link targets or fragments, or duplicate IDs, were found in the captured seven-page set.
- The public HTML contains the main content. Robots and sitemap are present; no blocking noindex was observed. HTTP responses include HSTS, nosniff, a referrer policy and frame protection. These facts do not establish actual Google indexing or a complete security review.
- The live menu opens, exposes its links, updates aria-expanded and closes with Escape while restoring focus. The next keyboard stop was Services with a visible 2px outline. The sample ticker can be paused and reports its state.
- The site generally discloses fictional data, planned services and collection limits. The homepage distinguishes brand mentions from citations and gives denominators. The cited research includes meaningful scope caveats.
- Figma already uses extensive auto layout, eight text styles, 15 variables, seven components and 104 instances. Mobile counterparts exist for all seven current content pages. This is a usable foundation, not a blank canvas.

## Lighthouse results

All routes scored 100 for automated Best Practices and SEO. About scored 96 for automated accessibility; the other six scored 100. None had field-user data in PageSpeed Insights. A 100 does not establish complete accessibility or SEO quality.

| Page | Mobile performance | Desktop performance | Accessibility M/D | Mobile LCP | Report |
|---|---:|---:|---|---|---|
| home | 88 | 99 | 100/100 | 3.0 s | [PageSpeed](https://pagespeed.web.dev/analysis/https-mindleverx-com/rcg0nyoix4?form_factor=mobile) |
| method | 90 | 99 | 100/100 | 2.9 s | [PageSpeed](https://pagespeed.web.dev/analysis/https-mindleverx-com-method-html/1r44hm868b?form_factor=mobile) |
| geo | 88 | 99 | 100/100 | 3.0 s | [PageSpeed](https://pagespeed.web.dev/analysis/https-mindleverx-com-what-is-geo-html/136gif8rl1?form_factor=mobile) |
| research | 92 | 100 | 100/100 | 2.7 s | [PageSpeed](https://pagespeed.web.dev/analysis/https-mindleverx-com-research-hub-html/tdxw3memou?form_factor=mobile) |
| index-report | 90 | 99 | 100/100 | 2.9 s | [PageSpeed](https://pagespeed.web.dev/analysis/https-mindleverx-com-answer-engine-index-q3-2026-html/92fdvvfnl8?form_factor=mobile) |
| case-study | 90 | 99 | 100/100 | 2.9 s | [PageSpeed](https://pagespeed.web.dev/analysis/https-mindleverx-com-case-study-html/2lil3g9tae?form_factor=mobile) |
| about | 88 | 99 | 96/96 | 2.9 s | [PageSpeed](https://pagespeed.web.dev/analysis/https-mindleverx-com-about-html/jndkbvyarr?form_factor=mobile) |

Mobile FCP/LCP were 2.7–3.0 seconds, TBT 0ms, and CLS 0–0.004. Desktop FCP/LCP were 0.7–0.8 seconds. Those are lab measurements; field INP and Core Web Vitals status remain unverified. The direct unauthenticated PSI API returned a quota error; the official web UI subsequently completed all 14 results.

## Priorities and acceptance

**P1:** fix before treating this as a ready public experience or handing off the corresponding concept. **P2:** address in the next coherent design/content pass. **P3:** polish. Priorities are our project judgments, not labels assigned by Google or Figma.

### W01 · P1 · Seven tables lose content on narrow screens

**Scope:** Live website · **Basis:** Observed defect; WCAG accessibility target

**Evidence:** At a verified 320 CSS-pixel viewport, the GEO comparison table is 324.21px wide inside a 255px container; the sample Index table is 353.52px inside 255px. The five case-study tables are 292.97–342.52px inside 255px. Each parent has overflow-x:hidden and no tabindex. Source: site/what-is-geo.html:174; site/case-study.html:119; site/answer-engine-index-q3-2026.html:119.

**Why it matters:** Visitors can lose right-hand cells even though document.scrollWidth does not exceed the viewport. The absence of page-wide overflow is not a reflow pass.

**Recommended fix:** Use a labeled, keyboard-operable horizontal scroll region for genuinely tabular comparisons, or transform suitable rows into stacked labeled entries. Preserve all cells and headings.

**Acceptance check:** At 320 CSS pixels and equivalent zoom, reach every cell with keyboard and touch. Confirm no hidden columns, readable headers, visible focus and no unnecessary whole-page horizontal scrolling.

**Reference:** [WCAG 2.2: reflow](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html).

### W02 · P1 · About-page link has insufficient contrast

**Scope:** Live website · **Basis:** Observed defect; WCAG accessibility target

**Evidence:** Lighthouse accessibility 96 on mobile and desktop. Selector #method .textlink: “The full definition of GEO is here →”; computed #932C21 text on #1D1F23, 18px / weight 500. Source site/about.html:342, .textlink at line 38, .dark at line 156.

**Why it matters:** The link is difficult to see within the dark section. It does not meet the 4.5:1 normal-text contrast target.

**Recommended fix:** Give links in dark sections an appropriate semantic text color; verify default, hover, visited and focus states.

**Acceptance check:** Recalculate contrast against the rendered background and rerun About’s Lighthouse accessibility audit. Check both supported appearances separately.

**Reference:** [WCAG 2.2: contrast minimum](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html).

### W03 · P1 · A fictional chart is explicitly called measured

**Scope:** Live website · **Basis:** Observed contradiction; editorial reliability recommendation

**Evidence:** what-is-geo.html: the chart heading says “FIG. 01 · THIS DEFINITION, MEASURED”; its badge says SAMPLE and the caption says NOT MEASURED. Values include 63 citations, 3/4 engines, 41% share and invented changes. Saved live HTML lines 427–434.

**Why it matters:** The most prominent wording contradicts the disclosure and can mislead a scanning reader or an extracted snippet.

**Recommended fix:** Rename the heading “Illustrative definition report — fictional data.” Remove named-engine success claims from the example or use neutral fictional entities. Keep the sample disclosure adjacent to each exhibit.

**Acceptance check:** Search every page, metadata field and chart label for measured/sample contradictions; have a reviewer identify the provenance without reading surrounding paragraphs.

**Reference:** [Google: helpful, reliable, people-first content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content).

### W04 · P1 · GEO explainer makes unsupported, overly broad claims

**Scope:** Live website · **Basis:** Observed unsupported claims; official Google scope guidance

**Evidence:** Live GEO comparison promises a “Days” feedback loop; contrasts SEO with a human scanning ten links and AI with a model consuming sources; FAQ groups Gemini and AI Overviews. The opening defines GEO as engineering content so engines cite and recommend it. Source site/what-is-geo.html; saved live lines 413, 423, 450–476, 518–522.

**Why it matters:** Readers can infer reliable timing, a false SEO/AI separation, or equivalence between different Google products. Later caveats do not fully repair the specific claims.

**Recommended fix:** Define the work as improving site quality and observing product-specific answers. Remove the universal timing claim. Explain Google Search AI features and Gemini as distinct contexts; keep claims about other products separately sourced.

**Acceptance check:** Map each consequential platform claim to an official source and scope; label untested propositions as hypotheses. Check introduction, table, FAQ and metadata together.

**Reference:** [Google: optimizing for generative AI features](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide).

### W05 · P2 · Mobile rendering is delayed by blocking resources

**Scope:** Live website · **Basis:** Measured lab opportunity; implementation options need verification

**Evidence:** Seven mobile Lighthouse runs scored 88–92; LCP 2.7–3.0s. Homepage render-blocking insight estimates 2,380ms savings. Its expanded desktop report identifies /runtime.js and the Google Fonts stylesheet for Spectral, IBM Plex Sans and IBM Plex Mono. Each HTML file loads that stylesheet near line 11 and runtime.js synchronously.

**Why it matters:** The first useful content appears later on the simulated slow connection. This is a lab observation, not proof of failing real-user Core Web Vitals.

**Recommended fix:** Review whether runtime configuration is needed on the public static build; defer or inline it only after checking dependencies. Reduce font families/weights or serve selected optimized fonts with an intentional loading strategy. Compare visual stability and font fallback.

**Acceptance check:** Repeat comparable mobile runs after the change; retain medians and variation. Target better LCP without increasing CLS or hiding content. Do not add estimated savings arithmetically.

**Reference:** [Chrome: render-blocking requests](https://developer.chrome.com/docs/performance/insights/render-blocking).

### W06 · P2 · Primary journeys lead to unavailable services

**Scope:** Live website · **Basis:** Observed journey limitation; UX recommendation

**Evidence:** Homepage says “Start with a request” and “Free · No credit card” while requests are closed. About’s “How to reach the practice” supplies no address and a “Start here” link leads to the same closed availability section. These are functioning links, not HTTP failures.

**Why it matters:** The page promises an action the visitor cannot complete. Repeated availability explanations consume attention without offering a useful next step.

**Recommended fix:** While closed, make the main action a useful available resource: view a sample, read the method or review published findings. Use one concise availability statement. Add a contact or signup only when a real authorized channel exists.

**Acceptance check:** Follow each primary CTA as a new visitor and record the useful outcome. Confirm no invented mailbox, active-service promise, intake or launch date.

**Reference:** [Google: helpful, reliable, people-first content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content).

### W07 · P2 · Research presentation overemphasizes invented results

**Scope:** Live website · **Basis:** Observed content balance; editorial/UX recommendation

**Evidence:** Research Hub leads with a fictional Q3 benchmark, 1,200 prompts and 11.4%, then a sample engine feed. Homepage places invented percentages and an unvalidated 87/100 composite prominently. Disclosures are present and generally explicit.

**Why it matters:** The hierarchy lends visual authority to invented results. The page offers relatively little current original evidence; the potential effect on visitor trust is a hypothesis to test, not a proven ranking penalty.

**Recommended fix:** Lead with useful sourced analysis and the current measured website audit. Keep one clearly labeled example in an examples section. Use placeholders instead of fabricated quantitative precision when the number is not needed to explain the interface.

**Acceptance check:** Ask representative users what was actually measured and what they learned. Keep the fictional sample out of claims of customer results or research outcomes.

**Reference:** [Google: helpful, reliable, people-first content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content).

### W08 · P2 · Historical case study needs a current companion and tighter language

**Scope:** Live website · **Basis:** Observed currency gap; editorial recommendation

**Evidence:** The case study is correctly dated 27 July 2026 and labeled historical, but its body repeatedly says the site is not deployed, has six pages and 0/6 JSON-LD. Today all seven public pages return 200 and include parseable JSON-LD. It also says “Every competitor’s case study is a marketing artifact,” an unsupported universal comparison.

**Why it matters:** The historical disclosure prevents treating old numbers as current, but readers encounter stale present-tense assertions and cannot find a current follow-up beside them.

**Recommended fix:** Preserve the original dated record. Add a separate September audit and a prominent current-status link. Change historical narration to past tense and remove unsupported statements about all competitors.

**Acceptance check:** The old report remains dated and immutable as evidence; the current report identifies its own URL, time, commit and limits. No old measurement is silently overwritten.

**Reference:** [Google: helpful, reliable, people-first content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content).

### W09 · P2 · Real-user experience and search eligibility are not yet verified

**Scope:** Verification gap · **Basis:** Evidence gap, not a demonstrated implementation failure

**Evidence:** All seven PageSpeed reports say “No Data” for real users. No Search Console property, URL Inspection result, generative-AI inclusion setting, analytics conversion record or measured AI-answer panel was accessed in this audit.

**Why it matters:** Lab scores cannot establish field INP, a Core Web Vitals pass, indexing, rankings, AI inclusion or business results.

**Recommended fix:** Use Search Console and appropriate field measurement when available. Retain collection windows, device segments and provenance. Keep lab and field results separate.

**Acceptance check:** Record URL Inspection/indexing evidence and field LCP/INP/CLS at the relevant percentile and time window. Report insufficient data explicitly.

**Reference:** [Google: optimizing for generative AI features](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide), [Shared Lighthouse audit playbook](https://github.com/taitgoodwin-gmail/design-knowledge-base/blob/1332a7f3dc3aeaf1c4d144f30b81918669b532c3/tools/google-web-quality/lighthouse-audit-playbook.md).

### D01 · P1 · Internal design instructions appear in visitor-facing content

**Scope:** Figma concept · **Basis:** Observed content defect; UX/editorial recommendation

**Evidence:** Homepage nodes 13:184–185 display design intent and mobile reading-order instructions. Mobile Research 14:659 says “Do not invent entries or dates”; 14:663 tells the writer what to state; About 14:755 says “Do not invent or imply any of these.”

**Why it matters:** The design exposes writing instructions and development notes as product copy. It undermines clarity and makes the concept look unfinished.

**Recommended fix:** Move implementation requirements to named annotation frames outside customer screens. Replace instructions with concise, approved visitor information.

**Acceptance check:** Read all page text as a visitor; no authoring command, breakpoint instruction or owner decision log remains in the customer reading order.

**Reference:** [Shared Figma working practices](https://github.com/taitgoodwin-gmail/design-knowledge-base/blob/1332a7f3dc3aeaf1c4d144f30b81918669b532c3/tools/figma/README.md).

### D02 · P1 · Contrast failures are built into prominent labels

**Scope:** Figma concept and guide · **Basis:** Measured design-color defect against the WCAG target; not a browser conformance certification

**Evidence:** 17 text layers were flagged by solid-color contrast calculation: seven current concept layers, five guide layers and five older desktop layers. Report warning nodes 13:700 and 14:509 are #F7FAFF on #FF6B4A: 2.69:1. Five current coral status labels calculate about 4.26:1. Guide rust-on-light labels are about 4.15:1; white-on-rust guide labels 4.37:1.

**Why it matters:** The sample warning and service-status labels carry essential meaning but fail the normal-text contrast target. The guide would reproduce some failures if used unchanged.

**Recommended fix:** Create tested semantic foreground/background pairs for warnings, badges and actions. Adjust the pair rather than relying on the color name or increasing weight alone.

**Acceptance check:** Check every listed pair at its actual size/weight and state, then repeat in the implemented browser. The appendix records all 17 node IDs. Logos themselves are not included as ordinary-text failures.

**Reference:** [WCAG 2.2: contrast minimum](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html).

### D03 · P1 · Report status labels overflow their cards

**Scope:** Figma concept · **Basis:** Observed geometry defect; Figma layout behavior and our sizing practice

**Evidence:** Report 13:682: text 13:731 is 246px wide at x=16 inside a 229.33px card; its right edge exceeds the card by 32.67px. Text 13:734 is 230px at x=16 in another 229.33px card, exceeding it by 16.67px. Both use auto width. Screenshot confirms labels run beyond their cards.

**Why it matters:** Critical provenance labels become visually entangled with neighboring states. Checking only the page’s outer bounds misses this defect.

**Recommended fix:** Use fill-width, auto-height text with wrapping; simplify labels and give the three status cards consistent padding and deliberate row sizing.

**Acceptance check:** Check long labels at desktop and compact widths, including a longer translated label. Every label stays within its content box without hiding essential text.

**Reference:** [Figma: auto layout](https://help.figma.com/hc/en-us/articles/360040451373-Guide-to-auto-layout).

### D04 · P2 · Card grids lack consistent sizing and spacing

**Scope:** Figma concept · **Basis:** Visual observation and design recommendation

**Evidence:** Desktop About 13:893 shows the first two principle cards touching and lower cards much narrower than the first row. Research 13:791 has narrow, uneven source-category cards with large unused gaps. Mobile versions use more consistent single-column cards.

**Why it matters:** Items of equal conceptual importance look unrelated or differently weighted. The gap is visible in the screenshots; its conversion effect has not been tested.

**Recommended fix:** Use consistent fill-width grid tracks, explicit gaps and reusable card padding. Decide whether equal heights serve the content; do not force equal height everywhere.

**Acceptance check:** Resize a duplicate test frame through narrow, intermediate and desktop widths with long content; verify alignment, spacing and readable measure.

**Reference:** [Figma: auto layout](https://help.figma.com/hc/en-us/articles/360040451373-Guide-to-auto-layout), [Figma: components](https://help.figma.com/hc/en-us/articles/360038662654-Guide-to-components-in-Figma).

### D05 · P2 · There is no single reconciled visual baseline

**Scope:** Figma / implementation handoff · **Basis:** Observed version differences; project governance choice

**Evidence:** The guide uses a light canvas and rust accent; current concepts use navy, blue and coral. Concept typography is Manrope/DM Sans; the deployed site loads Spectral/IBM Plex Sans/IBM Plex Mono. The repository’s existing Figma pointer names a different file, UgtCQvjyZpBQVOxhZAK4sk, while this audit inspects OTfzO4cl4mosafK3Y74ayI.

**Why it matters:** A developer cannot safely infer which palette, font system, file and content version should ship. These may be valid alternatives, but their status is not reconciled.

**Recommended fix:** Name the approved implementation baseline, retain earlier directions as archived proposals, and version the palette, typography, components and content together. Link the correct file and frame IDs in project records.

**Acceptance check:** One handoff record identifies the approved file, frames, token version and corresponding code commit. Match browser and Figma at the same viewport.

**Reference:** [Shared Figma working practices](https://github.com/taitgoodwin-gmail/design-knowledge-base/blob/1332a7f3dc3aeaf1c4d144f30b81918669b532c3/tools/figma/README.md).

### D06 · P2 · Reusable tokens exist but are inconsistently connected

**Scope:** Figma design system · **Basis:** Observed binding inventory; implementation recommendation

**Evidence:** The file contains 15 variables, eight text styles, seven components and 104 instances. All 140 style-guide nodes have no variable bindings and all 75 guide text nodes have no text-style assignment. Desktop Method and GEO each have only two nodes with variable bindings; mobile counterparts have 91 and 65. Current coral #FF6B4A is absent from the 15-token collection.

**Why it matters:** Changing a named token or text style will not reliably update the guide and all screens. Counts identify inconsistent coverage; they do not imply that every decorative node must be bound.

**Recommended fix:** Add semantic status/action roles and bind applicable repeated colors, spacing and typography. Generate guide specimens from the same components and styles used on screens.

**Acceptance check:** Change a token in an isolated duplicate and confirm all intended consumers update. Check remaining literal values deliberately and document exceptions.

**Reference:** [Figma: variables, collections and modes](https://help.figma.com/hc/en-us/articles/14506821864087-Overview-of-variables-collections-and-modes), [Figma: components](https://help.figma.com/hc/en-us/articles/360038662654-Guide-to-components-in-Figma).

### D07 · P2 · Typography and interaction states need consolidation

**Scope:** Figma design system · **Basis:** Observed inventory; handoff recommendation

**Evidence:** The desktop report contains 18 Inter text nodes and the mobile report eight, amid the Manrope/DM Sans system. There are no component sets in the export. A focus example exists in the menu specification, but a consistent button/link state family is not established.

**Why it matters:** Text and interactive states may drift during implementation. Lack of component sets alone is not a Figma rule violation; the gap is the incomplete handoff of recurring states.

**Recommended fix:** Assign role-based text styles and define relevant default, hover, focus-visible, pressed and disabled states. Include long labels and actual hit areas.

**Acceptance check:** Inspect all report text roles and exercise repeated controls with mouse and keyboard in code. State coverage can use variants or another explicit documented pattern.

**Reference:** [Figma: components](https://help.figma.com/hc/en-us/articles/360038662654-Guide-to-components-in-Figma), [Shared Figma working practices](https://github.com/taitgoodwin-gmail/design-knowledge-base/blob/1332a7f3dc3aeaf1c4d144f30b81918669b532c3/tools/figma/README.md).

### D08 · P1 · Visible links are missing prototype destinations

**Scope:** Figma prototype · **Basis:** Observed missing wiring; prototype acceptance recommendation

**Evidence:** Homepage secondary link 13:196 (“View illustrative report”) and report secondary link 13:766 (“Learn what GEO means”) have no hyperlink or reaction on themselves or their ancestors. Research source URL text 14:969 and 14:976 likewise has no link/reaction. Other navigation is wired; 178 reaction-bearing records were inspected.

**Why it matters:** Important reading journeys stop in the prototype and source verification links cannot be followed there.

**Recommended fix:** Connect each CTA to its corresponding frame and source entries to their URLs. Put hotspots on the actual control; review action rows with overlapping parent/child hotspots.

**Acceptance check:** Execute home→report→GEO and research→source, then Back and restart in presentation view. This audit inspected wiring; it did not certify all 178 interactions through execution.

**Reference:** [Figma: connect prototypes](https://help.figma.com/hc/en-us/articles/360040315773-Connect-your-prototype).

### D09 · P2 · Research navigation is inconsistent between views

**Scope:** Figma navigation · **Basis:** Observed navigation mismatch; information-architecture recommendation

**Evidence:** Research is absent from the desktop header/footer but is present in the mobile open-menu frame. Desktop Research highlights “What is GEO.” The site-plan intentionally nests Research under Learn, but there is no clear subnavigation/current-page indication on the Research screen.

**Why it matters:** The hierarchy and current location are harder to understand; mobile and desktop offer different direct paths.

**Recommended fix:** Choose a consistent hierarchy: a clearly labeled Learn section with Research subnavigation, or a direct Research link. Align active states and footer paths.

**Acceptance check:** From every relevant route, locate Research and identify the current page on both layouts without guessing.

**Reference:** [Shared Figma working practices](https://github.com/taitgoodwin-gmail/design-knowledge-base/blob/1332a7f3dc3aeaf1c4d144f30b81918669b532c3/tools/figma/README.md).

### D10 · P2 · Menu specifications do not establish implemented accessibility

**Scope:** Figma handoff · **Basis:** Observed specification gap; implementation choice

**Evidence:** Frame 14:873 includes tab numbers and instructions to trap focus and make the background inert. The close action is BACK, correctly preserving navigation history. The file’s mobile menu is explicitly a Home example; annotations are shown inside the screen.

**Why it matters:** A screenshot cannot prove keyboard behavior. Applying modal focus trapping to a normal disclosure navigation would also be the wrong interaction model.

**Recommended fix:** Choose modal drawer versus nonmodal disclosure explicitly. Keep annotations outside the visitor screen and specify the correct focus, Escape, background and scroll behavior for that model.

**Acceptance check:** Test the chosen implementation with keyboard and a screen reader. Live-site disclosure-menu tests passed opening, next-link focus and Escape return; this does not verify the proposed Figma drawer.

**Reference:** [Figma: connect prototypes](https://help.figma.com/hc/en-us/articles/360040315773-Connect-your-prototype), [Shared Figma working practices](https://github.com/taitgoodwin-gmail/design-knowledge-base/blob/1332a7f3dc3aeaf1c4d144f30b81918669b532c3/tools/figma/README.md).

### D11 · P2 · Copy dismisses useful metrics too broadly

**Scope:** Figma copy · **Basis:** Observed methodological overstatement; our measurement practice

**Evidence:** Method 13:550 describes automated SEO scores as “fallacies”; homepage 13:246 contrasts evidence with unprovable scores. Proposed observed-answer evidence is useful, but Lighthouse and other well-defined measurements can support specific technical conclusions.

**Why it matters:** The argument conflicts with the intended use of Google quality auditing and obscures the difference between a valid limited metric and an unsupported composite.

**Recommended fix:** Say what each measurement establishes and what it cannot establish. Keep technical quality, search performance, observed answers and business outcomes separate; disclose scoring definitions and limitations.

**Acceptance check:** Read the method alongside the Lighthouse playbook: neither claims all scores prove outcomes nor rejects valid technical diagnostics.

**Reference:** [Shared Lighthouse audit playbook](https://github.com/taitgoodwin-gmail/design-knowledge-base/blob/1332a7f3dc3aeaf1c4d144f30b81918669b532c3/tools/google-web-quality/lighthouse-audit-playbook.md).

### D12 · P2 · Development status crowds out visitor value

**Scope:** Figma copy and hierarchy · **Basis:** Observed content structure; design recommendation and hypothesis

**Evidence:** Availability, About, footer and report repeat owner decisions, unconfigured mailboxes, undefined offers and unbuilt pipelines. The mobile homepage is 7,228px tall and the desktop hero alone is 975px. Long pages are not inherently wrong; much of this length repeats internal status rather than helping the visitor decide.

**Why it matters:** The target audience, concrete problem, useful output and available next step are harder to find. The effect on comprehension is a testable UX hypothesis.

**Recommended fix:** Lead with the buyer problem and one useful artifact. Retain a concise accurate availability notice and point to a detailed status page when needed. Move internal decisions into project notes.

**Acceptance check:** Run a short comprehension test: who is this for, what does it do, what evidence will I receive, what can I do now? Compare completion and answers before/after.

**Reference:** [Google: helpful, reliable, people-first content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content).

### D13 · P2 · Desktop and mobile are separate editorial versions

**Scope:** Figma content parity · **Basis:** Observed content divergence; implementation recommendation

**Evidence:** Desktop GEO says “Source Authority”; mobile says “Clear Source Content.” Desktop About has five principles in a grid; mobile adds a separate perspective section and revised statements. The desktop typo “04 / GUARANTEALS” is corrected on mobile. These are not just responsive rearrangements.

**Why it matters:** A developer has to choose which copy and concept are authoritative, and corrections may reach only one version.

**Recommended fix:** Use one approved content source for responsive variants, with explicitly justified short labels where necessary. Correct “GUARANTEALS” to “GUARANTEES.”

**Acceptance check:** Compare headings, claims, links and status labels side by side. Any intentional differences have a documented reason.

**Reference:** [Shared Figma working practices](https://github.com/taitgoodwin-gmail/design-knowledge-base/blob/1332a7f3dc3aeaf1c4d144f30b81918669b532c3/tools/figma/README.md).

### D14 · P2 · Status vocabulary and evidence promises are underspecified

**Scope:** Figma report model · **Basis:** Observed schema ambiguity; product-design recommendation

**Evidence:** The illustrative report mixes Observed, Not Collected, Unmeasured, [UNCOLLECTED] and [NOT TRACKED]. About promises exact model parameters for every documented answer even though consumer interfaces may not expose them. All report data is explicitly fictional.

**Why it matters:** The state labels can be mistaken for interchangeable meanings and the evidence contract may promise unavailable metadata.

**Recommended fix:** Define collection status separately from finding/result status. Distinguish not attempted, failed, collected, observed absence and not measurable. Record available model/product metadata and explicitly mark unknown values.

**Acceptance check:** Exercise representative successful, absent, failed and unavailable examples; every state has a definition and cannot be mistaken for zero.

**Reference:** [Shared Lighthouse audit playbook](https://github.com/taitgoodwin-gmail/design-knowledge-base/blob/1332a7f3dc3aeaf1c4d144f30b81918669b532c3/tools/google-web-quality/lighthouse-audit-playbook.md).

### D15 · P3 · The sample preview is named interactive without demonstrated interaction

**Scope:** Figma concept · **Basis:** Observed naming mismatch; editorial recommendation

**Evidence:** Homepage section 13:254 is titled “The Interactive Brief,” but the inspected design presents static sample states and navigation to a report. It does not demonstrate a working evidence drilldown.

**Why it matters:** The label raises expectations the current prototype does not establish.

**Recommended fix:** Call it “Sample report preview” until specific interactions are designed and verified, or implement a meaningful drilldown with retained evidence.

**Acceptance check:** The label accurately describes what a visitor can do in the demonstrated prototype.

**Reference:** [Figma: connect prototypes](https://help.figma.com/hc/en-us/articles/360040315773-Connect-your-prototype).

## Recommended sequence

1. **Repair verified live defects:** W01–W04 first. Keep the site’s existing evidence disclosures and working navigation.
2. **Choose the implementation baseline:** resolve the active Figma file, palette, typography, content and availability model before expanding screens.
3. **Repair Figma foundations:** D01–D08; bind applicable tokens, normalize cards and text sizing, remove internal instructions, correct links, and define recurring states.
4. **Edit the visitor journey:** reconcile desktop/mobile copy; clarify what can be used now; remove unsupported platform claims; lead with real useful evidence.
5. **Improve and remeasure performance:** address the verified blocking chain, then run comparable repeated mobile measurements.
6. **Complete assurance evidence:** keyboard and screen-reader testing, real zoom/reflow, all theme/state combinations, structured-data validation for intended uses, Search Console and field measurements where data exists. Do not mark these passed from this report alone.

## Frame-by-frame coverage

The older homepage pair and notes are retained as historical exploration; they are not silently treated as the current seven-page design. The four style-guide frames are evaluated as foundations, not customer pages.

| Frame | Size | Nodes / text | Review focus |
|---|---|---|---|
| [Style Guide — Color](https://www.figma.com/design/OTfzO4cl4mosafK3Y74ayI/?node-id=12-108) | 1280 × 853 | 45 / 25 | D02, D05, D06 |
| [Style Guide — Typography](https://www.figma.com/design/OTfzO4cl4mosafK3Y74ayI/?node-id=12-153) | 1280 × 853 | 23 / 14 | D05, D06, D07 |
| [Style Guide — Spacing](https://www.figma.com/design/OTfzO4cl4mosafK3Y74ayI/?node-id=12-176) | 1280 × 922 | 46 / 23 | D06; named spacing scale is useful |
| [Style Guide — Brand](https://www.figma.com/design/OTfzO4cl4mosafK3Y74ayI/?node-id=12-82) | 1280 × 706 | 26 / 13 | D02, D05, D06 |
| [MindLeverX — Homepage Concept](https://www.figma.com/design/OTfzO4cl4mosafK3Y74ayI/?node-id=13-167) | 1440 × 5204 | 151 / 85 | D01, D06, D08, D11, D12, D15 |
| [MindLeverX — Homepage Concept / Mobile](https://www.figma.com/design/OTfzO4cl4mosafK3Y74ayI/?node-id=13-322) | 390 × 7228 | 146 / 82 | D01, D06, D12, D14 |
| [site-plan](https://www.figma.com/design/OTfzO4cl4mosafK3Y74ayI/?node-id=13-43) | 1440 × 2445 | 122 / 70 | Planning artifact; D05, D11, D12 |
| [MindLeverX — Method](https://www.figma.com/design/OTfzO4cl4mosafK3Y74ayI/?node-id=13-480) | 1440 × 3207 | 121 / 68 | D06, D11, D12 |
| [MindLeverX — What is GEO](https://www.figma.com/design/OTfzO4cl4mosafK3Y74ayI/?node-id=13-602) | 1440 × 2556 | 81 / 46 | D06, D13; qualify platform claims |
| [MindLeverX — Illustrative Report](https://www.figma.com/design/OTfzO4cl4mosafK3Y74ayI/?node-id=13-682) | 1440 × 1697 | 99 / 54 | D02, D03, D07, D08, D14 |
| [MindLeverX — Research / Evidence](https://www.figma.com/design/OTfzO4cl4mosafK3Y74ayI/?node-id=13-791) | 1440 × 3714 | 118 / 73 | D02, D04, D08, D09 |
| [MindLeverX — About](https://www.figma.com/design/OTfzO4cl4mosafK3Y74ayI/?node-id=13-893) | 1440 × 2451 | 72 / 41 | D04, D12, D13, D14 |
| [MindLeverX — Availability](https://www.figma.com/design/OTfzO4cl4mosafK3Y74ayI/?node-id=13-966) | 1440 × 1865 | 86 / 44 | D02, D12 |
| [MindLeverX — Method / Mobile](https://www.figma.com/design/OTfzO4cl4mosafK3Y74ayI/?node-id=14-266) | 390 × 5057 | 135 / 66 | D06, D11, D12 |
| [MindLeverX — What is GEO / Mobile](https://www.figma.com/design/OTfzO4cl4mosafK3Y74ayI/?node-id=14-403) | 390 × 4384 | 84 / 44 | D13; preserve clearer wording |
| [MindLeverX — Illustrative Report / Mobile](https://www.figma.com/design/OTfzO4cl4mosafK3Y74ayI/?node-id=14-489) | 390 × 3054 | 101 / 51 | D02, D07, D14 |
| [MindLeverX — Research / Evidence / Mobile](https://www.figma.com/design/OTfzO4cl4mosafK3Y74ayI/?node-id=14-592) | 390 × 5821 | 123 / 71 | D01, D02, D08, D12 |
| [MindLeverX — About / Mobile](https://www.figma.com/design/OTfzO4cl4mosafK3Y74ayI/?node-id=14-701) | 390 × 4490 | 82 / 45 | D01, D12, D13, D14 |
| [MindLeverX — Availability / Mobile](https://www.figma.com/design/OTfzO4cl4mosafK3Y74ayI/?node-id=14-785) | 390 × 3804 | 86 / 46 | D12, D14 |
| [MindLeverX — Mobile Menu Open](https://www.figma.com/design/OTfzO4cl4mosafK3Y74ayI/?node-id=14-873) | 390 × 1515 | 88 / 33 | D09, D10 |
| [Desktop · 1440](https://www.figma.com/design/OTfzO4cl4mosafK3Y74ayI/?node-id=2-26) | 1440 × 5056 | 143 / 89 | Older exploration; D02, D05 |
| [Mobile · 390](https://www.figma.com/design/OTfzO4cl4mosafK3Y74ayI/?node-id=2-27) | 390 × 6829 | 134 / 85 | Older exploration; D05 |
| [Design notes & components](https://www.figma.com/design/OTfzO4cl4mosafK3Y74ayI/?node-id=2-28) | 850 × 813 | 15 / 11 | Internal notes/components; keep separate from visitor screens |

## Line-by-line evidence and interpretation

The accompanying searchable HTML and CSVs preserve every exported Figma text layer and every extracted live HTML text run, including repeated navigation/footer text. Findings are linked where a specific line triggers them; shared-system and section findings also apply. “No additional line-specific finding” is a review disposition, not a claim of standards compliance. The 2,127-node CSV is a structural inventory, not 2,127 independently certified interactions.

Source line numbers in the live-copy appendix refer to the saved deployed HTML, which includes build-injected CSS and metadata. Source-code references inside findings refer to the pinned repository files and can therefore have different line numbers. All evidence was captured on 23 September 2026; live Figma and web pages can change after capture.

## Limits that remain explicit

- No user research or conversion experiment was run; proposed improvements to trust, comprehension and conversion are hypotheses.
- No full screen-reader, browser zoom, dark-appearance or cross-browser matrix was executed. Responsive geometry and selected keyboard controls were tested.
- No external-source link crawl, independent reconstruction of the July case-study measurements, Google Search Console inspection, real-user performance dataset or AI-answer collection was performed.
- Figma contrast uses solid foreground and composited ancestor fills. It identifies specific design-color defects, not complete rendered accessibility. No original Figma frame was resized for stress testing.
- The full prototype was structurally inspected; every reaction was not clicked. API success and a screenshot are not proof of backend operation.
- JSON-LD parsed successfully and matched basic visible page identities. This does not establish a supported rich-result type or successful Rich Results Test.
- Missing CSP/COOP/Trusted Types headers are not treated as evidence of an exploitable vulnerability. Security testing was limited to public response-header observation and Lighthouse’s surface checks.

## Reusable reference location

The maintained Lighthouse/Google library is already stored in the private design-knowledge-base repository at `tools/google-web-quality/`, commit `1332a7f3dc3aeaf1c4d144f30b81918669b532c3`. The earlier overview is preserved under that module’s history directory and marked superseded. This audit is a dated project record; it does not turn observed site defects into universal platform requirements.

## Source register

The official sources below were checked on 23 September 2026. Repository links are pinned to the reference snapshot. Preserve their scope and recheck changeable guidance before implementation or release.

- [WCAG 2.2: contrast minimum](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html) — Requirement when claiming the project’s WCAG 2.2 AA target.
- [WCAG 2.2: reflow](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html) — Requirement when claiming WCAG 2.2 AA; tables can need two-dimensional layout, but information must remain available.
- [Figma: auto layout](https://help.figma.com/hc/en-us/articles/360040451373-Guide-to-auto-layout) — Documented tool behavior; layout choices are our recommendations.
- [Figma: components](https://help.figma.com/hc/en-us/articles/360038662654-Guide-to-components-in-Figma) — Documented tool behavior; reuse policy is our implementation choice.
- [Figma: variables, collections and modes](https://help.figma.com/hc/en-us/articles/14506821864087-Overview-of-variables-collections-and-modes) — Documented tool behavior; token architecture is our implementation choice.
- [Figma: connect prototypes](https://help.figma.com/hc/en-us/articles/360040315773-Connect-your-prototype) — Documented tool behavior; requested journeys define the acceptance test.
- [Google: optimizing for generative AI features](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide) — Official recommendation scoped to Google Search.
- [Google: helpful, reliable, people-first content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) — Official recommendation, not a numeric ranking checklist.
- [Chrome: render-blocking requests](https://developer.chrome.com/docs/performance/insights/render-blocking) — Official performance guidance; savings are estimates.
- [Shared Figma working practices](https://github.com/taitgoodwin-gmail/design-knowledge-base/blob/1332a7f3dc3aeaf1c4d144f30b81918669b532c3/tools/figma/README.md) — Our documented working practices, not universal Figma requirements.
- [Shared Lighthouse audit playbook](https://github.com/taitgoodwin-gmail/design-knowledge-base/blob/1332a7f3dc3aeaf1c4d144f30b81918669b532c3/tools/google-web-quality/lighthouse-audit-playbook.md) — Reusable measurement practice; source register is linked inside.

## Deliverable index

- `report.html`: readable report and searchable line-review appendix.
- `report.md`: portable report.
- `findings.csv` / `findings.json`: prioritized implementation backlog.
- `figma-line-review.csv`: 1,179 text-layer records.
- `live-copy-line-review.csv`: all extracted live text runs.
- `figma-node-inventory.csv`: all 2,127 nodes.
- `frame-coverage.csv`: all 23 top-level frames.
- `lighthouse-results.json`: 14 visible report results.
- `evidence/`: captured Figma node data, screenshots, deployed HTML, HTTP manifest and browser verification record.
