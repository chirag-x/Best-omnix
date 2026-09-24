# Omnix Architecture

## 1. System Overview
Omnix is a deterministic-first, local-first AI system that bridges natural language goals to Windows desktop execution. It uses one shared intelligence model (Gemma 4 31B) to power multiple specialized architectural roles (Agents). Agents reason; Capabilities execute.

## 2. Canonical Execution Lifecycle
1. **Input**: User speaks or types a request.
2. **Omnix Executive**: Receives input.
3. **Goal / Context**: Synthesizes into a Goal against the WorldStateStore.
4. **Planning**: Planner Agent creates/revises a PlanRevision.
5. **Agent Selection**: Executive routes task steps to specialized agents.
6. **Requested Capability**: Agents request a specific capability.
7. **Policy Engine**: Deterministically authorizes or denies the capability.
8. **Capability Router**: Dispatches if authorized.
9. **Execution**: Capability executes OS APIs or specific side effects.
10. **Observation**: Perception layers observe the outcome and create a new WorldStateSnapshot.
11. **Verification**: Deterministic Verification Engine checks the outcome. (Falls back to reasoning if UNCERTAIN).
12. **PASS/FAIL**:
    - If PASS, continue.
    - If FAIL, route to Recovery (Wait, Retry, or Replan).
13. **World State / Task State Update**: State is recorded.
14. **Communication**: Omnix communicates status naturally.

*Not every request requires every component. Conversational requests may skip execution.*

## 3. Package Architecture
The canonical directory structure for `src/omnix/`:
```text
src/
└── omnix/
    ├── core/              # Executive, orchestration, task lifecycle, events
    ├── contracts/         # Typed data models, Agent/Capability interfaces, schemas
    ├── agents/            # Specialized reasoning (Planner, Browser, Filesystem, Communication)
    ├── capabilities/      # Windows, application, and OS implementations
    ├── perception/        # UIA, OCR, Vision, Scene Modeler, Grounding
    ├── verification/      # Verification Engine and deterministic providers
    ├── recovery/          # Failure classification and recovery strategies
    ├── safety/            # Policy Engine, permissions, confirmation workflows
    ├── memory/            # SQLite + FTS5 logic
    ├── voice/             # STT, TTS, VAD, Wake Word
    ├── communication/     # Character Bridge, expression, presentation state
    ├── providers/         # External boundaries (Ollama, Playwright, Chatterbox)
    ├── platform/          # Windows-specific wrappers
    ├── automation/        # Background scheduler and event monitoring
    ├── integrations/      # External plugins (GitHub, Email)
    ├── observability/     # Logging and metrics
    ├── configuration/     # Environment parsing
    └── ui/                # PySide6 components
```

## 4. Module Dependency Rules
- **Contracts**: Must not depend on implementations.
- **Agents**: Depend on contracts and Models, but not directly on platform-specific implementations.
- **Capabilities**: Implement specific tasks behind interfaces.
- **Executive**: Coordinates agents/contracts, not raw Windows APIs.
- **Providers**: Implementation details (Ollama, Playwright) must not leak into core logic.
- **Safety**: Enforcement via the Policy Engine must never be bypassed by Agents.
- **Verification**: Must not be bypassed.
- **Communication/Character**: Must not directly execute computer actions or own intelligence.
- **Platform**: Must not contain global reasoning logic.

## 5. Core Architectural Components

### Omnix Executive
The central orchestrator. Owns the current user goal and task lifecycle. Coordinates specialists, maintains orchestration authority, requests capabilities through routing, manages cancellation, and determines progression. The Executive does not directly call Win32 APIs, Playwright, or act as the LLM itself.

### Contracts Architecture
Data flows via Pydantic schemas (AgentRequest, AgentResult, CapabilityRequest, CapabilityResult). Registries (AgentRegistry, CapabilityRegistry) resolve dependencies. The CapabilityRouter sits between agents and execution.

### Policy Engine (Safety)
Safety is deterministic-first. The Policy Engine evaluates RiskCategories (LOW_RISK, SENSITIVE, DESTRUCTIVE, IRREVERSIBLE, PRIVACY_SENSITIVE, EXTERNAL_SIDE_EFFECT). It makes ALLOW, DENY, or REQUIRE_CONFIRMATION decisions. A Safety Agent can advise, but the Engine is the absolute authority. LLM output cannot override a deterministic DENY.

### Verification Engine
Verification is deterministic-first. ProcessVerifier, WindowVerifier, and FilesystemVerifier provide PASS/FAIL/UNCERTAIN results. If UNCERTAIN, the VerificationAgent reasons about evidence.

### WorldStateStore
The world state is NOT a global mutable singleton. It is a versioned store supporting WorldStateSnapshots and WorldStateRevisions. Observations trigger new revisions, allowing safe concurrent reads by agents.

### Context and Memory
Memory relies on SQLite and SQLite FTS5 for text search. Context retrieval feeds relevant history to the Model Manager. **There is no embedding model or vector database by default.**

### Goals and Planning
Planning uses an acyclic `PlanRevision`. The task's entire lifecycle may include multiple `PlanRevisions` due to replanning.

### Model Manager and Shared Intelligence
One single shared intelligence model (Gemma 4 31B via Ollama). The Model Manager handles prompt wrapping, context window limits, timeouts, and streaming. There are no separate "vision models" or "fast models" in the baseline. Agent != Model.

### Perception, Scene Model, and Grounding
Layered observation: OS APIs -> UI Automation -> OCR -> Gemma visual reasoning. `GroundingEngine` merges observations into a `SceneModel`.

## 6. Forbidden Architecture Patterns
- **No hardcoded user-command system**: e.g., `if command == "open chrome"`, `open_notepad()`.
- **No app-specific macro architecture**: e.g., Spotify-specific task engines.
- **No unrestricted LLM shell**: Do not expose a global bash/PowerShell escape hatch.
- **Safety Agent as sole enforcement**: Deterministic Policy Engine is mandatory.
- **LLM-only verification**: Verification must prioritize deterministic OS checks.
- **Multiple AI models**: Do not load one separate 31B model per agent.
- **Silently added Vector DB**: SQLite/FTS5 is the baseline.
- **Mutable global WorldState singleton**: Use versioned snapshots.
- **Multiple disconnected automation pipelines**: Everything routes through the Executive and Policy Engine.
- **Character renderer owning intelligence**: Godot is presentation only.
- **UI directly controlling computer**: Must route through canonical runtime.
- **Browser Agent bypassing policy**: Playwright must respect the Policy Engine.
- **Agents directly calling Win32**: They must request Capabilities.
- **Parallel provider-specific execution paths**: All interactions go through canonical interfaces.
