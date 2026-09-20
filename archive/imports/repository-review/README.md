# Design knowledge repository: inventory and proposed organization

Prepared 20 September 2026. Status: review package; no GitHub repository has been created or populated by this task. The existing collection remains local. Notion pages have not been edited, moved, deleted, or exported in this inventory.

Recommendation: one private `design-knowledge-base` repository, organized by reusable topic, with project case studies and a dated evidence archive. GitHub would become the maintained source after migration is verified. This proposal does not claim that every prior conversation, website, or cloud document has been recovered.

## What we have

The file inventory contains **319 local files, 269 distinct SHA-256 hashes, and 50 exact-duplicate groups**. These are file counts, not research-paper counts. They include 192 images/renders, 15 generated build intermediates, 8 packaged artifacts and 104 other reference/record files. Do not equate file volume with knowledge quality.

| Collection | Located material | Evidence and limits | Proposed destination |
|---|---|---|---|
| Existing knowledge base, September 19 | 21 files; 41 source records; 9 historical MindLeverX findings; playbook, worked cases, worksheet, evidence, policy and templates | Preserved research, not a new validation of source currency or project outcomes | `principles/`, `workflows/`, `projects/`, `evidence/`, `sources/` |
| Figma draft, September 20 | 22 files; 14 modules; 40 source records; 138 observed controls; 18 exercises; 63 supplied scope URLs | 34 sources marked sections-reviewed, 4 index-reviewed, 2 excerpt-reviewed. One exercise has a limited pass; 17 not run. Draft packaging has missing supporting files | `tools/figma/` |
| Visual-design study, September 7–8 | 233 files including six research chapters, nine original screenshot references, interactive study book, material demo, presentation source, exports and renders | Covers history/print, perception/motion, contemporary materials, TikTok discovery, Lucy Eden, Zach Heffner/The Aisthetes. Many files are derived artifacts | `principles/`, `reference-library/`, `learning/`, `archive/` |
| Design Field Guide | Saved materials describe a private 56-slide Google Slides deck with source directory and notes | Included in the preceding 233 files. Historical native verification is saved; live deck was not refetched | `learning/field-guide/` with source link and versioned exports |
| Current MindLeverX design work | Seven files: three design directions, 45-element rationale table, contrast calculations, site inventory and preview implementation | Exploratory concepts; full rendered/accessibility/user testing outstanding; AI features proposed, not implemented | `projects/mindleverx/` |
| Earlier originals and packages | 12 files including the eight original research documents, Notion-import ZIP and two visual-study ZIPs | Exact duplicates and historical editions; ZIP contents may overlap unpacked files and are not counted as extra extracted records | `archive/imports/` and provenance records |
| Related project guidance | 24 selected files: Squarespace/Levarum design guidance, workflow demo, MindLeverX pre-design audit, handoffs and reference build | Related candidates, not automatically promoted to universal recommendations or an active second backlog | `tools/squarespace/`, project case studies, archive |
| Notion workspace | Plugin is available; content inventory not yet performed | User's “leave Notion alone” could mean copy without modifying, or exclude it. Clarification requested. Existing local Notion ZIP says prepared, not uploaded; it does not inventory the separate Notion stash | Pending scope decision |
| Other ChatGPT conversations/cloud documents | No complete history export available in this inventory | Current conversation and saved local deliverables are available; unsaved history cannot be claimed as collected | Record as gaps until accessible |

The two existing JSON source catalogs contain **81 records with 81 distinct exact URLs**. This is not a complete source count for the older visual study, the current rationale, or all previous research. Those collections still need normalization into one catalog. New integration sources for this review are recorded separately in [integration-sources.json](integration-sources.json).

Inspect [every inventoried file in CSV](inventory.csv), the [inventory and duplicate groups in JSON](inventory.json), and the [combined existing source register](source-register.json). Each inventory row records the original local path, size and SHA-256; hashing establishes identity, not correctness.

## Proposed tree

```text
design-knowledge-base/                   # private repository
├── README.md                            # start here; task-based navigation
├── AGENTS.md                            # concise rules for agents using this repo
├── CATALOG.md                           # browse by topic, tool and project
├── CHANGELOG.md
├── principles/
│   ├── user-research-and-usability/
│   ├── information-architecture/
│   ├── typography-color-and-layout/
│   ├── accessibility/
│   ├── motion-and-interaction/
│   └── human-ai-interaction/
├── tools/
│   ├── figma/
│   │   ├── capability-map.md
│   │   ├── modules/                     # Design, Motion, Make, Weave, etc.
│   │   ├── controls/                    # context, behavior, constraints
│   │   ├── exercises/                   # procedures and actual outcomes
│   │   └── known-gaps.md
│   └── squarespace/
├── integrations/
│   ├── figma-chatgpt-codex.md
│   ├── code-connect.md
│   └── github-reuse.md
├── workflows/                           # research → brief → design → build → QA
├── reference-library/                   # named sites, designers, provenance
├── learning/                            # study book, field guide, exercises
├── projects/
│   ├── mindleverx/                      # rationale and dated case studies
│   └── levarum/
├── sources/
│   ├── catalog.json                     # stable IDs, URLs, dates, scope
│   ├── coverage.csv                     # discovery/retrieval/review/test axes
│   └── conflicts.md                     # contradictory or superseded guidance
├── evidence/                            # dated observations and verification
├── templates/                           # brief, rationale, source, test, handoff
├── governance/                          # maintenance and source-use policies
├── inbox/                               # unsorted material; not authoritative
├── archive/imports/                     # preserved originals and manifests
└── checks/                              # links, schemas, IDs, provenance checks
```

