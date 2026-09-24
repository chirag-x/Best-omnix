# Phase 10: Verification Engine

## 1. What is being introduced?
Deterministic-first verification providers (Process, Window, UIA, Filesystem) and the Verification Agent (reasoning) to prove task success.

## 2. Why is it introduced now?
Omnix must know if its actions succeeded. Blindly assuming success leads to catastrophic failure chains. Verification must be deterministic where possible.

## 3. What components exist after this phase?
VerificationEngine, ProcessVerifier, WindowVerifier, VerificationAgent.

## 4. What interfaces/contracts exist?
IVerifier.

## 5. What data models/concepts exist?
VerificationResult (PASS, FAIL, UNCERTAIN), VerificationEvidence.

## 6. How does this specific subsystem work?
After a capability executes, the Executive calls the `VerificationEngine` with expected post-conditions. The engine checks deterministic verifiers (e.g., 'Is process X running?'). If evidence is UNCERTAIN, it escalates to the `VerificationAgent` (Gemma) to reason about the SceneModel.

## 7. What depends on it?
Phase 11 (Recovery).

## 8. What is explicitly out of scope?
Fixing the failure. Verification only observes and reports.

## 9. What are the actual development tasks?
1. Implement `VerificationEngine`.
2. Implement deterministic verifiers (Process, Window, Filesystem).
3. Implement `VerificationAgent` for complex state evaluation.
4. Define `PASS/FAIL/UNCERTAIN` logic.

## 10. What exact tests are required?
Unit tests for PASS/FAIL outcomes based on mock state, escalation logic tests.

## 11. What real runtime validation is meaningful?
Simulate a failed application launch and ensure the Verification Engine returns FAIL.

## 12. What constitutes success?
Omnix correctly identifies success and failure of its own actions without hallucinating success.

## 13. What failures must block progression?
LLM VerificationAgent overriding a deterministic FAIL, infinite verification loops.

## 14. What documentation must be updated?
Update `MEMORY.md`.

## 15. What does the next phase depend on?
Phase 11 uses Verification FAILs to trigger recovery.

## Technology Baseline
This phase must follow the approved technologies and provider boundaries defined in `../TECHNOLOGY.md`.
