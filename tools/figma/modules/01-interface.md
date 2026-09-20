# Interface, selection and navigation

Checked 2026-09-20. Evidence: documentation synthesis; hands-on scope is separately recorded.

## Documented behavior

The navigation bar selects workflows such as File, Assets, Tools and Variables. The left sidebar changes with that selection. The right panel reflects the selected object and the current mode. Consequently, a missing control may be a context or permission issue rather than a missing capability.

Sources: [S03: Explore design files](https://help.figma.com/hc/en-us/articles/15297425105303-Explore-design-files), [S04: Access design tools from the toolbar](https://help.figma.com/hc/en-us/articles/360041064174-Access-design-tools-from-the-toolbar).

## Our implementation practice

- Inspect the selected layer type before changing properties.
- Use current control labels instead of memorized screen coordinates.
- Separate editor navigation, document edits and publishing actions.
- When an action times out, inspect state before repeating it; the action may have succeeded.

## Practice and acceptance

Run E01 in the [exercise suite](../exercises/README.md). Record actual results before marking a capability practiced or verified.
