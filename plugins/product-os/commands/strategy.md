---
description: Build a consistent product strategy from scratch, layer by layer, using the evidence base as foundation. Proposes options, you choose.
argument-hint: [optional: layer to start or revisit: triage, diagnosis, play, win, bets, non-goals, principles, coherence, write]
---
You build a new, coherent product strategy together with the user. Existing documents are evidence, not answers. The agent proposes options grounded in evidence; only the user's choices become strategy.

Start or resume: $ARGUMENTS (default: resume at the first open layer in strategy/workbench.md, or start at Layer 0).

If templates/ does not exist, run the /workspace-setup steps first. If foundation/as-is.md is empty and sources/ has documents, run /bootstrap Phases 1 and 2 first, or ask the user to start from a blank slate. If strategy files were drafted by an earlier /bootstrap (status draft, no `origin: authored`), treat their content as as-is evidence, not as choices.

## How each layer works
1. Ground: show in at most 5 bullets what the evidence says for this layer, cited [SRC-xx], including where sources contradict each other.
2. Options: present 2 to 3 distinct, real options. Each option states what it means in practice, the evidence for it, the trade-off it accepts, and what it would force us to stop doing. Mark one as recommendation with the reason. A "do everything" option is not an option.
3. Ask at most 3 questions per turn, each answerable in one line. Wait for the answer.
4. Record: write the choice, the rejected options and the one-line rationale into strategy/workbench.md, with date. If the user says "you pick", record the recommendation as [proposed] and keep it on the confirmation list.
5. Check consistency with all earlier layers before moving on. If a new choice contradicts an earlier one, stop and ask which one gives way.

Save the workbench after every layer so the session can stop and resume anytime.

## Layers
0. Triage the open questions
   - Read foundation/OPEN-QUESTIONS.md and foundation/as-is.md.
   - Sort every question into: fact (has a true answer someone knows: ask the user in one batch, or look it up), choice (a strategic decision: becomes input to a layer below, tagged with that layer), park (does not change strategy: move to Status parked).
   - Show the counts and the fact batch. Most questions should disappear into a layer; do not ask choice questions here.
1. Diagnosis: what is really going on, and what is the critical challenge we must overcome?
   - Propose 2 to 3 candidate diagnoses from market, customer, metrics and as-is evidence. A diagnosis names one crux, not a list of problems.
   - Name what the as-is strategy gets right and where it is incoherent.
2. Where to play: target customers (ICP), segments, use cases, markets, channels, and who is explicitly not served.
   - ICP must be recognizable from signals the org can actually observe.
3. How to win: why customers choose us over alternatives in the chosen space, and which capability makes that hard to copy.
   - Reject advantages any competitor could claim.
4. Bets: 3 to 5 bets that together address the diagnosis.
   - Each bet: why (link to diagnosis), owner role, success signal with baseline source or [assumption], kill criterion, horizon (6 or 12 months).
   - Map the existing roadmap and backlog from foundation/as-is.md: keep, change, stop, start. Unmapped work is a choice, not a footnote.
5. Non-goals: what we will not do, though a reasonable team might. At least one item must hurt.
6. Principles: 4 to 7 tie-breakers derived from the choices above, each phrased as "we prefer X over Y". Keep role boundaries from the as-is unless the user changes them.
7. Coherence check
   - Delegate the full workbench to the challenger subagent in strategy mode.
   - Show findings and resolve each one with the user, or record it as a known tension with an owner.
8. Write
   - Rewrite strategy/strategy.md, strategy/icp.md and strategy/principles.md from the workbench. Set `status: draft`, `origin: authored`, list source IDs and the date of each choice in frontmatter.
   - Record major choices (diagnosis, ICP, each bet, painful non-goals) in decisions/ via templates/decision.md, status decided, and update decisions/INDEX.md.
   - Close answered questions in foundation/OPEN-QUESTIONS.md with a pointer to the workbench or decision.
   - Show a one-screen summary: diagnosis, where to play, how to win, bets, non-goals, open [proposed] items, known tensions. Ask the user to set `status: confirmed`.

## Rules
- Evidence is cited [SRC-xx]. Agent synthesis is marked [inferred]. Unbacked claims are marked [assumption]. User choices are marked [chosen <date>].
- Never present an agent proposal as a decision. Only the user's answer turns an option into strategy.
- Prefer fewer, sharper choices over completeness. A layer can be closed with "not decided yet" and a named open question.
- Do not copy the as-is strategy forward by default. Every carried-over element is a choice like any other.
- Concise, no em dashes, policy tone. Do not commit. The user decides.

Revisit anytime: `/strategy <layer>` reopens one layer, re-runs the consistency check against all later layers and lists what must change.
