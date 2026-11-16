# P07 — Results, human review and counters

## Status and entry gate
- Status: pending
- Dependencies: P06
- Implementation approval: not recorded.
- Legacy task mapping: T09.
- Read [agent contract](../../AGENTS.md), [phase index](../README.md), and [specification](../../docs/data-and-state-model.md), [specification](../../docs/testing-and-acceptance.md).

## Goal and scope
Complete the bounded tasks below without unrelated features. Required external inputs/permissions are entry gates; missing evidence is a blocker, not permission to simulate success.

## Tasks
- [ ] P07-T01: Integrate private result/evidence views and per-video review tied to explicit attempt.
- [ ] P07-T02: Support mixed false/true findings, zero boxes and needs-inspection outcomes.
- [ ] P07-T03: Derive well-defined report/video/detection counters without unique-pothole claims.

## Acceptance gate
- [ ] History and review changes preserve provenance and remain authorization-protected.
- [ ] Empty findings differ from failed processing and from confirmed safe roads.
- [ ] Counters remain correct across retry, partial failure and review edits.

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
