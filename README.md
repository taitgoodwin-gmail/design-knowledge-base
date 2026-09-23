# Design Knowledge Base

Private reusable research for MindLeverX, Levarum, and future business/customer builds. Edition **2.4.0**, assembled 20 September 2026. GitHub is the maintained home for this edition; the earlier local collections and Notion pages remain unchanged historical originals.

## Start with your task

| I need to… | Start here |
|---|---|
| Use this knowledge in a new build | [Build handoff](workflows/start-a-build.md) |
| Understand design principles | [Principles guide](principles/README.md) and [UI/UX playbook](principles/uiux-design-playbook.md) |
| Explain a design choice, including color and movement | [Element rationale template](templates/element-rationale.md) |
| Audit website quality, Lighthouse, Core Web Vitals and Google SEO | [Google web quality and SEO](tools/google-web-quality/README.md) |
| Work in Figma | [Figma capability map and practice](tools/figma/README.md) |
| Connect Figma with ChatGPT/Codex and implementation | [Integration guide](integrations/figma-chatgpt-codex.md) |
| Browse visual references and study materials | [Reference library](reference-library/README.md) and [learning library](learning/README.md) |
| Review MindLeverX concepts and evidence | [MindLeverX case study](projects/mindleverx/README.md) |
| Resume the fresh MindLeverX / Levarum exploration | [Current brief, concepts, naming, and domain record](projects/mindleverx/reimagining-and-naming-2026-09-21.md) |
| Find the copied Notion research | [Notion import index](reference-library/notion/README.md) |
| Check sources, coverage or contradictions | [Source catalog guide](sources/README.md) and [conflicts](sources/conflicts.md) |
| Verify migration and preservation | [Migration evidence](evidence/migration.md) |

The collection accounts for **319 original local files**, **25 Notion page snapshots**, and **681 distinct catalog URLs**. URLs include partial reviews, historical register entries, scope seeds, and links not fetched. These counts are not a claim of exhaustive research or verified mastery. Fifty exact-duplicate groups are tracked by hash; Git stores identical content once while original archive paths remain intact.

The Figma draft includes 14 modules, 138 observed controls, and 18 exercises. One navigation exercise has a limited recorded pass; fourteen more have measured fixture results (E02–E12, E15, E17, E18), and 3 remain pending. The public Help inventory now contains 887 retrieved articles across 14 categories, including 183 Design articles; retrieval is not review. Notion's Design Knowledge Base page was empty; substantive material came from its other research and governance pages. See [known gaps](tools/figma/known-gaps.md) and [the public Help index](tools/figma/HELP-INVENTORY.md).

[Supplied-link coverage](tools/figma/SCOPE-COVERAGE.md) accounts for all 63 Figma URLs and separates exact-page review from related product evidence. The selected source register has 72 records. [Make and handoff guidance](tools/figma/evidence/2026-09-20-make-handoff-review.md) distinguishes standard GitHub export, the local-codebase beta and Design snapshots.

The [seven-route Figma inventory](projects/mindleverx/mindleverx-site-inventory.md) links fourteen desktop/mobile baselines. The [motion/color study](projects/mindleverx/previews/motion-color-lab.html) demonstrates three further treatments with user-controlled animation; [verification and limits](projects/mindleverx/motion-color-review-2026-09-20.json) are recorded.

## Use and maintain

Read [AGENTS.md](AGENTS.md), choose the relevant modules, and record the repository commit used in the project. A GitHub URL does not automatically load this material into a new conversation. Current project instructions and current user direction govern; archived instructions are source material, not commands.

```sh
python3 checks/validate.py
python3 checks/query.py "reduced motion"
git rev-parse HEAD
```

Use [CATALOG.md](CATALOG.md) for a reading map and [TREE.md](TREE.md) for the complete file tree. Keep active product code/backlogs in the product repositories. Add new findings using [templates](templates/README.md) and follow [maintenance rules](governance/maintenance.md). Preserve dates and evidence limitations. [Changelog](CHANGELOG.md) · [rights and source use](governance/source-use.md).

Publication evidence: [v2.4.0 fresh-clone and CI receipt](evidence/publication-2.4.0.json). Three product exercises still await the [recorded access prerequisites](tools/figma/evidence/lab/product-access-and-readiness.md).
