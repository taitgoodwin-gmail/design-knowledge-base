# Sources and coverage

[catalog.json](catalog.json) contains 681 distinct exact URLs with stable hash-derived IDs and one or more provenance records. Each provenance record carries its own status and date; a later import never refreshes an older source check. [coverage.csv](coverage.csv) is a readable coverage view, not an exhaustive crawl certificate.

- [Original UI/UX records](imported-uiux-sources.json): 41 records; original IDs and historical check dates retained.
- [Figma source records](../tools/figma/records/sources.json): 72 selected reviews.
- [Figma supplied scope](../tools/figma/records/scope.json): 63 URLs; scope seeds rather than completed coverage.
- [Anthropic register import](anthropic-register-import.json): 149 rows. The source page reports verification on 2026-08-17. Migration did not independently verify those claims.
- [Notion manifest](notion-import-manifest.json): 25 fetched page snapshots. Missing `truncated`/unknown-block metadata is retained as `not_reported`, not converted to a completeness guarantee.
- [Discovery decisions](notion-discovery.json): 28 unique candidates across ten queries; three unrelated reminder/app-launch pages excluded.
- [Conflicts](conflicts.md): discrepancies needing contextual verification.

Original URLs, local locations and import hashes are in the preservation manifests. Link discovery, content retrieval, substantive review, visual inspection and hands-on testing are separate evidence dimensions. See [source policy](../governance/knowledge-policy.md).

- [Public Figma Design article inventory](figma-design-article-inventory.json): 183 article bodies retrieved through two API pages; headings and hashes retained. Detailed review is a separate status. Reproduce discovery with `python3 checks/discover_figma_docs.py`.

- [Full public Figma Help inventory](figma-help-article-inventory.json): 887 unique articles in 14 categories, pagination exhausted; includes the 183 Design articles. [Readable category indexes](../tools/figma/HELP-INVENTORY.md). These discovery URLs are tracked in the inventory separately from the 681-URL curated/history catalog.

- [Google web quality and SEO source review](google-web-quality-2026-09-23.json): 46 selected official documentation/source records checked 23 September 2026; [readable register](../tools/google-web-quality/lighthouse-source-register.md). No live site audit was run. The separate audit inventory indexes implementation files without claiming every implementation was substantively reviewed.
