# UI/UX design playbook: reasoning, standards, and evidence

Prepared for MindLeverX • 19 September 2026 • Research and teaching edition

Companions: [worked cases in design judgment](design-judgment-worked-cases.md) and [research worksheet](mindleverx-research-worksheet.md).

This guide turns the site review into a reusable practice. Its project rules, exercises, and proposed changes are recommendations. They are not an external certification, a claim of measured business improvement, or evidence that user testing has occurred. The intended teaching outcome is the ability to explain a design decision, trace its basis, recognize its limits, and test it.

The current working audience is prospective customers evaluating an audit. That audience remains a provisional project assumption. A product user, researcher, and buyer can need different routes through the same information.

**1. Begin with a decision someone needs to make.**

UI covers the controls and presentation people encounter. UX includes the broader experience of the service. A beautifully presented request form can therefore coexist with a disappointing experience if the expected service never follows. Norman and Nielsen explicitly distinguish these scopes. [NN/G: definition of UX](https://www.nngroup.com/articles/definition-user-experience/)

For MindLeverX, a useful working task is: “Determine whether this service is relevant to my company and understand what would happen if I requested an audit.” This is our proposed task definition, not a validated finding about every visitor.

Specify four things before evaluating a screen:

| Question | MindLeverX working example |
|---|---|
| Who is acting? | A prospective B2B SaaS customer evaluating help with AI visibility |
| What decision must they make? | Whether the offer merits a request or further investigation |
| What information do they need? | Scope, evidence, availability, requirements, and next steps |
| What would count as success? | An accurate explanation and an informed choice, including choosing not to proceed |

ISO 9241-210 addresses human-centred design across the system life cycle; ISO 9241-11 treats usability as an outcome of use. Only their public catalog descriptions were inspected here. This guide makes no ISO conformance claim. [ISO 9241-210](https://www.iso.org/standard/77520.html), [ISO 9241-11](https://www.iso.org/standard/63500.html)

Exercise: rewrite the task for a returning monitoring customer. An appropriate answer should shift toward interpreting changes, inspecting supporting observations, and deciding what work to prioritize. That shift should change the interface priorities too.

**2. Separate what is visible from what people infer.**

Norman describes a designer’s model, a system image, and a user’s model. People infer how a product works from its presentation. The designer cannot assume that an accurate sentence guarantees an accurate overall understanding. [Norman: Design as Communication](https://jnd.org/design-as-communication/)

Observed on the current homepage: an audit CTA, sample percentages, a sample feed, and statements that collection is not connected. Untested interpretation: visitors may infer that the service is operating more fully than the disclosures intend.

Our proposed design response is a coherent description of current availability beside the main action, with sample status attached to each illustrative result. That response needs a comprehension test; adding more disclaimers without testing could simply add reading burden.

Exercise: ask someone to describe what the service does today, then point to the evidence they used. Record the explanation before correcting it. Compare their understanding with the actual behavior of the preview.

**3. Design the route from a question to an answer.**

Information scent describes the cues that help a person predict whether a destination will satisfy an information need. Labels, nearby text, context, and prior knowledge contribute. The same label can be useful for one task and weak for another. [NN/G: Information Scent](https://www.nngroup.com/articles/information-scent/)

For a visitor seeking an example deliverable, “Readiness” may be less predictive than “See an example scorecard.” The replacement is a hypothesis and must accurately describe its destination. “Research” may remain appropriate for someone seeking underlying studies.

Make a route map with three columns: visitor question, promising link, answer at the destination. A mismatch at any point identifies a specific issue to investigate.

Hidden navigation is a separate issue. NN/G found discoverability disadvantages in its comparison of hidden and visible navigation. That supports examining the collapsed menu observed at 1,122px; it does not prescribe a breakpoint or establish a conversion loss on MindLeverX. [NN/G: hidden-navigation research](https://www.nngroup.com/articles/hamburger-menus/)

Exercise: draft one navigation for a buyer and one for a returning product user. Explain which links you expose and which tasks each supports. Do not judge the drafts by link count alone.

**4. Make hierarchy communicate importance and relationships.**

Scale, placement, contrast, spacing, and grouping help establish a reading order. NN/G’s visual-design principles describe these mechanisms. The MindLeverX hero already distinguishes its headline, supporting copy, primary action, and secondary link. [NN/G: visual-design principles](https://www.nngroup.com/articles/principles-visual-design/)

Our implementation proposal is to preserve that structure while bringing the meaning of the scorecard closer to its figures. A large percentage and a distant definition ask the visitor to connect two separated pieces of information. Putting them together is a testable grouping choice.

Proposed scorecard anatomy:

> **Illustrative citation rate**  
> **42%** — example value, not measured  
> A share of valid collected answers that cite the assessed domain.  
> A real result would show the prompt panel, valid observation count, period, engine conditions, and comparison basis.

This is explanatory sample copy, not an assertion that the current 42% has that definition. The operational definition must be settled before implementation.

Exercise: remove the headline and numbers from a screenshot mentally. Identify which elements still look like controls, explanations, and evidence. Explain what visual cues communicate those roles.

**5. Treat accessibility as requirements plus experience.**

The standing project guidance sets WCAG 2.2 AA as the default target. AA conformance involves A and AA criteria and the relevant full-page and complete-process requirements. A passing color sample does not establish conformance. [WCAG 2.2 conformance requirements](https://www.w3.org/TR/WCAG22/#conformance-reqs)

The sampled gray captions previously measured approximately 5.76:1 on white and 5.38:1 on light gray. Those combinations exceed the normal-text contrast threshold, but do not answer every readability question. [W3C: contrast](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html)

A working ticker pause was verified earlier. Other motion and reduced-motion behavior remain untested. [W3C: Pause, Stop, Hide](https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide.html)

For the audit journey, our proposed evaluation covers navigation, labels, keyboard operation, focus visibility, validation, error recovery, and truthful confirmation. Screen-reader and representative-user evaluation should complement technical checks. W3C cautions that neither user involvement nor conformance evaluation alone establishes the whole experience. [W3C: involving users](https://www.w3.org/WAI/test-evaluate/involving-users/)

Exercise: describe the successful submission and failure states in words before drawing them. Include what happened, what the user can do, and which information remains available.

**6. Make the mathematical meaning of a score explicit.**

A composite score combines observations through modeling choices. The OECD/JRC handbook discusses weighting, aggregation, compensability, and sensitivity analysis. Its context is policy indicators; these measurement concepts can inform our scorecard design, but the handbook does not validate any GEO metric. [OECD/JRC handbook](https://www.oecd.org/content/dam/oecd/en/publications/reports/2008/08/handbook-on-constructing-composite-indicators-methodology-and-user-guide_g1gh9301/9789264043466-en.pdf)

Consider a deliberately hypothetical four-dimension score:

| Profile | Dimension 1 | Dimension 2 | Dimension 3 | Dimension 4 | Equal-weight mean |
|---|---:|---:|---:|---:|---:|
| A | 0 | 100 | 100 | 100 | 75 |
| B | 75 | 75 | 75 | 75 | 75 |

The profiles have the same mean and very different weaknesses. If dimension 1 is an essential prerequisite, the mean can hide a blocker. Whether that dimension is truly essential requires evidence; it cannot be decided by the chart style.

For MindLeverX, document what “readiness” means, the component definitions, weights, missing-data policy, and interpretation before relying on an aggregate. Our provisional recommendation is to emphasize component evidence while the aggregate method remains unvalidated.

Exercise: increase dimension 1’s weight to one-half and give the other three one-sixth each. Profile A becomes 50; B remains 75. Explain why choosing weights changes the communicated judgment.

**7. Choose metrics from the intended outcome.**

Google’s HEART framework identifies Happiness, Engagement, Adoption, Retention, and Task success as categories for selecting metrics. Its goals–signals–metrics process links measurement to product objectives. The paper says teams need not use every category and that large-scale metrics complement formative research. [Google’s CHI 2010 publication](https://research.google/pubs/measuring-the-user-experience-on-a-large-scale-user-centered-metrics-for-web-applications/)

Our proposed application:

| Goal | Observable signal | Candidate measure |
|---|---|---|
| Understand current availability | Accurately explains what is available and planned | Correct interpretations among completed study sessions |
| Understand a score | States what it measures and recognizes sample status | Interpretation categories, with unresolved answers retained |
| Locate evidence | Finds relevant supporting information without guidance | Completion, path taken, and assistance required |
| Make an informed request | Correctly predicts the next step before proceeding | Comprehension evidence alongside request behavior |

These are proposed research measures, not current analytics. No single measure stands for overall UX quality.

**8. Match the research method to the question.**

NIST’s usability handbook describes task completion, time, errors, and satisfaction as evaluation measures. Its public-safety context differs from this website; the general measurement concepts are useful here. [NIST Handbook 161](https://nvlpubs.nist.gov/nistpubs/hb/2017/NIST.HB.161.pdf)

Our proposed first study is formative: observe misunderstandings and navigation problems in representative tasks. It would guide revisions without claiming a population conversion effect.

A later controlled experiment needs a falsifiable hypothesis, suitable metrics, a randomization plan, sufficient statistical power, and checks for unintended effects and data problems. Microsoft’s experimentation guidance provides these disciplines. [Microsoft: pre-experiment guidance](https://www.microsoft.com/en-us/research/articles/patterns-of-trustworthy-experimentation-pre-experiment-stage/)

Exercise: distinguish these claims: “Three participants misunderstood the example,” “30% of all buyers misunderstand the example,” and “The redesign reduces misunderstanding.” The first can describe observed sessions. The second needs justified population estimation. The third requires evidence supporting a comparison and causal attribution. One small formative test cannot establish all three.

**9. Preserve decisions in a design system.**

Carbon separates a color’s role from its theme-specific value. Semantic tokens enable consistent changes across components and themes. This is useful implementation guidance, not a requirement to adopt IBM’s palette. [Carbon: color and tokens](https://carbondesignsystem.com/elements/color/overview/)

Our proposal is a small MindLeverX system with named roles for primary text, supporting text, action, focus, border, and status. Each reusable component should specify content, behavior, keyboard interaction, states, and verification evidence. A measurement card would also specify provenance and sample/missing-data states.

Keep a decision record:

| Field | What to record |
|---|---|
| User task | The specific action or decision supported |
| Evidence | Observation, study, criterion, or heuristic; source and check date |
| Applicability | Why it applies to this audience and context |
| Choice | Exact proposed or implemented behavior |
| Alternatives | Material options considered and tradeoffs |
| Verification | Method, result, limitations, and remaining uncertainty |
| Maintenance | What change would trigger a new check |

**A worked conflict-resolution example.**

The homepage needs concise presentation and transparent limits. Our proposed resolution retains essential sample status beside the score, puts a clear metric description within the card, and offers detailed methodology through an obvious link. This applies progressive disclosure while keeping the facts needed for immediate interpretation visible. [NN/G: progressive disclosure](https://www.nngroup.com/articles/progressive-disclosure/)

We would reject a design that hides sample status inside methodology even if it looks cleaner. We would compare acceptable alternatives through comprehension tasks, rather than assigning an aesthetic score to resolve the question. This decision policy is our proposal.

**Assessment exercise.**

Choose one site element. Submit a short critique that includes its user task, the actual observation, one applicable source, the proposed change, a plausible alternative explanation, and the test that would change your mind. A strong answer distinguishes what the interface does from what users are assumed to think. This is a custom teaching rubric, not a certification.

**Evidence boundaries and maintenance.**

Sources were inspected on 19 September 2026 during this thread. Foundational research dates are not evidence of current effect sizes. The homepage text was re-read for this guide; earlier visual measurements are identified as earlier checks. No representative-user sessions, mobile or dark-theme audit, complete accessibility evaluation, or production experiment has been performed. The follow-on worksheet is ready for planning and piloting, not a completed study.

No visual artifact, citation count, or automated checklist establishes design mastery. This playbook supports a repeatable practice whose recommendations can be corrected by evidence.
