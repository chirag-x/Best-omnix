# Phase 12: Generic Desktop Interaction

## 1. What is being introduced?
The culmination of phases 1-11, proving Omnix can interact with an unfamiliar application using pure perception, planning, and capabilities.

## 2. Why is it introduced now?
This is the primary runtime milestone. It proves the generic, non-hardcoded architecture works end-to-end.

## 3. What components exist after this phase?
Integration of Executive, Planner, Capabilities, Perception, Verification, Recovery, and Safety.

## 4. What interfaces/contracts exist?
None (Integration Phase).

## 5. What data models/concepts exist?
None.

## 6. How does this specific subsystem work?
User provides a voice goal. Planner makes a plan. Capabilities execute (Window focus, UIA click, SendInput). Perception updates WorldState. Verification checks it. Recovery handles misses.

## 7. What depends on it?
Subsequent specialist intelligence phases (Browser, Filesystem).

## 8. What is explicitly out of scope?
Web-specific DOM logic (Phase 13).

## 9. What are the actual development tasks?
1. Create end-to-end integration tests.
2. Tune capability latency and grounding accuracy.
3. Optimize Gemma prompts for desktop reasoning.
4. Validate full policy enforcement.

## 10. What exact tests are required?
Extensive E2E tests against diverse dummy applications.

## 11. What real runtime validation is meaningful?
Instruct Omnix to open an unfamiliar application, find a specific text box, type a string, and click a non-standard button.

## 12. What constitutes success?
Successful goal completion in an unknown environment without app-specific macros.

## 13. What failures must block progression?
Relying on hardcoded 'if app == X' logic to pass the validation.

## 14. What documentation must be updated?
Update `MEMORY.md`, record E2E metrics.

## 15. What does the next phase depend on?
Phase 13 builds on this for the Browser.

## Technology Baseline
This phase must follow the approved technologies and provider boundaries defined in `../TECHNOLOGY.md`.
