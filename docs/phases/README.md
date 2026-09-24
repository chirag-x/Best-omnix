# Omnix Phase Documentation

This directory contains the detailed architectural and development specifications for every phase of the Omnix project.

## Phase Index

| Phase | Name | Purpose | Dependencies | Status | Phase File |
|-------|------|---------|--------------|--------|------------|
| 0 | Blueprint | Lock architecture/documentation | None | IN PROGRESS | [PHASE_00_BLUEPRINT.md](PHASE_00_BLUEPRINT.md) |
| 1 | Runtime Foundation | Base OS/app framework | Phase 0 | NOT STARTED | [PHASE_01_RUNTIME_FOUNDATION.md](PHASE_01_RUNTIME_FOUNDATION.md) |
| 2 | Omnix Executive | Core orchestration loop | Phase 1 | NOT STARTED | [PHASE_02_OMNIX_EXECUTIVE.md](PHASE_02_OMNIX_EXECUTIVE.md) |
| 3 | Agent & Capability Framework | Registries and interfaces | Phase 2 | NOT STARTED | [PHASE_03_AGENT_CAPABILITY_FRAMEWORK.md](PHASE_03_AGENT_CAPABILITY_FRAMEWORK.md) |
| 4 | Input/Output & Voice | Multi-modal I/O gateways | Phase 2 | NOT STARTED | [PHASE_04_INPUT_OUTPUT_VOICE.md](PHASE_04_INPUT_OUTPUT_VOICE.md) |
| 5 | World State & Context | State tracking and memory | Phase 2 | NOT STARTED | [PHASE_05_WORLD_STATE_CONTEXT.md](PHASE_05_WORLD_STATE_CONTEXT.md) |
| 6 | Brain, Goals & Planning | Dynamic LLM task graph generation | Phase 3, 5 | NOT STARTED | [PHASE_06_BRAIN_GOALS_PLANNING.md](PHASE_06_BRAIN_GOALS_PLANNING.md) |
| 7 | Application & Window System | Base OS capabilities (launch, focus) | Phase 3 | NOT STARTED | [PHASE_07_APPLICATION_WINDOW_SYSTEM.md](PHASE_07_APPLICATION_WINDOW_SYSTEM.md) |
| 8 | Perception & Vision Grounding | Scene modeling (UIA, OCR, Vision) | Phase 7 | NOT STARTED | [PHASE_08_PERCEPTION_VISION_GROUNDING.md](PHASE_08_PERCEPTION_VISION_GROUNDING.md) |
| 9 | Generic Desktop Interaction | Safe mouse/keyboard execution | Phase 8 | NOT STARTED | [PHASE_09_GENERIC_DESKTOP_INTERACTION.md](PHASE_09_GENERIC_DESKTOP_INTERACTION.md) |
| 10 | Browser Intelligence | Generic web navigation & DOM | Phase 9 | NOT STARTED | [PHASE_10_BROWSER_INTELLIGENCE.md](PHASE_10_BROWSER_INTELLIGENCE.md) |
| 11 | Filesystem Intelligence | File manipulation & search | Phase 3 | NOT STARTED | [PHASE_11_FILESYSTEM_INTELLIGENCE.md](PHASE_11_FILESYSTEM_INTELLIGENCE.md) |
| 12 | Verification Engine | Pre/post condition checking | Phase 6, 8 | NOT STARTED | [PHASE_12_VERIFICATION_ENGINE.md](PHASE_12_VERIFICATION_ENGINE.md) |
| 13 | Recovery & Replanning | Failure handling & loop prevention | Phase 12 | NOT STARTED | [PHASE_13_RECOVERY_REPLANNING.md](PHASE_13_RECOVERY_REPLANNING.md) |
| 14 | Memory | Episodic and Semantic storage | Phase 5 | NOT STARTED | [PHASE_14_MEMORY.md](PHASE_14_MEMORY.md) |
| 15 | Communication & Personality | Natural language generation | Phase 6 | NOT STARTED | [PHASE_15_COMMUNICATION_PERSONALITY.md](PHASE_15_COMMUNICATION_PERSONALITY.md) |
| 16 | Safety & Permissions | Risk assessment & user confirmation | Phase 3 | NOT STARTED | [PHASE_16_SAFETY_PERMISSIONS.md](PHASE_16_SAFETY_PERMISSIONS.md) |
| 17 | Multi-Agent Collaboration | Complex inter-agent delegation | Phase 6 | NOT STARTED | [PHASE_17_MULTI_AGENT_COLLABORATION.md](PHASE_17_MULTI_AGENT_COLLABORATION.md) |
| 18 | Complex Long-Running Tasks | Suspend, resume, check-pointing | Phase 17 | NOT STARTED | [PHASE_18_COMPLEX_LONG_RUNNING_TASKS.md](PHASE_18_COMPLEX_LONG_RUNNING_TASKS.md) |
| 19 | Background Automation | Scheduled and event-driven goals | Phase 18 | NOT STARTED | [PHASE_19_BACKGROUND_AUTOMATION_EVENTS.md](PHASE_19_BACKGROUND_AUTOMATION_EVENTS.md) |
| 20 | External Integrations | Third-party APIs and services | Phase 3 | NOT STARTED | [PHASE_20_EXTERNAL_INTEGRATIONS.md](PHASE_20_EXTERNAL_INTEGRATIONS.md) |

## How Phases are Executed

**REQUIRED WORKFLOW FOR EVERY PHASE:**
1. **READ**: Thoroughly read the Phase document and core architecture docs (including `../TECHNOLOGY.md`).
**Prerequisites**: Before implementing any phase, coding agents should read README, PRD, ARCHITECTURE, TECHNOLOGY, RULES, DECISIONS, MEMORY, TEST_PLAN, SECURITY, and the relevant phase specification.
2. **UNDERSTAND**: Clarify all dependencies and constraints.
3. **PLAN**: Design the specific implementation (classes, interfaces).
4. **IMPLEMENT**: Write the code in `src/`.
5. **TEST**: Write tests in `tests/`.
6. **REVIEW**: Ensure strict adherence to `docs/RULES.md` (no hardcoding!).
7. **FIX**: Resolve bugs and architectural violations.
8. **REAL RUNTIME VALIDATION**: Run it against the real OS/Environment.
9. **DOCUMENT**: Update `MEMORY.md` and any new architectural decisions.
10. **COMPLETE PHASE**: Move status to COMPLETED.

**Crucial Rule:** Do not start the next phase while foundational failures remain in the current one.
