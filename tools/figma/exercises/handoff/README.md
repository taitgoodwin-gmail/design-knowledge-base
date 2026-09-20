# E12 — evidence-card browser handoff

A local learning fixture, not the MindLeverX application. Start from the repository root:

```sh
python3 -m http.server 38823 --bind 127.0.0.1 --directory tools/figma/exercises/handoff
```

Open `http://127.0.0.1:38823/`. It loads only local HTML, CSS, JavaScript and a licensed Inter font. Stop the server with Ctrl-C when done.

## Mapping

| Design contract | Code equivalent | Intentional adaptation |
|---|---|---|
| `LAB / Evidence card` 57:32 | `.evidence-card` | Static reference plus working article |
| State Default/Open/Error | `state`, `render()`, `data-state` | Native status semantics; simulated error copy |
| Question text property | `#card-question` | Semantic heading, long-text option |
| Show source Boolean | `#show-source` control | JavaScript state; not a CSS Boolean |
| Source list SLOT | `#source-list` children | Variable-length paragraphs in order 3→1→2 |
| Surface/text/accent/error tokens | `--lab-surface`, `--lab-text`, `--lab-accent`, `--lab-error` | Light/Dark aliases resolved into CSS values |
| Padding/gap/radius | `--lab-padding:24px`, `--lab-gap:12px`, `--lab-radius:16px` | Same measured values |
| LAB / Body | Inter Regular, 16px/24px | Self-hosted exact upstream font asset |
| 360px card | `width:min(360px,100%)` | Shrinks with page padding; grows vertically |
| 24px source text | Native disclosure button, 44px minimum | Adds 20px in default card; expanded/collapsed semantics |
| Smart Animate prototype | Immediate browser state changes | Reading content does not overlap during motion |

The working control uses `aria-expanded`, `aria-controls`, native Enter/Space activation and a visible focus ring. Focus stays on the same button when disclosure changes. Hidden content uses `hidden`; it is removed from layout and the inspected accessibility tree. No screen-reader announcement claim is made without an assistive-technology test.

## Recheck

Compare the static card with [the Figma reference](../../evidence/lab/e12-default-reference.png). Then open/close with Enter and Space, simulate error and retry, toggle long text and source availability independently from appearance, and reset. Inspect at 320/390/768/1440: no horizontal overflow, ordered sources, no overlap, following content below the card. Current [results and limits](../../evidence/lab/prototype-and-handoff.md) were checked 2026-09-20.

Font [provenance](assets/provenance.json) and [license](assets/Inter-LICENSE.txt) are retained. No automatic Figma sync or Code Connect mapping is claimed; future edits need an explicit comparison.
