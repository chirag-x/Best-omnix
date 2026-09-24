# Omnix Project Memory

## Current Phase: Phase 0
**Status**: COMPLETE (Pending final audit confirmation)

## Current Objective
Finalize architecture corrections and detailed phase specifications. Ensure a deterministic, single-model, non-hardcoded architecture is strictly documented.

## Completed Work
- `TECHNOLOGY.md` created and acts as the authoritative source of truth.
- `generate_phases.py` and `update_docs.py` scripts deleted to prevent documentation overwriting.
- Phase order corrected to the canonical 21-phase roadmap.
- 21 Phase specifications explicitly rewritten to remove TBDs and boilerplate.
- `.env.example` corrected to remove vector DB, fast LLM, and unrestricted shell execution flags.
- Canonical Risk Taxonomy (`LOW_RISK`, `SENSITIVE`, `DESTRUCTIVE`, etc.) defined.
- Safety architecture updated to mandate a deterministic Policy Engine over an AI Safety Agent.
- Verification architecture updated to prioritize deterministic OS checks over an AI Verification Agent.
- WorldState explicitly defined as a versioned `WorldStateStore`, not a mutable singleton.
- Task planning architecture refined to use acyclic `PlanRevisions`.
- Memory explicitly constrained to SQLite/FTS5 (no embeddings).
- Test plan stripped of arbitrary 100% requirements; focused on critical safety and architectural contracts.
- Latency targets in PRD marked as TARGET / PROVISIONAL.
- Package architecture explicitly laid out in `ARCHITECTURE.md`.
- Canonical execution lifecycle documented.
- Forbidden patterns explicitly cataloged.

## Known Issues
- None structurally.

## Validations Required (Future Tasks)
- Validate Chatterbox-Turbo under exact Python 3.13.15 runtime environment.
- Validate Rhubarb integration/runtime behavior.
- Validate Python <-> Godot IPC method.
- Validate exact character asset format and packaging composition.
- Validate exact GPU allocation strategy and latency/performance targets.
