# Phase 20 — External Integrations

## Status
NOT STARTED

## Purpose
Extend Omnix beyond local desktop operation.

## Why This Phase Exists
This phase establishes the necessary foundation for External Integrations, ensuring that Omnix can fulfill its architectural requirements without resorting to hardcoded solutions.

## User / System Outcome
Upon completion, the system will support External Integrations capabilities dynamically and safely.

## Dependencies
Phase 3

## Prerequisites
Completion of dependent phases and architectural review.

## Architecture Context
Integrates into the Omnix Executive pipeline. Adheres to the Zero Hardcoded Command principle.


## Technology Baseline
This phase must follow the approved technologies and provider boundaries defined in:
`../TECHNOLOGY.md`

Relevant technologies for this phase: `httpx`/provider/plugin abstractions.

## Scope
email, calendar, messaging, cloud storage, GitHub, APIs, smart-home/device systems, external tools/services.

## Out of Scope
Hardcoding providers into Omnix Core.

## Components Introduced
- (To be defined during detailed design)

## Responsibilities
- Implement External Integrations interfaces and logic.

## Interfaces / Contracts Required
- Standard Omnix Agent/Capability contracts.

## Data Models / Concepts
- Integration Plugins

## Runtime Flow
1. Executive requests capability.
2. Capability executes.
3. Verification checks outcome.

## Detailed Tasks
- TBD during implementation planning.

## Suggested Task IDs
- OMX-PH20-001

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
- Call a mocked external API safely.

## Acceptance Criteria
- External integrations adhere to the standard safety and capability interfaces.

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
Proceed to Phase 21 once completed.
