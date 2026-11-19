---
description: Prepare a meeting or 1:1 from workspace artifacts, and record 1:1 agreements afterwards.
argument-hint: <meeting or person> [topic] | <person> after [notes]
---
If strategy/ or templates/ does not exist in this workspace, stop and tell the user to run /workspace-setup in an empty product-os repository first.

Input: $ARGUMENTS

Use recent work/digests/ for what changed in the relevant artifacts.

For a meeting: goal, what to decide, relevant ideas, initiatives, decisions and risks, 3 questions to ask.

For a 1:1 with a person in team/ORG.md:
1. Read their file in team/people/: scope, responsibilities, agreed focus. If they are not in the roster, say so and offer /team.
2. Read the last notes in team/notes/<id>-<slug>/: open agreements and open asks in both directions.
3. Collect their artifacts by scope, not by guessing: ideas, initiatives and bets they decide, status vs success metrics, open decisions, upcoming risks, digest changes in their domains.
4. Flag structure issues worth raising: owned areas with no recent work, work in their name outside their scope, areas where they and someone else both decide.
5. Output on one screen: open agreements first, then what changed in their scope, decisions they need from you, 3 to 5 coaching questions about the work, and what you owe them.

After a 1:1 (`<person> after`, or when the user pastes notes): write team/notes/<id>-<slug>/<date>.md from templates/one-on-one.md. Record topics, agreements with owner and due date, open asks. Mark earlier agreements done or carried over. Offer to add the user's own agreements to tasks/todo.md. If the agreed focus or scope changed, propose the change via /team.

Hard rules:
- Work only from artifacts, outcomes and agreements. No scoring, ranking or performance judgments of the person. Performance conversations are the leader's job, not the agent's.
- Notes record work topics and agreements only. No assessments, health or private matters. team/notes/ is gitignored; never copy note content into committed files.
