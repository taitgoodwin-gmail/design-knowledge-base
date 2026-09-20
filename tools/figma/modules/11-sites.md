# Sites and responsive publishing

Checked 2026-09-20. Evidence: documentation synthesis; hands-on scope is separately recorded.

## Documented behavior

Sites has webpage breakpoints and cascading edits from the primary breakpoint. Additional widths can adjust appearance and interaction. Auto layout can help reflow content. A responsive Design frame and a Sites breakpoint are related concepts but different features. Publishing, domains, forms, CMS, SEO and operational behavior are still pending dedicated verification.

Sources: [S22: Sites breakpoints](https://help.figma.com/hc/en-us/articles/31242797809815-Add-or-delete-breakpoints-in-a-webpage).

## Our implementation practice

- Use a disposable draft to test primary versus overridden values.
- Check the width immediately above and below each breakpoint.
- Validate interactions on touch as well as pointer devices.
- Treat publication and production integration as separate delivery steps.

## Practice and acceptance

Run E13 in the [exercise suite](../exercises/README.md). Record actual results before marking a capability practiced or verified.

## Inheritance detail and current access

Primary changes propagate property by property. A modified secondary fill can remain independent while an unmodified height inherits. Reset all changes restores inheritance for reset properties. [Official editing guide](https://help.figma.com/hc/en-us/articles/31242788601879-Add-select-and-edit-objects-across-multiple-breakpoints), checked 20 September 2026. Exact boundary widths and real inheritance remain [pending the Sites terms screen](../evidence/lab/product-access-and-readiness.md).
