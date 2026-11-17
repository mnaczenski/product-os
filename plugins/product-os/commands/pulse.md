---
description: What changed in the org's work: roadmap, docs, boards, designs, epics, releases. Linked to bets and ideas, with drift and gaps.
argument-hint: [daily | weekly | <work source id> | all]
---
If work/sources.yml does not exist, stop and tell the user to run /workspace-setup first.

Scope: $ARGUMENTS (default: every enabled work source that is due).

1. Determine due sources from work/sources.yml and work/.state/. List them before starting.
2. Delegate each source to the work-scout subagent. Sources run in parallel.
3. Synthesize all changes into work/digests/<date>.md:

   ## Changes by bet and initiative
   Group by strategy bet, then idea or initiative. One line per change with link.

   ## Drift
   - Roadmap or epic changes without a matching approved idea or recorded decision
   - Approved ideas whose roadmap position, scope or date changed without a decision
   - Work started on problems with no ICP evidence

   ## Gaps
   - New idea or epic docs without success metrics, evidence or strategy link (candidates for /challenge)
   - Designs ready for handoff on ideas without a validation result
   - Releases on initiatives without an /outcome review date

   ## Unmapped
   Changes that could not be linked. Suggest labels or ids that would fix the mapping.

4. Update work/.state/<id>.json for successful sources only. Delete processed work/.raw/ files.
5. Show the digest headline: top 5 changes that matter, drift count, gap count, and suggested commands.

Rules: artifacts only, never individual activity. Do not draw conclusions about a person from the digest.
