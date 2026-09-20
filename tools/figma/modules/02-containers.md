# Frames, groups and responsive layout

Checked 2026-09-20. Evidence: documentation synthesis; hands-on scope is separately recorded.

## Documented behavior

Groups follow their children’s bounds; frames give independent container bounds, clipping and layout behavior. Auto layout has horizontal, vertical and grid flows. Hug sizes around children; Fill uses available parent space; Fixed holds a dimension. Fill is not a top-level-frame option. A fill child can change a hugging parent’s behavior on the same axis. Ignore auto layout removes an object from normal flow. Grid auto layout arranges content; layout guides are visual aids. Grid tracks support fractional distribution and objects can span cells.

Sources: [S05: Groups versus frames](https://www.figma.com/best-practices/groups-versus-frames/), [S06: Guide to auto layout](https://help.figma.com/hc/en-us/articles/360040451373-Guide-to-auto-layout), [S07: Grid auto layout](https://help.figma.com/hc/en-us/articles/31289469907863-Use-the-grid-auto-layout-flow).

## Our implementation practice

- For a website, model structural containers before decorative elements.
- Inspect parent and child resizing together when layout behaves unexpectedly.
- Use min/max constraints to express design intent instead of dragging every instance.
- Use a normal-flow source disclosure so surrounding content makes room.
- Treat desktop/mobile mockups as examples; verify intermediate widths separately.

## Practice and acceptance

E02 and E03 now have [measured fixture results](../evidence/lab/README.md): 16 card states and three-width guide/wrap/grid comparisons. These verify the named fixtures, not arbitrary responsive pages.

Refresh note: a stretch layout guide can alter constraint-relative positions even though it does not wrap content. Do not describe it as having no layout effect. [Official guide/constraint explanation](https://help.figma.com/hc/en-us/articles/360039957934-Combine-layout-guides-and-constraints), checked 2026-09-20; E18 records the rerun.
