# Omnix System Architecture

## Architecture Goals
- Provide a robust, generic computer-use foundation.
- Eliminate hardcoded, brittle automation scripts.
- Ensure all actions are planned dynamically and verified post-execution.
- Keep agent logic (reasoning) strictly separated from capability execution (actions).

## Architectural Principles
- **One Canonical Executive**: All inputs converge to the Omnix Executive.
- **Specialized Domains**: Agents own domains (Browser, Desktop), not workflows.
- **Verification First**: Action without observation is considered unsafe.
- **Fail Gracefully**: Built-in recovery from the ground up.

## System Context
User interacts via Voice or Text -> Input Gateway -> Omnix Executive -> Planner -> Capability Router -> OS/Applications.

## Layered Architecture
1. **Input/Output Layer**: Voice, text, UI.
2. **Cognitive Layer**: Omnix Executive, Planner, Brain.
3. **Specialist Layer**: Browser Agent, Desktop Agent, Vision Agent.
4. **Execution Layer**: Capability Router, Safety Boundary, Controlled Capabilities.
5. **Perception Layer**: Scene Modeler, UIA, OCR, OS Hooks.

## Omnix Core / Executive
The central orchestrator. It receives abstract goals, maintains the session, and triggers planning.

## Request / Goal Lifecycle
1. User provides input.
2. Input parsed into Goal Representation.
3. Executive delegates to Planner.
4. Planner selects Agents.
5. Agents select Capabilities.
6. Execution and Verification.
7. Executive communicates outcome.

## Goal Representation
An abstract, machine-readable format describing the desired end state and constraints, rather than the steps to get there.

## Task Representation
A discrete unit of work resulting from the planning phase.

## Task Graph
A DAG (Directed Acyclic Graph) of tasks. Supports parallel execution and dependencies.

## Planning Architecture
Dynamic generation of Task Graphs based on Goal, World State, and available Agents.

## Agent Architecture
Agents are pure reasoning modules. They take a sub-goal and World State, and return a sub-plan or capability request.

## Agent Interface Concept
```python
class Agent:
    def can_handle(goal, state) -> float: ...
    def propose_plan(goal, state) -> TaskGraph: ...
```

## Agent Lifecycle
Registered at startup. Stateless per request, relying on World State for context.

## Agent Metadata
Self-describing JSON/YAML detailing an agent's domain expertise.

## Agent Registry
Central registry queried by the Executive/Planner.

## Agent Discovery
Dynamic lookup based on goal constraints.

## Agent Selection
Based on confidence scores returned by `can_handle`.

## Agent Communication
Message passing via the Executive. No P2P agent swarms.

## Capability Architecture
Capabilities are pure side-effecting functions wrapped in a standardized interface.

## Capability Interface Concept
```python
class Capability:
    def execute(params) -> Result: ...
    def required_permissions() -> list: ...
```

## Capability Metadata
Describes inputs, outputs, and safety level (e.g., DESTRUCTIVE).

## Capability Registry
Stores all available actions.

## Capability Discovery
Agents query the registry for capabilities matching their needs.

## Capability Router
Routes execution requests through the Safety Boundary before invocation.

## Capability Safety Classification
- SAFE (read-only)
- SENSITIVE (privacy)
- DESTRUCTIVE (modify/delete)

## World State
A unified, real-time representation of the OS, apps, and UI.

## Context Engine
Maintains conversation history and pronoun resolution (e.g., "that window").

## Brain / Reasoning
The core LLM router/wrapper for interpreting goals.

## Model Manager
Abstracts underlying AI providers. Technology baseline -> Ollama + Gemma 4 31B. See `TECHNOLOGY.md`.

## Model Routing
Routes requests to fast/cheap models or slow/smart models based on task complexity.

## Input Architecture
Handles multimodal streams (audio, text, image).

## Voice Architecture
VAD -> STT -> Input Gateway -> Executive. Barge-in interrupts current execution. Technology baseline -> DeepFilterNet, Silero VAD, openWakeWord, faster-whisper, Whisper large-v3-turbo, Chatterbox. See `TECHNOLOGY.md`.

## Output Architecture
Executive -> Communication Agent -> TTS -> Audio Out.

## Communication Architecture
Separates raw technical results from natural language phrasing.

## Personality / Expression
Applies tone (helpful, concise, unsure) to the Output.

