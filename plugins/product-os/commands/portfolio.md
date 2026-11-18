---
description: Check the portfolio: strategy fit, 12/6-month backlog health, capacity vs bets, drift.
argument-hint: [domain or unit]
---
If strategy/ or templates/ does not exist in this workspace, stop and tell the user to run /workspace-setup in an empty product-os repository first.

Data sources: use connected MCP tools when available (e.g. Jira/Confluence, Amplitude, Superset, Slack, HubSpot, meeting transcripts). Otherwise use files in inbox/ or ask the user to paste input. Never invent data. Mark anything not traceable to a source as [assumption].

Scope: $ARGUMENTS (default: whole portfolio).

Check:
1. Every approved idea and running initiative maps to a bet or option in a horizon of strategy/strategy.md. List orphans.
2. H1 and H2 bets without any idea or initiative. List gaps.
3. Horizons: are H1 bets evidence-backed and current, are H2 bets building on H1 proof, has any H3 signpost been hit?
4. Investment mix: actual capacity across H1, H2 and H3 vs the mix in strategy/strategy.md.
5. Initiatives without pre-defined success metrics.
6. Design and engineering capacity vs strategic bets, if data is available. Flag mismatches.
7. Drift: work started since last review that was never approved. Use work/digests/ since the last portfolio review.

Output a one-page portfolio view and 3 recommended trade-offs. The user decides.
