---
description: Add, complete, snooze or drop tasks and routines, in plain language.
argument-hint: <natural language, e.g. "challenge Lisa's roadmap by Friday" | "every Monday: review open proposals" | done 2 | snooze 3 to tomorrow | list>
---
If tasks/ does not exist in this workspace, stop and tell the user to run /workspace-setup first.

Input: $ARGUMENTS

Interpret the input:
- One-off ("by Friday", "tomorrow", no recurrence): add to tasks/todo.md with the next free T-xxxx id, due date, source manual. Suggest an assist (a product-os command or a short instruction) and confirm it in one line.
- Recurring ("every", "each", "weekly", "before 1:1s"): add to tasks/routines.yml with cadence, assist, tool, minutes, enabled: true. Show the entry.
- done <n or id>: tick it in today's list. For routines, record completion in tasks/.state/routines.json and advance the rotation. For to-dos, set status done.
- snooze <n or id> to <when>: move the due date. If an item was snoozed 3 times, ask whether to drop or delegate it.
- drop <n or id>: remove with a one-line reason in the daily log.
- list: open to-dos and enabled routines with next due date.

Keep tasks phrased as actions. Tasks about people stay about their work: "challenge <PM>'s roadmap", never "assess <PM>".
