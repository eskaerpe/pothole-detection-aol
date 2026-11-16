# P01 — Readiness and decisions

## Status and entry gate
- Status: pending
- Dependencies: none
- Implementation approval: not recorded.
- Legacy task mapping: T01.
- Read [agent contract](../../AGENTS.md), [phase index](../README.md), and [specification](../../docs/PRD.md), [specification](../../docs/security-and-storage.md).

## Goal and scope
Complete the bounded tasks below without unrelated features. Required external inputs/permissions are entry gates; missing evidence is a blocker, not permission to simulate success.

## Tasks
- [ ] P01-T01: Approve stack, Python/dependency strategy and actual hardware/storage budget using live checks.
- [ ] P01-T02: Confirm rubric/deadline, upload defaults, runtime target and Git branch/PR policy.
- [ ] P01-T03: Resolve authorization boundaries for installs, test media/archive inspection and future training.

## Acceptance gate
- [ ] Owner approval and proposed versus approved choices are recorded in decisions.md.
- [ ] Live resource checks and Git remote/branch state have sanitized evidence.
- [ ] No archive extraction, installation or GPU usage occurs without explicit approval.

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
