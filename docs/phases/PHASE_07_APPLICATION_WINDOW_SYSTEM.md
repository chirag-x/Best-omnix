# Phase 07 — Application Window System

## Status
NOT STARTED

## Purpose
Provide generic Windows control foundations.

## Why This Phase Exists
This phase establishes the necessary foundation for Application Window System, ensuring that Omnix can fulfill its architectural requirements without resorting to hardcoded solutions.

## User / System Outcome
Upon completion, the system will support Application Window System capabilities dynamically and safely.

## Dependencies
Phase 3

## Prerequisites
Completion of dependent phases and architectural review.

## Architecture Context
Integrates into the Omnix Executive pipeline. Adheres to the Zero Hardcoded Command principle.


## Technology Baseline
This phase must follow the approved technologies and provider boundaries defined in:
`../TECHNOLOGY.md`

Relevant technologies for this phase: Windows native APIs, `pywin32`, `pywinauto`, `psutil`.

## Scope
Application: discover, inspect, launch, focus, terminate. Window: enumerate, inspect, focus, restore, move, resize, minimize, maximize. System: keyboard, mouse, clipboard, process/state primitives.

## Out of Scope
App-specific launch scripts (e.g., open_chrome).

## Components Introduced
- (To be defined during detailed design)

## Responsibilities
- Implement Application Window System interfaces and logic.

## Interfaces / Contracts Required
- Standard Omnix Agent/Capability contracts.

## Data Models / Concepts
- Window Handles
- Process Primitives

## Runtime Flow
1. Executive requests capability.
2. Capability executes.
3. Verification checks outcome.

## Detailed Tasks
- TBD during implementation planning.

## Suggested Task IDs
- OMX-PH07-001

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
- Launch calc.exe, move its window, and close it.

## Acceptance Criteria
- Can manage app/window lifecycle dynamically via OS APIs.

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
Proceed to Phase 08 once completed.
