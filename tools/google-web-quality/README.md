# Google web quality and SEO reference library

Reusable guidance for **MindLeverX, Levarum, our other sites, and customer projects**. Added 23 September 2026 at the owner's request to preserve Google/Lighthouse/SEO research for reuse.

This private GitHub repository is the maintained home. Conversation output files are delivery copies. Keep future corrections here with source dates and a changelog entry; copying a document does not refresh its verification date.

## Choose the reference

| Need | Read |
| --- | --- |
| Understand the complete Lighthouse and customer-audit approach | [Audit playbook](lighthouse-audit-playbook.md) |
| Apply Google's foundational search guidance | [Google SEO foundations](google-seo-foundations.md) |
| Design collection, reporting or storage | [Evidence and reporting specification](lighthouse-evidence-spec.md) |
| Look up an audit ID, category or configured weight | [Lighthouse 13.5.0 inventory](lighthouse-audit-inventory.md) |
| Import the inventory into tooling | [Inventory JSON](lighthouse-audit-inventory.json) |
| Verify a claim, date or scope | [Source register](lighthouse-source-register.md) and [source records](../../sources/google-web-quality-2026-09-23.json) |
| Review the first, superseded overview | [Historical initial overview](history/lighthouse-initial-overview-2026-09-23.md) |

## Coverage and status

- Lighthouse, PageSpeed Insights, Core Web Vitals, CrUX API/History/Vis/BigQuery, CI, RUM, accessibility review and foundational Google Search guidance.
- 46 selected source/document reviews, checked 23 September 2026. This is not an exhaustive copy or review of every Google/SEO document.
- Lighthouse 13.5.0 default configuration: 165 category references / 162 unique audit IDs. Manual, hidden, unscored and mode-dependent entries are included; not all execute on every page.
- Source/document review and inventory validation are complete for the stated scope. Live site baselines, API integration, customer reports, pricing and monitoring are not implemented by this research.
- Experimental agentic checks are separate from search visibility and actual agent task-success measurements.

## Reuse in a project

1. Read the relevant documents and their evidence limits.
2. Record this repository's actual commit and files used in the project record.
3. Recheck changing guidance before consequential implementation or release.
4. Keep that project's URLs, customer data, audit artifacts, decisions and accepted thresholds in its own project/evidence store.
5. Feed reusable corrections back here. Do not copy customer results into general guidance as universal facts.

A GitHub link does not automatically load the library in a fresh chat; include it in the project's handoff or instructions. [Shared build handoff](../../workflows/start-a-build.md).

## Reproduce the static inventory

Use a local checkout of Lighthouse **13.5.0**, commit `cb853a38a6410617518b363590c967b3fe211949`:

```sh
python3 tools/google-web-quality/extract_inventory.py --source /path/to/lighthouse-13.5.0 --output /path/to/scratch-inventory
python3 checks/validate.py
```

The extractor only reads source configuration and resolves files. It does not install Lighthouse or launch Chrome. Updating to another version requires updating the extractor's pinned version metadata and reviewing behavior changes.

## Corrections to the initial overview

The earlier document is retained as history. The deeper review establishes five categories in the 13.5.0 default source despite older four-category documentation; the fifth is experimental. A missing `llms.txt` can be N/A. Lab INP exists in qualifying timespan runs. PSI's planned CrUX removal and LHCI's optimistic aggregation default need explicit integration choices. Use the maintained playbook for current guidance.
