# Phase 6: Brain + Goal Understanding + Dynamic Planning

## 1. What is being introduced?
Integration of Ollama (Gemma 4 31B), the Model Manager, Goal interpretation, and the Planner Agent producing acyclic PlanRevisions.

## 2. Why is it introduced now?
To give Omnix the intelligence to translate natural language into structured, revisable task graphs rather than relying on hardcoded commands.

## 3. What components exist after this phase?
ModelManager, OllamaProvider, GoalInterpreter, PlannerAgent.

## 4. What interfaces/contracts exist?
IModelProvider, IPlanner.

## 5. What data models/concepts exist?
Goal, DesiredOutcome, Constraint, PlanRevision, TaskGraph, TaskStep, Dependency.

## 6. How does this specific subsystem work?
The `ModelManager` connects to Ollama/Gemma. The user input becomes a `Goal`. The `PlannerAgent` creates a `PlanRevision` (an acyclic graph of `TaskStep`s). The Executive executes the `PlanRevision`. Model Manager handles timeouts and context length.

## 7. What depends on it?
Phase 11 (Recovery/Replanning) and overall intelligence.

## 8. What is explicitly out of scope?
Vector DB embedding models, separate LLMs for vision/planning. Hardcoding natural language to specific capability IDs.

## 9. What are the actual development tasks?
1. Implement `OllamaProvider` integrating with local Ollama.
2. Implement `ModelManager` (context/health management).
3. Define `PlanRevision` and `TaskStep` data models.
4. Implement `PlannerAgent` with Gemma prompts.
5. Integrate Planner with Executive.

## 10. What exact tests are required?
Mock Ollama responses, PlanRevision validation (ensure acyclic), Goal generation unit tests.

## 11. What real runtime validation is meaningful?
Send a text prompt to the real local Gemma model and successfully parse a valid JSON PlanRevision.

## 12. What constitutes success?
Omnix can dynamically generate a valid plan from a natural language request using the single shared Gemma model.

## 13. What failures must block progression?
Model timeouts crashing the system, generation of cyclic task graphs, hallucinated capability IDs.

## 14. What documentation must be updated?
Update `MEMORY.md`, record Gemma inference benchmarks.

## 15. What does the next phase depend on?
Phase 7 needs goals derived from Voice.

## Technology Baseline
This phase must follow the approved technologies and provider boundaries defined in `../TECHNOLOGY.md`.
