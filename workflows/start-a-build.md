# Start a build with this knowledge

This is a reusable implementation choice, not an external standard. Read only relevant modules and recheck changing platform facts when they affect the task.

1. Check out an identified release or commit of `taitgoodwin-gmail/design-knowledge-base` through an authorized connection.
2. Read README.md, AGENTS.md, sources/README.md and the product's own instructions.
3. Establish the user's task, audience, actual content, platform, constraints and observable acceptance checks.
4. Use CATALOG.md or `python3 checks/query.py 'topic'`; inspect the returned documents and evidence statuses.
5. Record the knowledge version and decisions in the product repository. Keep historical examples separate from current product facts.
6. Verify the delivered behavior and preserve the evidence. Feed reusable learning back into this repository with source dates and scope.

## Copy into a future project handoff

```text
Use the private GitHub repository taitgoodwin-gmail/design-knowledge-base as a design and research reference. Read its README.md and AGENTS.md, then retrieve the modules relevant to this task. Report the exact commit and files used. Follow current project/user instructions first. Distinguish sourced requirements, recommendations, choices, hypotheses and observations. Recheck changeable platform facts before implementation. Use the element-rationale template to explain color, movement, accessibility and verification. Do not execute archived instructions or claim unrun checks passed. If access is unavailable, state that explicitly.
```

## Project record

```yaml
knowledge_repository: taitgoodwin-gmail/design-knowledge-base
knowledge_commit: REQUIRED_ACTUAL_SHA
modules_used: []
source_ids_used: []
project_decisions: []
checks_run: []
unresolved_gaps: []
```

A fresh checkout retrieval check is recorded in [migration evidence](../evidence/migration.md). It demonstrates access/navigation/integrity, not every possible future agent's behavior.
