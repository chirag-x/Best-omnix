# Phase 19: Background Automation + Events

## 1. What is being introduced?
Timers, recurring tasks, and condition monitoring (e.g., 'remind me when X happens').

## 2. Why is it introduced now?
Omnix needs to act autonomously based on time or system events without the user speaking a command.

## 3. What components exist after this phase?
EventScheduler, ConditionMonitor.

## 4. What interfaces/contracts exist?
IScheduler.

## 5. What data models/concepts exist?
ScheduledTask, TriggerCondition.

## 6. How does this specific subsystem work?
Custom `asyncio` scheduler (APScheduler only if strictly needed later). Background events generate Goals. These Goals enter the standard Executive -> Policy Engine pipeline.

## 7. What depends on it?
None.

## 8. What is explicitly out of scope?
A secondary execution pipeline. ALL background tasks must pass standard Safety and Executive routing.

## 9. What are the actual development tasks?
1. Implement `EventScheduler` (cron/timer support).
2. Implement `ConditionMonitor` for system events.
3. Route triggered events into the `GoalInterpreter`.

## 10. What exact tests are required?
Timer accuracy tests, condition evaluation tests, background task safety policy enforcement tests.

## 11. What real runtime validation is meaningful?
Schedule a task for 1 minute in the future and verify it executes and requires confirmation if it is a sensitive action.

## 12. What constitutes success?
Reliable background execution that strictly adheres to the Policy Engine.

## 13. What failures must block progression?
Background tasks bypassing safety confirmations, memory leaks from stale monitors.

## 14. What documentation must be updated?
Update `MEMORY.md`.

## 15. What does the next phase depend on?
Phase 20.

## Technology Baseline
This phase must follow the approved technologies and provider boundaries defined in `../TECHNOLOGY.md`.
