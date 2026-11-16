# P05 — Bounded video processing

## Status and entry gate
- Status: pending
- Dependencies: P04
- Implementation approval: not recorded.
- Legacy task mapping: T07.
- Read [agent contract](../../AGENTS.md), [phase index](../README.md), and [specification](../../docs/architecture.md), [specification](../../docs/security-and-storage.md).

## Goal and scope
Complete the bounded tasks below without unrelated features. Required external inputs/permissions are entry gates; missing evidence is a blocker, not permission to simulate success.

## Tasks
- [ ] P05-T01: Implement metadata/probe, bounded decode/sampling and timestamp/frame association.
- [ ] P05-T02: Produce private frame evidence with coordinate/dimension checks independent of a real detector.
- [ ] P05-T03: Handle corrupt/unsupported videos, timeout and capacity failures with approved fixtures.

## Acceptance gate
- [ ] Actual authorized video decodes with verified timestamps and evidence frames.
- [ ] Corrupt input, unsupported format and decode timeout fail safely without unbounded work.
- [ ] Measured resources are compared with approved limits; no fabricated performance numbers.

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
