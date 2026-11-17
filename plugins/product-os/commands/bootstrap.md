---
description: Builds the workspace foundation from existing documents: strategy, ICP, principles, templates, and seeded ideas, initiatives and decisions.
argument-hint: [optional: folder, Confluence space, Drive folder, or category to focus on]
---
You build the foundation of this product-os workspace from documents that already exist. Focus: $ARGUMENTS (default: everything in sources/ plus any locations the user names).

If templates/ does not exist, run the /workspace-setup steps first.

Phase 1: Inventory
- List documents in sources/. Ask the user whether to also pull from connected tools (e.g. Confluence, Google Drive) and which spaces or folders.
- Classify each document: strategy, ICP and market, roles and principles, process (operating model, proposal template, feedback process), roadmap and backlog, metrics and OKRs, customer research, competitive, other.
- Register every document in foundation/SOURCES.md with ID SRC-xx, category, date, owner, location.
- Show the inventory and ask the user to confirm: which documents are current, which are outdated, which to ignore. Wait for the answer.

Phase 2: Extract (parallel)
- Delegate each category to the `librarian` subagent with its source IDs. Categories can run in parallel.

Phase 3: Draft the foundation
- strategy/strategy.md: goals, bets, explicit non-goals.
- strategy/icp.md: who is ICP, recognizable signals, who is not.
- strategy/principles.md: operating principles and role boundaries, in the organization's own wording.
- CLAUDE.md: fill "Who I work for" and add organization-specific rules found in the sources.
- templates/idea.md: if a proposal template exists in the sources, replace the generic one with it. If it lacks evidence, hypothesis, success metrics or validation plan, do not change it silently: propose those additions to the user.
- Set each strategy file to `status: draft`, list its source IDs in frontmatter.

Phase 4: Seed (optional, ask first)
- Roadmap and backlog items -> ideas/ or initiatives/ with their current status.
- Documented decisions -> decisions/.
- Customer research and feedback exports -> signals/, only where each signal traces to a real source.
- Mark every seeded file with `origin: bootstrap` and its source ID. Update all INDEX files.

Phase 5: Review gate
Present on one screen:
- Readiness per foundation file: complete, partial, missing
- Conflicts between sources that need a decision
- Top 10 open questions from foundation/OPEN-QUESTIONS.md, most impactful first
- What was seeded, with counts

Ask the user to review and set `status: confirmed` on each strategy file when satisfied. Until then, all commands treat the foundation as provisional.

Rules:
- Never invent strategy, targets or decisions. Gaps go to OPEN-QUESTIONS.md.
- Never copy confidential raw content into files beyond what the foundation needs. Raw documents stay in sources/, which is gitignored.
- Do not commit. The user decides.

Re-run anytime with new documents: update existing files, never overwrite confirmed content without asking.