## Perception Architecture
Aggregates state from multiple sources. Technology baseline -> DXcam, OpenCV, UIA, pywinauto, RapidOCR, Gemma visual reasoning. See `TECHNOLOGY.md`.

## UI Automation
Reads OS accessibility trees (UIA on Windows).

## OCR
Extracts text from screenshots as a fallback.

## Vision
Uses VLM to understand semantics of the screen.

## Browser DOM / Accessibility
Specific deep perception for web pages. Technology baseline -> Playwright. See `TECHNOLOGY.md`.

## Scene Model
The fused result of UIA, OCR, and Vision. A single source of truth for grounding.

## Grounding
Mapping a semantic target (e.g., "Submit button") to exact screen coordinates or UI elements.

## Application Agent
Reasons about app lifecycle (is it installed? is it running?).

## Window Agent
Reasons about window z-order, focus, and bounds.

## Desktop Agent
Reasons about generic mouse/keyboard tasks.

## Browser Agent
Reasons about web navigation and DOM interaction.

## Filesystem Agent
Reasons about file paths, contents, and metadata.

## System Agent
Reasons about OS-level settings (volume, network).

## Research Agent
Reasons about gathering information (web search, reading docs).

## Verification Agent
Specialist in confirming whether an action achieved its expected state.

## Recovery Agent
Specialist in proposing alternate plans when a task fails.

## Memory Agent
Specialist in storing and retrieving episodic memory.

## Safety Agent
Enforces policies and requests user confirmation.

## Automation Agent
Handles cron/scheduled goals.

## Integration Agent
Reasons about external APIs (e.g., sending an email via SMTP).

## Event System
Pub/Sub bus for internal system state changes.

## Scheduler
Manages background and recurring tasks.

## Background Tasks
Task graphs executing without blocking the main interaction loop.

## Resource Manager
Throttles LLM calls and manages memory usage.

## Observability
Telemetry for all Agent and Capability boundaries.

## Logging
Structured JSON logging for debugging.

## Tracing
OpenTelemetry tracing for request lifecycles.

## Error Architecture
Typed errors (Recoverable vs Fatal).

## Cancellation
Task graphs can be aborted mid-execution (e.g., user barge-in).

## Interruption
Pauses execution to ask the user a clarifying question.

## Concurrency
Task graphs support parallel node execution.

## Task Persistence
Task state is saved, allowing resume after reboot/crash.

## Safety Boundaries
Capability Router checks all requests against Safety Agent policies.

## Trust Boundaries
LLM output is treated as untrusted and must be validated.

## Data Flow
Goal -> Planner -> Agent -> Capability -> Result -> Verification.

## Canonical Execution Lifecycle
1. INGEST
2. PLAN
3. EXECUTE
4. VERIFY
5. RESPOND

## Example Simple Goal Flow
"Type hello" -> Desktop Agent -> TypeCapability -> Verify Text -> Success.

## Example Multi-Step Goal Flow
"Open notepad and type hello" -> App Agent (launch) -> Verify -> Desktop Agent (type) -> Verify -> Success.

## Example Perception Goal Flow
"What is on screen?" -> Vision Agent -> Scene Modeler -> Comm Agent -> Speak.

## Example Failure / Recovery Flow
Click(X,Y) -> Verify(Did window change?) -> No -> Recovery Agent -> Propose Vision fallback -> Re-execute -> Verify.

## Example Contextual Follow-Up Flow
"Close it" -> Context Engine resolves "it" to the last focused window -> Window Agent (close) -> Verify.

## Example Unknown Application Flow
Goal involves unknown app -> Desktop Agent uses Vision to locate elements -> Generic click/type capabilities used.

## Folder Architecture Proposal
```
src/
  core/         # Executive, Planner, State
  agents/       # Specialists
  capabilities/ # Action Primitives
  perception/   # Scene Modeler, Vision
  communication/# Voice, NLP out
  safety/       # Policies
```

## Module Dependency Rules
- Agents depend on Core interfaces.
- Capabilities depend on nothing but OS/Libs.
- Core depends on Registries.

## Extensibility Rules
New agents are added by dropping a module into `src/agents/` and registering. No Core changes allowed.

## Forbidden Architecture Patterns
- Hardcoded string matching for intents.
- LLM generating raw shell scripts executed directly.
- Capability execution bypassing the Safety Router.

## Architectural Invariants
- The Executive owns the goal.
- Actions require Verification.
- Recovery is preferred over raw failure.
