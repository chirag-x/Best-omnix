# Phase 18: Complex / Long-Running Tasks

## 1. What is being introduced?
Persistence, pausing, resuming, and checkpointing for large task graphs.

## 2. Why is it introduced now?
Some tasks take hours. Omnix must survive application restarts and allow users to pause or intervene.

## 3. What components exist after this phase?
TaskPersister, CheckpointManager.

## 4. What interfaces/contracts exist?
ITaskPersister.

## 5. What data models/concepts exist?
PersistentTaskState, Checkpoint.

## 6. How does this specific subsystem work?
Executive serializes the current `TaskState` and `PlanRevision` to SQLite via `TaskPersister` at step boundaries. On startup, incomplete tasks can be resumed. Long-running verification handles asynchronous delays.

## 7. What depends on it?
Phase 19 (Background automation).

## 8. What is explicitly out of scope?
Distributed task execution across multiple machines.

## 9. What are the actual development tasks?
1. Implement TaskState serialization.
2. Implement pause/resume primitives in Executive.
3. Build `CheckpointManager`.
4. Handle long-polling verification.

## 10. What exact tests are required?
Serialization/deserialization tests, pause/resume state preservation tests.

## 11. What real runtime validation is meaningful?
Start a long task, kill the Omnix process, restart, and successfully resume execution from the last checkpoint.

## 12. What constitutes success?
Task state is durable and robust to process death.

## 13. What failures must block progression?
Corrupted state on resume, inability to cancel a long-running resumed task.

## 14. What documentation must be updated?
Update `MEMORY.md`.

## 15. What does the next phase depend on?
Phase 19.

## Technology Baseline
This phase must follow the approved technologies and provider boundaries defined in `../TECHNOLOGY.md`.
