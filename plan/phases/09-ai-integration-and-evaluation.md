# P09 — Real detector integration and evaluation

## Status and entry gate
- Status: pending
- Dependencies: P07, P08
- Implementation approval: not recorded.
- Legacy task mapping: T12, T13.
- Read [agent contract](../../AGENTS.md), [phase index](../README.md), and [specification](../../docs/ai-and-dataset.md), [specification](../../docs/testing-and-acceptance.md).

## Goal and scope
Complete the bounded tasks below without unrelated features. Required external inputs/permissions are entry gates; missing evidence is a blocker, not permission to simulate success.

## Tasks
- [ ] P09-T01: Replace test double with validated detector through the stable adapter and persist model/config provenance.
- [ ] P09-T02: Run full upload-to-review flow on authorized real positive/negative videos.
- [ ] P09-T03: Tune on validation only; run documented held-out evaluation with honest limitations.

## Acceptance gate
- [ ] Real evidence boxes/timestamps correspond to the input and selected model/config.
- [ ] Batch recovery and review regressions pass with real adapter; simulation remains separate.
- [ ] Observed metrics/methodology and video failure cases are reported without unique-count or safety claims.

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
