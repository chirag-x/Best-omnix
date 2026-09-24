# Phase 06 — Brain Goals Planning

## Status
NOT STARTED

## Purpose
Create cognitive interpretation and dynamic planning.

## Why This Phase Exists
This phase establishes the necessary foundation for Brain Goals Planning, ensuring that Omnix can fulfill its architectural requirements without resorting to hardcoded solutions.

## User / System Outcome
Upon completion, the system will support Brain Goals Planning capabilities dynamically and safely.

## Dependencies
Phase 3, Phase 5

## Prerequisites
Completion of dependent phases and architectural review.

## Architecture Context
Integrates into the Omnix Executive pipeline. Adheres to the Zero Hardcoded Command principle.


## Technology Baseline
This phase must follow the approved technologies and provider boundaries defined in:
`../TECHNOLOGY.md`

Relevant technologies for this phase: Ollama, Gemma 4 31B, Model Manager.

## Scope
Brain Agent, model abstraction, goal interpreter, goal representation, constraint extraction, success condition, planner, task graph, plan validation, dynamic replanning.

## Out of Scope
Direct capability execution inside the brain.

## Components Introduced
- (To be defined during detailed design)

## Responsibilities
- Implement Brain Goals Planning interfaces and logic.

## Interfaces / Contracts Required
- Standard Omnix Agent/Capability contracts.

## Data Models / Concepts
- Goal Representation
- Task Graph
- Planner

## Runtime Flow
1. Executive requests capability.
2. Capability executes.
3. Verification checks outcome.

## Detailed Tasks
- TBD during implementation planning.

## Suggested Task IDs
- OMX-PH06-001

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
- Pass natural language input, verify it generates a valid Task Graph representing the goal.

## Acceptance Criteria
- Natural-language input -> abstract goal representation (NOT command ID).

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
Proceed to Phase 07 once completed.
