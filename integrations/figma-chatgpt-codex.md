# Figma, ChatGPT, Codex and GitHub

Source sections checked 20 September 2026. These are documented capabilities, not a complete account entitlement or integration test.

| Route | Use |
|---|---|
| Dedicated Figma app in ChatGPT | Figma documents generating FigJam diagrams and Figma Slides; do not transfer that article's scope to every current plugin surface. [Figma help](https://help.figma.com/hc/en-us/articles/35326636109975-Use-ChatGPT-with-Figma) |
| Codex with the remote Figma MCP/plugin | Read design structure and variables; use Code Connect; write native designs and capture live interfaces. Figma recommends the remote server for its broadest capabilities. [Setup](https://help.figma.com/hc/en-us/articles/39888629089175-Codex-and-Figma-Set-up-the-MCP-server) |
| Native canvas work | `use_figma` creates/updates real components, variables, frames and auto layout. Inspect actual structure and reuse the existing system. [Write to canvas](https://developers.figma.com/docs/figma-mcp-server/write-to-canvas/) |
| Live interface capture | Running UI can be captured as editable frames; specify the routes and states. Capturing the homepage does not import the entire application. [Code to canvas](https://developers.figma.com/docs/figma-mcp-server/code-to-canvas/) |
| Design to implementation | Codex reads selected design context and implements changes in the target project. Validate the result; this workflow does not prove automatic synchronization. [OpenAI workflow](https://developers.openai.com/blog/building-frontend-uis-with-codex-and-figma) |

OpenAI documents plugins as reusable skills/MCP capabilities on supported ChatGPT and Codex surfaces. Check the current host's tools and connection rather than inferring access from a product name. [Plugins](https://learn.chatgpt.com/docs/plugins).

In this session, tools for context, screenshots, variables, native writes, capture, Code Connect, motion, shaders and Weave were listed. This is tool-discovery evidence only. The historical UI navigation test is in [Figma evidence](../tools/figma/evidence/2026-09-20-ui-inspection.md). Account, plan and file permissions must be checked when using gated features; [documentation conflicts](../sources/conflicts.md) remain explicit.

## Our reusable workflow

1. Load a named version of this repository and the product's current instructions.
2. Define audience, task, content, states, components and acceptance checks.
3. Use a specific Figma file/frame link and inspect its structure.
4. Create variants with reusable components and variables. Record decision rationale.
5. Implement in the product repository using its existing components and conventions.
6. Compare rendered results at relevant widths and states; check keyboard, reduced motion, errors and real content.
7. Store dated lessons here and active implementation changes in the product repository.

This process is our implementation practice. A representative component round-trip test remains future product work, not a completed migration test.
