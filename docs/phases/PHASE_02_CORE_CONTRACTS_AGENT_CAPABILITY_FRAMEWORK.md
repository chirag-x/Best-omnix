# Phase 2: Core Contracts + Agent / Capability Framework

## 1. What is being introduced?
The abstract interfaces and Pydantic data contracts that define what an Agent is, what a Capability is, and how they communicate.

## 2. Why is it introduced now?
To establish the boundary between Omnix Executive and the specialized workers BEFORE implementing the Executive itself. We must know the shape of a request before routing it.

## 3. What components exist after this phase?
AgentRegistry, CapabilityRegistry, BaseAgent, BaseCapability.

## 4. What interfaces/contracts exist?
IAgent, ICapability, ICapabilityRouter, IProvider.

## 5. What data models/concepts exist?
AgentId, AgentMetadata, AgentRequest, AgentResult, CapabilityId, CapabilityMetadata, CapabilityRequest, CapabilityResult, CapabilityEffectType (READ_ONLY/SIDE_EFFECTING).

## 6. How does this specific subsystem work?
Through strict Pydantic schemas. Agents receive an `AgentRequest` and return an `AgentResult`. Capabilities expose their required arguments and effect types. Registries store these for discovery.

## 7. What depends on it?
Phase 3 (Omnix Executive) and Phase 5 (Safety).

## 8. What is explicitly out of scope?
Implementing real capabilities (e.g., open_app) or real LLM-backed agents (e.g., Planner).

## 9. What are the actual development tasks?
1. Define `CapabilityEffectType` enum.
2. Define Agent/Capability request/result schemas in Pydantic.
3. Implement `AgentRegistry` and `CapabilityRegistry`.
4. Create abstract base classes for Agents/Capabilities.

## 10. What exact tests are required?
Pydantic validation tests, Registry registration/retrieval tests, contract mock implementations.

## 11. What real runtime validation is meaningful?
Mock agents and mock capabilities successfully registering and passing static type analysis (Pyright).

## 12. What constitutes success?
A complete, type-safe contract layer that prevents arbitrary function calls.

## 13. What failures must block progression?
Pydantic validation errors, missing effect types on capabilities, tight coupling to specific implementations.

## 14. What documentation must be updated?
Update `MEMORY.md`, map contracts in `ARCHITECTURE.md`.

## 15. What does the next phase depend on?
Phase 3 depends on `AgentRequest` and `CapabilityRequest` to coordinate execution.

## Technology Baseline
This phase must follow the approved technologies and provider boundaries defined in `../TECHNOLOGY.md`.
