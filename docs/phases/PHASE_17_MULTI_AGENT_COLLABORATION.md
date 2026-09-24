# Phase 17: Dynamic Multi-Agent Collaboration

## 1. What is being introduced?
Delegation and shared context boundaries between multiple specialized agents (e.g., Planner delegating to BrowserAgent delegating to FilesystemAgent).

## 2. Why is it introduced now?
Complex tasks require agents with different prompt contexts and specialized tools to collaborate without overwhelming a single prompt.

## 3. What components exist after this phase?
AgentCollaborationManager, SubTask delegation logic.

## 4. What interfaces/contracts exist?
None (enhances `IExecutive`).

## 5. What data models/concepts exist?
DelegationRequest, AgentHealth.

## 6. How does this specific subsystem work?
The Executive manages sub-tasks. Planner produces a PlanRevision that includes a step assigned to `BrowserAgent`. The Executive provisions the `BrowserAgent` with a localized Context, executes it, and returns the result to update the WorldState.

## 7. What depends on it?
Phase 18 (Complex tasks).

## 8. What is explicitly out of scope?
Uncontrolled peer-to-peer swarms. All delegation routes through the Executive.

## 9. What are the actual development tasks?
1. Implement sub-task delegation in Executive.
2. Implement context pruning for specialized agents.
3. Handle agent failures/unavailable states during collaboration.

## 10. What exact tests are required?
Delegation context isolation tests, multi-agent failure recovery tests.

## 11. What real runtime validation is meaningful?
Execute a task requiring web search (BrowserAgent) and saving to disk (FilesystemAgent) cleanly coordinated by the Executive.

## 12. What constitutes success?
Specialized agents accomplish complex goals without context window contamination.

## 13. What failures must block progression?
Agents calling each other directly and bypassing the Executive/Policy Engine.

## 14. What documentation must be updated?
Update `MEMORY.md`.

## 15. What does the next phase depend on?
Phase 18.

## Technology Baseline
This phase must follow the approved technologies and provider boundaries defined in `../TECHNOLOGY.md`.
