# Draw, illustration and visual effects

Checked 2026-09-20. Evidence: documentation synthesis; hands-on scope is separately recorded.

## Documented behavior

Draw lives within a Design file and changes the toolbar and sidebars toward illustration. Pen, Brush and Pencil are readily available; transforms are exposed in the right panel. Some Design controls require switching back to Design mode. Individual illustration tools, vector editing, effects and shader authoring still require dedicated exercises.

Sources: [S21: Explore Figma Draw](https://help.figma.com/hc/en-us/articles/31440394517143-Explore-Figma-Draw).

## Our implementation practice

- Use original citation/connection artwork that supports the business story.
- Keep readable text out of decorative geometry.
- Preserve editable vectors when that supports future revisions.
- Test exported artwork for clipping and visual differences.

## Practice and acceptance

E10 has [native-vector and export evidence](../evidence/lab/motion-and-vector.md). The SVG rendered with its shadow in Chrome, while its Figma reimport did not visibly preserve that effect. Keep editable native source and verify each actual delivery format. Brush tools and advanced Draw transforms remain outside this exercise.
