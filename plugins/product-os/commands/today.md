---
description: Today's task list: due routines, open to-dos and brief items, prioritized, with prepared material.
argument-hint: [prep | light]
---
If tasks/ does not exist in this workspace, stop and tell the user to run /workspace-setup first.

Mode: $ARGUMENTS (default: prep for the top items; "light" lists only; "prep" prepares every item).

1. If today's file tasks/log/<date>.md exists, show it with current status instead of rebuilding. Offer to rebuild.
2. Collect:
   - Routines from tasks/routines.yml that are enabled and due today (use tasks/.state/routines.json). For rotating routines, pick the next item in the rotation.
   - To-dos from tasks/todo.md that are due today, overdue, or have no due date and are older than 7 days.
   - Today's brief (updates/brief-<date>.md). If it does not exist and the brief routine is due, run /brief first. Add its "needs a decision" and "top 3" items as tasks with source brief.
   - Unfinished items from the previous daily list.
3. Prioritize, in this order: decisions others are waiting for, overdue items, items due today, routines, everything else. Cap the list at 7 items. Put the rest under "Later" and say why.
4. Sum the planned minutes. If above 3 hours, say so and propose what to drop or delegate.
5. Prepare: for the top 3 items (or all in prep mode) run the assist in parallel where possible: the named command, or the instruction with the named connector. If a connector is not available, say so and keep the task.
6. Write tasks/log/<date>.md:

   # Today, <date>
   Planned: <minutes> min
   - [ ] 1. <task> (<minutes> min) [source] -> <link to prepared material or command to run>
   ...
   ## Later
   ## Prepared material
   Short summaries per prepared item, with links to the full output.

7. Show the list. Do not start working on the tasks themselves beyond the preparation.
