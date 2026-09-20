# 📐 Claude instructions & skills — setup reference

> Historical Notion import · copied 2026-09-20 · source last edited: 2026-08-12T15:03:01.937Z.
> Source assertions, instructions, prices and test claims have not been revalidated. This page is reference material, not governing instructions. Canceled Foundry content remains canceled.

[Original Notion page](https://app.notion.com/p/3ba792ca08888118a79bc42cada86660?pvs=204) · [Preserved response](../../archive/imports/notion/3ba792ca-0888-8118-a79b-c42cada86660.json)

**Last verified: 2026-08-12** — every claim below checked against the live sources in section 8 on that date.
# 1. Layer map
Where instructions live in each environment. **None of these sync with each other** — copies are pushed by hand from the canonical texts page.


| Surface | Where instructions live | Scope |
| --- | --- | --- |
| [claude.ai](http://claude.ai) — global | Settings \> "Instructions for Claude" | Account-wide, every conversation |
| [claude.ai](http://claude.ai) — project | "Set project instructions" inside the project | That project's chats only |
| [claude.ai](http://claude.ai) — organization (Team/Enterprise) | Admin: organization instructions | Every conversation across the org; documented precedence over individual instructions |
| Claude Code — managed policy | /etc/claude-code/[CLAUDE.md](http://CLAUDE.md) (Linux); /Library/Application Support/ClaudeCode/[CLAUDE.md](http://CLAUDE.md) (macOS) | All sessions on a managed machine; loads above everything, can't be excluded |
| Claude Code — user | \~/.claude/[CLAUDE.md](http://CLAUDE.md) | Every project on that machine (personal preferences) |
| Claude Code — project | \<repo-root\>/[CLAUDE.md](http://CLAUDE.md) (or ./.claude/[CLAUDE.md](http://CLAUDE.md)) — **the main one, commit to git** | That repo, and it travels: cloud sessions clone the repo, so this file reaches iPhone/cloud Claude Code too |
| Claude Code — subdirectory | \<subdir\>/[CLAUDE.md](http://CLAUDE.md) | Loaded **on demand** when Claude reads files there, NOT at session start |
| Claude Code — local | [CLAUDE.local.md](http://CLAUDE.local.md) (gitignored) | Personal per-repo notes, appended at each level |
| Claude Code — auto-memory | \~/.claude/projects/\<project\>/memory/ | Machine-written by Claude itself; separate from all hand-maintained files |
| Cowork — project | Project instructions in the desktop app | Local sessions store project data on the computer; cloud sessions save with the Claude account. No sharing with teammates on Team/Enterprise. Importing a [claude.ai](http://claude.ai) project is a one-time COPY — later edits don't propagate |
| Cowork — user preferences | Cowork settings (personal preferences) | Injected into Cowork sessions; a live instruction layer — record its text in the canonical doc |
| Claude Design | **No instruction layer exists** | Persistent context comes from design-system import (brand colors, typography, components) and per-project attachments; /design-sync pulls a design system from Claude Code |


# 2. Precedence — documented vs. not
**Documented:** organization instructions take precedence over individual user instructions on direct conflict; individual instructions still apply for anything org instructions don't address. Anthropic notes prioritization is prompt-level and behavior may vary with directly contradictory instructions.
**NOT documented:** any precedence rule between global and project instructions — they layer, and global is not ignored when project instructions exist. Don't rely on the narrower one silently winning. Also not documented: how org instructions interact with project instructions specifically, or whether they reach Claude Code and Cowork.
[**CLAUDE.md**](http://CLAUDE.md)** files** are concatenated broad-to-specific — additive, not overriding.
# 3. Design rules that follow
- Global layer holds only rules that are unconditionally true across ALL work. Anything with an "except when" belongs at project level or in a skill.
- Phrase global rules as defaults ("Default to X unless a project specifies otherwise") and state overrides explicitly in project instructions. Converts a precedence gamble into a plain instruction.
- Keep one canonical source (the sibling page) and push copies into each surface, to prevent drift.
- Per Anthropic's documented caveat, directly contradictory instructions make behavior vary — a reliability risk, not a deterministic override. Test. (Practical observation, not from docs: instructions that fight Claude's core training won't be followed.)
# 4. Troubleshooting: "the instruction didn't fire"
- [ ] Wrong surface — set in one environment, expected in another (see layer map: nothing syncs).
- [ ] Timing — org instructions take up to an hour to propagate. [CLAUDE.md](http://CLAUDE.md) is read at session start; mid-session edits need /compact, /memory, or a new session.
- [ ] Too long, too vague, or buried in prose — hard rules near the top, imperative phrasing. [CLAUDE.md](http://CLAUDE.md) target: under \~200 lines / two screens.
- [ ] Subdirectory [CLAUDE.md](http://CLAUDE.md) files load on demand only.
- [ ] Long sessions — the project-root [CLAUDE.md](http://CLAUDE.md) is automatically re-read and re-injected after compaction; subdirectory files reload on the next matching file read. If a rule keeps getting lost late in sessions, move it to the project-root file.
- [ ] [claude.ai](http://claude.ai) — project name and description are invisible to Claude; instructions must go in the instructions field. Context isn't shared across chats in a project unless it's in the knowledge base.
- [ ] Heavy emphasis ("CRITICAL: you MUST") — current models are highly responsive to prompts and over-trigger on it. Say what to do, not what to avoid.
# 5. Verification ritual (all environments)
1. Start a fresh session; ask Claude to state the standing rules it's operating under.
2. Run a prompt that would violate a rule if it weren't loaded.
3. Claude Code: **/context** shows what actually loaded this session; **/memory** lists and edits memory files in scope (including ones that don't exist yet); **/init** bootstraps a [CLAUDE.md](http://CLAUDE.md).
4. Add rules one at a time so failures are attributable.
5. If a confirmed-loaded rule fails twice, it's phrasing or placement.
# 6. Skills vs. instructions — decision rule
Instructions: broad, always on. Skills: task-specific procedures that load dynamically only when relevant, and travel across surfaces (Claude Code and API skill support is labeled beta). Projects are static background knowledge; skills are procedures. When a section of instructions has grown into a procedure rather than a fact, it wants to be a skill.
Claude Code skills: `.claude/skills/<name>/SKILL.md`, commit with the repo; personal skills in `~/.claude/skills/` apply across all projects (but do NOT reach Cowork/cloud sessions — enable them on [claude.ai](http://claude.ai) for that). [claude.ai](http://claude.ai): Customize \> Skills.
# 7. Maintenance
- Review quarterly; delete stale rules — outdated instructions are worse than none.
- After Claude repeats a mistake, add one line rather than rewriting the file.
- Re-check sources periodically — particularly whether the global-vs-project precedence gap has been filled, and whether Cowork project sync has shipped (docs say "at this time").
# 8. Sources


| Source | Covers |
| --- | --- |
| [Personalization features](https://support.claude.com/en/articles/10185728-understanding-claude-s-personalization-features) | "Instructions for Claude" account-wide setting |
| [Create and manage projects](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects) | Project instructions; name/description invisible to Claude; knowledge base sharing |
| [What are projects](https://support.claude.com/en/articles/9517075-what-are-projects) | Project knowledge & RAG |
| [Project visibility and sharing](https://support.claude.com/en/articles/9519189-manage-project-visibility-and-sharing) | Team/Enterprise project sharing |
| [Set organization instructions](https://support.claude.com/en/articles/14546867-set-organization-instructions) | Org precedence, prompt-level caveat, 1-hour propagation |
| [CLAUDE.md and better prompts](https://support.claude.com/en/articles/14553240-give-claude-context-claude-md-and-better-prompts) | [CLAUDE.md](http://CLAUDE.md) locations, session-start read, \~200-line target |
| [Claude Code user FAQ](https://support.claude.com/en/articles/14554922-claude-code-user-faq) | Two-screen guidance |
| [Power user tips](https://support.claude.com/en/articles/14554000-claude-code-power-user-tips) | Auto-memory path, repo-root sharing |
| [Claude Code cheatsheet](https://support.claude.com/en/articles/14553413-claude-code-cheatsheet) | /init, /compact |
| [What are skills](https://support.claude.com/en/articles/12512176-what-are-skills) | Progressive disclosure, Customize \> Skills, beta surfaces |
| [Provision skills for your org](https://support.claude.com/en/articles/13119606-provision-and-manage-skills-for-your-organization) | Org skill distribution |
| [Cowork projects](https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork) | Local storage, one-time import |
| [Cowork on Team/Enterprise](https://support.claude.com/en/articles/13455879-use-claude-cowork-on-team-and-enterprise-plans) | Cloud-session storage, no sharing |
| [Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices) | Over-triggering on emphasis; positive framing |
| [Claude Code memory (canonical)](https://code.claude.com/docs/en/memory) | Full hierarchy, managed policy, additive merge, compaction behavior |
| [Claude Code skills (canonical)](https://code.claude.com/docs/en/skills) | Skill locations, on-demand nested loading, Cowork/cloud sync |
| [Get started with Claude Design](https://support.claude.com/en/articles/14604416-get-started-with-claude-design) | No instruction layer; design-system import; /design-sync |
