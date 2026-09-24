# Omnix Technology Stack and Technical Platform

**AUTHORITY STATEMENT:**
`TECHNOLOGY.md` is the authoritative source of truth for approved technology, runtime, model, framework, engine, tool, library, storage, UI, voice, character, perception, testing and packaging decisions in Omnix. Other documentation may reference these decisions but should not maintain independent conflicting technology lists. If a future technology decision changes:
1. Update `TECHNOLOGY.md`.
2. Record the architectural reason in `DECISIONS.md`.
3. Update affected phase documents.
4. Update `ARCHITECTURE.md` if architectural behavior changes.
5. Update `MEMORY.md` if the project state changes.

## Locked Foundational Technologies

### OPERATING SYSTEM
- **Primary target:** Windows 11
- Omnix is initially a Windows-first desktop AI system. The architecture may eventually allow additional platforms, but Windows is the primary implementation platform for current phases.

### PROGRAMMING LANGUAGE
- **Python 3.13.15** (LOCKED)
- All primary Omnix Python runtime development should target Python 3.13.15. Do not silently downgrade Python. If a dependency is incompatible with Python 3.13.15, document the incompatibility, evaluate alternatives, and do not silently change the project Python version.

### PYTHON ENVIRONMENT
- Use standard Python `venv`.
- Expected environment: `.venv`
- Do NOT replace this with uv, Conda, Poetry, or Pipenv unless the architecture is deliberately changed later through an ADR.

### PACKAGE MANAGEMENT
- Use `pip` with project dependency metadata and pinned/reproducible dependency records where appropriate.

## Main AI System
- **AI runtime:** Ollama
- **Primary intelligence model:** Gemma 4 31B-class dense model
- **Current Ollama target:** `gemma4:31b`
- This model provides intelligence for ALL major Omnix cognitive roles. Do NOT design Omnix around separate LLMs for Brain, Planner, Recovery, etc.
- **IMPORTANT:** Agent != model. An agent is an architectural role (responsibility, context, permissions). Gemma is the shared intelligence engine. Do NOT load one independent 31B model per agent.

## Model Manager
- A Model Manager / Brain Provider abstraction must isolate Omnix Core from Ollama-specific implementation details.
- **Responsibilities:** connect to Ollama, manage Gemma model availability, model health, context management, inference requests, cancellation, streaming, timeout handling, resource awareness, model unload/load policy, error reporting.

## Voice Input Architecture
- **Microphone capture:** `sounddevice` / PortAudio
- **Noise suppression:** DeepFilterNet
- **Voice activity detection:** Silero VAD
- **Wake word:** openWakeWord (Wake phrase: "Hey Omnix")
- **Speech-to-text engine:** faster-whisper
- **Primary STT model:** Whisper large-v3-turbo

## Wake Word System
- **Primary wake word technology:** openWakeWord
- Default wake phrase: "Hey Omnix". Must remain behind a `WakeWordProvider` abstraction. Requires licensing review before release.

## Speech-to-Text
- **Primary engine:** faster-whisper (Whisper large-v3-turbo model)
- Chosen for strong transcription quality, local inference, and no paid API required. Must remain behind a `SpeechRecognitionProvider` abstraction.

## Voice Activity Detection
- **Primary:** Silero VAD
- Responsibilities: detect start/end of speech, avoid transcribing silence, assist barge-in, improve latency. VAD must not decide user intent.

## Noise Suppression
- **Primary:** DeepFilterNet
- Purpose: Improve microphone input. Must be configurable as some microphones already perform strong noise suppression.

## Text-to-Speech
- **Primary target:** Chatterbox-Turbo
- Purpose: Natural local expressive Omnix voice. Must remain behind a TTS provider interface. Python 3.13.15 compatibility must be validated.

## Omnix Voice Identity
- Omnix should have its own original voice identity (natural, warm, clear, expressive). Execution logs must not be directly spoken to users.

## Omnix Character / Avatar
- **Character runtime:** Godot 4.x
- Purpose: Render the live Omnix character/avatar independently of the Python intelligence runtime. The character has ZERO independent task intelligence; it only reflects Omnix state.

## Character Creation
- **Primary character creation tool:** Blender
- Pipeline: Concept -> Blender -> 3D Model -> Rig -> Facial blend shapes -> Animations -> Export -> Godot.
- Preferred format: `glTF 2.0`.

## Character States
- Planned states: IDLE, LISTENING, UNDERSTANDING, THINKING, WORKING, TALKING, CURIOUS, HAPPY, CONCERNED, CONFUSED, SUCCESS, ERROR, SLEEPING, WAKING.
- These are presentation states mapped by the Presence/Character Controller.

## Facial Animation
- Use blend shapes / morph targets.
- Character rendering belongs in Godot, authoring in Blender, intelligence in Python.

