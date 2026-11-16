# AI and dataset contract

## Responsibilities and early handoff
Dataset contributor first provides independent forward-facing videos and a small labeled evaluation-frame set with versioned provenance. Implementer evaluates the downloaded pretrained candidate and reports concrete failures. Collect optional fine-tuning data only when the pilot identifies a need; do not wait for a large training dataset to begin evaluation.

Each handoff includes source URLs, license/usage constraints, version, class mapping, annotation format, image/label pairs, source-video/trip grouping, split manifest, negative examples, separate full test videos and known quality limitations. Preserve raw originals separately; never silently modify a dataset used in a run.

## Detection dataset
One target class: `pothole`. Agree bounding-box detection format (YOLO is proposed) before merging. Classification-only labels are not equivalent; segmentation data needs explicit conversion/validation. Validate image readability, label pairing, class IDs, finite normalized coordinates and box bounds, empty negative labels, duplicates and inconsistent definitions. Favor camera perspectives resembling uploaded videos and include shadows, patches, cracks/manholes and lighting variation.

## Leakage and provenance
Split by source video/trip, not adjacent random frames. Deduplicate across splits and log grouping limitations for public datasets. Keep test data out of training and threshold tuning. Source/license ambiguity blocks use until resolved. A COCO-general model is not assumed to contain a pothole class. Check detector library AND weight/data licenses, including applicable Ultralytics AGPL/commercial obligations, before adoption.

## Pretrained-first pilot and optional fine-tuning
Record dataset version/split, environment, seed/config, model/weights identity, parameters and hardware. Validate configuration before any smoke run. Training, archive extraction and every GPU run require explicit permission; no accuracy/latency claims before actual measurements. Use CPU checks where appropriate but do not pretend they are GPU benchmarks.

Pilot gates must be agreed before evaluation: valid pothole detections on independent authorized video; understandable evidence/timestamps; measured runtime/resource use compatible with agreed limits; reviewed false positives/negatives. No invented numeric target. If unsuitable, stop phase 08 and fix data/model before integration.

## Evaluation and honest reporting
Report precision/recall and suitable detection metrics only if actually computed with ground truth and documented methodology; state sample size, split and limitations. Test full videos separately from image evaluation, including negatives and confusing scenes. Tune only on validation data. Confidence threshold and sampling rate are experiments, not universal constants. Bounding-box detections do not establish unique-pothole counts. Preserve real run logs/config outside Git when large/private; commit small non-sensitive summaries and reproducible commands.

## Selected baseline (downloaded, not inference-validated)
Use `peterhdd/pothole-detection-yolov8` as the first candidate, not a proven best-performing model. Repository revision, filenames and SHA-256 checksums are pinned in [the manifest](../models/pothole-baseline.json). Local artifacts are `weights/peterhdd/best.pt` and `weights/peterhdd/best.onnx`; the upstream model card is preserved locally beside them. Binary files must stay out of Git.

Evaluate existing pothole weights before considering training. Fine-tuning is conditional on concrete failures and separate approval, not an acceptance prerequisite. Use independent forward-facing walking footage as the primary scenario and dashcam footage as a separate scenario. Training frames and evaluation videos must remain independent. Library, weights and training-data licensing remain a review gate; an Apache-2.0 model-card declaration alone does not clear all dependencies.

No dependencies installed or inference/GPU run is implied by this download. Do not load an untrusted PyTorch checkpoint outside an isolated, approved environment. Prefer inspecting ONNX metadata and validating source/checksum before runtime adoption. Model outputs need the existing detector contract and human review; no automatic unique-pothole count.

## Target capture and evaluation protocol
Primary target: phone footage facing forward while walking, with road surface and approaching potholes visible. Dashcam footage is a distinct secondary scenario; do not pool results to imply equal performance. This is recorded-video upload and manual batch processing, not live inference.

Before the pilot, agree evaluation labels, inclusion rules and tolerable missed detections/false positives with the owner. Use an evaluation frame set for boxes and separate video checks for motion, blur, sampling and timestamps. Log predictions against labels, confidence settings, precision/recall and appropriate detection metrics when supported; report scenario-specific failures and actual CPU/GPU timing without fabricated targets. Tune thresholds only on a development subset, freeze settings, then evaluate held-out footage. Record possible overlap with the upstream training data; unknown overlap must be disclosed.

Pilot outcomes: accept baseline within agreed limits; evaluate an alternative pretrained candidate; or request bounded fine-tuning. Failure does not automatically authorize training or a GPU run. Downloaded PT/ONNX files have not yet passed load, parity or performance tests; neither runtime format is final.
