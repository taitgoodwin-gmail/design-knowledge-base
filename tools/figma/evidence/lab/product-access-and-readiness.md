# Remaining product prerequisites and ready-to-run checks

Observed 20 September 2026. E13, E14 and E16 are **pending prerequisites**, not passed exercises. Their official sources were reviewed separately from execution. Questions were sent while independent repository work continued; silence is not approval.

| Exercise | Exact observed prerequisite | Current artifact / evidence |
|---|---|---|
| E13 Sites | Get started explicitly accepts Beta Terms and names the Acceptable Use Policy; optional AI names subprocessors. Button not selected. | [Unpublished setup draft](https://www.figma.com/site/nXUpdS6kEV7nv9FwC2qZES) |
| E14 Weave | MCP returned that Figma is not linked to Weave; no tool list or generation was available. | [Actual response](85-weave-access.json) |
| E16 Buzz | Get started explicitly accepts Beta Terms. Button not selected. | [Unpublished setup draft](https://www.figma.com/buzz/4XVJZX8jKUvLYkNm44KeSJ) |

The Chrome-control confirmation policy requires current confirmation before accepting legal terms. This is the reason Sites/Buzz stop here; no local repository skill creates that gate. Weave needs the account owner to link Figma in its Profile → Linked accounts. Running a charged Weave tool also has a cost-confirmation gate in the connector contract; no cost has yet been quoted or incurred.

## E13 prepared procedure

Create a small source card on a primary desktop 1280px breakpoint and secondary tablet 800/mobile 375 breakpoints. Use one text, one color field and a vertical auto-layout group. Record every original value and the Always select matching layers state.

| Step | Expected behavior from official guidance; verify in UI |
|---|---|
| Set primary fill blue | Matching unmodified secondary fills inherit |
| Set mobile fill coral | Only mobile changes; record override |
| Change primary fill teal | Desktop/tablet change; mobile keeps coral |
| Change primary height | Inherits where height has no override, independently of fill |
| Reset mobile changes | Reset properties inherit primary again |
| Preview widths | Inspect 374/375/376, 799/800/801, 1279/1280/1281 plus 600 and 1000; record exact boundary behavior rather than infer equality from prose |

[Breakpoint creation/ranges](https://help.figma.com/hc/en-us/articles/31242797809815-Add-or-delete-breakpoints-in-a-webpage) and [property-level inheritance](https://help.figma.com/hc/en-us/articles/31242788601879-Add-select-and-edit-objects-across-multiple-breakpoints), relevant sections checked 20 September 2026. Our width matrix is a test choice. Do not equate Design-frame resize with Sites breakpoint verification. No publishing is part of this exercise.

## E16 prepared data and inspection

Use three synthetic rows mapped to separate Headline, EvidenceStatus and Image objects: short label + valid fixture image; long label + valid image; short label + missing image. The valid public fixture image must be chosen and verified before creating assets; no placeholder URL is a passed input.

Expected row count is three generated assets, with the original retained separately. Inspect all three for exact text mapping, clipping, image presence/fallback, dimensions and order; document the actual blank-image behavior rather than assume it. Keep the longest label intact and fix template layout if it clips.

[Buzz bulk create](https://help.figma.com/hc/en-us/articles/31271824185623-Bulk-create-assets-in-Figma-Buzz), checked 20 September 2026: CSV/XLSX header-to-object mapping; compatible text/image types; one field per object; public image URLs or XLSX in-cell images; template locks affect selectable objects. These documented requirements do not establish the missing-image outcome.

## E14 prepared reproducibility record

The [Weave MCP guide](https://help.weavy.ai/en/articles/16202764-running-weave-tools-from-external-agents-mcp) says the linked account's active workspace determines available tools; creating/editing workflows through MCP is not supported. Our installed tool contract directs Weave execution through its MCP tools, not browser automation. A pre-existing published workflow can be inspected and run after account linking; that alone would not demonstrate workflow construction.

For a branded motif variant, record: recipe ID/version, every exposed input/default, model/version where exposed, prompt, seed if supported, input bytes/hash, size, aspect, quoted/actual usage, run IDs/status, and output hashes/dimensions. Use one unchanged repeat and one controlled color change. Compare composition, palette, legibility and unintended lettering; do not promise identical pixels when the model does not guarantee determinism. The reusable native citation motif is in [E10 evidence](motion-and-vector.md).

Official sections checked 20 September 2026:

- [Prompt variables](https://help.weavy.ai/en/articles/14047674-prompt-variables): connect Text nodes to Prompt inputs; reusable references simplify controlled changes.
- [Tools](https://help.weavy.ai/en/articles/12267755-tools): Output nodes enable tools, exposed inputs can be locked, and tool versions/sharing are distinct from workflow editing/sharing.
- [Version history](https://help.weavy.ai/en/articles/16110597-version-history): inspect, restore or duplicate saved workflow versions; these actions are not tested here.
- [Figma node](https://help.weavy.ai/en/articles/16440592-figma-node): after connection, Weave changes push into Figma automatically; edits made in Figma require Update to pull them back into Weave. Copying a frame into a workflow alone does not write back.

No tool was run, no image generated, no account connected, no terms accepted, no plan changed and no site/template published in these pending exercises.
