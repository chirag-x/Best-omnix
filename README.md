# Omnix

Omnix is a voice-first, fully autonomous, local-first AI assistant for Windows 11. It uses generic computer perception and dynamic planning to interact with any application naturally.

## Technology
- Python 3.13.15, `.venv`
- Ollama, Gemma 4 31B
- Local voice pipeline (DeepFilterNet, Silero VAD, openWakeWord, faster-whisper, Chatterbox-Turbo)
- PySide6/QML, Godot character
- Windows-native capabilities, layered perception
- SQLite, Playwright

See: `docs/TECHNOLOGY.md` for the authoritative complete technology stack.

## High-Level Architecture
- **Voice Input**: Captures and transcribes user intent locally.
- **Executive**: Orchestrates the task lifecycle.
- **Planning**: Generates dynamic acyclic `PlanRevisions`.
- **Policy Engine**: Deterministically enforces safety rules.
- **Capabilities**: Execute controlled OS functions.
- **Perception**: Layered OS, UIA, and Vision understanding.
- **Verification Engine**: Deterministically verifies action success.
- **Character**: Expressive Godot-based presentation of technical state.

## Documentation Map
Before contributing, you MUST read the following in order:

1. `README.md`: This file.
2. `AGENTS.md`: Strict rules for coding agents working on this repo.
3. `docs/PRD.md`: Product requirements and out-of-scope boundaries.
4. `docs/ARCHITECTURE.md`: Canonical system design and execution lifecycle.
5. `docs/TECHNOLOGY.md`: Approved technology stack and decisions.
6. `docs/DESIGN.md`: UX and character interaction principles.
7. `docs/RULES.md`: Absolute architectural laws.
8. `docs/TASKS.md`: Delivery roadmap.
9. `docs/DECISIONS.md`: Architecture Decision Records (ADRs).
10. `docs/MEMORY.md`: Current project status.
11. `docs/TEST_PLAN.md`: Testing philosophy and gates.
12. `docs/SECURITY.md`: Safety and Policy Engine boundaries.
13. `docs/phases/README.md`: Execution rules for phase implementation.

## Phase Specifications
Detailed specifications for all 21 delivery phases are located in `docs/phases/`.

## License
TBD
