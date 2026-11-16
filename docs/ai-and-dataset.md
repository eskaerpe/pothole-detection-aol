# AI and dataset contract

## Responsibilities and early handoff
Dataset contributor provides small labeled samples early, then versioned releases. Implementer validates technical compatibility and returns concrete failures; contributor supplements data while the application proceeds independently.

Each handoff includes source URLs, license/usage constraints, version, class mapping, annotation format, image/label pairs, source-video/trip grouping, split manifest, negative examples, separate full test videos and known quality limitations. Preserve raw originals separately; never silently modify a dataset used in a run.

## Detection dataset
One target class: `pothole`. Agree bounding-box detection format (YOLO is proposed) before merging. Classification-only labels are not equivalent; segmentation data needs explicit conversion/validation. Validate image readability, label pairing, class IDs, finite normalized coordinates and box bounds, empty negative labels, duplicates and inconsistent definitions. Favor camera perspectives resembling uploaded videos and include shadows, patches, cracks/manholes and lighting variation.

## Leakage and provenance
Split by source video/trip, not adjacent random frames. Deduplicate across splits and log grouping limitations for public datasets. Keep test data out of training and threshold tuning. Source/license ambiguity blocks use until resolved. A COCO-general model is not assumed to contain a pothole class. Check detector library AND weight/data licenses, including applicable Ultralytics AGPL/commercial obligations, before adoption.

## Training and pilot
Record dataset version/split, environment, seed/config, model/weights identity, parameters and hardware. Validate configuration before any smoke run. Training, archive extraction and every GPU run require explicit permission; no accuracy/latency claims before actual measurements. Use CPU checks where appropriate but do not pretend they are GPU benchmarks.

Pilot gates must be agreed before evaluation: valid pothole detections on independent authorized video; understandable evidence/timestamps; measured runtime/resource use compatible with agreed limits; reviewed false positives/negatives. No invented numeric target. If unsuitable, stop phase 08 and fix data/model before integration.

## Evaluation and honest reporting
Report precision/recall and suitable detection metrics only if actually computed with ground truth and documented methodology; state sample size, split and limitations. Test full videos separately from image evaluation, including negatives and confusing scenes. Tune only on validation data. Confidence threshold and sampling rate are experiments, not universal constants. Bounding-box detections do not establish unique-pothole counts. Preserve real run logs/config outside Git when large/private; commit small non-sensitive summaries and reproducible commands.
