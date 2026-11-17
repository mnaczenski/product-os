# product-os

Agent-driven product management operating system for Claude Code. Runs on a markdown workspace repo, one per product organization.

## Install
```
/plugin marketplace add <org>/product-os-marketplace   (or a local path)
/plugin install product-os@product-os-marketplace
/reload-plugins
```
Create an empty private git repo (e.g. product-os-workspace), open Claude Code there, run `/workspace-setup`.

Build the foundation from existing documents: drop strategy decks, role descriptions, operating principles, proposal templates, roadmaps, ICP and research docs into `sources/`, then run `/bootstrap`. It drafts strategy, ICP, principles and CLAUDE.md with source citations, adopts your proposal template, optionally seeds ideas, initiatives and decisions, and lists conflicts and open questions. Review and set `status: confirmed` on each strategy file.
Connect MCP servers you use (Jira/Confluence, Amplitude, Superset, Slack, HubSpot, meeting transcripts) so commands can pull data directly.

## Rhythm
| When | Command | Purpose |
|---|---|---|
| Once, then on new docs | `/bootstrap` | Foundation from existing documents, cited, with open questions |
| Daily | `/today` | Task list: due routines, to-dos and brief items, prioritized, top items prepared |
| Anytime | `/task <text>` | Add, finish, snooze or drop tasks and routines in plain language |
| Daily | `/brief` | What changed, what needs a decision, top 3 |
| Once, then as needed | `/sources` | Configure, test and enable signal and work sources |
| Daily | `/pulse` | What changed in roadmap, docs, Miro, Figma, Jira, GitHub, linked to bets, with drift and gaps |
| Daily | `/collect` | Pull signals from all due sources, dedupe, ICP-tag, link to problems |
| Anytime | `/signal [input]` | Ad-hoc input outside the configured sources |
| Daily | `/challenge <doc>` | Red-team an idea or epic, coaching questions for the owner |
| Daily | `/reply <request>` | Close feedback loops, including "we will not do this" |
| Weekly | `/synthesize` | Cluster signals into ICP-weighted problems |
| Weekly | `/idea <problem>` | Shape a bet: evidence, hypothesis, metrics, validation |
| Weekly | `/prep <meeting or 1:1>` | Prep from artifacts, never person scoring |
| Weekly | `/decide <topic>` | Options, recommendation, recorded decision |
| Monthly | `/portfolio` | Strategy fit, backlog health, capacity vs bets, drift |
| Monthly | `/outcome <initiative>` | Results vs metrics defined before build |
| Monthly | `/update <audience>` | State of the Unit, leadership, stakeholders |
| Monthly | `/radar` | Market and competitor changes that matter |
| Monthly | `/reflect` | Did our bets work, how should the system improve |

## Agents
librarian, collector, work-scout, signal-analyst, challenger, metrics-analyst, market-scout, writer.

## Work sources
Defined in `work/sources.yml`: tool, scope, what changes matter, cadence, how to link to ideas and epics. Examples ship disabled: roadmap, PM docs, Miro discovery boards, Figma, Jira epics, GitHub releases. `/pulse` writes a digest per run with changes by bet, drift (work without approved idea or decision), gaps (docs without metrics, handoffs without validation) and unmapped changes.

Artifact level only: no per-person activity, counts or comparisons. This keeps the system out of performance monitoring (BetrVG §87(1) No. 6). If you want to change that, align with the works council first.

## Tasks
Routines live in `tasks/routines.yml` (cadence, optional rotation, assist, connector, minutes). To-dos live in `tasks/todo.md`. `/today` builds the daily list in `tasks/log/<date>.md`, capped at 7 items, and prepares the top 3 by running their assist, e.g. a Figma change summary or a `/challenge` of the rotated PM's roadmap.

## Signal sources
Defined in `signals/sources.yml`: type (mcp, web, folder, manual), tool, query, cadence, kind, trust, ICP hint. All examples ship disabled. Test with `/sources test <id>` before enabling. `/collect` runs incrementally per source, keeps a cursor in `signals/.state/`, dedupes across sources and never advances the cursor of a failed source.

Unattended runs are possible with Claude Code in headless mode from cron or launchd, e.g. `claude -p "/collect daily"` in the workspace. Connectors must be authenticated for that user.

## Boundaries
- Humans decide priorities, bets and people matters.
- PMs work at epic level. No user stories, no delivery planning.
- Evidence must trace to real sources. Inferred evidence is marked [assumption].
- No scoring or ranking of individuals. If performance evidence is ever added, align with the works council first (BetrVG §87(1) No. 6) and GDPR.

## Relation to agent-stack
Independent. product-os works without agent-stack. If you use both, an approved idea's Handoff section can be pasted into agent-stack's `/pm` in a code repository.
