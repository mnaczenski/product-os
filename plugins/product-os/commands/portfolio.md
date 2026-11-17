---
description: Check the portfolio: strategy fit, 12/6-month backlog health, capacity vs bets, drift.
argument-hint: [domain or unit]
---
If strategy/ or templates/ does not exist in this workspace, stop and tell the user to run /workspace-setup in an empty product-os repository first.

Data sources: use connected MCP tools when available (e.g. Jira/Confluence, Amplitude, Superset, Slack, HubSpot, meeting transcripts). Otherwise use files in inbox/ or ask the user to paste input. Never invent data. Mark anything not traceable to a source as [assumption].

Scope: $ARGUMENTS (default: whole portfolio).

Check:
1. Every approved idea and running initiative maps to a bet in strategy/strategy.md. List orphans.
2. Bets without any idea or initiative. List gaps.
3. 12-month options and 6-month priorities: are they distinct, current, and evidence-backed?
4. Initiatives without pre-defined success metrics.
5. Design and engineering capacity vs strategic bets, if data is available. Flag mismatches.
6. Drift: work started since last review that was never approved. Use work/digests/ since the last portfolio review.

Output a one-page portfolio view and 3 recommended trade-offs. The user decides.
