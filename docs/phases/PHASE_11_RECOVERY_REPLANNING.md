# Phase 11: Recovery + Dynamic Replanning

## 1. What is being introduced?
The logic to handle Verification FAILs by employing recovery strategies (retry, wait, alternate capability) and generating new PlanRevisions.

## 2. Why is it introduced now?
Because real computer interaction is flaky. Windows move, apps take time to load, clicks miss. Omnix must gracefully recover.

## 3. What components exist after this phase?
RecoveryManager, Replanning logic in PlannerAgent.

## 4. What interfaces/contracts exist?
IRecovery.

## 5. What data models/concepts exist?
RecoveryContext, RecoveryStrategy, FailureClassification.

## 6. How does this specific subsystem work?
When Verification returns FAIL, Executive passes context to `RecoveryManager`. It classifies the error. If simple (e.g., UI loading), it waits/retries. If blocked, it asks the `PlannerAgent` for a new `PlanRevision` (acyclic graph) starting from the new WorldState.

## 7. What depends on it?
Phase 12 (Generic Desktop Interaction).

## 8. What is explicitly out of scope?
Bypassing safety. Recovery actions must still pass the Policy Engine.

## 9. What are the actual development tasks?
1. Define `FailureClassification`.
2. Implement `RecoveryManager` with retry/wait/reground strategies.
3. Update `PlannerAgent` to accept `RecoveryContext` and produce a new `PlanRevision`.
4. Implement retry limits.

## 10. What exact tests are required?
Recovery limit tests, strategy selection tests, replanning generation tests.

## 11. What real runtime validation is meaningful?
Intentionally fail an action (e.g., close target window mid-task) and verify Omnix generates a valid recovery plan.

## 12. What constitutes success?
Omnix survives unexpected state changes by adapting its plan without crashing.

## 13. What failures must block progression?
Infinite retry loops, generating cyclic recovery plans, bypassing safety policies during recovery.

## 14. What documentation must be updated?
Update `MEMORY.md`.

## 15. What does the next phase depend on?
Phase 12 combines this into a complete autonomous loop.

## Technology Baseline
This phase must follow the approved technologies and provider boundaries defined in `../TECHNOLOGY.md`.
