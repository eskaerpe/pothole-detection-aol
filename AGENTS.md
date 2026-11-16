# Agent contract

## Context routing and authority
1. Read [README.md](README.md), [plan/README.md](plan/README.md), and this contract.
2. Read only the active phase and its linked specifications; do not load every document into every turn.
3. Product requirements: [docs/PRD.md](docs/PRD.md). Technical contracts: [docs/README.md](docs/README.md). Approved decisions: [plan/decisions.md](plan/decisions.md).
4. User instructions take precedence. Surface conflicts before changing behavior; never silently expand scope. PRD proposals are not approved runtime decisions. Record approved changes and update all affected specs and tests together.

## Scope and product invariants
- Current approval additionally covers the selected pretrained baseline download, provenance recording and documentation alignment, with ordinary commit/push. It does not approve installation, training, GPU use or full application implementation. Application implementation requires approval of a bounded phase/task. Documentation completion does not complete an implementation phase.
- Public video upload creates a report only. No public account, inference on upload, or inference on selection.
- Authenticated admin explicitly starts a batch from selected reports. One host, one active batch, sequential work in a separate Python worker with a durable queue.
- Results are suspected findings with timestamp/frame/box/confidence, followed by human review. No detections is not proof of a pothole-free road.
- Bounding-box totals are not unique potholes. No unique counting, automatic severity, precise inferred GPS, automatic repair decisions or scheduling in MVP.
- Proposed stack: FastAPI/Jinja2/minimal JavaScript, SQLAlchemy/Alembic/SQLite, private filesystem, OpenCV/FFmpeg and replaceable detector adapter. Confirm it in phase 01 before installing or implementing.

## Execution and traceability
- One implementer/writer and one active phase at a time. Reviewers may inspect independently, not edit the same files concurrently.
- Present task scope, affected files, tests and risks; obtain approval before non-trivial work. Complete routine steps within approved scope without repeated confirmations.
- Follow dependency gates in plan/README.md. Use the phase's stable task IDs. Keep unchecked work pending; simulation is not real AI evidence.
- Implement tests for contracts and failure paths, run them, inspect results, then record actual evidence. Never fabricate metrics, API responses, test passes or model output.
- Every defect records originating phase, reproduction, expected/actual outcome, affected contract, fix and regression evidence. Reopen the originating phase when its gate no longer holds; rerun dependent regression checks. Do not reset unaffected successful work.
- Update the phase file, phase index and affected docs together. No competing task/status source: root PLAN.md and TASKS.md are pointers only.

## Version control — mandatory
- Before edits inspect branch, status, diff and upstream. Preserve unrelated user changes. Never stage everything blindly.
- Track AGENTS.md, docs/, plan/ and the root documentation. Keep secrets, uploads, datasets, weights, evidence media, local DBs and environments excluded. Review staged diff for credentials, private content and large binaries before committing.
- Each verified revision/task receives a focused commit. A phase may have several commits; after its gate passes, create a final phase checkpoint containing code/tests/docs/evidence summaries, then push to the approved GitHub remote. Do not squash away useful phase checkpoints without approval.
- Messages: `docs(planning): ...`, `feat(phase-04): ...`, `test(phase-06): ...`, `fix(phase-06): ...`, `chore(phase-06): close acceptance gate`. Always identify the originating phase for fixes.
- Work on the approved branch; do not silently create/switch branches. Current documentation baseline uses main; phase 01 must confirm future main-versus-feature-branch/PR policy. Respect branch protection; do not bypass it.
- Phase approval includes ordinary commits and phase-end push to the existing approved origin, unless the owner restricts it. New remotes, other destinations, releases, deployment, force-push, history rewrite, branch deletion, destructive reset/clean and source deletion require separate approval.
- Fetch/check remote state before pushing. If it diverged, stop and report; never overwrite remote work. Stage explicit paths and review `git diff --cached --check` and `git diff --cached`.
- Run required phase tests before commit. Push the explicit approved branch. Verify `git ls-remote origin refs/heads/<branch>` equals local HEAD after push; a successful command alone is not proof of synchronization.
- Record validation commands/results and commit/push state separately. If push fails: `verified locally; push blocked`, with actual error. No next phase until resolved or explicitly waived by owner.
- Do not embed a commit's own hash in that commit. The closing report gives the exact final SHA; a later phase may record prior checkpoint SHAs. Avoid endless status-only commits.
- Windows Git authentication is preferred if WSL authentication fails, but executing Windows binaries still requires permission. Do not expose credentials, copy tokens into docs, install a router or silently switch authentication providers.

