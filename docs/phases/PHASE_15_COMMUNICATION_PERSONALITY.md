# Phase 15 — Communication Personality

## Status
NOT STARTED

## Purpose
Make Omnix communicate naturally without mixing speech with execution.

## Why This Phase Exists
This phase establishes the necessary foundation for Communication Personality, ensuring that Omnix can fulfill its architectural requirements without resorting to hardcoded solutions.

## User / System Outcome
Upon completion, the system will support Communication Personality capabilities dynamically and safely.

## Dependencies
Phase 6

## Prerequisites
Completion of dependent phases and architectural review.

## Architecture Context
Integrates into the Omnix Executive pipeline. Adheres to the Zero Hardcoded Command principle.


## Technology Baseline
This phase must follow the approved technologies and provider boundaries defined in:
`../TECHNOLOGY.md`

Relevant technologies for this phase: Chatterbox, Godot, Blender-created assets, Rhubarb, PySide6/QML integration.

## Scope
Communication Agent, response planning, task progress narration, personality, expression/emotional tone, concise speech, technical-output filtering, uncertainty expression, success/failure communication.

## Out of Scope
Reading raw JSON logs to the user.

## Components Introduced
- (To be defined during detailed design)

## Responsibilities
- Implement Communication Personality interfaces and logic.

## Interfaces / Contracts Required
- Standard Omnix Agent/Capability contracts.

## Data Models / Concepts
- Personality Filter
- Natural Language Generation

## Runtime Flow
1. Executive requests capability.
2. Capability executes.
3. Verification checks outcome.

## Detailed Tasks
- TBD during implementation planning.

## Suggested Task IDs
- OMX-PH15-001

## Development Order
1. Define interfaces.
2. Implement core logic.
3. Integrate with Capability Router.
4. Add tests.

## Architecture Constraints
- MUST NOT use hardcoded natural-language command routing.
- MUST NOT bypass the Omnix Executive.

## Failure Cases
- Missing permissions.
- Timeout during execution.

## Safety Considerations
- Follow `SECURITY.md` guidelines for all new capabilities.

## Observability Requirements
- Structured logging for all state changes.

## Unit Testing Requirements
- 100% coverage on core logic.

## Integration Testing Requirements
- Test with simulated World State.

## Real Runtime Testing Requirements
- Transform a technical exception into a polite apology.

## Acceptance Criteria
- Output is strictly separated from internal technical state.

## Definition of Done
- Code merged.
- Tests passing (including real runtime).
- Documentation updated.

## Required Evidence
- Test logs demonstrating successful dynamic execution.

## Documentation Updates
- Update `MEMORY.md` and `TASKS.md`.

## Risks
- Unexpected OS behavior.

## Open Questions
- (To be determined)

## Next Phase
Proceed to Phase 16 once completed.
