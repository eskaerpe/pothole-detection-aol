# Pothole Inspection AI

University MVP: public video reporting, admin-selected manual AI batches, evidence and human review.

## Current state
Documentation bootstrap only. No app, trained model, runnable commands or benchmark is claimed. `pothole_video.zip` is an existing user artifact; its contents, license and suitability have not been inspected.

## Read these files
- AGENTS.md: behavior and safety contract for coding agents.
- docs/PRD.md: complete product/technical concept copied from the final course brief.
- PLAN.md: phased execution and explicit gates.
- TASKS.md: acceptance-based work queue.
- DATASET_CONTRACT.md: Nevan/Rei handoff agreement.

The PRD's statement that stack selection is provisional remains true. PLAN.md controls execution order while dataset collection is in progress: application foundations may proceed, but final AI integration cannot pass without a real model pilot.

## Recommended agent arrangement
Rei owns scope and approvals. One implementer (OpenCode/OMP, Codex or Hermes) owns each approved task. Hermes can coordinate and independently review. Do not launch multiple writers in the same working tree. No agent-specific plugin/config is required by this repository.

## Starter prompt
> Read AGENTS.md, README.md, PLAN.md, TASKS.md and DATASET_CONTRACT.md, then relevant sections of docs/PRD.md. Inspect current state without modifying user artifacts. Propose T01 only, list commands, dependencies and acceptance checks, and wait for approval. Do not install, extract archives, train or implement other tasks.

## Responsibilities
Nevan: source/license tracking, annotations, provenance, data preparation and independent test video collection.
Rei: system architecture, data validation, training pipeline, evaluation, detector, web and integration.

No setup/run command is documented until it actually exists and has been exercised.
"# pothole-detection-aol" 
