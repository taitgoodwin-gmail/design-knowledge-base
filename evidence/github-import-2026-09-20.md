# Initial GitHub import — 20 September 2026

## Scope and implementation choices

Owner requested a separate design repository. Created `taitgoodwin-gmail/design-knowledge-base` as private. Imported a filesystem snapshot from `/Users/tag/Documents/Codex/design-knowledge-base`, preserving 459 files and their bytes. The source checkout had uncommitted reorganization; its working tree and local-only Git remote were left unchanged. The import is a new Git history. The original local history remains available in the source checkout.

Added a root README, full tree, `.gitignore`, Figma location record, this receipt, and a per-file hash manifest. No MindLeverX website/application source was moved or altered. No collaborator access or deployment was configured.

## Official guidance

- Source: https://cli.github.com/manual/gh_repo_create
- Checked: 2026-09-20.
- Documented behavior: GitHub CLI supports creating a private repository from a local source repository and pushing committed files.
- Project choices: private visibility, separate design repository, current filesystem snapshot, independent Git history.

## Verification scope

The manifest records the original imported files with byte sizes and SHA-256 hashes. Import checks compare those files against the snapshot and committed Git blobs. The complete tree lists committed source paths. Remote visibility, branch, commit, and file inventory are checked after push.

A basic credential-pattern and sensitive-filename scan, including ZIP contents, found no matches. This is not a comprehensive security audit. Research claims and historical relative links were not revalidated during this storage task; dated source guidance remains dated. Figma's native design content was linked, not exported.

## Verified result

- Repository: https://github.com/taitgoodwin-gmail/design-knowledge-base
- Visibility: private. Default branch: `main`.
- Initial import commit: `03d0c7d23582dd09fc284af15be2eb88e041dbb9`.
- GitHub recursive tree was complete, with 465 files.
- All 465 remote Git blob hashes matched the local committed tree; all 459 original imported paths were present.
- All 459 copied files matched their recorded SHA-256 hashes before commit.
