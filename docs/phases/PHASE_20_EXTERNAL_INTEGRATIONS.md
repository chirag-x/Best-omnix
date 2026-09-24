# Phase 20: External Integrations

## 1. What is being introduced?
Provider architecture for integrating external APIs (Email, Calendar, GitHub, IoT).

## 2. Why is it introduced now?
Omnix eventually needs to interact with the broader digital world beyond the local Windows machine.

## 3. What components exist after this phase?
IntegrationRegistry, PluginBase.

## 4. What interfaces/contracts exist?
IIntegrationProvider.

## 5. What data models/concepts exist?
IntegrationConfig, AuthToken.

## 6. How does this specific subsystem work?
External actions are wrapped as standard Capabilities. They must declare their `CapabilityEffectType` and `RiskCategory` (often EXTERNAL_SIDE_EFFECT). The Policy Engine governs them exactly like local capabilities.

## 7. What depends on it?
None.

## 8. What is explicitly out of scope?
Hardcoding specific third-party API logic into Omnix Core.

## 9. What are the actual development tasks?
1. Define `IIntegrationProvider`.
2. Implement secure token storage (Windows Credential Manager).
3. Map external actions to RiskCategories.
4. Build example integration (e.g., GitHub).

## 10. What exact tests are required?
Integration capability mapping tests, token storage security tests, external side-effect policy tests.

## 11. What real runtime validation is meaningful?
Execute a mock external integration and ensure the Policy Engine correctly requires confirmation for the EXTERNAL_SIDE_EFFECT.

## 12. What constitutes success?
A clean plugin architecture that extends capabilities without compromising core safety or design.

## 13. What failures must block progression?
Hardcoding API keys, external integrations bypassing the Capability Router.

## 14. What documentation must be updated?
Update `MEMORY.md`.

## 15. What does the next phase depend on?
