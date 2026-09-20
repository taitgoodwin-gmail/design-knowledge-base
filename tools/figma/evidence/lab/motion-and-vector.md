# E09 and E10 — original vectors and native motion

Checked 2026-09-20 in the same [Figma lab](https://www.figma.com/design/UgtCQvjyZpBQVOxhZAK4sk/MindLeverX?node-id=34-8). These are bounded exercise passes, not general mastery of Draw or Motion.

## E10: editable illustration

Created original source-connection artwork at node `46:8`: three editable vector nodes, three ellipse markers, an 8-degree rotation and a drop shadow. [Construction](18-e10-create.json) and [SVG export with editable-vector readback](19-e10-export.json) preserve the actual geometry. All recorded render bounds fit the 500×300 frame.

The [original render](e10-original.png), [exported SVG](e10-citation-motif.svg), and [Figma reimport render](e10-roundtrip.png) show different verification surfaces. Chrome rendered the exported SVG with the intended geometry and shadow; all important details remained visible. Reimporting the same SVG into Figma did not visibly retain the shadow. Keep the native source for editing effects; do not promise lossless SVG round-tripping. [Chrome observation](25-e10-browser-observation.json).

The exercise used editable paths and ordinary rotation through the Plugin API. It did not exercise every Draw brush, advanced repeat/skew transform or shader tool. Source stays editable in the original frame regardless of the imported comparison.

## E09: source-connection reveal

Created motion copy `48:19`; only its connection vector `48:20` animates. Opacity runs from 0 at 0.0s to 1 at 0.6s, then holds. Recorded [linear easing](22-e09-linear.json), changed to [ease-out](23-e09-ease-out.json), and verified that the track/keyframe IDs stayed stable. Existing two-second timeline duration was preserved.

The intent is to reveal the relationship between the source markers and citation tile. No reading text sits under the animation. Color and geometry stay constant, so the reveal does not imply a changing confidence score or live AI process. Duration and easing are our design choices, not universal standards.

Created [static alternative](24-e09-static.json) `50:8`: all paths visible, no manual tracks or animation styles on any child. A production implementation must select this alternative for reduced motion; creating the Figma frame does not wire that behavior into a website.

Exported the actual timeline to [MP4](e09-native-reveal.mp4), 500×300, 5fps, low quality. In Chrome, inspected 0.0s (paths absent), 0.2s (partial reveal), 0.6s (complete), and 1.8s (held). [Observed metadata and findings](26-e09-browser-observation.json). The MP4 reports 2.2s while the timeline reports 2.0s; investigate if frame-exact delivery is required. The preview contains one reveal; the Figma editor's looping preference was not checked.

## Repeat the export checks

Serve this directory locally, then open `export-preview.html` in Chrome. Its timestamp buttons inspect the saved native export. The page is a diagnostic aid, not a replacement animation implemented in HTML.

```sh
python3 -m http.server 38821 --bind 127.0.0.1 --directory tools/figma/evidence/lab
```

Browser screenshots were inspected in-session but not stored as separate PNG files; the source SVG, original/reimport PNGs, native MP4 and observations are retained.

Official sources checked: [Draw](https://help.figma.com/hc/en-us/articles/31440394517143-Explore-Figma-Draw), [exportAsync](https://developers.figma.com/docs/plugins/api/properties/nodes-exportasync/), [Motion timeline](https://help.figma.com/hc/en-us/articles/41405906446999-Use-the-Figma-Motion-timeline). Source statements, authoring choices and observed results are separated above.
