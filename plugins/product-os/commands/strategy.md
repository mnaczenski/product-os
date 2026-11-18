---
description: Build a consistent product vision and strategy from scratch: diagnosis, 3 to 5 year vision, where to play, how to win, horizons H1 to H3, non-goals, principles. Proposes options, you choose.
argument-hint: [optional: layer to start or revisit: triage, diagnosis, vision, play, win, horizons, non-goals, principles, coherence, write]
---
You build a new, coherent product vision and strategy together with the user. Existing documents are evidence, not answers. The agent proposes options grounded in evidence; only the user's choices become strategy.

The shape: a vision describes the target state in 3 to 5 years. The strategy gets there in three horizons, planned backwards from the vision:
- H1 (default 0 to 12 months): commit. Fully specified bets, owners, success signals, kill criteria.
- H2 (default 12 to 36 months): build. Bets as hypotheses, with what H1 must prove first.
- H3 (default 36 months to vision year): explore. Options and signposts that tell us when to invest.

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
1. Diagnosis: where are we today, and what is the critical challenge we must overcome?
   - Propose 2 to 3 candidate diagnoses from market, customer, metrics and as-is evidence. A diagnosis names one crux, not a list of problems.
   - Name what the as-is strategy gets right and where it is incoherent.
   - Name the 2 to 3 market and technology shifts that will shape the next 5 years, with evidence. Offer /radar if evidence is thin.
2. Vision: the target state in 3 to 5 years.
   - First ask for the vision year (default: 4 years out) and whether the company already has a vision the product vision must serve.
   - Propose 2 to 3 candidate visions. Each has: a one-sentence statement, a short narrative of what is true for customers, the business and the product in the vision year, and 3 to 5 measurable target-state indicators (e.g. share of revenue from ICP, adoption of a capability, market position).
   - Each candidate must follow from the diagnosis and the shifts. A vision that would be just as true without them is a slogan.
   - Challenge before choosing: delegate the candidates to the challenger subagent in vision mode. Show its findings next to the options. After the user chooses, run the challenge once more on the chosen and edited vision and resolve findings before moving on.
3. Where to play: target customers (ICP), segments, use cases, markets, channels, and who is explicitly not served.
   - State where we play today and where we play in the vision year. If they differ, name in which horizon the shift happens.
   - ICP must be recognizable from signals the org can actually observe.
4. How to win: why customers choose us over alternatives in the chosen space, and which capability makes that hard to copy.
   - Name the capabilities we have today and those the vision requires. The gap is the backbone of the horizons.
   - Reject advantages any competitor could claim.
5. Horizons: plan backwards from the vision.
   - Confirm the horizon lengths. Defaults: H1 0 to 12 months, H2 12 to 36 months, H3 36 months to vision year.
   - For each horizon, first agree on the end state: what must be true at its end so the next horizon is possible. H3's end state is the vision.
   - H3 (explore): 1 to 3 options, each with the signpost that triggers investment and the cheapest way to keep the option open.
   - H2 (build): 2 to 4 bets as hypotheses, each with the H1 proof it depends on and the capability it builds.
   - H1 (commit): 3 to 5 bets, each with why (link to diagnosis and H2 end state), owner role, success signal with baseline source or [assumption], kill criterion.
   - Investment mix: propose a capacity split across H1, H2 and H3 (e.g. 70/20/10) and compare it with today's actual split from as-is evidence.
   - Map the existing roadmap and backlog from foundation/as-is.md to horizons: keep, change, stop, start. Unmapped work is a choice, not a footnote.
6. Non-goals: what we will not do, though a reasonable team might. At least one item must hurt. Name non-goals that hold until the vision year and those that hold only for H1.
7. Principles: 4 to 7 tie-breakers derived from the choices above, each phrased as "we prefer X over Y". Keep role boundaries from the as-is unless the user changes them.
8. Coherence check
   - Delegate the full workbench to the challenger subagent in strategy mode.
   - Show findings and resolve each one with the user, or record it as a known tension with an owner.
9. Write
   - Write strategy/vision.md, strategy/strategy.md, strategy/icp.md and strategy/principles.md from the workbench. Set `status: draft`, `origin: authored`, list source IDs and the date of each choice in frontmatter.
   - Record major choices (diagnosis, vision, ICP, each H1 bet, investment mix, painful non-goals) in decisions/ via templates/decision.md, status decided, and update decisions/INDEX.md.
   - Close answered questions in foundation/OPEN-QUESTIONS.md with a pointer to the workbench or decision.
   - Show a one-screen summary: vision and indicators, diagnosis, where to play, how to win, H1 to H3 with end states, investment mix, non-goals, open [proposed] items, known tensions. Ask the user to set `status: confirmed`.

## Rules
- Evidence is cited [SRC-xx]. Agent synthesis is marked [inferred]. Unbacked claims are marked [assumption]. User choices are marked [chosen <date>].
- Never present an agent proposal as a decision. Only the user's answer turns an option into strategy.
- Prefer fewer, sharper choices over completeness. A layer can be closed with "not decided yet" and a named open question.
- Do not copy the as-is strategy or vision forward by default. Every carried-over element is a choice like any other.
- Detail decreases with distance: H1 is specific and measurable, H3 is options and signposts. Do not invent precision for H2 and H3.
- Concise, no em dashes, policy tone. Do not commit. The user decides.

Revisit anytime: `/strategy <layer>` reopens one layer, re-runs the consistency check against all later layers and lists what must change. Suggested cadence: vision yearly, horizons every 6 months, or when /radar or /reflect shows a signpost was hit or a bet was killed.
