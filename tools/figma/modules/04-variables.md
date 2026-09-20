# Variables, modes, styles and semantic tokens

Checked 2026-09-20. Evidence: documentation synthesis; hands-on scope is separately recorded.

## Documented behavior

Current documentation lists color, number, string, boolean, timing and easing variables. Collections organize variables and modes; modes supply contextual values. Variables can alias other variables of the same type. Styles combine properties, while variables provide reusable values and can support styles. Scopes narrow applicable properties. Timing and easing variables support Motion. Mode names do not themselves establish browser breakpoint behavior. A wording conflict about boolean variables and boolean component properties is logged for a sandbox check.

Sources: [S12: Variable types, collections and modes](https://help.figma.com/hc/en-us/articles/14506821864087-Overview-of-variables-collections-and-modes), [S13: Create variables and aliases](https://help.figma.com/hc/en-us/articles/15145852043927-Create-and-manage-variables), [S14: Variable modes](https://help.figma.com/hc/en-us/articles/15343816063383-Modes-for-variables).

## Our implementation practice

- Separate palette primitives from semantic roles such as text/primary and action/background.
- Model compact spacing and dark appearance as explicit contexts rather than duplicated screens.
- Validate alias chains and mode behavior before consolidating imported values.
- Keep token changes traceable to their affected components and states.

## Practice and acceptance

Run E06 in the [exercise suite](../exercises/README.md). Record actual results before marking a capability practiced or verified.