## Lip Sync
- **Primary planned system:** Rhubarb Lip Sync
- Converts generated speech audio into mouth-shape/viseme timing for Godot Character.

## Desktop UI
- **Primary application UI:** PySide6
- **Primary rich UI layer:** Qt Quick / QML
- Use for settings, tray, status, logs. Godot should NOT replace the entire application UI.

## Character Bridge
- Future process boundary between Python Omnix and Godot. IPC mechanisms (local WebSocket, named pipe) will be typed/versioned.

## Screen Capture
- **Primary Windows capture technology:** DXcam
- Purpose: fast Windows screen capture, efficient frame access, NumPy/OpenCV integration. Do not continuously send every full screen frame to Gemma.

## Image Processing
- **Use:** OpenCV, NumPy, Pillow
- Deterministic tools for crops, resizing, change detection. Do not use Gemma for tasks basic image processing can solve.

## Windows Structured UI Perception
- **Primary technology:** Microsoft Windows UI Automation
- **Python interface:** `pywinauto` (potential lower-level Win32 access via `pywin32`, `ctypes`).
- Use structured information where available before falling back to OCR/Vision.

## OCR
- **Primary OCR:** RapidOCR
- **Inference:** ONNX Runtime
- Reads visible interface text when UIA is missing. OCR is a perception provider, it does not independently decide actions.

## Gemma Visual Reasoning
- The SAME Gemma 4 31B model provides high-level visual reasoning. Used when lower-cost structured perception cannot sufficiently understand the interface. Do NOT create a second vision LLM by default.

## Grounding Engine
- Converts semantic references ("the blue button") into actionable target candidates using World State, UIA, OCR, Vision, etc.

## Windows Control
- **Primary underlying technologies:** `pywin32`, `ctypes`, Windows APIs, Microsoft UI Automation, SendInput, `psutil`, `subprocess`, `pathlib`.
- All must remain behind Omnix capability interfaces.

## Keyboard and Mouse
- **Primary low-level architecture:** Windows native SendInput / appropriate Win32 input APIs. Do not make PyAutoGUI the central intelligence architecture.

## Application Discovery
- Application discovery should be generic (running processes, active windows, Start Menu). DO NOT create app-specific launch macros.

## Window Management
- Use Windows APIs/UI Automation through generic capabilities (enumerate, focus, restore, move, resize).

## Browser Technology
- **Primary:** Playwright Python
- Structured browser control. Browser capabilities run Playwright. Fallback is UIA -> OCR -> Vision. Do NOT build Chrome-specific hardcoded intelligence.

## Filesystem
- **Use:** `pathlib`, `os`, `shutil`, Windows APIs. Kept behind capability interfaces.

## Process and System State
- **Primary:** `psutil` plus Windows-native APIs where required.

## Clipboard
- Use native Windows clipboard APIs / appropriate `pywin32` abstraction.

## Memory Storage
- **Primary database:** SQLite
- **Local searchable text memory:** SQLite FTS5
- Do NOT add a separate embedding AI model by default. Gemma is the only intelligence model. Memory retrieval combines FTS, keywords, metadata, and timestamps.

## Task Graph / Planning
- Use custom Omnix task/plan model. NetworkX may be used if it adds clear value, but it is not the architecture.

## Agent Framework
- Use custom Omnix agent framework. Do NOT make LangChain, LangGraph, CrewAI, or AutoGen foundational dependencies.

## Data Contracts
- **Primary:** Pydantic v2. Use typed data models across subsystem boundaries.

## Configuration
- **Use:** `pydantic-settings`.

## Concurrency
- **Primary:** `asyncio` for orchestration, events, etc.
- **Heavy workers:** `multiprocessing` (e.g., STT, TTS, Vision).

## HTTP / External Communication
- **Primary Python HTTP client:** `httpx` (behind integration abstractions).

## Event System
- Custom in-process `asyncio` event system. Do not introduce Kafka, RabbitMQ, etc.

## Scheduling / Automation
- Automation architecture remains custom to Omnix. `APScheduler` may be used later if appropriate.

## Logging
- **Use:** Python standard `logging`, `structlog` (for structured events), `Rich` (for readable CLI).

## Testing
- **Primary:** `pytest`, `pytest-asyncio`, `pytest-cov`, `Hypothesis`, Playwright/pytest integration. Testing outcomes over function invocation.

## Code Quality
- **Use:** `Ruff` (formatting/linting), `Pyright` (static type analysis).

## Security Tooling
- **Use:** `pip-audit`, `Bandit`.

## Secret Storage
- `.env` locally. Prefer Windows Credential Manager / DPAPI for production. No secrets in Git.

