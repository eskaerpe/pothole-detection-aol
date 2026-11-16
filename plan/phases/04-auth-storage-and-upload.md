# P04 — Authentication, private storage and upload

## Status and entry gate
- Status: pending
- Dependencies: P03
- Implementation approval: not recorded.
- Legacy task mapping: T05, T06.
- Read [agent contract](../../AGENTS.md), [phase index](../README.md), and [specification](../../docs/security-and-storage.md), [specification](../../docs/data-and-state-model.md).

## Goal and scope
Complete the bounded tasks below without unrelated features. Required external inputs/permissions are entry gates; missing evidence is a blocker, not permission to simulate success.

## Tasks
- [ ] P04-T01: Implement migrations, admin credentials/sessions/CSRF and authorized private media access.
- [ ] P04-T02: Implement bounded validated upload, consent/report metadata and authenticated inbox.
- [ ] P04-T03: Make file finalization/DB consistency and temporary cleanup explicit.

## Acceptance gate
- [ ] Migration/rollback and unauthorized/session/CSRF/path-access tests pass.
- [ ] Valid, invalid, oversized and partial uploads have observed tests.
- [ ] Instrumentation/tests prove zero inference during upload and selection.

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
