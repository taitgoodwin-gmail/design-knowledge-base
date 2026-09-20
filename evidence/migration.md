# Migration evidence — 20 September 2026

Scope: known local design research inventory plus relevant Notion search results in the AugMind.ai workspace. This is preservation/organization, not a full web crawl or independent verification of every source claim.

- 319 original local files are byte-preserved in [the archive manifest](../archive/imports/local-manifest.json); 269 distinct SHA-256 hashes and 50 duplicate groups.
- 25 Notion pages were fetched read-only from 28 discovered candidates. Three unrelated reminder/app-launch pages were excluded with a recorded reason. No Notion pages were edited or deleted.
- Notion completeness metadata was not returned; it is recorded as `not_reported`. Returned page bodies were preserved. This is not an exhaustive workspace export or proof that every embedded resource was captured.
- The Anthropic register parsed into 149 rows, with its reported 2026-08-17 verification date preserved. Current model/pricing/platform claims were not independently revalidated.
- 442 distinct exact URLs are cataloged, including scope seeds and links not retrieved. No full chat-history export, exhaustive site scrape, live Slides refresh, or Figma practice suite completion is claimed.
- Original local files and earlier baseline Git commit are preserved. Converted Notion Markdown is for reading; original JSON hashes establish snapshot identity.
- Missing Figma README/inspection narrative/conflict records were supplied. Inspection narrative explicitly states its reconstruction from prior same-session observations.

Run `python3 checks/validate.py` for preservation, record and maintained-link checks; `python3 checks/retrieval_smoke.py` checks five navigation queries. Machine results and remote verification are saved alongside this file after execution.

## Remaining research work

The seventeen unrun Figma exercises, source conflicts, full reference-site interactions, original asset attributions, external Drive links and unsaved past conversations remain identified gaps. They do not prevent preserving and using this bounded collection, but they constrain claims made from it.

## Existing GitHub history reconciled

An independent publication of the in-progress local collection was found at `c82cff3407b8df523ace706c88e3ddb04b87d639`. Its [initial import receipt](github-import-2026-09-20.md) and manifest remain historical records of that snapshot. This edition merges that history with the original local baseline and completes the missing navigation/evidence/checks. Initial-import hashes describe the initial commit, not subsequently revised maintained files.

## Verified publication

The private GitHub repository was read back at content commit `b453f0a03512eb26afdf1089d34ffa1ba69b9b60`. All 502 remote blob paths/hashes matched the local committed tree. A fresh authenticated GitHub clone passed the archive/hash, JSON, source-ID, maintained-link and five-query retrieval checks. GitHub Actions passed for that commit. See [machine-readable remote verification](remote-verification.json) and [the successful workflow](https://github.com/taitgoodwin-gmail/design-knowledge-base/actions/runs/35529511661). This final documentation update records the evidence; release tag v2.0.0 identifies the completed edition.
