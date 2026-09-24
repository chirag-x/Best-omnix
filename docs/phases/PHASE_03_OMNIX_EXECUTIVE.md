# Phase 3: Omnix Executive

## 1. What is being introduced?
The central orchestration loop that receives a goal, invokes agents, requests capabilities, and manages task lifecycle.

## 2. Why is it introduced now?
Because Omnix requires a single authority to manage execution state, handle cancellations, and route data between agents and capabilities without agents calling each other blindly.

## 3. What components exist after this phase?
OmnixExecutive, TaskOrchestrator.

## 4. What interfaces/contracts exist?
IExecutive.

## 5. What data models/concepts exist?
TaskState, ExecutionStatus.

## 6. How does this specific subsystem work?
The Executive runs an `asyncio` loop. It takes a goal, passes it to the planning agent (mocked for now), receives a plan, iterates through steps, dispatches capability requests to the router, handles failures, and updates task state.

## 7. What depends on it?
Phase 6 (Brain/Goals) and all capability execution phases.

## 8. What is explicitly out of scope?
Real LLM reasoning, real policy enforcement, real verification. These will be plugged in later.

## 9. What are the actual development tasks?
1. Implement `OmnixExecutive`.
2. Implement basic orchestration loop.
3. Handle agent dispatching.
4. Handle capability routing (bypassing safety for now with mocks).
5. Handle task completion/cancellation.

## 10. What exact tests are required?
Unit tests for the orchestration loop, task state transitions, and cancellation.

## 11. What real runtime validation is meaningful?
Running a hardcoded mock task graph through the Executive and verifying it completes correctly.

## 12. What constitutes success?
The Executive can coordinate a multi-step mock plan, route requests, and gracefully stop.

## 13. What failures must block progression?
Infinite execution loops, unhandled capability exceptions crashing the executive.

## 14. What documentation must be updated?
Update `MEMORY.md`, confirm Executive lifecycle in `ARCHITECTURE.md`.

## 15. What does the next phase depend on?
Phase 4 (World State) is needed for the Executive to maintain context.

## Technology Baseline
This phase must follow the approved technologies and provider boundaries defined in `../TECHNOLOGY.md`.
