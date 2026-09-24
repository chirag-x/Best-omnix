# Omnix Project Roadmap & Tasks (TASKS.md)

This document contains the master project roadmap. Each phase has a corresponding detailed specification in `docs/phases/`.

## Status Key
- **IN PROGRESS**: Currently being worked on.
- **NOT STARTED**: Pending future development.
- **COMPLETED**: Fully implemented, tested, and validated in runtime.

---

## Phase 0: Blueprint (IN PROGRESS)
**Goal**: Create and lock the architecture/documentation blueprint.
- **Key Tasks**: Write PRD, ARCHITECTURE, RULES, DESIGN, SECURITY, TEST_PLAN, and Phase 1-20 specs.
- **Constraints**: No implementation code. Ensure cross-document consistency.

## Phase 1: Runtime Foundation (NOT STARTED)
**Goal**: Build the runtime foundation without intelligence.
- **Key Tasks**: Setup logging, config parsing, dependency injection, event bus, core interfaces.
- **Technology Baseline**: Python 3.13.15, venv, pip, Pydantic, asyncio, logging/testing (See `TECHNOLOGY.md`).

## Phase 2: Omnix Executive (NOT STARTED)
**Goal**: Create the central Omnix Executive.
- **Key Tasks**: Implement the main orchestration loop, session management, and task state tracking.

## Phase 3: Agent & Capability Framework (NOT STARTED)
**Goal**: Establish agent and capability architecture.
- **Key Tasks**: Implement `AgentRegistry`, `CapabilityRegistry`, `CapabilityRouter`, and abstract base classes.

## Phase 4: Input/Output & Voice (NOT STARTED)
**Goal**: Create interaction foundation.
- **Key Tasks**: Text input gateway, basic STT/TTS abstractions, output gateway.
- **Technology Baseline**: sounddevice, DeepFilterNet, Silero VAD, openWakeWord, faster-whisper, Whisper, Chatterbox (See `TECHNOLOGY.md`).

## Phase 5: World State & Context (NOT STARTED)
**Goal**: Give Omnix coherent contextual/environment awareness.
- **Key Tasks**: Implement `WorldState` singleton, conversation history buffer, and entity resolution interfaces.

## Phase 6: Brain, Goals & Planning (NOT STARTED)
**Goal**: Create cognitive interpretation and dynamic planning.
- **Key Tasks**: LLM integration, goal parsing, task graph generation, dynamic replanning logic.

## Phase 7: Application & Window System (NOT STARTED)
**Goal**: Provide generic Windows control foundations.
- **Key Tasks**: Capabilities to enumerate, launch, focus, and close apps/windows via OS APIs.
- **Technology Baseline**: pywin32, ctypes, pywinauto, psutil, native Windows APIs (See `TECHNOLOGY.md`).

## Phase 8: Perception & Vision Grounding (NOT STARTED)
**Goal**: Give Omnix layered computer perception.
- **Key Tasks**: Screen capture, UI Automation (UIA) tree parsing, OCR integration, Scene Modeler.
- **Technology Baseline**: DXcam, OpenCV, RapidOCR, ONNX Runtime, UIA, Gemma vision (See `TECHNOLOGY.md`).

## Phase 9: Generic Desktop Interaction (NOT STARTED)
**Goal**: Combine perception + grounding + capabilities for unknown apps.
- **Key Tasks**: Coordinate-based clicking, typing, scrolling linked to semantic UI elements.

## Phase 10: Browser Intelligence (NOT STARTED)
**Goal**: Create a generic Browser Agent.
- **Key Tasks**: DOM parsing, accessibility tree analysis, web navigation capabilities.
- **Technology Baseline**: Playwright (See `TECHNOLOGY.md`).

## Phase 11: Filesystem Intelligence (NOT STARTED)
**Goal**: Create generic filesystem intelligence.
- **Key Tasks**: Safe file read/write, search, metadata inspection capabilities.

## Phase 12: Verification Engine (NOT STARTED)
**Goal**: Make verification a formal subsystem.
- **Key Tasks**: Pre/post condition checkers for capabilities, visual verification via Scene Modeler.

## Phase 13: Recovery & Replanning (NOT STARTED)
**Goal**: Handle real-world failures intelligently.
- **Key Tasks**: Failure diagnosis, bounded retry logic, fallback to alternative capabilities.

## Phase 14: Memory (NOT STARTED)
**Goal**: Design purposeful Omnix memory.
- **Key Tasks**: Semantic/vector storage for long-term user preferences and episodic task history.
- **Technology Baseline**: SQLite + FTS5 (See `TECHNOLOGY.md`).

## Phase 15: Communication & Personality (NOT STARTED)
**Goal**: Make Omnix communicate naturally.
- **Key Tasks**: Implement Communication Agent to translate technical states into natural language.
- **Technology Baseline**: Chatterbox, Godot character integration, Rhubarb, PySide6/QML (See `TECHNOLOGY.md`).

## Phase 16: Safety & Permissions (NOT STARTED)
**Goal**: Implement policy and permission architecture.
- **Key Tasks**: Risk classification for capabilities, user confirmation prompts, boundary enforcement.

## Phase 17: Multi-Agent Collaboration (NOT STARTED)
**Goal**: Enable dynamic collaboration between specialists.
- **Key Tasks**: Agent delegation protocols via the Executive.

## Phase 18: Complex Long-Running Tasks (NOT STARTED)
**Goal**: Support long, multi-step goals.
- **Key Tasks**: Task persistence, pause/resume, checkpointing.

## Phase 19: Background Automation & Events (NOT STARTED)
**Goal**: Add asynchronous/event-driven behavior.
- **Key Tasks**: Cron scheduler, trigger listeners, background task execution.

## Phase 20: External Integrations (NOT STARTED)
**Goal**: Extend Omnix beyond local desktop operation.
- **Key Tasks**: Plugin architecture for APIs (Email, Calendar, GitHub, etc.).
