---
description: Manage signal sources: list, add, edit, test, enable or disable.
argument-hint: [list | add | edit <id> | test <id> | enable <id> | disable <id>]
---
Two registries:
- signal: signals/sources.yml (customers and market), collected by /collect with the collector subagent
- work: work/sources.yml (where the org works: Miro, Confluence, Jira, GitHub, Figma, roadmap tool), pulled by /pulse with the work-scout subagent
If either file does not exist, stop and tell the user to run /workspace-setup first.

Action: $ARGUMENTS (default: list both). The user may prefix with signal or work, e.g. "add work" or "test design". Resolve ids across both registries.

- list: table of all sources with type, tool, cadence, kind, trust, enabled, last run and last result from signals/.state/. Flag enabled sources whose tool is not connected.
- add: interview the user for each field, one short question at a time. Suggest kind, trust and icp_hint based on the source type. Append to sources.yml with enabled: false.
- edit <id>: change fields the user names. Keep the rest.
- test <id>: delegate to the collector (signal) or work-scout (work) subagent in test mode. Show the 3 sample items and the filter decisions. Ask whether the query needs adjustment.
- enable / disable <id>: only enable after a successful test in this or an earlier session.

For work sources, keep scope narrow (specific spaces, boards, projects, repos) and check that "watch" describes artifact changes, never individual activity.

For signal sources, advise on trust: a single low-trust item should never drive a decision on its own. High trust is for direct customer evidence (interviews, RFPs, analytics).
