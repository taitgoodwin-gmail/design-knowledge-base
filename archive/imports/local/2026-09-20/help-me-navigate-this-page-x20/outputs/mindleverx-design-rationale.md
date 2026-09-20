# MindLeverX: design rationale and element audit

Checked: 20 September 2026. Scope: the locally authored Signal Observatory, Human Current and Proof Studio concept previews in `work/mindleverx-directions.html`. This is not a complete audit of the imported live website or every Figma layer. Figma tab context was read; its selected frame is the earlier bright/playful mobile frame. No Figma designs were modified in this audit.

The previews are exploratory. Their CSS and behavior were inspected, and specified color pairs were calculated. Full rendered, screen-reader, keyboard, mobile and user testing remains outstanding. There is no live AI service or implemented animation in the preview. Theme switching and a source disclosure are implemented.

## Decision framework

- **Standard:** applicable WCAG 2.2 success criteria; default build target AA. W3C Understanding pages explain the normative standard. APG describes recommended widget patterns.
- **Guidance:** established usability heuristics, visual design principles, progressive disclosure, Carbon motion and Microsoft HAX. These guide judgment; they do not prove conversion or business outcomes.
- **Choice:** our application of guidance to MindLeverX, including typography, exact colors and motion timing.
- **Hypothesis:** a proposed effect on comprehension, preference or qualified inquiries that requires testing.

The following tables contain our design choices and judgments. Principle names identify their basis, not a claim that a source prescribes this specific layout.

## Element-by-element audit

