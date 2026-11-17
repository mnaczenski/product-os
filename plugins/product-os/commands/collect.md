---
description: Collect signals from all due sources (or named ones), dedupe, structure, link to problems.
argument-hint: [daily | weekly | monthly | <source id> | all]
---
If signals/sources.yml does not exist, stop and tell the user to run /workspace-setup first.

Scope: $ARGUMENTS (default: every enabled source that is due according to its cadence and last run).

1. Determine due sources from signals/sources.yml and signals/.state/. List them before starting.
2. Delegate each source to the collector subagent. Sources run in parallel. Manual sources: ask the user for input in one combined question at the end.
3. Hand all new raw items to the signal-analyst subagent:
   - Dedupe by source_id plus external_id, and by near-identical content across sources (keep one signal, list all sources).
   - Create signals from templates/signal.md with source_id, kind, trust, external_id, url.
   - Decide ICP using the source's icp_hint and strategy/icp.md.
   - Link to existing problems or propose new ones.
4. Update signals/.state/<id>.json for every source that succeeded (last_run, cursor, collected ids). Never advance the cursor of a failed source.
5. Delete processed files in signals/.raw/.

Report on one screen:
- Per source: items collected, signals created, failures (not connected, auth, empty)
- New signals by kind, ICP share, trust mix
- Problems that gained ICP signals, rising problems, new problems proposed
- Suggested next step: /synthesize if many new signals, /reply for requests that need an answer
