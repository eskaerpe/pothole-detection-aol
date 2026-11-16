# Data, state and counters

## Logical records (schema approval in phase 02)
- Report: opaque ID, road/area description, observed date, consent, private media reference, received time and selection disposition. No public name/contact requirement.
- Batch: ID, immutable selected-report snapshot, timestamps and lifecycle state.
- Batch item / attempt: batch/report relationship, attempt identity, worker ownership, timestamps, processing state, error, model/config/dataset provenance where applicable.
- Detection/evidence: attempt ID, frame/timestamp/dimensions, class/confidence/box and private evidence reference.
- Human review: report and reviewed attempt, disposition, finding confirmations and optional note; preserve reviewer/time/history.

## Three separate state dimensions
1. Selection disposition: pending, selected or rejected; only eligible reports can enter a new batch.
2. Processing lifecycle (per attempt): queued → processing → succeeded or failed; abandoned processing → interrupted. Retrying creates a new attempt rather than rewriting successful history.
3. Human review: not reviewed, confirmed suspected finding(s), no confirmed finding, or needs further inspection. Mixed true/false findings and zero-detection videos must be reviewable.

These are conceptual labels, not frozen DB enums. Phase 02 approves exact labels, allowed transitions, guards and batch aggregation. Do not collapse selection, inference and review into one ambiguous status.

## Invariants
- Backend prevents duplicate batch start and more than one active batch.
- Snapshot membership does not change when new reports arrive.
- Attempt outputs belong to that attempt; stale retries cannot overwrite a later accepted result.
- Report-level current result points to an explicit attempt; previous attempts remain inspectable.
- Partial output is not a successful outcome. Define safe transaction/file-finalization order and compensating cleanup before implementation.
- Keep timestamps in a consistent stored convention and explicit UI timezone; document it in phase 02.

## Counter definitions
Reports, eligible/queued videos, successful videos and failed/interrupted videos count their explicitly defined persisted entities, not detection boxes. A detection total counts boxes for the selected attempt(s), not unique physical potholes. Human-confirmed findings and unreviewed AI boxes are different measures. Zero boxes means no detections at that configuration, not a road safety conclusion. Test retry/partial-failure counters against double counting.
