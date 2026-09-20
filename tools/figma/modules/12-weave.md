# Weave workflows and reusable media tools

Checked 2026-09-20. Evidence: documentation synthesis; hands-on scope is separately recorded.

## Documented behavior

Figma links to help.weavy.ai as Weave’s knowledge center. Its editor documentation covers nodes, edges, prompt variables, media, version history, tools and a timeline. September release notes describe a Figma node connecting frames to workflows and syncing source design changes. Detailed node/model behavior and account access remain untested.

Sources: [S29: Weave knowledge center](https://help.weavy.ai/en/), [S30: Weave editor](https://help.weavy.ai/en/collections/15341378-weave-s-editor), [S36: Release notes](https://www.figma.com/release-notes/).

## Our implementation practice

- Record model, prompt, inputs, parameters, output and usage for repeatable generation.
- Build controlled brand variation workflows, then review each output.
- Use a small non-sensitive fixture before processing customer materials.
- Retain editable source design separately from generated media.

## Practice and acceptance

Run E14 in the [exercise suite](../exercises/README.md). Record actual results before marking a capability practiced or verified.

## Deeper source review and actual access

The [prepared workflow record](../evidence/lab/product-access-and-readiness.md) now covers prompt variables, published tools versus workflows, history, MCP and the Figma node. Current MCP supports tool discovery/input inspection/running/status/cancellation, not workflow creation or editing. Runs consume Weave credits, separate from Figma AI credits. The actual connector returned **account not linked**; no generation was performed.

After a Figma node is connected, changes from Weave push automatically to Figma. Direct Figma edits require Update in Weave to pull them back. Treat that directionality as part of the workflow, not a claim of automatic two-way sync. Sources S47–S51, checked 20 September 2026.
