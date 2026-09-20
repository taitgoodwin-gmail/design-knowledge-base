# AI agent, Make, plugins and MCP

Checked 2026-09-20. Evidence: documentation synthesis; hands-on scope is separately recorded.

## Documented behavior

The agent in Design works in design files; Make builds interactive apps and prototypes. MCP supports extracting design context and writing native canvas content. Plugins offer editor APIs, while REST, MCP and UI automation have different capabilities. AI costs and availability vary; reviewed beta conditions must not be treated as permanent. A prompt completing is not proof that the output is correct, editable, accessible or deployable.

Sources: [S23: Figma agent](https://help.figma.com/hc/en-us/articles/37998629035799-Work-with-the-Figma-agent-in-design-files), [S24: AI credits](https://help.figma.com/hc/en-us/articles/33459875669015-How-AI-credits-work), [S25: Generate plugins](https://help.figma.com/hc/en-us/articles/43028920030743-Generate-plugins-with-the-Figma-agent), [S26: Figma MCP](https://developers.figma.com/docs/figma-mcp-server/), [S40: Plugin API](https://developers.figma.com/docs/plugins/).

## Our implementation practice

For Make kits, standard GitHub export, the separate local-codebase beta and preview-layer copying, use the [dated route comparison](../evidence/2026-09-20-make-handoff-review.md), based on S52–S56. These additional routes are documentation-only; E11 does not test them.

- Before generation, specify selected scope, component/library context and acceptance criteria.
- Inspect generated layer structure, typography, tokens and behavior.
- Keep credit limits and irreversible/publishing operations explicit.
- Use native or API operations for repeatable structural work when supported.
- Record actual tool access separately from product capability.

## Practice and acceptance

Run E11 in the [exercise suite](../exercises/README.md). Record actual results before marking a capability practiced or verified.

## Recorded fixture

[E11 selected-frame rewrite](../evidence/lab/ai-automation.md) passed its word limits and structure/style checks. Current UI reported 0 credits during beta, with 26 displayed for after beta. This is a dated observation, not a lasting price or a claim about arbitrary generation quality.
