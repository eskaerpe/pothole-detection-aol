# Phase execution index

## Baseline and status ownership
Documentation restructuring is not implementation. All ten implementation phases remain pending; no phase is active. This table and each linked phase are the authoritative work queue, replacing the legacy root lists.

| Phase | Work | Dependencies | Gate | Execution evidence |
| --- | --- | --- | --- | --- |
| P01 | [Readiness and decisions](phases/01-readiness.md) | None | pending | not run |
| P02 | [Contracts and foundation](phases/02-contracts-and-foundation.md) | P01 | pending | not run |
| P03 | [Two-POV UI prototype](phases/03-ui-prototype.md) | P02 | pending | not run |
| P04 | [Authentication, private storage and upload](phases/04-auth-storage-and-upload.md) | P03 | pending | not run |
| P05 | [Bounded video processing](phases/05-video-pipeline.md) | P04 | pending | not run |
| P06 | [Durable batch worker and recovery](phases/06-batch-worker-and-recovery.md) | P05 | pending | not run |
| P07 | [Results, human review and counters](phases/07-results-and-review.md) | P06 | pending | not run |
| P08 | [Pretrained baseline and independent-video pilot](phases/08-dataset-and-model-pilot.md) | P02 | pending | not run |
| P09 | [Real detector integration and evaluation](phases/09-ai-integration-and-evaluation.md) | P07, P08 | pending | not run |
| P10 | [Hardening, restore and demonstration](phases/10-hardening-and-demo.md) | P09 | pending | not run |

## Sequencing and external data
Default single-writer order: P01 → P02 → P08 → P03 → P04 → P05 → P06 → P07 → P09 → P10. P08 is intentionally scheduled early after P02 so the key AI assumption is tested before lengthy web work. Phase IDs remain stable for defect/commit traceability. Do not run two implementation phases concurrently in the same worktree. P03–P07 need no training dataset, but default progression waits for the P08 gate; any exception requires an explicit owner decision. P09 requires BOTH P07 and a passed P08 pilot. Contributors collect independent evaluation videos/labels now; training data is optional until a documented failure justifies fine-tuning.

Downloaded artifacts are a preparation result, not a completed P08. All implementation gates remain pending. Next executable scope is P01 readiness, not automatic inference or a full-project run.

## Status vocabulary
`pending` → `in_progress` → `verified_local` → `closed` after verified push. Use `blocked` with exact dependency/error; use `reopened` when a prior gate fails. No test evidence means no verified gate. An explicit waiver records owner, scope, impact and downstream restrictions, not a fabricated pass.

## Phase workflow
Read the phase and linked specs → propose bounded work and obtain approval → implement/tests → independent review → update evidence/specs → focused commits and closing checkpoint → push/verify remote → final report. Follow [AGENTS.md](../AGENTS.md). Every verified revision has a commit; a phase can have several. [Decisions](decisions.md) records approved choices. Stable task IDs are Pxx-Tyy; old T01–T15 mappings remain in the phase files for traceability.

## Failure localization
Assign a bug to the earliest broken contract's phase, not automatically the discovery phase. Record reproduction, originating phase, fix task and downstream regression. Reopen that gate when necessary; preserve successful unrelated work. Commit fixes as `fix(phase-xx): ...` and verify their push. Never use force-push/reset as routine recovery.
