# Omnix Implementation Phases

This directory contains the canonical specifications for each phase of Omnix development.

**Prerequisites**: Before implementing any phase, coding agents must read README, PRD, ARCHITECTURE, TECHNOLOGY, RULES, DECISIONS, MEMORY, TEST_PLAN, SECURITY, and the relevant phase specification.

## Sequential Execution
Phases MUST be executed sequentially (0 through 20).
Architectural dependencies mandate this order:
- Contracts (Phase 2) must exist before the Executive (Phase 3).
- The Policy Engine (Phase 5) must exist before side-effecting Capabilities (Phase 8).
- The Verification Engine (Phase 10) must exist before Generic Interaction (Phase 12).
- Recovery (Phase 11) depends on Verification (Phase 10).

## Phase Documents
- `PHASE_00_BLUEPRINT.md`
- `PHASE_01_RUNTIME_FOUNDATION.md`
- `PHASE_02_CORE_CONTRACTS_AGENT_CAPABILITY_FRAMEWORK.md`
- `PHASE_03_OMNIX_EXECUTIVE.md`
- `PHASE_04_WORLD_STATE_CONTEXT.md`
- `PHASE_05_SAFETY_POLICY_PERMISSIONS.md`
- `PHASE_06_BRAIN_GOALS_PLANNING.md`
- `PHASE_07_INPUT_OUTPUT_VOICE.md`
- `PHASE_08_APPLICATION_WINDOW_SYSTEM_CAPABILITIES.md`
- `PHASE_09_PERCEPTION_VISION_GROUNDING.md`
- `PHASE_10_VERIFICATION_ENGINE.md`
- `PHASE_11_RECOVERY_REPLANNING.md`
- `PHASE_12_GENERIC_DESKTOP_INTERACTION.md`
- `PHASE_13_BROWSER_INTELLIGENCE.md`
- `PHASE_14_FILESYSTEM_INTELLIGENCE.md`
- `PHASE_15_MEMORY.md`
- `PHASE_16_COMMUNICATION_PERSONALITY_CHARACTER.md`
- `PHASE_17_MULTI_AGENT_COLLABORATION.md`
- `PHASE_18_COMPLEX_LONG_RUNNING_TASKS.md`
- `PHASE_19_BACKGROUND_AUTOMATION_EVENTS.md`
- `PHASE_20_EXTERNAL_INTEGRATIONS.md`

Do not create boilerplate placeholders. Each document defines exactly WHAT, WHY, and HOW for its respective milestone.