This is a proposed structure, not a representation of folders already migrated. Keep one canonical copy of each maintained topic; tag and link it from multiple catalogs instead of creating separate competing copies. Preserve different versions and contradictory evidence. Exact duplicates can share one archived object with multiple provenance paths; originals stay where they are.

Keep live product code and active implementation issues in their existing project repositories. The knowledge base carries reusable practices, dated examples, and links to the active work. Keep binary build intermediates out of the main reading path. Decide packaging for large assets after selecting final exports and recording their provenance.

## Have we scraped every detail from every site?

**No. There has been no exhaustive crawl, full visual/state capture, or comprehensive feature test.** The current Figma material is selected documentation research plus a limited UI inspection. The supplied 63 URLs are scope seeds, not 63 fully reviewed sites and not a denominator for all Figma documentation. Firecrawl previously reported insufficient credits, so selected sources were retrieved with the web tool; that did not produce a complete offline archive.

| Source or reference | Existing coverage | Still missing |
|---|---|---|
| Figma Help Center, best-practice guides and developer docs | 40 source records with explicit partial review labels; 14 synthesized modules | Complete article inventory, linked subpage coverage, full feature/context/entitlement matrix and practical tests |
| Dirtverse | Prior record says live text and screenshot inspected | All pages, responsive states and interaction/motion behavior |
| Brim | Prior live text retrieval and user's visual description | Direct visual verification in this recorded pass; responsive/motion review |
| Future Human | Opening screen visually inspected | Full experience, content, mobile and motion review |
| Jowinski and Amit Goyani | Framer gallery previews visually inspected | Live portfolio pages, interactions and mobile behavior |
| Earlier visual study | Six chapters and bounded original-source notes | Several original artwork credits, full video viewing, blocked source content, audience/production claims |
| MindLeverX website/Figma import | Saved record describes homepage imports at 1440 and 390 widths | Six other inventoried pages not imported in that session; full import fidelity not verified. This is a historical record, not a fresh audit of today's Figma file |
| Notion and full historical chats | Not inventoried here | Read/export scope and accessible material |

For completeness we need a **bounded source manifest**: allowed domains/sections, discovered canonical URLs, included/excluded pages with reasons, retrieval dates, redirects, failures, assets/video coverage, and linked descendants. Track retrieval, substantive review, visual inspection and hands-on testing separately. A successful HTML download cannot establish hover behavior, keyboard use, responsive layout, or comprehension.

Store our notes, evidence and lawful excerpts with links. Do not treat a private GitHub repo as permission to republish complete third-party sites or books. Original screenshot attribution remains an explicit research item. “Complete” should mean all items in an agreed manifest are accounted for, including exclusions and unresolved access failures.

## Figma, ChatGPT, Codex and GitHub

