# Prototype behavior and state

Checked 2026-09-20. Evidence: documentation synthesis; hands-on scope is separately recorded.

## Documented behavior

A prototype interaction combines a hotspot, trigger, action and transition. Smart Animate matches layer names and hierarchy. Naming or nesting changes can alter which objects animate. Multiple actions and conditionals support state-dependent behavior; animations on one trigger can run sequentially. Prototype state is simulated behavior and does not establish a working production backend.

Sources: [S17: Connect prototypes](https://help.figma.com/hc/en-us/articles/360040315773-Connect-your-prototype), [S18: Smart Animate](https://help.figma.com/hc/en-us/articles/360039818874-Smart-animate-layers-between-frames), [S19: Multiple actions and conditionals](https://help.figma.com/hc/en-us/articles/15253220891799-Multiple-actions-and-conditionals).

## Our implementation practice

- Define closed, open, loading, empty and error states before animation.
- Use duplicated structured frames to control matching, then inspect matches deliberately.
- Test repeated opening, closing, back navigation and reset behavior.
- Separate interaction requirements from proposed transition timing.

## Practice and acceptance

Run E08 in the [exercise suite](../exercises/README.md). Record actual results before marking a capability practiced or verified.
