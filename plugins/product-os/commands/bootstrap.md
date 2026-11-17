---
description: Builds the evidence base from existing documents: documented as-is strategy, conflicts, open questions, role boundaries, templates, and seeded ideas, initiatives and decisions. Input for /strategy.
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

Phase 3: Draft the evidence base
- foundation/as-is.md: what the sources say today about goals, bets, roadmap, ICP and market, positioning, principles and metrics. Cited, with conflicts side by side. This is the record of the documented strategy, not the new strategy.
- strategy/principles.md: fill only "Who owns what" with the role boundaries found, in the organization's own wording. Leave the strategic principles to /strategy.
- CLAUDE.md: fill "Who I work for" and add organization-specific rules found in the sources.
- templates/idea.md: if a proposal template exists in the sources, replace the generic one with it. If it lacks evidence, hypothesis, success metrics or validation plan, do not change it silently: propose those additions to the user.
- Do not write strategy/strategy.md or strategy/icp.md. /strategy builds them with the user.
- Tag each open question with a type: fact (someone knows the answer), choice (a strategic decision) or unclear.

Phase 4: Seed (optional, ask first)
- Roadmap and backlog items -> ideas/ or initiatives/ with their current status.
- Documented decisions -> decisions/.
- Customer research and feedback exports -> signals/, only where each signal traces to a real source.
- Mark every seeded file with `origin: bootstrap` and its source ID. Update all INDEX files.

Phase 5: Review gate
Present on one screen:
- Coverage of foundation/as-is.md per section: complete, partial, missing
- Where the documented strategy is incoherent: conflicts between sources, bets without goals, roadmap items without a bet
- Open questions by type, with the fact questions listed so the user can answer them in one go
- What was seeded, with counts

Then recommend /strategy to build the new strategy. Choice questions are answered there, layer by layer, not as a list.

Rules:
- Never invent strategy, targets or decisions here. Gaps go to OPEN-QUESTIONS.md. Building strategy is the job of /strategy.
- Never copy confidential raw content into files beyond what the foundation needs. Raw documents stay in sources/, which is gitignored.
- Do not commit. The user decides.

Re-run anytime with new documents: update foundation/as-is.md and the registry, never overwrite confirmed content without asking. If a confirmed strategy exists, list new evidence that challenges it and suggest `/strategy <layer>`.
