# Repeating the lab

These are recorded, plain JavaScript Figma MCP scripts for the existing lab file. Read the applicable Figma skill and inspect current IDs/state before running them. They are not shell scripts or a generic plug-in installation.

1. Open the [lab evidence](../../evidence/lab/README.md) and confirm the file/page/node IDs still exist.
2. For E02, run `e02-test-width.js` with `width` set to each of 320, 390, 768 and 1440. It changes fixture text and visibility, so preserve any later customizations first.
3. For E03, start with the recorded three-column, two-row grid before running `e03-resize.js`; `e03-span.js` intentionally changes the grid to three rows and mixed tracks. Reinitialize that fixture when repeating the original comparison.
4. For E07, run `e07-test.js` and `e07-resizing-modes.js`. Record both successful and rejected operations and inspect renders.
5. For E18, `e18-guide-refresh-control.js` is the successful no-guide/stretch-guide comparison. `e18-guide-refresh.js` preserves a rejected fixed-guide attempt; it is not a supported recipe.

Creation scripts are historical construction recipes and will create duplicates if rerun unchanged in this file. For a fresh sandbox, run the same procedure with newly returned page/node IDs and save a new run ledger. Never substitute guessed IDs. The test scripts intentionally leave their last test state; restore the documented presentation state after collecting results.

`python3 checks/verify_figma_lab.py` checks the saved observations. It does not run Figma again or prove that later edits still match those observations.

## Component wave

See [the locked plan](../component-lab-plan.md) and [results](../../evidence/lab/components-and-variables.md). Run order is collections → corrected primitives → semantics → foundations → card base → variants → combined family → before-main-update → after-main-update → slot customization → state switches → boolean binding → corrected probe variants → probe family → variant binding → final audit. Scripts labeled corrected/combined follow earlier preserved failures. The original failing scripts are negative evidence, not recommended setup steps.

The state ledger is [saved with evidence](../../evidence/lab/component-state-ledger.json). Actual IDs and existing objects must be inspected before reuse; scripts are not a blind idempotent installer.
