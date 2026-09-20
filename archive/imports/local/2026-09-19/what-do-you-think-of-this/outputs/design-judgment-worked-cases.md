# Design judgment: resolving conflicts and testing explanations

Advanced companion to the [UI/UX playbook](uiux-design-playbook.md). Sources checked 19 September 2026. The examples below distinguish published criteria, research guidance, observations, and our proposed decisions. They teach a reasoning method; they do not certify expertise or report a completed user study.

**1. Apparent conflicts often disappear when you restore scope.**

“How large must a button be?” is incomplete. Specify the platform, input, conformance target, actual interactive region, and surrounding controls.

| Source | What it specifies | Scope |
|---|---|---|
| WCAG 2.2 SC 2.5.8, Target Size (Minimum) | At least 24 × 24 CSS pixels, subject to specified exceptions | Level AA, pointer targets on web content |
| WCAG 2.2 SC 2.5.5, Target Size (Enhanced) | At least 44 × 44 CSS pixels, subject to its exceptions | Level AAA |
| Google Android accessibility guidance | Recommends touch targets of at least 48 × 48dp | Android; dp is a platform unit, not a prescription for CSS |

Sources: [WCAG normative standard](https://www.w3.org/TR/WCAG22/#target-size-minimum), [W3C minimum explanation](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html), [W3C enhanced explanation](https://www.w3.org/WAI/WCAG22/Understanding/target-size-enhanced.html), [Google Android guidance](https://support.google.com/accessibility/android/answer/7101858?hl=en).

The minimum criterion includes spacing, equivalent-control, inline, user-agent-control, and essential exceptions; inspect their actual conditions before using one. The enhanced criterion does not inherit the minimum criterion's spacing exception. The graphic inside a button and the region that accepts input can have different dimensions.

Our proposed web practice: aim for at least 44 × 44 CSS pixels for standalone primary actions where appropriate, check the actual interactive area, and evaluate surrounding layout and input needs. This is a project choice above the AA size baseline, not a claim of whole-site AAA conformance. Do not enlarge every inline link into a block button by applying that rule without context.

Exercise: a control has a 20-pixel icon inside a 48-pixel square button. What do you measure? Answer: verify the region that actually accepts the action. Icon size alone cannot establish a target-size failure. A screenshot of the icon alone is insufficient evidence.

**2. Use constraints to establish acceptable options, then compare tradeoffs.**

Our synthesis is a two-stage decision process:

1. Identify applicable requirements and factual constraints. Eliminate options that fail them.
2. Compare the remaining options against the user's task, using evidence appropriate to the question.

This is our decision policy, not a named external standard. Its accessibility basis is WCAG's conformance model: satisfying some criteria does not compensate for failing another applicable criterion at the claimed level. [WCAG conformance](https://www.w3.org/TR/WCAG22/#conformance-reqs)

For a sample scorecard, our factual constraint is that the presentation must identify illustrative data accurately. We can then compare a brief adjacent explanation with a somewhat longer one. The shortest version is not automatically best; the relevant question is whether it supports correct interpretation without unnecessary effort.

Progressive disclosure offers a way to separate immediately needed information from secondary detail. It requires a sensible split and a discoverable route to the detail. It does not tell us which facts are essential for this particular buyer. [Nielsen: progressive disclosure](https://www.nngroup.com/articles/progressive-disclosure/)

Proposed application: keep sample status and the metric's meaning with the number; put detailed collection rules behind a clearly labeled methodology link. Test whether buyers understand the first layer and can find the second. If they need the supposedly secondary detail to make the primary decision, revise the split.

**3. Diagnose competing explanations before selecting a repair.**

Suppose a future study finds that a participant does not open the methodology. That observation alone does not tell us why. The following are hypothetical alternatives, not findings:

| Possible explanation | Evidence that would help distinguish it | Candidate response if supported |
|---|---|---|
| The link was not noticed | Unprompted navigation, followed by a retrospective probe | Change placement or visual emphasis |
| Its label did not predict useful content | Ask what the participant expected behind the link | Improve the label |
| The participant already had enough information | Accurate interpretation without visiting it | Preserve the concise route |
| The participant did not care about the measure | Explanation of their actual decision criteria | Reconsider the metric's prominence |
| Navigation could not be operated | Direct keyboard or assistive-technology evaluation | Repair interaction semantics or behavior |

These tests do not guarantee a unique diagnosis. The purpose is to avoid treating every missed click as a visibility problem. Information scent depends on the task and the cues a person interprets. [NN/G: information scent](https://www.nngroup.com/articles/information-scent/)

Exercise: propose two explanations for someone spending a long time on the page. “Interested” and “confused” are both plausible. State what additional observation would help separate them. More time alone does not decide which explanation is right; Google's HEART paper explicitly discusses ambiguity in generic behavioral metrics. [Google research](https://research.google/pubs/measuring-the-user-experience-on-a-large-scale-user-centered-metrics-for-web-applications/)

**4. Distinguish evidence that a problem exists from evidence that a remedy works.**

Our proposed claim ladder:

| Claim | What would support it |
|---|---|
| “The page displays illustrative percentages.” | Inspection of the tested page and its labels |
| “This participant interpreted them as real results.” | An actual session record, with context and moderator prompts |
| “This interpretation is common among our intended buyers.” | A sampling and measurement design that supports population inference |
| “The new presentation reduces misunderstanding.” | A credible comparison that addresses alternative causes |
| “The change increases valuable customer acquisition.” | Evidence for that business outcome, with suitable attribution and time horizon |

Advancing one row requires new evidence. A citation to a heuristic does not supply missing participant observations, and a successful comprehension study does not establish a revenue effect.

Microsoft's experimentation guidance supports predeclared hypotheses, appropriate metrics, randomization, adequate power, and data-quality checks. It also cautions against assuming that results in an internal or special population will transfer exactly to the general population. [Microsoft Research](https://www.microsoft.com/en-us/research/articles/patterns-of-trustworthy-experimentation-pre-experiment-stage/)

For a formative study, report participant observations and limits directly. Use the [research worksheet](mindleverx-research-worksheet.md) to investigate the first misunderstandings before designing a quantitative effect study. A task instructed by a moderator also differs from spontaneous browsing; preserve that distinction when reporting what happened.

**5. Treat source accuracy as part of interface design.**

Rechecking the current homepage found an attribution issue that does not require a user study to identify. The page attributes “Citation, not clicks, is the KPI” to Pew. That statement is not supported as a quotation by the cited Pew article.

Pew reports traditional-result clicks on 8% of visits with a Google AI summary, versus 15% without; clicks on a link within the summary occurred on 1% of visits with a summary. Its scope was Google searches associated with tracked browsing by 900 U.S. adults in March 2025, with search results subsequently collected in April. This does not establish a universal KPI hierarchy across answer engines. [Pew article and methods](https://www.pewresearch.org/short-reads/2025/07/22/google-users-are-less-likely-to-click-on-links-when-an-ai-summary-appears-in-the-results/)

Recommended correction: remove the unsupported quotation attribution, describe the finding within its scope, and label the choice to measure citations as MindLeverX's strategic proposal. The original study, the company's interpretation, and a promised customer outcome are three different claims.

This is also why familiar logos and academic references cannot substitute for a source that actually supports the nearby statement. Stanford's credibility guidelines recommend making information verifiable; their historic research does not establish a current conversion effect for this site. [Stanford credibility guidelines](https://credibility.stanford.edu/guidelines/)

An adjacent applicability check: Google's official documentation says its AI Overviews and AI Mode use existing SEO foundations, require no special AI markup, and do not guarantee inclusion. This is guidance for those Google Search features. It does not prove identical behavior in ChatGPT, Claude, Perplexity, or the Gemini app. [Google Search documentation](https://developers.google.com/search/docs/appearance/ai-features)

**6. Teach decisions through counterexamples.**

Use the following three prompts to check understanding. These are custom teaching exercises, not a standardized examination.

| Prompt | Strong answer |
|---|---|
| “Our control is below 44 CSS pixels, therefore it fails AA.” | Identify the applicable AA criterion, measure the target, and inspect exceptions; do not substitute the AAA number. |
| “The disclosure lowered requests, therefore it damaged UX.” | Check whether visitors now understand availability and whether the requests are appropriate. Request volume alone does not settle UX quality. |
| “A respected study supports the idea, therefore our redesign will work.” | Identify what transfers, what differs, and the evidence still needed for this audience and implementation. |

For each answer, require a concrete observation, applicable source, proposed action, alternative explanation, and disconfirming test. A disconfirming test is one whose result could make you revise the recommendation. This turns a critique into an argument that can be checked.

**How these documents fit together.**

Read the playbook for the underlying concepts. Use these cases to practice decisions under competing advice. Use the worksheet to prepare a real study. Technical checks, user research, and business evaluation answer different questions; combine their evidence without claiming that any one replaces the others. W3C explicitly recommends combining user involvement with conformance evaluation. [W3C: involving users](https://www.w3.org/WAI/test-evaluate/involving-users/)

This research and teaching package is complete as an explanatory deliverable. It does not establish that the website meets all accessibility requirements, that the proposed changes improve outcomes, or that the reader has demonstrated mastery. Those claims require their own evidence.