## Packaging
- **Primary target:** Windows executable
- **Preferred:** Nuitka (with `pyside6-deploy`).
- **Installer target:** Inno Setup.

## Version Control
- **Use:** Git, GitHub.

## Provider Abstraction Rule
- Technology selection must NOT create hard coupling. Use interfaces (`ModelProvider`, `TTSProvider`, `SpeechRecognitionProvider`, `ScreenCaptureProvider`, `OCRProvider`).

## Technology Status Classification
### LOCKED
- Windows 11 primary
- Python 3.13.15
- standard venv / .venv
- pip
- Ollama
- Gemma 4 31B-class model
- one shared main intelligence model architecture
- custom Omnix agent framework
- SQLite
- goal-driven / non-hardcoded architecture

### APPROVED BASELINE
- faster-whisper, Whisper large-v3-turbo, Silero VAD, openWakeWord, DeepFilterNet
- PySide6, Qt Quick/QML, Godot 4, Blender, Rhubarb lip-sync baseline
- DXcam, OpenCV, Windows UI Automation, pywinauto, RapidOCR, ONNX Runtime, Playwright
- pywin32, psutil, Pydantic v2, asyncio, pytest, Ruff, Pyright, Nuitka, Inno Setup
- Windows native capability architecture, provider abstraction requirement

### VALIDATION REQUIRED
- Chatterbox-Turbo under exact Python 3.13.15
- Rhubarb integration
- Python <-> Godot IPC method
- exact character asset format, packaging composition, GPU allocation strategy, latency targets

### FUTURE / OPTIONAL
- semantic vector database, separate embedding model, alternate platforms, cloud model providers, alternative TTS, additional external integrations.

## Resource Architecture
- Deterministic capability > Structured perception > Gemma. Do not use Gemma for tasks determinism solves.

## GPU / Resource Management
- Resource Manager subsystem will understand and govern GPU/memory load state across AI subsystems.

## Complete Technology Flow
```text
                         USER
                           │
               ┌───────────┴────────────┐
               │                        │
             VOICE                    TEXT/UI
               │                        │
          sounddevice                   │
               ↓                        │
        DeepFilterNet                   │
               ↓                        │
          Silero VAD                    │
               ↓                        │
       openWakeWord                     │
               ↓                        │
       faster-whisper                   │
               ↓                        │
          Whisper STT                   │
               └───────────┬────────────┘
                           ↓
                     INPUT GATEWAY
                           ↓
                    OMNIX EXECUTIVE
                           │
         ┌─────────────────┼─────────────────┐
         ▼                 ▼                 ▼
      Context           World State        Task
         │                 │                 │
         └─────────────────┼─────────────────┘
                           ▼
                     MODEL MANAGER
                           ↓
                         OLLAMA
                           ↓
                     GEMMA 4 31B
                           │
            ┌──────────────┼──────────────┐
            ▼              ▼              ▼
         Brain          Planner         Vision
            │              │              │
         Recovery       Research     Communication
            │
            ▼
                     AGENT SYSTEM
                           ↓
                 CAPABILITY ROUTER
                           ↓
      ┌──────────┬─────────┼────────┬──────────┐
      ▼          ▼         ▼        ▼          ▼
 Application   Window   Desktop   Browser     Files
      │          │         │        │          │
      └──────────┴─────────┼────────┴──────────┘
                           ↓
                         WINDOWS
                           ↓
                       OBSERVATION
                           │
       ┌───────────────────┼──────────────────┐
       ▼                   ▼                  ▼
 Windows UIA             OCR               DXcam
       │                   │                  │
       └───────────────────┼──────────────────┘
                           ↓
                       Grounding
                           ↓
                      Verification
                           ↓
                    Success / Recovery
                           ↓
                    Communication
                           ↓
                     Chatterbox
                           ↓
                    Speech Audio
                      ┌────┴────┐
                      ▼         ▼
                   Speaker    Rhubarb
                                ↓
                         Character Bridge
                                ↓
                             Godot
                                ↓
                       Omnix Character
```

## Document Technology Principles
1. Use free/local technology whenever practical.
2. Prefer deterministic technology for deterministic tasks.
3. Gemma is intelligence, not a replacement for OS APIs.
4. Agents reason; capabilities execute.
5. Technologies remain behind provider/interface boundaries.
6. No one library owns Omnix architecture.
7. Avoid unnecessary frameworks, cloud dependency, and paid API dependency.
8. Maintain Python 3.13.15 unless an explicit architectural decision changes it.
9. Use `.venv`. Keep technology choices replaceable.
10. Evaluate licenses before redistribution. Evaluate Python 3.13 compatibility.
11. Measure real-world latency.
12. Prefer structured computer state over screenshot AI. Use Gemma only where intelligence adds value.
13. User-facing technology must serve the canonical Omnix execution architecture.
