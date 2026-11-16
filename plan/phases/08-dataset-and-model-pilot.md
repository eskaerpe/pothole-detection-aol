# P08 — Pretrained baseline and independent-video pilot

## Status and entry gate
- Status: pending
- Dependencies: P02
- Implementation approval: not recorded.
- Legacy task mapping: T10, T11.
- Read [agent contract](../../AGENTS.md), [phase index](../README.md), and [specification](../../docs/ai-and-dataset.md).

## Goal and scope
Complete the bounded tasks below without unrelated features. Required external inputs/permissions are entry gates; missing evidence is a blocker, not permission to simulate success.

## Tasks
- [ ] P08-T01 — Verify the pinned artifact hashes, declared class mapping and library/weights/data licenses; validate independent evaluation-video provenance and annotation format. Do not execute an untrusted PT checkpoint merely to inspect it.
- [ ] P08-T02 — Obtain bounded runtime/dependency and input permissions, then run the pretrained candidate on approved forward-facing walking footage; evaluate dashcam separately. GPU use always requires explicit permission. Record environment, parameters, frame/timestamp mapping and actual latency.
- [ ] P08-T03 — Evaluate against labeled independent frames and agreed acceptance limits; freeze threshold settings before held-out testing. Record missed potholes, shadows/patch false positives and sampling limitations. Decide accept, compare another pretrained model, or propose optional fine-tuning; report tested results only.

## Acceptance gate
- [ ] Dataset/model/license/split/run configurations are recorded; test data is excluded from tuning.
- [ ] Pretrained real-video pilot has actual evidence and resource measurements; fine-tuning is optional.
- [ ] Owner accepts pilot suitability before phase 09; failure blocks integration, not unrelated app work.

## Validation and evidence
- Commands and environment: not run. Record exact reproducible commands after execution.
- Inputs/artifacts: PeterHdd PT and ONNX downloaded at pinned revision; source and SHA-256 recorded in models/pothole-baseline.json. Runtime loading and independent-video evaluation remain pending.
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

## Position and exit decision
Execute after P02 and before P03 by default; retain P08 IDs for traceability. Download preparation is recorded but none of the above tasks is complete. Full application integration belongs to P09. A failed model gate pauses default progression until the owner accepts a remediation or an explicit exception.
