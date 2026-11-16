# P02 — Contracts and foundation

## Status and entry gate
- Status: pending
- Dependencies: P01
- Implementation approval: not recorded.
- Legacy task mapping: T02, T03.
- Read [agent contract](../../AGENTS.md), [phase index](../README.md), and [specification](../../docs/architecture.md), [specification](../../docs/data-and-state-model.md).

## Goal and scope
Complete the bounded tasks below without unrelated features. Required external inputs/permissions are entry gates; missing evidence is a blocker, not permission to simulate success.

## Tasks
- [ ] P02-T01: Define detector fixtures, coordinates/timestamps, error types and three-dimensional state transition guards.
- [ ] P02-T02: Approve schema/provenance/counter invariants and web-worker transaction boundaries.
- [ ] P02-T03: Create approved isolated environment, locked dependencies, minimal app and reproducible test harness.

## Acceptance gate
- [ ] Actual install/start/smoke-test commands pass in the approved environment.
- [ ] Contract tests reject invalid boxes/classes/timestamps and invalid transitions.
- [ ] Configuration/secrets and dependency setup are documented without claiming AI readiness.

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

## Next checkpoint
After this gate, execute P08 pretrained pilot before P03 by default. Keep detector interface replaceable across PT/ONNX and do not choose a runtime based on file availability alone.
