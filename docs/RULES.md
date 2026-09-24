# Omnix Architectural Rules (RULES.md)

This document represents the absolute architectural constitution for the Omnix project. These rules are non-negotiable. If a feature cannot be built without breaking these rules, the architecture or the feature must be redesigned.

## 1. Zero Hardcoded Commands
No hard-coded natural-language commands. User input is never mapped via `if intent == "open_browser"`.

## 2. No Fixed Routing
No command-to-fixed-function architecture. The mapping of a goal to execution steps happens dynamically.

## 3. No App-Specific Intelligence
No app-specific general computer-use intelligence. Omnix interacts with Chrome the same way it interacts with a random bespoke desktop app: by perceiving the UI and acting.

## 4. No Fixed Workflows
No fixed workflow per user phrase.

## 5. Single Canonical Pipeline
No duplicate execution pipelines. Text, voice, and events all route through the same Omnix Executive.

## 6. Goals, Not Commands
User requests are considered "goals" (desired outcomes), not literal commands to be executed blindly.

## 7. Global Goal Ownership
Omnix Executive owns the global goal. Specialists do not hijack the entire session.

## 8. Bounded Responsibilities
Agents have bounded responsibilities. A Vision Agent does not decide to delete files.

## 9. Agents Reason, Capabilities Act
Agents think and propose plans. Capabilities are dumb, safe, controlled primitives that execute actions.

## 10. Generic Capabilities
Generic capabilities are preferred. `launch_application(target)` is preferred over `launch_spotify()`.

## 11. Dynamic Selection
Agent selection must remain dynamic. The planner chooses the best agent based on confidence and metadata.

## 12. Discoverability
Capabilities must be discoverable at runtime via the Capability Registry.

## 13. Verification is Mandatory
Meaningful side effects require verification. You must check if the action achieved the expected state.

## 14. No Unverified Success
Never report unverified success to the Executive.

## 15. Graceful Recovery
Failure should enter recovery when safe. Do not crash the task graph immediately on a missed click.

## 16. Bounded Recovery
Recovery must be bounded. Prevent infinite retry loops.

## 17. Unbypassable Safety
Safety cannot be bypassed. The Capability Router must enforce policies on all executions.

## 18. No Unrestricted Shell Access
LLMs do not receive unrestricted shell authority. All shell commands must be strictly parameterized and validated.

## 19. No Capability Duplication
Do not duplicate existing capabilities. If a click capability exists, do not write a new one inside an agent.

## 20. Replaceable Providers
Keep AI providers and models replaceable. Do not leak OpenAI or Gemini specific API quirks into the Core.

## 21. Replaceable Agents
Keep agents replaceable. The system should function (perhaps with degraded capability) if a specific agent is disabled.

## 22. Avoid Hidden Coupling
Agents should not share undocumented state. Use the World State.

## 23. Interface Boundaries
Use interfaces/contracts across major subsystem boundaries (e.g., between Planner and Agent).

## 24. Read Before Coding
Coding agents must read documentation (`README.md`, `RULES.md`, `ARCHITECTURE.md`, `PRD.md`) before writing code.

## 25. Inspect Before Modifying
Inspect the existing implementation in the filesystem before attempting to modify it.

## 26. Focused Changes
Do not modify unrelated files.

## 27. Test with Implementation
Add tests concurrently with implementation.

## 28. Test Before Completion
Run tests before marking a task complete.

## 29. Fix Regressions
Fix regressions immediately before moving to the next phase.

## 30. Real Runtime Testing
Perform real runtime testing (e.g., interacting with actual Windows applications) where required by the phase.

## 31. Document Changes
Update documentation (ADRs, Memory) after making architecture changes.

## 32. Record Decisions
Record permanent architectural decisions in `DECISIONS.md`.

## 33. Maintain State
Update `MEMORY.md` after meaningful development to leave a breadcrumb trail for future sessions.

## 34. Real World Validation
No phase is complete based only on mocked/unit success. If it says it can click a button, it must click a real button.

## 35. Do Not Bypass the Executive
Do not bypass the canonical Omnix runtime to get something working quickly.


## Technology Governance
- Read `TECHNOLOGY.md` before adding a dependency.
- Do not replace approved technologies silently.
- Do not add another LLM without explicit architecture approval.
- Do not add another agent framework.
- Do not replace `.venv` with another environment manager.
- Do not downgrade Python (target 3.13.15).
- Do not introduce paid/cloud dependencies into the baseline without explicit approval.
- Do not couple agents directly to provider-specific APIs; keep implementations behind interfaces.
- Check licenses before redistribution.
- Check Python 3.13.15 compatibility.
- Record permanent technology changes in `DECISIONS.md`.
- Update `TECHNOLOGY.md` when approved technology changes.
