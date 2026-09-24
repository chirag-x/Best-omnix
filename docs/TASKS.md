# Omnix Development Tasks & Roadmap (Phases 0-20)

This roadmap outlines the exact sequential delivery phases for Omnix. Phases must be executed in order, as each builds architectural dependencies for the next.

## Phase 0: Blueprint + Architecture + Technology
- **Status**: IN PROGRESS
- **Goal**: Finalize architecture, technical boundaries, safety models, and documentation before implementation begins.
- **Dependencies**: None.
- **Completion Criteria**: Clean documentation without TBD placeholders. Strict alignment on a single-model, deterministic-safety architecture.

## Phase 1: Runtime Foundation
- **Status**: NOT STARTED
- **Goal**: Build the core Python execution environment.
- **Dependencies**: Phase 0.
- **Major Deliverables**: Configuration loader, DI container, logging, event bus, cancellation primitives.
- **Testing Gates**: Clean bootstrap and shutdown, unit tests for DI.

## Phase 2: Core Contracts + Agent / Capability Framework
- **Status**: NOT STARTED
- **Goal**: Define the Pydantic data schemas and abstract interfaces.
- **Dependencies**: Phase 1.
- **Major Deliverables**: Agent/Capability Request/Result schemas, CapabilityEffectType, Registries.
- **Testing Gates**: Pydantic validation tests, mock registry tests.

## Phase 3: Omnix Executive
- **Status**: NOT STARTED
- **Goal**: Implement the central orchestration loop.
- **Dependencies**: Phase 2.
- **Major Deliverables**: OmnixExecutive, TaskOrchestrator, capability routing (mocked safety).
- **Testing Gates**: Successfully orchestrating a mock task graph.

## Phase 4: World State + Context
- **Status**: NOT STARTED
- **Goal**: Build versioned, read-safe state management.
- **Dependencies**: Phase 3.
- **Major Deliverables**: WorldStateStore, snapshots, revisions, context management.
- **Testing Gates**: Concurrency tests for safe read/writes.

## Phase 5: Safety / Policy / Permissions Foundation
- **Status**: NOT STARTED
- **Goal**: Implement the deterministic Policy Engine.
- **Dependencies**: Phase 4.
- **Major Deliverables**: PolicyEngine, RiskCategories, confirmation workflows.
- **Testing Gates**: Deterministic blocking of DESTRUCTIVE mock capabilities.

## Phase 6: Brain + Goals + Planning
- **Status**: NOT STARTED
- **Goal**: Integrate Ollama/Gemma and the Planner Agent.
- **Dependencies**: Phase 5.
- **Major Deliverables**: OllamaProvider, ModelManager, PlannerAgent, PlanRevision schemas.
- **Testing Gates**: Generating acyclic PlanRevisions from Gemma inference.

## Phase 7: Input / Output / Voice Foundation
- **Status**: NOT STARTED
- **Goal**: Implement the local audio pipeline.
- **Dependencies**: Phase 6.
- **Major Deliverables**: sounddevice capture, DeepFilterNet, Silero VAD, openWakeWord, faster-whisper, Chatterbox TTS.
- **Testing Gates**: Voice-in to Goal-generation, TTS audio output.

## Phase 8: Application + Window + System Capabilities
- **Status**: NOT STARTED
- **Goal**: Build deterministic OS control primitives.
- **Dependencies**: Phase 7.
- **Major Deliverables**: Window enumeration/focus, SendInput, application discovery.
- **Testing Gates**: Successfully wrapping pywin32/pywinauto calls in capability interfaces.

## Phase 9: Perception + Vision + Grounding
- **Status**: NOT STARTED
- **Goal**: Build layered computer perception.
- **Dependencies**: Phase 8.
- **Major Deliverables**: DXcam capture, UI Automation parsing, RapidOCR, SceneModeler.
- **Testing Gates**: Accurately mapping screen elements to a Grounded SceneModel.

## Phase 10: Verification Engine
- **Status**: NOT STARTED
- **Goal**: Deterministic-first action verification.
- **Dependencies**: Phase 9.
- **Major Deliverables**: VerificationEngine, ProcessVerifier, PASS/FAIL/UNCERTAIN logic.
- **Testing Gates**: Correctly reporting FAIL on unsuccessful mock actions.

## Phase 11: Recovery + Dynamic Replanning
- **Status**: NOT STARTED
- **Goal**: Handle Verification FAILs gracefully.
- **Dependencies**: Phase 10.
- **Major Deliverables**: RecoveryManager, wait/retry limits, replanning contexts.
- **Testing Gates**: Generating a new PlanRevision upon simulated failure.

## Phase 12: Generic Desktop Interaction
- **Status**: NOT STARTED
- **Goal**: End-to-end integration proving generic desktop control.
- **Dependencies**: Phases 1-11.
- **Major Deliverables**: Complete autonomous execution loop on an unknown application.
- **Testing Gates**: Interacting with an unfamiliar UI successfully.

## Phase 13: Browser Intelligence
- **Status**: NOT STARTED
- **Goal**: Structured web navigation via Playwright.
- **Dependencies**: Phase 12.
- **Major Deliverables**: BrowserAgent, PlaywrightProvider, DOM reasoning.
- **Testing Gates**: Navigating and extracting data from a web page.

## Phase 14: Filesystem Intelligence
- **Status**: NOT STARTED
- **Goal**: Safe filesystem manipulation.
- **Dependencies**: Phase 13.
- **Major Deliverables**: FilesystemAgent, safe path capabilities.
- **Testing Gates**: Policy Engine successfully gatekeeping DESTRUCTIVE file deletes.

## Phase 15: Memory
- **Status**: NOT STARTED
- **Goal**: SQLite/FTS5 working and conversational memory.
- **Dependencies**: Phase 14.
- **Major Deliverables**: MemoryManager, FTS5 indexer, context injection.
- **Testing Gates**: Storing and retrieving facts accurately across restarts.

## Phase 16: Communication + Personality + Character
- **Status**: NOT STARTED
- **Goal**: Natural expression and Godot character bridge.
- **Dependencies**: Phase 15.
- **Major Deliverables**: CommunicationAgent, CharacterBridge (IPC), Rhubarb lip sync.
- **Testing Gates**: Character changing state synchronously with task execution.

## Phase 17: Dynamic Multi-Agent Collaboration
- **Status**: NOT STARTED
- **Goal**: Enable Executive-managed delegation.
- **Dependencies**: Phase 16.
- **Major Deliverables**: Sub-task isolation, shared context boundaries.
- **Testing Gates**: Successful delegation from Planner to BrowserAgent.

## Phase 18: Complex / Long-Running Tasks
- **Status**: NOT STARTED
- **Goal**: Persistence and pause/resume capabilities.
- **Dependencies**: Phase 17.
- **Major Deliverables**: TaskPersister, CheckpointManager.
- **Testing Gates**: Surviving a process kill mid-task and resuming.

## Phase 19: Background Automation + Events
- **Status**: NOT STARTED
- **Goal**: Timers and conditional triggers.
- **Dependencies**: Phase 18.
- **Major Deliverables**: EventScheduler, ConditionMonitor.
- **Testing Gates**: Background tasks passing the Policy Engine identically to foreground tasks.

## Phase 20: External Integrations
- **Status**: NOT STARTED
- **Goal**: Architecture for external APIs.
- **Dependencies**: Phase 19.
- **Major Deliverables**: IntegrationRegistry, credential management.
- **Testing Gates**: Mock external API requiring EXTERNAL_SIDE_EFFECT confirmation.
