# Phase 4: World State + Context

## 1. What is being introduced?
The versioned, snapshot-based storage for the current state of the computer and the active conversation.

## 2. Why is it introduced now?
Because agents must not freely mutate a global singleton. They need a consistent, read-safe snapshot of the world to reason about, and updates must be explicitly managed via observations.

## 3. What components exist after this phase?
WorldStateStore, ContextManager.

## 4. What interfaces/contracts exist?
IWorldStateStore, IContextManager.

## 5. What data models/concepts exist?
WorldStateSnapshot, WorldStateRevision, ObservationState, SessionContext, TaskContext.

## 6. How does this specific subsystem work?
Using a versioned immutable data structure or controlled in-memory SQLite tables. When new observations arrive, a new revision is created. Agents query specific revisions.

## 7. What depends on it?
Phase 6 (Planning) and Phase 9 (Perception).

## 8. What is explicitly out of scope?
Long-term episodic memory (Phase 15). UI automation extraction (Phase 8).

## 9. What are the actual development tasks?
1. Define `WorldStateSnapshot` schema.
2. Implement `WorldStateStore` with revision tracking.
3. Implement `ContextManager` for session scope.
4. Expose query methods for current state.

## 10. What exact tests are required?
Concurrency tests for reading/writing state, revision history validation, context isolation tests.

## 11. What real runtime validation is meaningful?
Simulate concurrent capability observations and verify the state store maintains consistent revisions without race conditions.

## 12. What constitutes success?
Agents can reliably query a specific snapshot of the world state, and updates generate new sequential revisions.

## 13. What failures must block progression?
State corruption, race conditions on read/write, memory leaks from storing unbounded revisions.

## 14. What documentation must be updated?
Update `MEMORY.md`.

## 15. What does the next phase depend on?
Phase 5 (Safety) needs World State to evaluate contextual risk.

## Technology Baseline
This phase must follow the approved technologies and provider boundaries defined in `../TECHNOLOGY.md`.
