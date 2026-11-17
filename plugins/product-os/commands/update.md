---
description: Draft an update for a given audience and period.
argument-hint: <audience: leadership | state-of-the-unit | all-hands | stakeholders | release> [period]
---
If strategy/ or templates/ does not exist in this workspace, stop and tell the user to run /workspace-setup in an empty product-os repository first.

Input: $ARGUMENTS

Collect from the workspace: outcomes from initiatives/, decisions/, approved ideas, notable signal patterns, risks.
Delegate drafting to the writer subagent using templates/update.md.
Save to updates/<date>-<audience>.md.
List any claim the writer could not source, so the user can fill or cut it.
