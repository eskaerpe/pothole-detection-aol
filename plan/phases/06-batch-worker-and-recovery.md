# P06 — Durable batch worker and recovery

## Status and entry gate
- Status: pending
- Dependencies: P05
- Implementation approval: not recorded.
- Legacy task mapping: T08.
- Read [agent contract](../../AGENTS.md), [phase index](../README.md), and [specification](../../docs/architecture.md), [specification](../../docs/data-and-state-model.md).

## Goal and scope
Complete the bounded tasks below without unrelated features. Required external inputs/permissions are entry gates; missing evidence is a blocker, not permission to simulate success.

## Tasks
- [ ] P06-T01: Implement atomic fixed-membership batch start, singleton-active-batch guard and sequential durable claims.
- [ ] P06-T02: Use labeled simulation adapter for deterministic success/failure contract tests.
- [ ] P06-T03: Implement interrupted detection/recovery, per-video retries and retained successful attempt history.

## Acceptance gate
- [ ] Double/concurrent starts are rejected; new uploads do not join the running snapshot.
- [ ] One video failure does not stop others; restart and retry do not duplicate success or counters.
- [ ] Web/worker concurrency and stale ownership/output handling have exercised tests.

## Validation and evidence
- Commands and environment: not run. Record exact reproducible commands after execution.
- Inputs/artifacts: none inspected for this phase. Record authorized fixture/data identity and sanitized evidence locations.
- Observed results/exit codes: not run.
- Remaining limitations/waivers: none approved.
- Review: not performed.

## Defects and improvement loop
No phase implementation defects have been assessed yet. For each defect record ID, originating phase, reproduction, expected/actual result, severity, fix task and regression command/result. Reopen this phase if its gate is invalidated; rerun affected downstream tests.

## Git checkpoint and handoff
- Branch/base: verify when phase starts.
- Verified task commits: none.
- Closing checkpoint: not created. Use the phase ID in messages.
- Push: not attempted; record actual outcome after gate validation.
- Remote SHA verification: not run. Give final local/remote SHA in the post-commit report; do not embed this commit's own SHA in itself.
- Handoff: update phase index and affected specifications, list unresolved restrictions; start next phase only after gate and verified push or explicit owner waiver.
