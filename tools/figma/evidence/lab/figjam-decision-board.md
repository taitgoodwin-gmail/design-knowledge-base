# E17 — traceable FigJam decision board

Checked 20 September 2026. **Passed in the recorded fixture.** [Open the editable board](https://www.figma.com/board/sSMlagZLamtpFKG3zwYABm?node-id=2-2). File `sSMlagZLamtpFKG3zwYABm`, board `2:2`, editor `figjam`; new draft in the single team returned by the connection. The account reported a Full seat on Professional; this does not establish every other product entitlement.

## What the board does

| Category | Content and role | Evidence link |
|---|---|---|
| Observation | The actual six-second prototype revealed transient overlapping text. Limited to a fixture. | Recorded E08/E12 experiment |
| Assumption | Reading motion may distract; source trails may help if useful. Explicitly unvalidated. | Official-source working practice |
| Decision | Immediate browser disclosure, native buttons and visible focus; expressive motion away from reading. A project choice. | Working E12 handoff |
| Disagreement | A restrained transition might aid orientation; immediate change could feel abrupt. A counter-hypothesis. | Official Smart Animate article |
| Test | Proposed user comparison; not run. Completed keyboard/layout checks shown separately. | Measured browser baseline |
| Revisit | Reopen the choice when evidence changes; preserve task, context and result. | W3C disclosure pattern |

Six labeled groups, six native text hyperlinks and seven directed connectors keep evidence, interpretation and disagreement distinct. Four GitHub links are pinned to published commit `dd81a55a646080b0a3c60b497601dbbfd61685b6`. Color softly groups categories, while text labels and arrows carry meaning independently of color. No animation is needed for this reading task.

## Checks and limits

- [Final API audit](79-figjam-final-audit.json): 40 nodes, 12 nested sections, six category headings, six links, seven connectors; no recorded bounds/overlap issues or missing fonts.
- [Full tree](78-figjam-final-tree.json) and [render](e17-decision-board.png) retained. Render and live Chrome board visually inspected; all six cards and connector labels were readable.
- Selected the W3C link in Chrome and opened its link control; it displayed `https://www.w3.org/WAI/ARIA/apg/patterns/disclosure/` exactly. This verifies source recovery in the editor, not navigation by an independent reader or every link click.
- Connector endpoint magnets were submitted as directional values; API readback normalized section endpoints to `CENTER`. The rendered connectors terminated at the expected section boundaries. Preserve the observation rather than assuming unsupported behavior.
- No user study, collaboration/voting test, screen-reader audit, or evidence of GEO/conversion lift is claimed. Share/access settings were not changed.

## Repeat the workflow

Read the six `e17-*.js` scripts in [exercise scripts](../../exercises/scripts/README.md), create a new FigJam draft with the create-file skill, inspect its root before writing, and substitute its file/node IDs. Build wrapper → paired cards → content reflow → connectors. Keep the observed fact and the hypothesis in different cards. Replace pinned evidence links only with records that support the actual observation, then rerun structural audit and inspect the rendered board. Scripts are a construction record, not an idempotent update command.
