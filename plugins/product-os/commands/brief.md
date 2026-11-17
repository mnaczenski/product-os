---
description: Daily brief: what changed, what needs a decision, top 3 for today.
---
If strategy/ or templates/ does not exist in this workspace, stop and tell the user to run /workspace-setup in an empty product-os repository first.

Data sources: use connected MCP tools when available (e.g. Jira/Confluence, Amplitude, Superset, Slack, HubSpot, meeting transcripts). Otherwise use files in inbox/ or ask the user to paste input. Never invent data. Mark anything not traceable to a source as [assumption].

Produce today's brief for the user. Keep it to one screen.

0. If daily sources are due, run /collect daily and /pulse daily first. Report sources that failed or have not run within their cadence.
   Include from the work digest: top changes that matter, drift, gaps.

1. New since last brief: signals (count, ICP share, notable ones), metric alerts on launched initiatives, new market findings in radar/.
2. Needs a decision: ideas with status proposed, decisions with status proposed, initiatives past a review date.
3. Risks: initiatives off target, ideas approved without success metrics, problems with rising ICP signals and no owner.
4. Feedback loop: signals or requests older than the agreed response time without a reply.
5. Top 3 for today, with the command to run for each.

Save as updates/brief-<date>.md. The top 3 and decision items are picked up by /today as tasks. Do not repeat items the user marked done in the previous brief.
