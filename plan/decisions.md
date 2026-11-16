# Decisions and unresolved gates

## Recorded decisions
- D001 — Scope: small local university MVP, public report upload and authenticated admin manual batch/review. No automatic inference on upload/selection, no unique-pothole guarantee.
- D002 — Documentation: separate product/technical docs from ten phase task/evidence files; role-based language, one authoritative phase index; retain root compatibility pointers.
- D003 — Version control: track project docs, focused commits per verified revision, closing checkpoint and verified GitHub push per approved phase. Documentation restructuring commit/push is authorized. No destructive history operations or data publication.
- D004 — Agent skills: Antislop core plus task-specific skills are required; use actual installed files and preserve mode-selection rules. No global plugin changes authorized.

## Unresolved before relevant implementation
- P01: approve final stack/versions, resources, runtime, rubric/deadline and main versus feature-branch/PR policy. Current observed documentation branch is main, origin is https://github.com/eskaerpe/pothole-detection-aol.git; recheck live state before writes.
- P01/P04/P05: approve upload size/duration/codec, decode/storage/time limits, abuse protection and retention policy. PRD suggestions are not tested defaults.
- P02: approve exact schema/status enums/transition guards, timestamp/box units, counter definitions and lock/recovery policy.
- P03: approve rendered visual direction; no pixel-exact claim before reference comparison.
- P08: dataset/model/weight licenses, grouped split reliability, hardware and every GPU run; agree pilot criteria before execution.
- P10: approve backup destination/restore scope and demo handoff; public deployment is not authorized.

## Change record format
For each later decision record ID, owning phase, owner approval evidence/date, alternatives, chosen option, rationale, affected specs/tests and superseded decision if applicable. Do not invent dates, approvals or benchmarks. Resolve conflicts before changing the implementation contract.

## Pretrained-first baseline
Owner approved downloading and adapting an existing pothole model. Selected PeterHdd as the first evaluable candidate because weights, ONNX export, training-source reference and companion code are accessible. No measured superiority is claimed. Files are pinned in models/pothole-baseline.json. Training is optional, subject to pilot failures and approval. License compatibility and independent footage performance remain unresolved gates.