| Element | Recognized basis | Decision and purpose | Color and movement |
|---|---|---|---|
| Three concept buttons | Recognition; system status [U] | Keep in review tool. Keep copy identical when comparing visual styles. Remove from customer site. | Maintain pressed state plus outline/check; instant change, no animated page reshuffle. |
| Remembered concept choice | User control [U] | Keep for review convenience; do not silently change a visitor's experience. | No visual flourish needed. |
| Atmosphere/accent controls | User control [U]; contrast [C] | Review-only. Unrestricted accent changes are not validated production themes. | Recheck contrast after any color change. |
| Wordmark and accented x | Consistency [U]; hierarchy [V] | Keep compact; make it a named home link on the real website. | Accent x can repeat as a brand motif. No continuous spinning. |
| Evidence navigation | Recognition [U] | Keep descriptive destination and visible link behavior. | Clear focus treatment; underline or another non-color cue. |
| Our method navigation | Match with real-world meaning [U] | Fix: current destination is answer anatomy, not the complete service method. | Point to genuine method content; normal navigation. |
| GEO / 2026 edition | Minimalism [U] | Remove unless it identifies a meaningful dated report. | Avoid technical-looking decoration that implies measurement. |
| Navigation divider | Grouping [V] | Keep subtle boundary; not essential information. | Static; decorative contrast need not match text contrast. |
| Desktop two-column hero | Balance and hierarchy [V] | Keep message dominant and example secondary. | Bright artwork must not become the first or only focal point. |
| Whitespace and grid | Proximity [V] | Use tighter spacing within groups and larger gaps between them. | Keep these relationships when panels expand and at mobile widths. |
| GEO eyebrow | Recognition [U] | Expand terminology; current 10px treatment is too small for useful explanation. | Quiet but readable. Static. |
| Hero headline | Scale [V]; task-oriented language [U] | Keep customer question prominent. Test whether visitors can explain the service. | Stable, high contrast; no letter-by-letter entrance. |
| Different headlines across themes | Experimental control; implementation choice | Hold wording constant for visual comparison; test messaging separately. | Otherwise preference cannot be attributed to typography or palette. |
| Serif follow-up question | Hierarchy [V] | Keep as a secondary human voice, not a competing headline. | Accent optional; no animated word cycling. |
| Introductory service paragraph | Match to user language [U] | Increase current 13px size; state deliverable and who it serves. | Use a solid or reliably dark backing; static readable text. |
| Explore an example CTA | Recognition; hierarchy [U,V] | Keep descriptive low-commitment action. Add a real inquiry path when available. | Reserve strong fill for main action; visible keyboard focus. |
| Diagonal arrow on CTA | Consistency [U] | Replace: it suggests leaving the page, but currently scrolls within it. | Use down/right arrow matching behavior; icon need not move. |
| Button shape differences | Consistency [U] | Pick one family within the final identity. Shape alone cannot prove trust or conversion. | Rounded, square and soft-square are aesthetic choices. |
| Blue radial atmosphere | Figure/ground [V] | Keep as subordinate decoration if it strengthens identity in testing. | Fixed contrast-safe text region; optional short entrance. |
| Halo circle | Figure/ground [V] | Decorative hypothesis, not a usability necessity or data visualization. | Remove if distracting; no endless pulse behind reading. |
| Elliptical orbits | Continuity/grouping [V] | Remove unless they meaningfully connect answer and evidence, or justify them purely as decoration. | If meaningful, select a citation to highlight its connection; no random orbiting. |
| Human copper arch | Balance [V] | Potential signature shape; no claim that it universally feels trustworthy. | Keep light band away from text; one optional entrance. |
| Proof giant x | Scale/figure-ground [V] | Reduce if it competes with the customer's problem. | Static background silhouette; avoid overlap with readable content. |
| Follow the source label | Signposting [U] | Enlarge current 9px text or remove if redundant. | Match real citation color and number; remain readable. |
| Answer card container | Common region [V] | Keep content together on an opaque reading surface. | Card separates text from atmospheric effects. |
| Card border and shadow | Figure/ground [V] | Keep restrained separation; hard shadow is a style choice. | Shadow should not imply dragging if dragging is unavailable. |
| Card rotation | Legibility; implementation judgment | Straighten interactive text. Current -6°, +4° and +8° rotations add unnecessary reading effort. | Tilt only a decorative backing layer; no pointer-following readable card. |
| Answer anatomy heading and 01 | Hierarchy; recognition [V,U] | Enlarge 8px label. Give number a real relationship or remove it. | No animated count-up or fake precision. |
| Quoted customer question | Match to user language [U] | Keep, but label it as the question, not an observed AI answer. | Stable readable type. |
| Three gray text bars | Visibility of system status [U] | Replace: they resemble a loading skeleton although nothing loads. | Show actual labeled example text; animate only real loading. |
| [1] See the source | Progressive disclosure [D]; disclosure pattern [APG] | Fix promise mismatch: it currently reveals generic explanation. Supply source or rename it. | Button expands nearby panel; clear expanded state; avoid hover-only behavior. |
| Expanded source panel | Progressive disclosure [D] | Show URL, relevant excerpt, date and collection conditions when real evidence exists. | Highlight matching citation and excerpt with number/underline as well as color. |
| Illustrative/not measured disclaimer | Accurate expectations [H2] | Keep adjacent and enlarge current 8px treatment. | Readable contrast; never fade it away. |
| Less guesswork stamp | Minimalism [U] | Optional personality, not evidence. Avoid implied certification. | Static small accent; do not obscure source content. |
| Evidence section background | Grouping [V] | Keep a distinct reading zone after the hero. | Neutral/light surface; no moving background. |
| 01 / The evidence section label | Hierarchy [V] | Enlarge or simplify; numbering needs a real sequence. | Static. |
| Evidence section headline | Recognition [U] | Keep only if users can actually follow a finding back to evidence. | Clear hierarchy without distracting entrance. |
| Three answer/source/next-move columns | Proximity; progressive disclosure [V,D] | Keep as evidence anatomy, clearly separate from the service method. | One semantic accent connects related details; not three arbitrary colors. |
| Step numbers, rules and headings | Similarity/grouping [V] | Use consistent alignment and spacing; numbers communicate sequence. | Static rules; selected detail has an additional text/shape cue. |
| Step body copy | Readability; implementation choice | Increase current 11px copy; include a concrete example. | Contrast-safe body color across all three palettes. |
| Footer direction-study label | Match to context [U] | Keep in prototype; replace with useful company/navigation content in production. | Current 9px text needs enlargement. |
| Audit availability message | Accurate expectations [U] | Place near relevant inquiry CTA, not only in tiny footer. Verify actual availability before publishing. | Text label, not just a colored status dot. |
| Three font families | Consistency [U] | Simplify to one readable sans plus one expressive serif unless third has a necessary role. | Reduce visual competition and test font-loading shifts. |
| Mobile stacking and line breaks | Reflow [R] | Keep single column; test 320 CSS px, text enlargement and content expansion. Remove brittle breaks. | Oversized text and overflow:hidden are risks to inspect, not confirmed failures. |
| Focus, targets and landmarks | WCAG and APG [T,F,APG] | Verify keyboard order, visible focus, main landmark and controls. Prefer 44px targets; AA minimum is 24px with exceptions. | Focus must remain visible on every palette; animation cannot replace state. |

