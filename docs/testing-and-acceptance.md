# Testing and acceptance

## Evidence contract
Every phase records exact commands, environment/inputs, exit results, observed behavior, artifact locations and limitations. `Not run` is valid; invented passes are not. Documentation/link validation is not application, security or AI validation. CI success is separate from local success. Keep private media, full logs and binaries out of Git; commit small sanitized summaries.

## Required regression matrix
| Owning phase | Coverage |
| --- | --- |
| 01 | Approved stack/resources, repository policy and unresolved decisions |
| 02 | Environment smoke tests, detector fixtures, transition/box/timestamp validation |
| 03 | Both POVs, responsive views, contrast, keyboard/focus, loading/empty/error states; labeled mocks |
| 04 | Migrations/rollback, auth/CSRF/session expiry, private media, valid/invalid upload, no inference on upload/selection |
| 05 | Authorized video decode, timestamp/frame evidence, corrupt codec/input, timeout and bounded resources |
| 06 | Concurrent/double start rejection, fixed snapshot, sequential claims, partial failure, crash/restart/interruption/retry, no duplicated success |
| 07 | Mixed/no detections, review revisions, attempt history, truthful counters, unauthorized result access |
| 08 | Data/labels/licenses/leakage, reproducible smoke training and independent real-video pilot |
| 09 | End-to-end real detector, model/config provenance, validation-only tuning and held-out evaluation |
| 10 | Full regressions, storage failures, isolated backup/restore, reproducible install/demo and stated limitations |

## Gate and defect policy
A phase closes only after all required acceptance checks pass or a specific owner-approved waiver records impact and downstream restriction. Waivers never turn unrun tests into passes. Push must be verified before the next phase unless explicitly waived. If a regression invalidates a previous phase, record defect ownership and reopen that gate; fixes carry the original phase ID and downstream regressions.

## UI and AI limitations
Use actual rendered checks for UI; Antislop skill availability is not proof of compliance. Separate synthetic adapter tests from real model outputs. No detections is not road safety evidence, image scores do not prove video quality, and repeated boxes are not unique holes.

## Final demonstration
Use an authorized positive and negative video, public receipt, admin selection/start, progress, result evidence and human review. Demonstrate a controlled failure/retry. Record real observed output; do not script fake success. Owner reviews the final limitations and handoff instructions.

## Early pretrained gate
Run P08 after P02 and before default web implementation. Evaluate pinned pretrained weights on independent walking footage first, dashcam separately; agree limits before the run and record real detections, misses, false positives and latency. Download success is not inference success. Training is optional remediation, never a mandatory readiness gate.
