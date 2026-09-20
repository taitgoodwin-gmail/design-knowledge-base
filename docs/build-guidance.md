# Build guidance for this repository

Apply [official-source practice](../governance/official-source-build-practice.md) proportionately. This is a knowledge migration, not a new website release or a claim of complete Figma proficiency.

GitHub official repository creation and file-size guidance were checked 2026-09-20. Chosen implementation: a private repository, ordinary Git for the current bounded collection, preserved baseline history and a validation workflow. All imported files are below GitHub's 100 MiB hard limit; the largest is approximately 27 MB.

Sources: [Create a repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository), [large files](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github).

Checks: source/archive hashes, valid JSON, unique source IDs, resolving maintained file links, no credential-like content introduced, remote private visibility, remote/local commit equality, and fresh-checkout retrieval. A link check or source import does not revalidate a website, source claim, user outcome or accessibility conformance.