## Safety, data and AI
- Use native WSL tools and an approved isolated environment. No Docker, global/heavy installs, Windows executables or /mnt/c writes without explicit approval. GPU usage needs explicit permission for each run.
- Existing pothole_video.zip is user-owned, uninspected input. Do not extract, delete or rewrite it without approval. Preserve immutable dataset originals and record provenance/licenses/grouped splits.
- Never train or evaluate on synthetic results presented as real. Test set stays out of tuning; image metrics do not prove video counting or accuracy.
- Private media is outside static routes. Enforce auth, CSRF, session expiry, limits, safe paths, bounded decoding, timeout/disk-full/partial-write handling. Validate with tests, not documentation claims.
- Preserve successful attempts; retries create attempt history, not duplicated accepted results. Isolate per-video failures; interrupted work must be recoverable.
- No external sends other than approved Git push, public deployment, purchases or unapproved service calls. Never delete user artifacts on initiative.

## Completion report
State phase/task IDs, changed paths, exact test commands/results, remaining risks, commit SHA, branch and observed remote SHA. Distinguish documentation checks, runtime tests, security checks, real model evaluation and visual review. Never claim production security, measured accuracy or pixel-exact UI without evidence.

<!-- antislop:start -->
## Required skill routing (OMP and Hermes on WSL)
Before applicable work, read the actual skill files, not just this summary. Installation does not prove that a skill has been loaded. Load only the core and task-relevant skills, not every skill on every turn.

Verified OMP skill root at bootstrap:
`/home/eska/.omp/plugins/cache/plugins/anti-slop___antislop___3.2.20/skills/`

Hermes fallback root:
`/home/eska/.hermes/skills/`

Resolve each path as `<root>/<skill-name>/SKILL.md`:
- UI, copy, accessibility, responsive layout or code-comment work: read `antislop` core first.
- Code comments: `antislop-code`. Its scope is comment hygiene, not a substitute for code review, correctness or tests.
- UI and visual composition: `antislop-ui`.
- User-facing text, labels, validation and documentation copy: `antislop-copywriting`.
- Accessibility, contrast, keyboard, focus and interaction states: `antislop-human`. Its `contrast-check.py` helper exists alongside the OMP skill; use it where applicable.
- Responsive/mobile layouts: `antislop-layoutmobile`.
- A full web UI task normally requires core, UI, copywriting, human and layoutmobile; add code-comment guidance when editing comments.

If an OMP upgrade changes the versioned cache path, use OMP skill discovery to resolve the installed equivalent. If unavailable, read the verified Hermes fallback. If neither is available, report the missing skill and resolve it before claiming compliance. Never download instructions or modify global plugins automatically.

Follow the core's mode resolution exactly: explicit session choice first, then the `mode` field in `/home/eska/.config/antislop/settings.json`, otherwise ask the project owner to choose `during` or `after` before applicable UI planning/auditing/building. Announce the resolved mode and its actual source as required by the core. `during` is recommended for implementation, but is not a recorded user choice. Do not silently persist a preference.

Before UI implementation, read visual direction in docs/PRD.md and any user-approved DESIGN.md/references. If direction is insufficient, ask one decisive question; do not invent a final identity. Antislop is a quality filter, not a replacement for design direction.

Apply the core's Delivery Gate to applicable deliverables. Record actual browser interaction, responsive, keyboard, state and contrast evidence. Mark unavailable checks as unverified; do not claim a gate PASS from documentation or source inspection alone. Preserve product requirements and obtain approval for conflicts rather than silently changing scope.

These routing instructions apply to every delegated implementer/reviewer. Pass the relevant skill paths and require each agent to read them; a parent reading a skill does not prove a child loaded it.
<!-- antislop:end -->

## Pretrained baseline policy
Evaluate the pinned PeterHdd candidate before training. Read [AI contract](docs/ai-and-dataset.md) and [artifact manifest](models/pothole-baseline.json). Verify checksums before loading; never treat download success as model suitability. Keep binary weights excluded from Git. No automatic training, checkpoint execution or GPU use. Fine-tune only after documented pilot failures and approval.