## Palette evidence

Ratios calculated from CSS values using WCAG relative luminance; complete evidence in `mindleverx-contrast-checks.json`. Gradient-stop checks are risk indicators, not rendered text-location tests.

| Pair | Ratio | Decision |
|---|---:|---|
| Signal CTA navy on lime | 13.32:1 | Strong text contrast. |
| Human CTA dark brown on cream | 9.88:1 | Strong text contrast. |
| Proof CTA cream on dark green | 13.31:1 | Strong text contrast. |
| Signal body on brightest specified blue stop | 4.76:1 | Clears 4.5:1 for this pair; verify actual composed background/states. |
| Human body on brightest copper stop | 3.02:1 | Below normal-text threshold if text occupies that region. Keep body over dark surface. |
| Proof coral subheading on cream | 4.39:1 | Current 19px bold can qualify for large-text threshold, but darken if used for smaller text. |
| Proof evidence body on lime | 5.79:1 | Clears normal-text threshold for this pair. |
| Signal card disclaimer | 6.65:1 | Contrast is sufficient for this pair; 8px size still needs correction. |

WCAG AA generally requires 4.5:1 for normal text and 3:1 for qualifying large text, with stated exceptions [C]. A passed color pair is not full accessibility conformance. Blue/trust, copper/humanity and lime/playfulness are creative associations to test, not universal psychological rules. Use semantic tokens for surface, text, action, focus, warning and error; accompany status colors with labels/icons [COLOR].

## Proposed motion specification

No animation is currently implemented. Exact durations below are our starting choices, not mandated standards. Carbon distinguishes productive and expressive motion [M].

| Interaction | Proposed behavior | Purpose and color relationship |
|---|---|---|
| Buttons | 120–180ms state transition; focus indicator immediate | Feedback; restrained fill change with sufficient contrast. No magnetism. |
| Source disclosure | 180–240ms gentle expansion/appearance | Preserve answer-to-source relationship; matching number and highlight persist after motion. |
| Citation trail | One short line reveal when explicitly selected | Explain which source supports which statement; keep a static readable equivalent. |
| Atmospheric entrance | Optional 400–600ms, once; copy and CTA immediately available | Expressive identity; no ongoing loop behind text. |
| Case/example gallery | User-driven 250–350ms transition | Retain context; visible buttons and keyboard alternative. No auto-advance. |
| Actual AI request | Real phase labels, cancellation and retry | Distinguish collecting, analyzing and failure; never fabricated percent progress. |
| Reduced-motion setting | Immediate state changes; remove travel, rotation and parallax | Same information and actions without decorative motion. |

Interaction-triggered motion disabling is WCAG 2.3.3 AAA, adopted here as a stronger project choice [A]. Automatically starting movement lasting more than five seconds alongside other content is subject to the pause/stop/hide requirement, except essential cases [P]. Prefer transform/opacity where appropriate and profile costly effects [PERF]. Status updates must be available to assistive technology where SC 4.1.3 applies [STATUS].

## Proposed AI and evidence features

All are proposals, not current capabilities. Provider integrations, operating costs and evaluation need separate implementation work.

| Priority / feature | User purpose | Recognized basis | Interaction, color and verification |
|---|---|---|---|
| First: Evidence Explorer | Inspect a real answer beside cited source excerpts and collection conditions. Can start with curated records without live AI. | Progressive disclosure [D]; inspectable explanations [H11] | Select numbered citation; reveal matching excerpt. Validate every source mapping; missing evidence is explicit. |
| First: Evidence Passport | Persistent compact record of engine, date, question, locale/method and limitations. | System status [U]; expectations [H2] | Neutral metadata; labeled missing/stale badges. Recorded means captured, not verified true. |
| Next: Ask about this finding | Explain a specific evidence record in plain language. | Capabilities [H1]; explanations [H11] | Suggested questions, cited responses and clear limits; uncertainty shown in words. Test unsupported questions and contradictory evidence. |
| Next: Recommendation workbench | Turn an observed issue into a draft action with supporting evidence and human review. | Correction [H9] | Edit, reject, undo; distinguish observation/inference/proposal with labels. No automatic publishing. |
| Next: Guided brief builder | Help a prospect describe goals and scope, then review a structured brief. | Capabilities [H1]; correction [H9] | Editable answers and review screen; no claim that filling it performs an audit. |
| Later: Change over time | Compare retained observations under stated collection conditions. | Recognition [U]; expectations [H2] | Stable axes, dates, sample sizes and missing-data labels. Separate API tests from consumer AI observations; no causal lift claim from a short before/after. |
| Later: Evidence-supported case-study walkthrough | Let prospects inspect problem, action and documented outcome at their own pace. | Progressive disclosure [D] | User-controlled sequence and labeled limitations; no fabricated client evidence or animated fake metrics. |

