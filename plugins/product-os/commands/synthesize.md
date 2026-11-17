---
description: Cluster signals into problems and opportunities, ICP-weighted.
argument-hint: [domain or period]
---
If strategy/ or templates/ does not exist in this workspace, stop and tell the user to run /workspace-setup in an empty product-os repository first.

Scope: $ARGUMENTS (default: all signals of the last 30 days).

Delegate to the signal-analyst subagent in clustering mode.
Create or update problems/ from templates/problem.md, update signal counts and problems/INDEX.md.

Present to the user:
- Top 5 problems by ICP signal count, with trend
- Rising problems without an owner or idea
- Likely noise: high volume, low ICP
- Suggested next step per top problem: /idea, more discovery, or park
