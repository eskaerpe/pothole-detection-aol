# P10 — Hardening, restore and demonstration

## Status and entry gate
- Status: pending
- Dependencies: P09
- Implementation approval: not recorded.
- Legacy task mapping: T14, T15.
- Read [agent contract](../../AGENTS.md), [phase index](../README.md), and [specification](../../docs/security-and-storage.md), [specification](../../docs/testing-and-acceptance.md).

## Goal and scope
Complete the bounded tasks below without unrelated features. Required external inputs/permissions are entry gates; missing evidence is a blocker, not permission to simulate success.

## Tasks
- [ ] P10-T01: Run security/storage/recovery regressions and isolate remaining defects by originating phase.
- [ ] P10-T02: Perform approved isolated consistent backup and actual restore drill with hash verification.
- [ ] P10-T03: Write tested setup/run/test/demo instructions and hand off limitations, model/config identity and pending risks.

## Acceptance gate
- [ ] Full required matrix is run with observed results or explicit impact-bearing waivers.
- [ ] Restore can query records and open referenced media, not merely match checksums.
- [ ] Demo is reproducible from documented commands; final commit/push are verified and remaining risks acknowledged.

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
