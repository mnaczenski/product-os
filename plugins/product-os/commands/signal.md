---
description: Capture customer, sales, support or market input as structured signals.
argument-hint: [text, file path, or empty to process inbox/]
---
If strategy/ or templates/ does not exist in this workspace, stop and tell the user to run /workspace-setup in an empty product-os repository first.

Data sources: use connected MCP tools when available (e.g. Jira/Confluence, Amplitude, Superset, Slack, HubSpot, meeting transcripts). Otherwise use files in inbox/ or ask the user to paste input. Never invent data. Mark anything not traceable to a source as [assumption].

Input: $ARGUMENTS (if empty, process every file in inbox/ except README.md).

This command is for ad-hoc input. Recurring sources belong in signals/sources.yml and are collected with /collect.
Use source_id `manual`. Ask for kind and trust if not obvious.

Delegate to the signal-analyst subagent. Create signals in signals/<year>/ from templates/signal.md with the next free SIG id, update signals/INDEX.md, link or propose problems.
Move processed inbox files to inbox/processed/<date>/.
Report: signals created, ICP share, problems touched, anything surprising.
