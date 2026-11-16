# P03 — Two-POV UI prototype

## Status and entry gate
- Status: pending
- Dependencies: P02
- Implementation approval: not recorded.
- Legacy task mapping: T04.
- Read [agent contract](../../AGENTS.md), [phase index](../README.md), and [specification](../../docs/PRD.md), [specification](../../docs/testing-and-acceptance.md).

## Goal and scope
Complete the bounded tasks below without unrelated features. Required external inputs/permissions are entry gates; missing evidence is a blocker, not permission to simulate success.

## Tasks
- [ ] P03-T01: Prototype public upload/receipt and admin inbox, selection, progress, detail and review views.
- [ ] P03-T02: Use explicitly labeled fixture data and cover mobile/desktop empty/loading/error/partial states.
- [ ] P03-T03: Apply Antislop routing and obtain owner visual feedback before wiring backend behavior.

## Acceptance gate
- [ ] Rendered screenshots are reviewed, with keyboard/focus/contrast and responsive evidence.
- [ ] No UI pretends mock detections or placeholder buttons are working AI.
- [ ] Upload/selection/manual-start distinctions and counter labels match product rules.

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
