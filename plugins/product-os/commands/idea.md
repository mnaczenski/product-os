---
description: Shape an idea or epic: problem, evidence, hypothesis, metrics, validation plan.
argument-hint: <problem id, topic, or rough idea>
---
If strategy/ or templates/ does not exist in this workspace, stop and tell the user to run /workspace-setup in an empty product-os repository first.

Data sources: use connected MCP tools when available (e.g. Jira/Confluence, Amplitude, Superset, Slack, HubSpot, meeting transcripts). Otherwise use files in inbox/ or ask the user to paste input. Never invent data. Mark anything not traceable to a source as [assumption].

Input: $ARGUMENTS

1. Find related problems, signals, ideas and decisions. Mention overlaps.
2. If no problem with evidence exists, say so and offer /synthesize or a discovery plan instead of a solution.
3. Draft ideas/IDEA-xxxx-<slug>.md from templates/idea.md. Fill evidence only from sources. Mark gaps as [assumption].
4. Propose success metrics with baseline source. Flag where baseline data is missing.
5. Propose a validation plan for the riskiest assumption, with real users.
6. Run the challenger subagent on the draft. Show its verdict and top 3 gaps.
7. Set status draft, update ideas/INDEX.md. Ask the user which gaps to close now.
