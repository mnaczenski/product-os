---
description: Define and maintain the org structure: people, roles, reporting lines, scope and responsibilities. Plain language.
argument-hint: [empty for guided setup | show | check | a change in plain language, e.g. "Anna now owns checkout and reports to Ben"]
---
If templates/ does not exist in this workspace, stop and tell the user to run /workspace-setup first.

Input: $ARGUMENTS

Files: team/ORG.md (people, reporting lines, responsibility matrix), team/people/<id>-<slug>.md from templates/person.md, one per person. If team/ is missing, create it from the workspace-setup templates. Make sure .gitignore contains team/notes/; add it if missing and say so.

## Modes
Guided setup (no input, or team/ORG.md has no people):
1. Offer to import first: org charts and role descriptions in sources/ (delegate to the librarian with category "roles and org"), or a pasted list. Imported entries are cited [SRC-xx] and shown for confirmation before writing.
2. Then ask in short batches, waiting for answers:
   - You: name and role (take them from CLAUDE.md "Who I work for" if filled), who you report to.
   - Your direct reports: name, role, unit, 1:1 cadence.
   - How deep to go: only your direct reports, or also their reports.
   - For each person: scope (domains, products, bets), what they decide, and what is explicitly not theirs. Offer a draft from their role description and strategy/strategy.md, marked [proposed].
3. Write the files, then run check.

Change (plain language input):
- Parse the change: add, remove, rename, change role, change manager, change scope, assign or move a responsibility, set focus or 1:1 cadence.
- Show the exact change across all affected files (both sides of a reporting line, the matrix, the previous owner of an area) and ask for confirmation. Then write.
- Moving a responsibility always names who loses it.
- Removing a person sets status: left, keeps the file, and lists the areas, bets and ideas they owned that now need an owner.

Show:
- Reporting tree from the workspace owner, the responsibility matrix, and areas without a Decides owner.

Check (also after every setup and change):
1. Reporting lines: everyone except the top has exactly one manager, no cycles, reports_to and direct_reports agree.
2. Matrix: every area has exactly one Decides owner. List areas with none or several.
3. Coverage: every bet and option in strategy/strategy.md, every domain in work/sources.yml and every owner named in ideas/ and initiatives/ maps to a person in the roster.
4. Boundaries: person-level decision rights are consistent with the role-level table "Who owns what" in strategy/principles.md. A PM deciding HOW or a delivery role deciding priority is flagged.
5. Gaps: people without scope, scope without responsibilities, overlapping scope between two people.
Regenerate the reporting tree in team/ORG.md and set `updated`. Add unresolved items to "Open structure questions".

## Rules
- Store only what defines the structure: name, role, unit, reporting line, scope, responsibilities, agreed work focus, 1:1 cadence.
- Never store ratings, performance assessments, compensation, health, private matters or activity statistics. If the user offers such content, decline and suggest the HR system.
- Structure is the user's decision. Proposals are marked [proposed] until confirmed.
- Do not commit. The user decides.
