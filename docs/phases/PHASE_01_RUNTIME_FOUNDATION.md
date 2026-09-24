# Phase 1: Runtime Foundation

## 1. What is being introduced?
The core Python executable environment, logging, configuration loading, error handling, cancellation primitives, and dependency injection.

## 2. Why is it introduced now?
Because every higher-level component (Executive, Agents, Capabilities) needs a stable, structured environment to run, log its actions, and load its configuration.

## 3. What components exist after this phase?
Configuration Loader, Dependency Container, Logger Foundation, Event Bus (local), Cancellation Tokens, Core Error hierarchy.

## 4. What interfaces/contracts exist?
IEventBus, IConfiguration, ILoggerProvider.

## 5. What data models/concepts exist?
OmnixConfig, OmnixError, EventMessage.

## 6. How does this specific subsystem work?
Using `pydantic-settings` to load `.env`, standard `logging`/`structlog` for structured stdout, and an `asyncio`-based dependency registry to inject singletons and transients.

## 7. What depends on it?
Phase 2 (Core Contracts) and all subsequent phases.

## 8. What is explicitly out of scope?
AI/LLM integration, task planning, agent intelligence, Windows capabilities.

## 9. What are the actual development tasks?
1. Set up `src/` layout.
2. Implement `OmnixConfig` with `pydantic-settings`.
3. Set up structlog and Rich formatting.
4. Build `asyncio` event bus.
5. Create Dependency Container.
6. Implement Cancellation primitives.

## 10. What exact tests are required?
Unit tests for config loading, event publish/subscribe, DI resolution, and structured error serialization.

## 11. What real runtime validation is meaningful?
Starting the application should successfully initialize DI, read valid `.env`, and shut down cleanly when cancelled.

## 12. What constitutes success?
The application can bootstrap, inject mock dependencies, run a simple event loop, and gracefully terminate.

## 13. What failures must block progression?
Failing to load config, DI cyclical dependencies, or hanging event loops block progression.

## 14. What documentation must be updated?
Update `MEMORY.md`, add module structure details.

## 15. What does the next phase depend on?
Phase 2 depends on the DI container and error models to define contracts.

## Technology Baseline
This phase must follow the approved technologies and provider boundaries defined in `../TECHNOLOGY.md`.
