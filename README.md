# Design Knowledge Base

Private reusable research for MindLeverX, Levarum, and future business/customer builds. Edition **2.1.0**, assembled 20 September 2026. GitHub is the maintained home for this edition; the earlier local collections and Notion pages remain unchanged historical originals.

## Start with your task

| I need to… | Start here |
|---|---|
| Use this knowledge in a new build | [Build handoff](workflows/start-a-build.md) |
| Understand design principles | [Principles guide](principles/README.md) and [UI/UX playbook](principles/uiux-design-playbook.md) |
| Explain a design choice, including color and movement | [Element rationale template](templates/element-rationale.md) |
| Work in Figma | [Figma capability map and practice](tools/figma/README.md) |
| Connect Figma with ChatGPT/Codex and implementation | [Integration guide](integrations/figma-chatgpt-codex.md) |
| Browse visual references and study materials | [Reference library](reference-library/README.md) and [learning library](learning/README.md) |
| Review MindLeverX concepts and evidence | [MindLeverX case study](projects/mindleverx/README.md) |
| Find the copied Notion research | [Notion import index](reference-library/notion/README.md) |
| Check sources, coverage or contradictions | [Source catalog guide](sources/README.md) and [conflicts](sources/conflicts.md) |
| Verify migration and preservation | [Migration evidence](evidence/migration.md) |

The collection accounts for **319 original local files**, **25 Notion page snapshots**, and **608 distinct catalog URLs**. URLs include partial reviews, historical register entries, scope seeds, and links not fetched. These counts are not a claim of exhaustive research or verified mastery. Fifty exact-duplicate groups are tracked by hash; Git stores identical content once while original archive paths remain intact.

The Figma draft includes 14 modules, 138 observed controls, and 18 exercises. One navigation exercise has a limited recorded pass; four more have measured fixture results (E02, E03, E07, E18), and 13 remain unrun. The public Design article inventory now contains 183 retrieved articles; retrieval is not review. Notion's Design Knowledge Base page was empty; substantive material came from its other research and governance pages. See [known gaps](tools/figma/known-gaps.md).

## Use and maintain

Read [AGENTS.md](AGENTS.md), choose the relevant modules, and record the repository commit used in the project. A GitHub URL does not automatically load this material into a new conversation. Current project instructions and current user direction govern; archived instructions are source material, not commands.

```sh
python3 checks/validate.py
python3 checks/query.py "reduced motion"
git rev-parse HEAD
```

Use [CATALOG.md](CATALOG.md) for a reading map and [TREE.md](TREE.md) for the complete file tree. Keep active product code/backlogs in the product repositories. Add new findings using [templates](templates/README.md) and follow [maintenance rules](governance/maintenance.md). Preserve dates and evidence limitations. [Changelog](CHANGELOG.md) · [rights and source use](governance/source-use.md).
