# Motion timeline and reusable animation

Checked 2026-09-20. Evidence: documentation synthesis; hands-on scope is separately recorded.

## Documented behavior

Motion is a separate editor mode currently described as open beta. The timeline exposes playback, auto-keyframing, current time, duration, time units, playback modes, tracks and zoom. Auto-keyframing records property changes when enabled. Timing and easing variables can help keep motion consistent. Mode navigation was exercised here; keyframe creation, exports and implementation were not.

Sources: [S20: Motion timeline](https://help.figma.com/hc/en-us/articles/41405906446999-Use-the-Figma-Motion-timeline), [S12: Variable types, collections and modes](https://help.figma.com/hc/en-us/articles/14506821864087-Overview-of-variables-collections-and-modes).

## Our implementation practice

- Keep auto-keyframing off until deliberately authoring a sequence.
- Animate a relationship or state change with a stated purpose.
- Provide a reduced-motion design and static endpoint.
- Verify actual runtime behavior after handoff; a working timeline alone is insufficient.

## Practice and acceptance

Run E09 in the [exercise suite](../exercises/README.md). Record actual results before marking a capability practiced or verified.
