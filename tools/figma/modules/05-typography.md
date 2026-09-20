# Typography, dimensions and reading behavior

Checked 2026-09-20. Evidence: documentation synthesis; hands-on scope is separately recorded.

## Documented behavior

Text styles collect typography properties without requiring a style for each text color. Text dimensions/resizing are in Layout; additional typography options are in Type settings. Truncation and max-lines options have resizing prerequisites. Current text controls include Auto, Balance and Pretty wrapping. Font features depend on the selected font. Figma rendering is not proof of equivalent browser support or accessible reading behavior.

Sources: [S15: Typography systems](https://www.figma.com/best-practices/typography-systems-in-figma/), [S16: Text properties](https://help.figma.com/hc/en-us/articles/360039956634-Explore-text-properties).

## Our implementation practice

- Start with display, heading, body, label and metadata roles.
- Use long labels, multiple paragraphs and missing-font scenarios as test content.
- Never use truncation to hide necessary evidence or disclaimers.
- Check actual text dimensions, not only the nominal font size.

## Practice and acceptance

E07 has [recorded font/width and resizing results](../evidence/lab/README.md) for Inter, Noto Sans, Japanese text and a long identifier. Six final auto-height cases fit the measured bounds. Auto-width and an undersized fixed box demonstrated why dimensions need checking. This does not establish equivalence in browser rendering.
