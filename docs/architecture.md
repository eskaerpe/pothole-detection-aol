# Architecture and integration boundaries

## Proposed baseline; not yet approved runtime
Single-host FastAPI + Jinja2 + minimal JS/CSS; SQLAlchemy/Alembic and SQLite; private local files; separate sequential Python worker; OpenCV/FFmpeg; replaceable detector adapter. Phase 01 verifies machine/resources and approves versions/stack. No cloud services, distributed queues, scheduler or public deployment is required.

## Components and flow
1. Public route validates report metadata, consent and bounded upload, writes a private file and report. It must not call inference.
2. Authenticated admin previews/selects eligible reports. Selection has no compute side effect.
3. Explicit start snapshots report IDs atomically into a batch; backend rejects concurrent starts. Uploads after snapshot do not join it.
4. Separate worker claims one durable item/attempt at a time. Decode/sample frames within limits, call detector, store bounded evidence and attempt outcome. One bad video must not abort others.
5. Admin reviews findings and no-finding outcomes per video, preserving attempt/model provenance. Counters are derived from persisted state.

## Contracts to freeze in phase 02
- Frame input: image dimensions, frame index and monotonic video timestamp with explicit units.
- Detection output: class, bounded box coordinates, confidence, frame reference; no inferred unique identity.
- Attempt metadata: report/batch/model/weights/config identities, sampling policy, start/end, status and failure reason.
- Declare box format, timestamp convention, threshold semantics and error classes; test fixtures cover boundaries and malformed output.
- Real and simulated detectors implement the same adapter. Simulation uses isolated fixtures and conspicuous labels, never production-like fabricated AI evidence.

## Concurrency and recovery
Use a transactional singleton-active-batch invariant and atomic item claims. SQLite is a proposed fit, not a concurrency guarantee; verify locking, bounded busy handling and worker/web coexistence. Only one approved worker is assumed. Do not hold a DB transaction while decoding or inferencing. Persist enough information to mark abandoned work interrupted and retry safely; do not rerun successful items or overwrite prior evidence.

## Integration gate
No real-detector integration before phase 08 passes its pilot. Downstream worker/UI can be developed with labeled test doubles. Every component must have explicit failure handling and regression tests listed in [acceptance](testing-and-acceptance.md).
