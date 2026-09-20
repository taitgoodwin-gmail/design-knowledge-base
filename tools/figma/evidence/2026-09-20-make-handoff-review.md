# Make, handoff and accessible editor operation

Checked 20 September 2026 against eight official Help articles, also present in the dated public Help inventory. **Sections reviewed; these workflows were not executed.** Body hashes in the accompanying [review record](2026-09-20-make-handoff-review.json) identify the retrieved versions. This extends source knowledge without upgrading the 18 exercise results.

## Choose the integration by its actual direction

| Route | Documented behavior | Our implementation choice |
|---|---|---|
| Standard Make → GitHub export | Creates a repository for that Make file, then pushes to its default branch. It does not pull subsequent GitHub edits into Make; a later push overwrites them. Existing unrelated repositories and branch management are not supported by this route. The connection applies to the Figma team/organization. | Decide which environment owns edits before exporting. Preserve a separate reviewed development branch/copy for subsequent engineering. Never treat this as synchronization with the knowledge repository. |
| Make in a local codebase | Separate closed beta, limited to admitted accounts using the Mac beta desktop app. It works with a local or cloned Git repository and supports local commits, branches and GitHub pull requests. Repository setup uses `.figma/make` scripts and environment configuration. | Check admission first; use the product repository and its existing development checks. No desktop installation, application or repository connection was performed for this review. |
| Make preview → Design layers | Copies the current preview state into editable layers. The result has no Make connection or working interactions and is not automatically tied to the design system; available variables may be matched. | Record route, viewport and state when capturing. Rebuild and verify component relationships and interaction states before using the copy as a specification. |

Sources: [S55: Standard GitHub push](https://help.figma.com/hc/en-us/articles/35463818346647-Push-from-Figma-Make-to-GitHub), [S54: Local codebase beta](https://help.figma.com/hc/en-us/articles/40775535020695-Make-in-your-local-codebase), [S56: Copy preview layers](https://help.figma.com/hc/en-us/articles/35060759685015-Copy-a-Figma-Make-preview-as-design-layers).

These routes have different scopes; their different GitHub behavior is not an unresolved documentation conflict. The existing Codex → Figma context → local implementation fixture is a fourth, separately [exercised route](lab/prototype-and-handoff.md).

## Give Make reusable design context

[S52: Explore Make](https://help.figma.com/hc/en-us/articles/31304412302231-Explore-Figma-Make) describes design/image inputs, chat, preview, editable code and publication. Its new editing panel and annotations are rolling out for new files, so an older file may expose a different interface. File viewers can see chat history; public visitors to a published app do not thereby receive access to its source Make file. Publishing also requires appropriate rights for incorporated material. A functioning preview is not evidence of production readiness.

[S53: Make kits](https://help.figma.com/hc/en-us/articles/39241689698839-Get-started-with-Make-kits) combine npm code packages, published Design variables/styles and guidelines. Full seats on paid plans are documented for kits; publishing a kit requires moving it out of Drafts. Guidance should explain token units and escaping, semantic choices, type roles and composed values. Test a kit against the actual system before publishing it.

Our suggested MindLeverX kit would contain existing implementation components, semantic surface/text/action tokens, approved type roles and an evidence-card specification. Its instructions should require source links, explicit simulated-data labels, error recovery and a static motion alternative. This is a proposed application of the knowledge base, not an installed kit or a claim that prompts enforce every constraint.

## Handoff signals have limits

[S57: Inspecting](https://help.figma.com/hc/en-us/articles/22012921621015-Guide-to-inspecting) varies by plan, seat and file permission. Design Mode still provides inspection routes without Dev Mode. Dev Mode adds context such as variable alias chains, component exploration and change comparison; file copying restrictions can hide code output. A source-image download and a rendered layer export serve different purposes. Record the intended asset, selected state and actual permissions rather than assuming a missing panel means a missing product capability.

[S58: Statuses](https://help.figma.com/hc/en-us/articles/26781702258583-Dev-Mode-statuses-and-notifications) documents Ready for dev and a plan-gated Completed status. The automatic Changed state does **not** catch an existing variable/style value change or a shared-library instance update. Status changes can notify prior Dev Mode viewers. Our practice: include library/token versions and implementation checks in a handoff; a status badge alone is not a complete change detector or a test result. No status was changed during this review.

## Make the editor usable, then test the product separately

[S59: Accessibility at Figma](https://help.figma.com/hc/en-us/articles/35063862380311-Accessibility-at-Figma) documents screen-reader adaptation, enhanced contrast, region navigation with F6 on Mac/Control+F6 on Windows, Actions search and keyboard canvas selection. It describes Figma as working toward WCAG 2.2 AA, not a blanket completed-conformance assertion. Its annotation guidance notes that adding measurements by keyboard is currently unavailable.

Our practice: choose relevant editor settings with the person using the tool; verify navigation and shortcuts on their operating system. Separately test the produced website's semantic structure, focus, contrast, motion and assistive-technology behavior. Editor accessibility controls do not certify the exported or implemented website. No settings were changed and no screen-reader test was run for this review.

## What is still unverified

Make generation, kit publication, standard GitHub export, local-codebase beta access and the new inspection/accessibility operations above remain documentation-only. Existing E11 evidence concerns the native **Design agent**, not Make. Sites/Buzz terms and Weave linking remain separate [pending prerequisites](lab/product-access-and-readiness.md).
