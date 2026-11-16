# Pothole Inspection AI

Small university MVP: public video reports → admin-selected manual AI batch → evidence → human review. No inference on upload or selection.

## Current state
Documentation baseline only; no implementation, trained model, benchmark or security-test result is claimed. The existing `pothole_video.zip` is uninspected and must not be extracted without approval.

## Start here
- [AGENTS.md](AGENTS.md): mandatory execution, skill routing and version-control rules.
- [docs/README.md](docs/README.md): product and technical specifications.
- [plan/README.md](plan/README.md): phase dependencies and authoritative progress index.
- [plan/decisions.md](plan/decisions.md): approved choices and unresolved gates.

## Roles
Project owner approves scope/resources; dataset contributor prepares traceable data; implementer builds/tests the system; reviewer checks evidence independently. One writer per working tree. OMP (Oh My Pi), OpenCode and Hermes are distinct tools; this repository does not require a particular harness.

## First implementation prompt
> Read AGENTS.md and plan/README.md, then phase 01 and linked specifications. Inspect the live repository without changing artifacts. Propose P01 scope, environment checks and acceptance evidence; wait for approval before implementation, installation, archive extraction or training. Do not skip phases or mark documentation as application completion.

## Git checkpoints
Every verified revision gets a focused commit; every completed phase gets a closing checkpoint and verified push. Data, media, weights, databases and secrets stay out of Git. See AGENTS.md for approval boundaries and failure handling. There are no verified application startup/test commands yet; phase 02 must supply them after actual execution.

## Downloaded pretrained candidate
PeterHdd YOLOv8s pothole weights are available locally in `weights/peterhdd/` (PT and ONNX), excluded from Git. See [manifest](models/pothole-baseline.json) for pinned revision/checksums and [AI policy](docs/ai-and-dataset.md) for the evaluation gate. Downloaded does not mean inference-tested. No training required before a pretrained pilot.
