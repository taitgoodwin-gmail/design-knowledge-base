# MindLeverX comprehension and navigation study worksheet

Prepared 19 September 2026 • Proposed formative study • No participants tested

This worksheet operationalizes the [UI/UX design playbook](uiux-design-playbook.md). It is a proposed protocol, not an industry-mandated procedure. Its aim is to identify misunderstandings and interaction problems in the current preview before using behavioral metrics to judge improvements.

**Research decision.** Determine whether the current homepage helps intended prospects understand current availability, sample measurements, the request process, and where supporting information can be found.

**Participants and scope.** The provisional audience is people involved in evaluating marketing or growth services for B2B SaaS companies. Confirm the actual audience before recruitment. Include relevant differences in GEO familiarity, decision-making responsibilities, device use, and access needs. The number and composition of participants must follow the study’s learning goals and resources; this protocol does not prescribe a universal sample size or a statistical inference from a convenience sample.

**Before the session.** Record the page version, date, viewport, browser, device, and scenario. Verify the actual preview behavior with the responsible owner so the interpretation rubric is accurate. Prepare a safe test environment if submission is ever included. This initial study stops before sending or saving a request. Obtain appropriate consent before recording sessions and avoid collecting unnecessary personal information.

**Opening script.**

“We are evaluating the website, not your knowledge. Please explore it as you normally would. There are no expected positive opinions. I may wait before answering questions so we can see what the page explains on its own. We will not submit an audit request or enter your real contact information.”

**Task 1: understand the offer.**

“Imagine you are considering help with your company’s visibility in AI answers. Explore this page enough to decide what you would investigate next.”

After natural exploration: “In your own words, what does this company offer today? What seems available now, and what seems planned?”

Record the answer before probing. Then ask: “What on the page led you to that conclusion?” Do not introduce the terms “sample,” “local,” or “not connected” before the initial interpretation.

**Task 2: interpret a score.**

Point to the engine scorecard: “What do you think this percentage represents? What would you need to know before using it in a decision?”

Record whether the participant recognizes illustrative status, supplies an unsupported metric definition, asks for a denominator or period, or expresses uncertainty. Uncertainty is a legitimate response when the page is underspecified. Do not mark someone wrong for failing to infer information the page does not provide.

**Task 3: inspect supporting evidence.**

“Find information you would use to decide whether the company’s approach is credible.”

Record the first route, destinations visited, whether relevant material was found, requests for help, and the reasons the participant considers it useful. If the task is abandoned, record the stopping point and reason. Keep absence of evidence distinct from failure to find existing evidence.

**Task 4: predict the request outcome.**

“Before using this audit-request button, explain what you expect would happen immediately and afterward.”

Ask what they expect to receive, whether they expect an email, whether they expect an audit to run, and what remains uncertain only after their initial unprompted response. Stop before submission.

**Task 5: retrospective discussion.**

“What felt clear? What required interpretation? Which information mattered most to your decision? What would you need before proceeding?”

Treat expressed preferences as one form of evidence. Compare them with observed behavior instead of assuming that preference proves successful task performance.

**Interpretation rubric: draft to confirm against the tested build.**

| Item | Accurate current-preview interpretation | Misunderstanding to investigate |
|---|---|---|
| Measurement status | Homepage figures are illustrative | Figures treated as actual company or customer performance |
| Request behavior | The preview says the request is stored locally | An audit or email is assumed to run automatically |
| Future service | Some workflows are described as planned | All advertised workflows assumed available today |
| Engine percentage | Definition or basis is recognized as insufficiently specified | An exact unsupported meaning is confidently supplied |
| Evidence route | A relevant source or explanation is found and accurately described | A sample illustration is treated as proof of results |

Use descriptive categories: accurate, partly accurate, inaccurate, uncertain, not elicited. Preserve notes explaining each classification. Do not collapse these into a single “UX score.” The categories are a project-specific rubric.

**Session record template.**

| Field | Entry |
|---|---|
| Anonymous participant ID | |
| Relevant background and access needs | |
| Build and test conditions | |
| Unprompted explanation of offer | |
| Interpretation of score and sample status | |
| Evidence route and outcome | |
| Expected request outcome | |
| Assistance or moderator intervention | |
| Observed errors and recovery | |
| Participant’s explanation | |
| Researcher interpretation and alternatives | |

**Analysis discipline.** Keep observations separate from interpretations. Record contradictory cases. Identify whether a problem appears related to wording, grouping, navigation, service ambiguity, or an access barrier. Report what was tested and which audiences or conditions were absent. If comparing variants in a formative study, account for learning effects: seeing the first version may teach someone how to interpret the second. Do not call a small preference comparison a causal experiment.

**Proposed revision decision.** Treat a consequential misunderstanding as a reason to investigate and revise its likely cause. Review the revision against the actual service behavior and test it again. Determine release acceptance criteria separately; this study is not an accessibility-conformance assessment or a production release gate.

For a later quantitative experiment, specify the hypothesis, primary measure, denominator, randomization unit, sample/power assumptions, duration, exclusion rules, guardrail measures, and analysis before launch. If available traffic cannot support the intended inference, continue qualitative work or narrow the question rather than report an unsupported lift.

The method draws on [NIST’s usability evaluation guidance](https://nvlpubs.nist.gov/nistpubs/hb/2017/NIST.HB.161.pdf), [W3C’s guidance on user evaluation and its limits](https://www.w3.org/WAI/test-evaluate/involving-users/), and [Microsoft’s experiment-design guidance](https://www.microsoft.com/en-us/research/articles/patterns-of-trustworthy-experimentation-pre-experiment-stage/). The specific tasks and rubric are proposals for MindLeverX.
