---
description: Post-launch review against the success metrics defined before build.
argument-hint: <initiative id or idea id>
---
If strategy/ or templates/ does not exist in this workspace, stop and tell the user to run /workspace-setup in an empty product-os repository first.

Data sources: use connected MCP tools when available (e.g. Jira/Confluence, Amplitude, Superset, Slack, HubSpot, meeting transcripts). Otherwise use files in inbox/ or ask the user to paste input. Never invent data. Mark anything not traceable to a source as [assumption].

Input: $ARGUMENTS. If an idea was just approved and launched, create initiatives/INI-xxxx from templates/initiative.md and copy the metrics unchanged.

Delegate to the metrics-analyst subagent. Fill results, log the review, recommend iterate, double down or sunset.
Also check qualitative signals since launch (signals/ linked to the same problems) and support trends.
Update initiatives/INDEX.md. If the result changes a bet, propose a decision with /decide.
