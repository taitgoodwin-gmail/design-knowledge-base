# Dev Mode, Code Connect and implementation

Checked 2026-09-20. Evidence: documentation synthesis; hands-on scope is separately recorded.

## Documented behavior

Code Connect associates Figma components with repository components. Its UI mapping and CLI snippet workflows differ; the reviewed UI documentation says mappings do not themselves display production snippets in Inspect. Access depends on seat/plan and library prerequisites. Exported assets, inspect values and component mappings are distinct handoff materials, not a complete application.

Sources: [S27: Code Connect](https://developers.figma.com/docs/code-connect/), [S28: Code Connect UI](https://developers.figma.com/docs/code-connect/code-connect-ui-setup/), [S35: Static exports](https://help.figma.com/hc/en-us/articles/360040028114-Export-static-designs-from-Figma).

## Our implementation practice

- Hand off content, states, responsive rules, focus behavior and motion endpoints.
- Verify component mapping against the real implementation.
- Compare implemented screens at matching sizes and with realistic content.
- Keep export formats and file permissions explicit.

## Practice and acceptance

Run E12 in the [exercise suite](../exercises/README.md). Record actual results before marking a capability practiced or verified.

## Verified fixture

E12 now has an [implemented HTML/CSS/JavaScript example](../exercises/handoff/README.md) and [browser evidence](../evidence/lab/prototype-and-handoff.md). Static geometry/tokens matched the Figma default; a native 44px disclosure button intentionally increased working-card height. Enter/Space, error recovery, independent appearance/state, source ordering and four widths were checked. This does not verify Code Connect publication or a production backend.