| Route | Documented capability | How we should use it |
|---|---|---|
| Figma's dedicated ChatGPT integration | Figma's help article describes generating FigJam diagrams and Figma Slides, then opening them in Figma | Use for diagrams/presentations; do not assume that this article describes every Codex/plugin capability. [Figma help](https://help.figma.com/hc/en-us/articles/35326636109975-Use-ChatGPT-with-Figma) |
| Codex + remote Figma MCP/plugin | Structured design context, variables, components, Make resources, Code Connect, native canvas work and live-UI capture | Main route for building and refining MindLeverX. Figma recommends remote MCP for its broadest capabilities. [Official setup](https://help.figma.com/hc/en-us/articles/39888629089175-Codex-and-Figma-Set-up-the-MCP-server) |
| Native canvas editing | `use_figma` can create/update real frames, components, variables and auto layout | Generate editable variations using the file's design system; inspect resulting structure. [Write to canvas](https://developers.figma.com/docs/figma-mcp-server/write-to-canvas/) |
| Running UI → Figma | Live browser UI can become editable frames; code-to-canvas is separate from native generation | Capture specified routes and states for comparison; do not infer that capturing a homepage captures a whole site. [Code to canvas](https://developers.figma.com/docs/figma-mcp-server/code-to-canvas/) |
| Figma → implementation | Design context can inform code generation; the agent implements the changes | Reuse project components and test the implementation. This is an instructed workflow, not proof of automatic synchronization. [OpenAI workflow](https://developers.openai.com/blog/building-frontend-uis-with-codex-and-figma) |
| Plugins across ChatGPT/Codex | OpenAI describes a shared plugin catalog and skills/MCP capabilities across supported surfaces; actual access depends on the host and connection | Check tools in the active session instead of transferring assumptions between products. [OpenAI plugins](https://learn.chatgpt.com/docs/plugins) |
| GitHub knowledge → future build | Our proposed handoff: load a named knowledge release, select relevant modules and write project decisions | Add a short project `AGENTS.md` pointer and record the knowledge commit used. Codex discovers project instruction files; it does not automatically ingest an unrelated remote repository. [Instruction discovery](https://learn.chatgpt.com/docs/agent-configuration/agents-md) |

Observed in this session: Figma tool metadata includes design context, screenshots, variable definitions, native editing, web capture, Code Connect, motion, shaders and Weave operations. This confirms availability in the tool list, not successful execution of each feature or the user's entitlement to every action. No additional integration was installed or tested for this review.

The documentation itself needs reconciliation: Figma's dedicated ChatGPT article describes a narrower route than the current plugin/MCP material. Separate product surfaces in the catalog. The Figma developer write guide and newer Help Center summary also differ on Dev-seat draft editing; confirm the exact account/file context before relying on that detail. Tool availability, documented support, and verified execution require separate fields.

Recommended flow: **versioned GitHub guidance → scoped brief in ChatGPT/Codex → Figma components and variations → code implementation → browser/accessibility/behavior checks → dated learning back into GitHub**. This flow is our proposed working practice.

## What else we need

| Addition | Why it matters | Acceptance evidence |
|---|---|---|
| Task-based start page and compact build handoff | Future agents need a usable entry point, not hundreds of files pasted into context | In a fresh project, retrieve the right guidance and report the exact release/commit used |
| Stable source and decision IDs | Connect every important recommendation to its basis without making preference sound like law | Each decision labels requirement, recommendation, project choice, hypothesis or observation; links resolve |
| Element rationale template | Carry the user's requested design rigor into every build | Element → user task → recognized principle/source → choice → color → motion → reduced-motion behavior → validation |
| Practical Figma capability tests | Reading articles and seeing buttons do not establish proficiency | Record reproducible exercises, actual outputs, screenshots, constraints and failures; finish the 17 unrun exercises in safe practice files |
| Documentation conflict and freshness queue | Figma capabilities and plans change; conflicting guidance already exists | Resolve or retain explicit exceptions; refresh affected guidance before consequential implementation, release or spending |
| A working component/token example | Connect theory to reusable implementation | One representative component and responsive section verified in Figma and code, including states and accessibility behavior |
| AI interaction patterns and evaluations | Make AI features useful and trustworthy | Test citations, unsupported answers, stale/conflicting evidence, correction, cancellation, loading/error states, latency and cost |
| Retrieval and decision evaluation cases | Establish whether the collection improves future builds | A small set of realistic questions/tasks finds the correct sources, preserves limitations, and rejects unsupported claims |
| Source coverage dashboard | Make missing research visible | Every manifest URL has a disposition and independent retrieval/review/visual/test fields |
| Maintenance and release rules | Prevent silent drift and competing editions | Changelog, owner, review triggers, release tags, link/schema checks and migration reconciliation |
| Asset provenance and archive policy | Preserve research without confusing authorship, reuse rights or generated output | Attribution/reuse status recorded; approved exports separate from build intermediates |
| User and product evidence | Attractive examples do not establish usability or commercial outcomes | Representative task research and project-specific measurement plans, kept separate from style preference |

My priority is: finish inventory and deduplication → repair packaging → publish a verified private repository → prove one fresh-build reuse workflow → deepen the missing Figma and interaction tests. A large retrieval service or custom plugin can wait until ordinary Markdown navigation and task-based retrieval are shown to work.

## Packaging defects found during this inventory

- Figma draft references `evidence/2026-09-20-ui-inspection.md`, but the file has not yet been written. Its 138 controls and limited exercise outcome cannot be presented as a complete evidence package yet.
- Figma draft lacks its own README and a written conflict record for the boolean-variable/component-property discrepancy referenced as X02.
- The older visual-study verification says four chapters, while six chapter files now exist. Preserve the historical verification scope and add a later reconciliation rather than silently treating the old check as covering later additions.
- Existing repository-level verification describes earlier source totals. A migration verification must recalculate current totals and check local links.
- Historical local paths and duplicate export editions need portable links and provenance mapping before GitHub import.

## Migration success criteria

1. Private repository URL is real and readable using the intended GitHub account.
2. Every in-scope source artifact is imported, linked, deduplicated with provenance, excluded with a reason, or marked inaccessible. No silent loss.
3. Original files and Notion pages are unchanged.
4. Source IDs, file links, JSON schemas and content hashes reconcile; historical check dates are preserved.
5. Readability and retrieval work from a fresh checkout/session, with an explicit knowledge version.
6. Missing research, untested features and source conflicts remain visible.

This review fulfilled the inventory/proposal stage. It did not perform the proposed migration, an exhaustive crawl, a live Slides refresh, or the Figma practice suite.
