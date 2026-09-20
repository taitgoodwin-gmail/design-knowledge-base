# Motion timeline and reusable animation

Checked 2026-09-20. Evidence: documentation synthesis; hands-on scope is separately recorded.

## Documented behavior

Motion is a separate editor mode currently described as open beta. The timeline exposes playback, auto-keyframing, current time, duration, time units, playback modes, tracks and zoom. Auto-keyframing records property changes when enabled. Timing and easing variables can help keep motion consistent. The separate exercise evidence now covers a manual keyframe reveal and a native MP4 export; deployed implementation remains a distinct check.

Sources: [S20: Motion timeline](https://help.figma.com/hc/en-us/articles/41405906446999-Use-the-Figma-Motion-timeline), [S12: Variable types, collections and modes](https://help.figma.com/hc/en-us/articles/14506821864087-Overview-of-variables-collections-and-modes).

## Our implementation practice

- Keep auto-keyframing off until deliberately authoring a sequence.
- Animate a relationship or state change with a stated purpose.
- Provide a reduced-motion design and static endpoint.
- Verify actual runtime behavior after handoff; a working timeline alone is insufficient.

## Practice and acceptance

E09 has [keyframe, easing, static-alternative and native-export evidence](../evidence/lab/motion-and-vector.md). Chrome checks at four timestamps confirmed the reveal and held final state. A Figma static alternative is not automatic operating-system reduced-motion support in a deployed site.

## Detailed choices and limits

See the [motion/color review](../evidence/2026-09-20-motion-color-review.md) for presets, keyframes, easing, anchors, paths, stroke trim, animated components, exports, gradients, effects and color profiles. It separates documented restrictions from our proposed MindLeverX applications.
