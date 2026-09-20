# E11 — selected-frame AI editing

Checked 20 September 2026. **Passed in the recorded fixture.** [Open the editable frame](https://www.figma.com/design/UgtCQvjyZpBQVOxhZAK4sk/MindLeverX?node-id=74-9), page `74:8`, frame `74:9`.

A copy of the E02 card was isolated on a new lab page. The native Figma agent received the selected frame and an explicit rewrite brief: Question ≤12 words; Answer ≤35 words; preserve the evidence caveat, native text, styling, layout and other content. [Exact prompt and UI observations](e11-browser-observations.json). The agent reported completion after 51 seconds; its self-report was then independently checked through the Plugin API and live render.

| Check | Actual result |
|---|---|
| Question / Answer | 10 and 22 words respectively; includes source/date/context, evidence versus interpretation and uncertainty |
| Native editability | Same six descendant IDs; five TEXT nodes and one button FRAME, no flattened bitmap |
| Layout | Width 320, height 640 → 496, vertical auto layout, auto primary sizing, 24px padding, 16px gaps, 48px button |
| Preserved content | Button label, disclaimer and following content unchanged |
| Styling | Compared frame properties and text typography/fills to the source: no differences |
| Scope | AI page retained one frame; original source card unchanged; nine original-page top-level IDs/names/geometry match baseline |
| Credits | Before run: 3,000 left. Prompt usage control reported 0 during beta and displayed 26 for after beta. No purchase or plan change |

Evidence: [before](86-ai-fixture-before.json), [after](87-ai-fixture-after.json), [style/scope comparison](88-ai-style-scope-check.json), [render](e11-ai-edited.png). These establish this rewrite and these scope checks, not arbitrary generation quality or a byte-level entire-file comparison.

Relevant official sections rechecked 20 September 2026: [Figma agent](https://help.figma.com/hc/en-us/articles/37998629035799-Work-with-the-Figma-agent-in-design-files) for selected context, edit access and undo; [credits](https://help.figma.com/hc/en-us/articles/33459875669015-How-AI-credits-work) for usage reporting. Current beta treatment is temporary; the displayed future number is not a guaranteed price.

Repeat using [setup script](../../exercises/scripts/e11-setup.js) with fresh IDs, verify the UI selection chip, record the balance, submit the bounded prompt, inspect its actual credit control and compare output structure/content to the untouched source. An agent's success message alone is insufficient evidence.
