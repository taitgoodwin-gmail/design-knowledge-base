# Components, properties, variants and slots

Checked 2026-09-20. Evidence: documentation synthesis; hands-on scope is separately recorded.

## Documented behavior

Main components define reusable structure; instances keep a relationship to them. Component properties include text, boolean, instance swap, variant and slot controls. Variants represent unique combinations of properties; a complete Cartesian product is not required. Slots permit variable content within instances without detaching; they bind to nested frames, not a component’s top-level layer. Current documentation says simplified instances are deprecated, so older tutorials may show different property visibility.

Sources: [S08: Guide to components](https://help.figma.com/hc/en-us/articles/360038662654-Guide-to-components-in-Figma), [S09: Component properties](https://help.figma.com/hc/en-us/articles/5579474826519-Explore-component-properties), [S10: Slots](https://help.figma.com/hc/en-us/articles/38231200344599-Use-slots-to-build-flexible-components-in-Figma), [S11: Variants](https://help.figma.com/hc/en-us/articles/360056440594-Create-and-use-variants).

## Our implementation practice

- Use a text property for a citation label and a boolean for an optional visual.
- Represent materially different interaction states with a deliberate variant structure.
- Consider a slot for a variable-length evidence list; test restrictions and inherited behavior.
- Avoid detaching an instance merely to customize content; inspect properties and slots first.
- Test overrides after main-component changes and variant switches.

## Practice and acceptance

Run E04,E05 in the [exercise suite](../exercises/README.md). Record actual results before marking a capability practiced or verified.