Explanations can increase trust without making an AI answer more accurate [H11]. Do not use a polished explanation, green check or uncalibrated confidence percentage as a substitute for verification.

## Direction and acceptance checks

Recommended direction: Signal Observatory, with a readable evidence workspace as its signature interaction. Keep blue atmosphere subordinate, lime for action/selection, cream for long reading. Use one coherent shape/type system. This is an expert design choice, not a proven conversion result.

Before implementation acceptance:

1. Fix misleading labels, pseudo-loading bars, tiny copy and rotated interactive text.
2. Hold copy constant when comparing visual directions. Test whether representative prospects can explain the offer, locate a source and distinguish an illustration from measured evidence. A small formative round diagnoses problems; it does not establish conversion lift.
3. Manually verify keyboard, screen reader, zoom/reflow, reduced motion, target sizes, gradient contrast and all expanded/error states. Automated checking supplements this.
4. Evaluate AI features against missing, stale, conflicting and unsupported evidence; verify source links actually support the associated claim. Test cancellation, retry, editing and deletion where applicable.
5. Validate on real mobile devices and slower connections; check typography loading, animation and layout shifts. Do not call the design accessible, fast or conversion-improving until corresponding evidence exists.

## Source ledger

All checked 2026-09-20. Design applications above are our judgments. Requirements apply at the stated conformance level; guidance is not a business-outcome guarantee.

| Key | Primary/recognized source | Scope and verification |
|---|---|---|
| U | https://www.nngroup.com/articles/ten-usability-heuristics/ | Usability heuristics; read during audit. |
| V | https://www.nngroup.com/articles/principles-visual-design/ | Scale, hierarchy, balance, contrast, Gestalt; read during audit. |
| D | https://www.nngroup.com/articles/progressive-disclosure/ | Secondary detail disclosure; retrieved during audit. |
| C | https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html | Text contrast thresholds; CSS ratios computed, rendered coverage pending. |
| COLOR | https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html | Do not rely on color alone; retrieved, implementation testing pending. |
| T | https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum | AA targets and exceptions; retrieved, rendered hitboxes pending. |
| R | https://www.w3.org/WAI/WCAG22/Understanding/reflow.html | Reflow; retrieved, layout verification pending. |
| F | https://www.w3.org/WAI/WCAG22/Understanding/focus-visible.html | Keyboard focus; retrieved, manual testing pending. |
| APG | https://www.w3.org/WAI/ARIA/apg/patterns/disclosure/ | Disclosure behavior; code uses native button and aria-expanded, assistive-tech test pending. |
| M | https://carbondesignsystem.com/elements/motion/overview/ | Productive/expressive motion. Current elements URL retrieved; older guidelines URL inaccessible. |
| A | https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html | AAA motion criterion; proposed stronger project practice. |
| P | https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide.html | Auto movement controls; no loops implemented. |
| PERF | https://web.dev/articles/animations-guide | Animation rendering guidance; proposal not profiled. |
| STATUS | https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html | Accessible status announcements; future AI feature testing needed. |
| H1 | https://www.microsoft.com/en-us/haxtoolkit/guideline/make-clear-what-the-system-can-do/ | Capability expectations; feature proposals only. |
| H2 | https://www.microsoft.com/en-us/haxtoolkit/guideline/make-clear-how-well-the-system-can-do-what-it-can-do/ | Performance expectations and uncertainty; read, no model evaluation completed. |
| H9 | https://www.microsoft.com/en-us/haxtoolkit/guideline/support-efficient-correction/ | Editing and recovery; proposals only. |
| H11 | https://www.microsoft.com/en-us/haxtoolkit/guideline/make-clear-why-the-system-did-what-it-did/ | Explanations and over-reliance; read, source-grounding evaluation pending. |

