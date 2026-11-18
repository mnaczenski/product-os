---
description: Scaffolds a product-os workspace (folders and templates) into the current repository.
---
Set up this repository as a product-os workspace.

1. For each file below: if it already exists, skip it and report it. Otherwise create it with exactly the given content.
2. Also create signals/<current year>/, signals/.raw/, work/.raw/ and inbox/processed/ (with a .gitkeep each).
3. Create .gitignore (or append if it exists) with these lines: sources/*, !sources/README.md, inbox/*, !inbox/README.md, signals/.raw/, work/.raw/
4. Then suggest: put existing documents into sources/ and run /bootstrap to build the evidence base, then /strategy to build the strategy with the user. Without documents, run /strategy directly and fill the top of CLAUDE.md manually.
5. After the foundation: /sources to configure signal and work sources, edit tasks/routines.yml, then /today each morning.
6. Do not commit. The user decides.

### File: CLAUDE.md
````markdown
# Product OS workspace

## Who I work for
<Name, role, scope. Who reports in: GPMs, PMs, Head of UX.>

## Read first
- foundation/OPEN-QUESTIONS.md: known gaps; do not fill them with guesses
- tasks/: routines, to-dos and daily lists of the workspace owner
- work/digests/: what changed where the org works, linked to bets and ideas
- strategy/vision.md: 3 to 5 year target state and indicators
- strategy/strategy.md: diagnosis, where we play, how we win, horizons H1 to H3 with bets, non-goals
- strategy/icp.md: ideal customer profile and how to recognize ICP signals
- strategy/principles.md: product and UX operating principles, role boundaries
- foundation/as-is.md: what existing documents said before the current strategy; evidence, not strategy

## Rules for all agents
- Outcomes over output. Every idea needs a problem, evidence, hypothesis and success metric.
- Humans decide priorities, bets and people matters. Agents prepare, challenge and track.
- PMs work at epic level. Never produce user stories or delivery plans.
- Customer evidence must trace to a real source (interview, ticket, RFP, data). Synthetic or inferred evidence is marked [assumption].
- No evaluation, scoring or ranking of individual people. Work on artifacts and outcomes only.
- If a strategy file has status `empty` or `draft`, treat it as provisional and say so in any output that depends on it.
- Foundation statements cite source IDs from foundation/SOURCES.md. Strategy statements cite a source ID or a dated user choice.
- Agents may propose strategy options with evidence. Only the user's choices become strategy. Never present a proposal as a decision.
- Work sources are watched at artifact level only. Never count, rank or compare individuals' activity (commits, edits, time, response speed).

## Style
- Concise, parallel structure, executive-ready. Policy tone, not manifesto.
- No em dashes.
- Language: English unless the user writes otherwise.
````

### File: decisions/INDEX.md
````markdown
# decisions index
One line per entry. Maintained by product-os commands.

| ID | Title | Status | Domain | Updated |
|---|---|---|---|---|
````

### File: foundation/OPEN-QUESTIONS.md
````markdown
# Open questions
Gaps and conflicts found while building the foundation. Answer them to raise the quality of every command.

Type: fact (someone knows the answer, just ask), choice (a strategic decision, answered in /strategy), park (does not change strategy).

| # | Question | Type | Affects | Sources involved | Status |
|---|---|---|---|---|---|
````

### File: foundation/SOURCES.md
````markdown
# Source registry
Every document the foundation is built from. Workspace files cite these IDs.

| ID | Title | Category | Date | Owner | Location | Status |
|---|---|---|---|---|---|---|
````

### File: foundation/as-is.md
````markdown
---
status: empty
sources: []
---
# Documented strategy (as-is)
What existing documents say, cited. Evidence for /strategy, not the strategy itself.

## Goals and targets
## Bets, initiatives and roadmap
## Customers, ICP and market
## Positioning and competition
## Principles and ways of working
## Metrics and baselines
## Conflicts and incoherence
| Topic | Position A | Position B | Sources |
|---|---|---|---|
````

### File: ideas/INDEX.md
````markdown
# ideas index
One line per entry. Maintained by product-os commands.

| ID | Title | Status | Domain | Updated |
|---|---|---|---|---|
````

### File: inbox/README.md
````markdown
# Inbox
Drop raw input here: interview notes, exports, transcripts, screenshots. /signal processes and archives them.
````

### File: initiatives/INDEX.md
````markdown
# initiatives index
One line per entry. Maintained by product-os commands.

| ID | Title | Status | Domain | Updated |
|---|---|---|---|---|
````

### File: problems/INDEX.md
````markdown
# problems index
One line per entry. Maintained by product-os commands.

| ID | Title | Status | Domain | Updated |
|---|---|---|---|---|
````

### File: radar/README.md
````markdown
# Radar
Market and competitive scans, one file per scan.
````

### File: signals/.state/README.md
````markdown
# Collection state
One JSON file per source: last successful run, cursor, IDs already collected. Written by /collect. Do not edit by hand.
````

### File: signals/INDEX.md
````markdown
# signals index
One line per entry. Maintained by product-os commands.

| ID | Title | Status | Domain | Updated |
|---|---|---|---|---|
````

### File: signals/sources.yml
````yaml
# Signal source registry. Used by /collect and managed with /sources.
# Every source starts disabled. Configure, test with "/sources test <id>", then set enabled: true.
#
# Fields
#   id          short unique id, used in signals and state
#   name        human-readable name
#   type        mcp | web | folder | manual
#   tool        mcp: connector to use (e.g. Jira, Slack, HubSpot, Zendesk, Amplitude, Superset, meeting transcripts)
#               web: search | fetch
#   query       what to collect, in plain language plus exact filters (JQL, channel names, URLs, paths)
#   cadence     daily | weekly | monthly
#   kind        interview | support | sales | rfp | analytics | partner | community | review | competitor | internal
#   trust       high | medium | low   (how much a single item counts as evidence)
#   icp_hint    how to decide whether an item comes from an ICP account
#   owner       who maintains the source
#   enabled     true | false

sources:
  - id: icp-interviews
    name: ICP interviews
    type: mcp
    tool: meeting transcripts
    query: Meetings tagged or titled as customer or ICP interview since last run
    cadence: weekly
    kind: interview
    trust: high
    icp_hint: Account named in meeting title or notes, match against strategy/icp.md
    owner: <name>
    enabled: false

  - id: support-tickets
    name: Support tickets
    type: mcp
    tool: <support tool>
    query: Tickets tagged as feature request, usability or bug with customer impact, created since last run
    cadence: weekly
    kind: support
    trust: medium
    icp_hint: Customer plan, segment or account field
    owner: <name>
    enabled: false

  - id: sales-feedback
    name: Sales feedback and lost deals
    type: mcp
    tool: HubSpot
    query: Closed-lost deals with loss reason, and deal notes mentioning missing features, since last run
    cadence: weekly
    kind: sales
    trust: medium
    icp_hint: Deal segment, company size and industry fields
    owner: <name>
    enabled: false

  - id: sales-slack
    name: Sales and CS Slack channel
    type: mcp
    tool: Slack
    query: Messages in <#channel> that describe customer problems or requests, since last run
    cadence: daily
    kind: sales
    trust: low
    icp_hint: Account name mentioned in the message
    owner: <name>
    enabled: false

  - id: rfps
    name: RFP requirements
    type: folder
    tool: ""
    query: inbox/rfp/ (new files since last run). Extract requirements we could not fully meet.
    cadence: weekly
    kind: rfp
    trust: high
    icp_hint: RFPs are ICP unless marked otherwise
    owner: <name>
    enabled: false

  - id: feedback-portal
    name: Idea and feedback portal
    type: mcp
    tool: Jira
    query: "JQL: project = <KEY> AND created >= <last_run>"
    cadence: weekly
    kind: internal
    trust: medium
    icp_hint: Reporter organization field
    owner: <name>
    enabled: false

  - id: product-analytics
    name: Product analytics anomalies
    type: mcp
    tool: Amplitude
    query: Significant drops or spikes in core journey metrics (first sale, admin setup, extension install) since last run
    cadence: weekly
    kind: analytics
    trust: high
    icp_hint: Segment by plan or merchant size if available
    owner: <name>
    enabled: false

  - id: community
    name: Developer and merchant community
    type: web
    tool: search
    query: New threads with problems or requests in <community forum URL> and GitHub issues of <repo>, since last run
    cadence: weekly
    kind: community
    trust: low
    icp_hint: Usually unknown; mark ICP only with clear evidence
    owner: <name>
    enabled: false

  - id: reviews
    name: Public reviews
    type: web
    tool: search
    query: New reviews of our product and extensions on <review sites>, since last run
    cadence: monthly
    kind: review
    trust: low
    icp_hint: Company size or industry in reviewer profile
    owner: <name>
    enabled: false

  - id: competitors
    name: Competitor releases
    type: web
    tool: fetch
    query: Changelogs and release notes at <competitor URLs>, entries since last run
    cadence: weekly
    kind: competitor
    trust: medium
    icp_hint: Not applicable
    owner: <name>
    enabled: false

  - id: partner-feedback
    name: Agency and partner feedback
    type: manual
    tool: ""
    query: Ask the user for notes from partner calls since last run
    cadence: monthly
    kind: partner
    trust: medium
    icp_hint: Partner names the end customer
    owner: <name>
    enabled: false
````

### File: sources/README.md
````markdown
# Sources
Drop existing documents here before running /bootstrap: strategy decks, role descriptions, operating principles, proposal templates, roadmaps, OKRs, ICP and market docs, research, feedback exports.
Raw files in this folder are gitignored. Only the extracted foundation is committed.
````

### File: strategy/icp.md
````markdown
---
status: empty
origin:
sources: []
confirmed:
---
# Ideal customer profile
## Who is ICP
## Signals that identify an ICP account
## Who is explicitly not ICP
````

### File: strategy/principles.md
````markdown
---
status: empty
origin:
sources: []
confirmed:
---
# Principles and role boundaries
## Product operating principles
Tie-breakers derived from the strategy, phrased as "we prefer X over Y".
## UX operating principles
## Who owns what
| Topic | Owner |
|---|---|
| WHY and WHAT, priority | PM |
| Experience quality, product analytics | Head of UX |
| HOW, backlog refinement | Engineering |
| Delivery and release | TDM / TPM |
````

### File: strategy/strategy.md
````markdown
---
status: empty
origin:
sources: []
confirmed:
---
# Strategy
Path from today to the vision in strategy/vision.md.
## Diagnosis
The critical challenge we must overcome, and the shifts that shape the next years.
## Where we play
Today and in the vision year. Details in strategy/icp.md.
## How we win
Why customers choose us in that space, what makes it hard to copy, and which capabilities the vision still requires.
## Horizons
| Horizon | Period | Mode | End state | Capacity share |
|---|---|---|---|---|
| H1 | 0 to 12 months | Commit | | |
| H2 | 12 to 36 months | Build | | |
| H3 | 36 months to vision year | Explore | Vision | |
### H1 bets
| Bet | Why (diagnosis, H2 link) | Owner | Success signal | Kill criterion |
|---|---|---|---|---|
### H2 bets
| Bet | Hypothesis | Depends on H1 proof | Capability built |
|---|---|---|---|
### H3 options
| Option | Signpost to invest | How we keep it open |
|---|---|---|
## What we explicitly do not do
| Non-goal | Holds until |
|---|---|
## Known tensions
| Tension | Owner | Revisit |
|---|---|---|
````

### File: strategy/vision.md
````markdown
---
status: empty
origin:
vision_year:
sources: []
confirmed:
---
# Product vision
## Vision statement
One sentence: what is true in the vision year.
## Target state
What is true for customers, for the business and for the product.
## Target-state indicators
| Indicator | Today (source) | Vision year target |
|---|---|---|
## Why this vision
Link to diagnosis and the market and technology shifts it rests on.
````

### File: strategy/workbench.md
````markdown
# Strategy workbench
Working record of /strategy: options considered, choices made, rationale. Resume with /strategy.

| Layer | Status | Choice | Rejected options | Rationale | Date |
|---|---|---|---|---|---|
| 0 Triage | open | | | | |
| 1 Diagnosis | open | | | | |
| 2 Vision | open | | | | |
| 3 Where to play | open | | | | |
| 4 How to win | open | | | | |
| 5 Horizons | open | | | | |
| 6 Non-goals | open | | | | |
| 7 Principles | open | | | | |
| 8 Coherence | open | | | | |
| 9 Write | open | | | | |

## Proposed, not yet confirmed by the user
## Known tensions
## Layer notes
````

### File: tasks/.state/README.md
````markdown
# Task state
routines.json holds the last completion date and rotation position per routine. Written by /today and /task. Do not edit by hand.
````

### File: tasks/log/README.md
````markdown
# Daily lists
One file per day, created by /today. Checkboxes are ticked with /task done or by editing the file.
````

### File: tasks/routines.yml
````yaml
# Recurring tasks. Managed with /task, turned into daily lists by /today.
# Every routine starts disabled. Fill placeholders, then set enabled: true.
#
# Fields
#   id        short unique id
#   title     what you do, as an instruction to yourself
#   cadence   daily | weekdays | weekly:<mon..fri> | biweekly:<mon..fri> | monthly:<day> | before:<meeting>
#   rotate    optional list; one item per occurrence, in order (e.g. PMs, domains)
#   assist    what the system prepares before you start: a product-os command or a plain instruction
#   tool      connector the assist needs, if any (e.g. Figma, Jira, Confluence)
#   minutes   rough time you plan for it
#   enabled   true | false

routines:
  - id: brief
    title: Read the brief and decide the top 3
    cadence: weekdays
    assist: /brief
    tool: ""
    minutes: 10
    enabled: true

  - id: figma-updates
    title: Look into Figma updates
    cadence: weekdays
    assist: /pulse design. Highlight designs that touch approved ideas or affect consistency across journeys.
    tool: Figma
    minutes: 15
    enabled: false

  - id: roadmap-challenge
    title: Challenge one PM roadmap
    cadence: weekly:tue
    rotate: [<PM 1>, <PM 2>, <PM 3>, <PM 4>]
    assist: /challenge on the current roadmap or 6-month priorities of the rotated PM (from the roadmap and pm-docs work sources). Prepare coaching questions, no rewrite.
    tool: Confluence
    minutes: 30
    enabled: false

  - id: open-proposals
    title: Clear proposals waiting for my decision
    cadence: weekly:mon
    assist: List ideas with status proposed and decisions with status proposed, oldest first, with /challenge verdicts if available.
    tool: ""
    minutes: 30
    enabled: false

  - id: feedback-loops
    title: Close overdue feedback loops
    cadence: weekly:thu
    assist: List requests without reply beyond the agreed response time and draft replies with /reply.
    tool: ""
    minutes: 20
    enabled: false

  - id: one-on-one-prep
    title: Prepare 1:1s
    cadence: before:1:1
    assist: /prep for each 1:1 on tomorrow's calendar
    tool: calendar
    minutes: 10
    enabled: false

  - id: state-of-the-unit
    title: Review State of the Unit draft
    cadence: monthly:1
    assist: /update state-of-the-unit
    tool: ""
    minutes: 30
    enabled: false
````

### File: tasks/todo.md
````markdown
# To-dos
One-off tasks. Managed with /task. Done items move to the daily log.

| ID | Task | Due | Assist | Source | Status |
|---|---|---|---|---|---|
````

### File: templates/decision.md
````markdown
---
id: DEC-0000
date:
decider:
status: proposed | decided | superseded
related: []
---
# <Decision>
## Context
## Options considered
## Decision and rationale
## Who needs to know
## Revisit when
````

### File: templates/idea.md
````markdown
---
id: IDEA-0000
owner:
domain:
status: draft | challenged | proposed | approved | rejected | parked
problems: []
bet:
---
# <Idea title>
<Replace this template with the Shopware product proposal template if it differs.>

## Problem (WHY)
## Evidence
Each point with source link. Mark [assumption] where no source exists.
## Hypothesis
We believe that <change> for <users> will result in <outcome>. We know we are right when <metric moves>.
## Success metrics
| Metric | Baseline | Target | Measured how | Owner |
|---|---|---|---|---|
## UX metrics (with Head of UX)
## Strategy link
## Market and competitive context
## Validation plan
How the riskiest assumption is tested with real users before engineering commits.
## Risks and dependencies
## Out of scope
## Decision log
## Handoff
Filled when approved: summary an engineering team or /pm can start from.
````

### File: templates/initiative.md
````markdown
---
id: INI-0000
idea:
owner:
status: building | launched | reviewing | iterate | sunset | done
launched:
review_dates: []
---
# <Initiative>
## Success metrics (copied from idea at approval, never edited after)
| Metric | Baseline | Target | Result 30d | Result 90d |
|---|---|---|---|---|
## Outcome review log
## Decision: iterate, double down, sunset
````

### File: templates/problem.md
````markdown
---
id: PRB-0000
domain:
status: open | shaped | addressed | parked
signals: []
icp_signals: 0
total_signals: 0
---
# <Problem statement: who struggles with what, and why it matters>
## Evidence
## Affected users and journeys
## Business impact
## Open questions
````

### File: templates/signal.md
````markdown
---
id: SIG-0000
date:
source_id:
kind: interview | support | sales | rfp | analytics | partner | community | review | competitor | internal
trust: high | medium | low
external_id:
url:
account:
icp: yes | no | unknown
domain:
problems: []
---
# <One-line signal>
## What was said or observed
## Context
## Link to source
````

### File: templates/update.md
````markdown
---
audience:
period:
---
# <Update title>
## Headline (3 sentences max)
## Outcomes since last update
## Decisions and trade-offs
## Risks and asks
## Next period
````

### File: updates/README.md
````markdown
# Updates
Drafted narratives, one file per update.
````

### File: work/.state/README.md
````markdown
# Work source state
One JSON file per work source: last run and cursor. Written by /pulse. Do not edit by hand.
````

### File: work/digests/README.md
````markdown
# Work digests
One file per /pulse run: what changed, linked to ideas, initiatives and bets, plus drift and gaps.
````

### File: work/sources.yml
````yaml
# Work source registry: where the product org works. Pulled by /pulse, managed with /sources.
# Tracks artifacts and their changes, never individual activity. See rules in CLAUDE.md.
# Every source starts disabled. Configure, test with "/sources test <id>", then enable.
#
# Fields
#   id        short unique id
#   name      human-readable name
#   tool      connector: Miro, Confluence, Jira, GitHub, Figma, Google Drive, <roadmap tool>
#   scope     exactly what to watch: boards, spaces, projects, repos, folders, files
#   watch     which changes matter (new artifacts, status changes, content changes, releases, decisions)
#   cadence   daily | weekly | monthly
#   link_to   how to map changes to workspace items: by idea id, epic key, domain, label
#   enabled   true | false

sources:
  - id: roadmap
    name: Product roadmap
    tool: <roadmap tool, e.g. Jira Product Discovery or Confluence>
    scope: <roadmap board, view or page>
    watch: Items added, removed, re-prioritized or moved between horizons; changed target dates
    cadence: daily
    link_to: Idea or epic key in the item, otherwise domain
    enabled: false

  - id: pm-docs
    name: PM idea and epic documents
    tool: Confluence
    scope: <space key and parent pages for ideas and epics>
    watch: New idea or epic docs, status changes, changes to problem, metrics or scope sections
    cadence: daily
    link_to: Idea id or epic key in the title
    enabled: false

  - id: discovery-boards
    name: Discovery boards
    tool: Miro
    scope: <boards or space used for discovery, journey maps, workshops>
    watch: New boards, new clusters or decisions on existing boards, research synthesis
    cadence: weekly
    link_to: Board title or tag with domain or idea id
    enabled: false

  - id: design
    name: Design files
    tool: Figma
    scope: <team, project or files>
    watch: New or substantially changed designs, files marked ready for review or dev handoff
    cadence: daily
    link_to: File or page name with idea id or epic key
    enabled: false

  - id: epics
    name: Engineering epics
    tool: Jira
    scope: "JQL: project in (<KEYS>) AND issuetype = Epic"
    watch: New epics, status changes, epics started without a linked approved idea, scope changes
    cadence: daily
    link_to: Epic link to idea, otherwise label
    enabled: false

  - id: releases
    name: Releases and shipped work
    tool: GitHub
    scope: <org/repo list>
    watch: Releases and release notes, merged changes referencing epics. No per-person statistics.
    cadence: weekly
    link_to: Epic key in release notes or PR title
    enabled: false
````
