# Slides, Buzz and FigJam workflows

Checked 2026-09-20. Evidence: documentation synthesis; hands-on scope is separately recorded.

## Documented behavior

Slides supports collaborative decks, notes and interactive review tools; live interactions are used in presentation mode. Buzz supports branded assets and template-controlled editing. Bulk create maps CSV/XLSX data into assets; each data row produces an asset and fields must match compatible objects. FigJam supports collaborative visual thinking with notes, shapes and diagrams. These products are documented at overview level here, not fully practiced.

Sources: [S31: Buzz overview](https://help.figma.com/hc/en-us/articles/31271566667543-Guide-to-Figma-Buzz), [S32: Buzz bulk create](https://help.figma.com/hc/en-us/articles/31271824185623-Bulk-create-assets-in-Figma-Buzz), [S33: Slides overview](https://help.figma.com/hc/en-us/articles/24170630629911-Explore-Figma-Slides), [S34: Slides live interactions](https://help.figma.com/hc/en-us/articles/24246820870807-Add-live-interactions-to-slides), [S39: Product overview](https://help.figma.com/hc/en-us/articles/14563969806359-What-is-Figma).

## Our implementation practice

- Use FigJam for evidence-to-decision mapping, Slides for a decision narrative and Buzz for campaign variants.
- For Buzz, test a three-row fixture with long text and a missing image before a large batch.
- For Slides, test presenter and audience views separately.
- Keep source provenance visible in review materials.

## Practice and acceptance

Run E15,E16,E17 in the [exercise suite](../exercises/README.md). Record actual results before marking a capability practiced or verified.

## Recorded hands-on scope

[E17 FigJam decision board](../evidence/lab/figjam-decision-board.md) now has six source-linked categories and a disagreement/revisit path. [E15 Slides fixture](../evidence/lab/slides-review.md) verifies a native poll and notes across three views, with popout-navigation/export limits. Buzz remains unrun. Notes are hidden in the audience surface, but [can-view users can open presenter view](https://help.figma.com/hc/en-us/articles/24245848829847-Add-and-view-presenter-notes); do not use notes as a confidentiality boundary.
