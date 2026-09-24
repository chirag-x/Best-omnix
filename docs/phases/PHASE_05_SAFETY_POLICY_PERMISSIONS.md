# Phase 5: Safety / Policy / Permissions Foundation

## 1. What is being introduced?
The deterministic Policy Engine, risk taxonomy, and safety boundaries that authorize or deny capabilities BEFORE they execute.

## 2. Why is it introduced now?
Safety must exist before Omnix gains significant side-effecting computer-control power. We cannot trust an LLM to self-police.

## 3. What components exist after this phase?
PolicyEngine, SafetyAgent (reasoning stub), CapabilityRouter (updated).

## 4. What interfaces/contracts exist?
IPolicyEngine, ICapabilityRouter.

## 5. What data models/concepts exist?
RiskCategory (LOW_RISK, SENSITIVE, DESTRUCTIVE, IRREVERSIBLE, PRIVACY_SENSITIVE, EXTERNAL_SIDE_EFFECT), PolicyDecision (ALLOW, DENY, REQUIRE_CONFIRMATION).

## 6. How does this specific subsystem work?
The `CapabilityRouter` receives a request, extracts the `CapabilityEffectType`, checks the `PolicyEngine` (which evaluates rules based on RiskCategory and WorldState). If `REQUIRE_CONFIRMATION`, the Executive pauses for user input. The `SafetyAgent` can optionally classify ambiguous targets, but the Engine decides.

## 7. What depends on it?
Phase 8 (Capabilities) and all subsequent execution phases.

## 8. What is explicitly out of scope?
Implementation of destructive actions. We are only building the gatekeeper here.

## 9. What are the actual development tasks?
1. Define canonical `RiskCategory`.
2. Implement deterministic `PolicyEngine`.
3. Integrate `PolicyEngine` into `CapabilityRouter`.
4. Implement confirmation pause flow in Executive.
5. Create stub `SafetyAgent`.

## 10. What exact tests are required?
Unit tests for every risk category, permission checks, deny/allow logic, and confirmation escalation.

## 11. What real runtime validation is meaningful?
Routing a mock `DESTRUCTIVE` capability request and verifying it is blocked or paused for confirmation deterministically.

## 12. What constitutes success?
Zero side-effecting capabilities can execute without passing the Policy Engine.

## 13. What failures must block progression?
Bypassing the policy engine, LLM overriding a deterministic DENY.

## 14. What documentation must be updated?
Update `SECURITY.md`, `MEMORY.md`.

## 15. What does the next phase depend on?
Phase 8 (Capabilities) relies on this to execute safely.

## Technology Baseline
This phase must follow the approved technologies and provider boundaries defined in `../TECHNOLOGY.md`.
