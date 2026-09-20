# Prototype and browser handoff — 20 September 2026

E08 and E12 passed in the bounded fixtures described here. These exercises test different surfaces: Figma presentation behavior and a small working browser implementation. Neither is a deployed MindLeverX website or a live AI feature.

## E08: source-disclosure prototype

[Open the flow](https://www.figma.com/proto/UgtCQvjyZpBQVOxhZAK4sk/MindLeverX?page-id=63%3A8&node-id=63-9&starting-point-node-id=63%3A9&scaling=scale-down). Page `63:8`; closed `63:9`, open `63:22`, error `63:35`. All three frames are 390×640 and use the existing E02 card as their experimental source. Plain frame copies deliberately expose Smart Animate name/hierarchy behavior; this is not a new product component library.

| Check | Observation | Reusable lesson |
|---|---|---|
| Repeated disclosure | Closed → Open → Closed → Open rendered correctly | Verify end states after repeated actions |
| Error and recovery | Open → Error → Back returned to Open; repeated error → Retry returned to Open | Distinguish unavailable evidence from a negative finding |
| Matching layer | At 6-second diagnostic timing, following content and controls moved down | Stable name and hierarchy preserve the match |
| Deliberate rename | Only open-frame following-content name changed; it stayed at its starting position early and appeared at the destination instead of moving with the other controls | Matching is structural, not semantic understanding of the text |
| Reset to closed | Navigated to closed; Back then returned to Open | Navigation to the start does not erase navigation history |
| Presentation restart | The displayed `R` shortcut returned to closed twice | Use and verify the actual presentation restart operation |
| Start guard | Back and an inactive pseudo-button removed from the closed view | Do not offer an action with no valid previous step |

The experiment revealed transient overlap while the newly visible disclosure faded into its destination and following text moved. The final diagnostic fixture uses 200ms ease-out, and the renamed layer was restored. This is not a claim that fast timing eliminates overlap. For the browser handoff, reading content changes immediately instead of moving through other text.

The first wiring script tried NAVIGATE from Error to itself. The installed tool rejected it; the corrected script targets Closed. The failed response is retained as negative evidence. Presentation Restart button clicks were unreliable through the tested automation route, including an unchanged/black canvas; `R` worked. Empty-history BACK also produced a black canvas in one observation. These are bounded observations, not a confirmed general Figma bug. The final closed frame offers no Back action.

Evidence: [browser observations](e08-browser-observations.json), [final structure/bounds](66-prototype-final-audit.json), [final render](e08-final-prototype.png), numbered responses 57–66 and [construction scripts](../../exercises/scripts/README.md). Final visible children fit without overlap; no missing fonts. Browser screenshots were inspected in the conversation; the saved PNG is a Figma render, not a browser capture.

Official sections refreshed: [Smart Animate](https://help.figma.com/hc/en-us/articles/360039818874-Smart-animate-layers-between-frames) and [Plugin Action](https://developers.figma.com/docs/plugins/api/Action/). Our timing and start guard are implementation choices. Name matching and BACK navigation are documented behavior; rendering observations are separate evidence.

## E12: design-to-code handoff

[Run/read the fixture](../../exercises/handoff/README.md). `get_design_context` was called for default instance `57:41`, open main `57:16` and error main `57:23` before coding. The React/Tailwind references were adapted to this repository's standalone HTML/CSS/JavaScript preview convention. No framework dependency or Code Connect publication was introduced.

The browser static reference measured 360×204, matching the Figma default. Inter loaded locally; 16px/24px typography, 24px padding, 12px gap, 16px radius and recorded light colors matched. The working card measured 360×224 because the 24px text indicator became a real 44px button. This 20px difference is deliberate, documented accessibility behavior, not unnoticed visual drift.

Enter opened and Space closed while retaining focus on the button. The accessibility snapshot exposed expanded/collapsed state. A visible 3px focus outline was observed. Error → Enter on Retry recovered to Open. Hiding the source option closed and hid the disclosure while preserving Dark appearance. Reset restored Default, Light, short text and source availability. Error copy explicitly says the failure is simulated, avoiding an unsupported external-original action in this local fixture.

| Browser width | Card width | Long/open height | Source width | Horizontal page overflow |
|---:|---:|---:|---:|---|
| 320 | 288 | 572 | 240 | None observed |
| 390 | 358 | 548 | 310 | None observed |
| 768 | 360 | 548 | 312 | None observed |
| 1440 | 360 | 548 | 312 | None observed |

All four long/open Dark cases kept the 3→1→2 source order, 44px button, content inside padding and a 16px gap before following content. Screenshot inspection covered the long mobile card. Appearance does not drive source visibility: E06's Light/Dark Boolean linkage was a diagnostic, not a production state model.

Evidence: [browser observations](e12-browser-observations.json), [Figma default render](e12-default-reference.png), context responses 67–69, [mapping and run instructions](../../exercises/handoff/README.md). These checks do not establish full WCAG conformance, screen-reader announcements, cross-browser fidelity or a working backend.

The [W3C disclosure pattern](https://www.w3.org/WAI/ARIA/apg/patterns/disclosure/) informed native button, keyboard and expanded-state semantics. Immediate state changes are our choice, informed by the observed overlap. Font bytes and the SIL OFL license come unchanged from the [official Inter repository](https://github.com/rsms/inter); provenance and hashes are included beside the asset.
