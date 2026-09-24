import os

base_dir = "e:/Best/Omnix"

def update_readme():
    path = os.path.join(base_dir, "README.md")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    if "## Technology" not in content:
        tech_section = """## Technology
- Python 3.13.15, `.venv`
- Ollama, Gemma 4 31B
- Local voice pipeline (DeepFilterNet, Silero VAD, openWakeWord, faster-whisper, Chatterbox-Turbo)
- PySide6/QML, Godot character
- Windows-native capabilities, layered perception
- SQLite, Playwright

See: `docs/TECHNOLOGY.md` for the authoritative complete technology stack.

"""
        content = content.replace("## High-Level Architecture", tech_section + "## High-Level Architecture")
    
    if "TECHNOLOGY.md" not in content:
        content = content.replace("- `docs/ARCHITECTURE.md`: System design", "- `docs/ARCHITECTURE.md`: System design\n- `docs/TECHNOLOGY.md`: Technology stack and decisions")
    
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

def update_agents():
    path = os.path.join(base_dir, "AGENTS.md")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    if "TECHNOLOGY.md" not in content:
        content = content.replace("- `docs/ARCHITECTURE.md`", "- `docs/ARCHITECTURE.md`\n- `docs/TECHNOLOGY.md`")
        
        tech_rule = """
- **Before adding or replacing a technology dependency, read `TECHNOLOGY.md` and `DECISIONS.md`.**
- Do not silently substitute approved technology. If implementation testing shows an approved technology is unsuitable, report the evidence first. Then update the relevant ADR/documentation before changing architecture.
"""
        content = content.replace("## CRITICAL DIRECTIVE", tech_rule + "\n## CRITICAL DIRECTIVE")
        
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

def update_prd():
    path = os.path.join(base_dir, "docs/PRD.md")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    if "## Technology Constraints" not in content:
        tech_section = """## Technology Constraints / Platform Requirements
- Windows 11 initial target
- Python 3.13.15 baseline
- Local/free-first operation
- Ollama/Gemma baseline intelligence
- Voice-first operation
- Animated character/presence
- Local perception/control
- Provider replaceability

Reference `TECHNOLOGY.md` for detailed implementation technology decisions.

"""
        content = content.replace("## Non-Functional Requirements", tech_section + "## Non-Functional Requirements")
    
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

def update_architecture():
    path = os.path.join(base_dir, "docs/ARCHITECTURE.md")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
        
    if "See TECHNOLOGY.md" not in content and "See `TECHNOLOGY.md`" not in content:
        content = content.replace("## Model Manager\nAbstracts underlying AI providers (Gemini, Claude, OpenAI).", "## Model Manager\nAbstracts underlying AI providers. Technology baseline -> Ollama + Gemma 4 31B. See `TECHNOLOGY.md`.")
        content = content.replace("## Voice Architecture\nVAD -> STT -> Input Gateway -> Executive. Barge-in interrupts current execution.", "## Voice Architecture\nVAD -> STT -> Input Gateway -> Executive. Barge-in interrupts current execution. Technology baseline -> DeepFilterNet, Silero VAD, openWakeWord, faster-whisper, Whisper large-v3-turbo, Chatterbox. See `TECHNOLOGY.md`.")
        content = content.replace("## Perception Architecture\nAggregates state from multiple sources.", "## Perception Architecture\nAggregates state from multiple sources. Technology baseline -> DXcam, OpenCV, UIA, pywinauto, RapidOCR, Gemma visual reasoning. See `TECHNOLOGY.md`.")
        content = content.replace("## Browser DOM / Accessibility\nSpecific deep perception for web pages.", "## Browser DOM / Accessibility\nSpecific deep perception for web pages. Technology baseline -> Playwright. See `TECHNOLOGY.md`.")
    
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

def update_design():
    path = os.path.join(base_dir, "docs/DESIGN.md")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
        
    if "TECHNOLOGY.md" not in content:
        content = content.replace("## Voice Experience\nVoice interaction is the primary modality.", "## Voice Experience\nVoice interaction is the primary modality. Implemented through approved TTS/STT stack in `TECHNOLOGY.md`.")
        content = content.replace("## Visual Interface\nThe primary UI is transparent/overlay based.", "## Visual Interface\nThe primary UI is transparent/overlay based. Application UI: PySide6/QML. Character: Godot runtime + Blender-created character (Lip sync: Rhubarb planned). See `TECHNOLOGY.md`.")
    
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

def update_rules():
    path = os.path.join(base_dir, "docs/RULES.md")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
        
    if "## Technology Governance" not in content:
        tech_rules = """
## Technology Governance
- Read `TECHNOLOGY.md` before adding a dependency.
- Do not replace approved technologies silently.
- Do not add another LLM without explicit architecture approval.
- Do not add another agent framework.
- Do not replace `.venv` with another environment manager.
- Do not downgrade Python (target 3.13.15).
- Do not introduce paid/cloud dependencies into the baseline without explicit approval.
- Do not couple agents directly to provider-specific APIs; keep implementations behind interfaces.
- Check licenses before redistribution.
- Check Python 3.13.15 compatibility.
- Record permanent technology changes in `DECISIONS.md`.
- Update `TECHNOLOGY.md` when approved technology changes.
"""
        content = content + "\n" + tech_rules
    
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

def update_tasks():
    path = os.path.join(base_dir, "docs/TASKS.md")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
        
    if "Technology Baseline:" not in content:
        content = content.replace("## Phase 1: Runtime Foundation (NOT STARTED)\n**Goal**: Build the runtime foundation without intelligence.\n- **Key Tasks**: Setup logging, config parsing, dependency injection, event bus, core interfaces.", "## Phase 1: Runtime Foundation (NOT STARTED)\n**Goal**: Build the runtime foundation without intelligence.\n- **Key Tasks**: Setup logging, config parsing, dependency injection, event bus, core interfaces.\n- **Technology Baseline**: Python 3.13.15, venv, pip, Pydantic, asyncio, logging/testing (See `TECHNOLOGY.md`).")
        content = content.replace("## Phase 4: Input/Output & Voice (NOT STARTED)\n**Goal**: Create interaction foundation.\n- **Key Tasks**: Text input gateway, basic STT/TTS abstractions, output gateway.", "## Phase 4: Input/Output & Voice (NOT STARTED)\n**Goal**: Create interaction foundation.\n- **Key Tasks**: Text input gateway, basic STT/TTS abstractions, output gateway.\n- **Technology Baseline**: sounddevice, DeepFilterNet, Silero VAD, openWakeWord, faster-whisper, Whisper, Chatterbox (See `TECHNOLOGY.md`).")
        content = content.replace("## Phase 7: Application & Window System (NOT STARTED)\n**Goal**: Provide generic Windows control foundations.\n- **Key Tasks**: Capabilities to enumerate, launch, focus, and close apps/windows via OS APIs.", "## Phase 7: Application & Window System (NOT STARTED)\n**Goal**: Provide generic Windows control foundations.\n- **Key Tasks**: Capabilities to enumerate, launch, focus, and close apps/windows via OS APIs.\n- **Technology Baseline**: pywin32, ctypes, pywinauto, psutil, native Windows APIs (See `TECHNOLOGY.md`).")
        content = content.replace("## Phase 8: Perception & Vision Grounding (NOT STARTED)\n**Goal**: Give Omnix layered computer perception.\n- **Key Tasks**: Screen capture, UI Automation (UIA) tree parsing, OCR integration, Scene Modeler.", "## Phase 8: Perception & Vision Grounding (NOT STARTED)\n**Goal**: Give Omnix layered computer perception.\n- **Key Tasks**: Screen capture, UI Automation (UIA) tree parsing, OCR integration, Scene Modeler.\n- **Technology Baseline**: DXcam, OpenCV, RapidOCR, ONNX Runtime, UIA, Gemma vision (See `TECHNOLOGY.md`).")
        content = content.replace("## Phase 10: Browser Intelligence (NOT STARTED)\n**Goal**: Create a generic Browser Agent.\n- **Key Tasks**: DOM parsing, accessibility tree analysis, web navigation capabilities.", "## Phase 10: Browser Intelligence (NOT STARTED)\n**Goal**: Create a generic Browser Agent.\n- **Key Tasks**: DOM parsing, accessibility tree analysis, web navigation capabilities.\n- **Technology Baseline**: Playwright (See `TECHNOLOGY.md`).")
        content = content.replace("## Phase 14: Memory (NOT STARTED)\n**Goal**: Design purposeful Omnix memory.\n- **Key Tasks**: Semantic/vector storage for long-term user preferences and episodic task history.", "## Phase 14: Memory (NOT STARTED)\n**Goal**: Design purposeful Omnix memory.\n- **Key Tasks**: Semantic/vector storage for long-term user preferences and episodic task history.\n- **Technology Baseline**: SQLite + FTS5 (See `TECHNOLOGY.md`).")
        content = content.replace("## Phase 15: Communication & Personality (NOT STARTED)\n**Goal**: Make Omnix communicate naturally.\n- **Key Tasks**: Implement Communication Agent to translate technical states into natural language.", "## Phase 15: Communication & Personality (NOT STARTED)\n**Goal**: Make Omnix communicate naturally.\n- **Key Tasks**: Implement Communication Agent to translate technical states into natural language.\n- **Technology Baseline**: Chatterbox, Godot character integration, Rhubarb, PySide6/QML (See `TECHNOLOGY.md`).")
        
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

def update_decisions():
    path = os.path.join(base_dir, "docs/DECISIONS.md")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
        
    if "ADR-016: Python 3.13.15 Baseline" not in content:
        adrs = """
## ADR-016: Python 3.13.15 Baseline
- **Context**: Need a stable, modern language baseline.
- **Decision**: Python 3.13.15 is the required baseline. Standard `venv` and `pip` are used.
- **Reason**: Balances modern features with wide library support.
- **Alternatives considered**: Python 3.12, Conda, uv.
- **Consequences**: Some native extensions might require verification on 3.13.15.
- **Status**: ACCEPTED

## ADR-017: Local AI Runtime
- **Context**: Omnix requires a local, free-first intelligence engine.
- **Decision**: Ollama will host the local AI runtime, running Gemma 4 31B.
- **Reason**: Provides a good balance of performance, local execution, and reasoning capability.
- **Alternatives considered**: vLLM, llama.cpp directly, cloud providers (OpenAI/Anthropic).
- **Consequences**: Heavy GPU requirements for end-users.
- **Status**: ACCEPTED

## ADR-018: Shared Intelligence Model
- **Context**: Multiple agents need to reason (Vision, Planner, Brain).
- **Decision**: Use a single shared intelligence model (Gemma 4 31B) for all cognitive roles. Agent != Model.
- **Reason**: Loading multiple 31B models is infeasible on standard consumer hardware.
- **Alternatives considered**: Smaller specialized models per agent.
- **Consequences**: The single model must be adept at various tasks via prompting/fine-tuning.
- **Status**: ACCEPTED

## ADR-019: Custom Omnix Agent Framework
- **Context**: Agents need to coordinate and execute tasks dynamically.
- **Decision**: Build a custom Omnix agent framework.
- **Reason**: Existing frameworks (LangChain, AutoGen) are too bloated or introduce conflicting architectural paradigms.
- **Alternatives considered**: LangChain, CrewAI.
- **Consequences**: Higher initial development effort, but absolute control over the execution lifecycle.
- **Status**: ACCEPTED

## ADR-020: Voice and STT Stack
- **Context**: Need fast, local speech recognition.
- **Decision**: Use faster-whisper (Whisper large-v3-turbo), DeepFilterNet (noise reduction), Silero VAD, openWakeWord.
- **Reason**: Best-in-class local performance without API costs.
- **Alternatives considered**: Cloud STT, standard Whisper.
- **Consequences**: Requires significant local compute for real-time transcription.
- **Status**: ACCEPTED

## ADR-021: Character and TTS
- **Context**: Omnix needs a presence and voice.
- **Decision**: Use Chatterbox-Turbo for TTS, Godot 4 for character rendering, Blender for authoring, Rhubarb for lip sync, and PySide6 for application UI.
- **Reason**: Separates heavy 3D rendering (Godot) from standard application UI (PySide6) and Python intelligence.
- **Alternatives considered**: Full UI in Godot, PyGame, Unity.
- **Consequences**: Requires IPC between Python and Godot.
- **Status**: ACCEPTED WITH VALIDATION REQUIRED

## ADR-022: Perception and UI Automation
- **Context**: Omnix must perceive the screen to act on unknown apps.
- **Decision**: Use DXcam (capture), Windows UI Automation/pywinauto (primary perception), RapidOCR (fallback), and Playwright (browser).
- **Reason**: UI Automation provides structured data which is far cheaper and more reliable than pure visual reasoning.
- **Alternatives considered**: Pure vision-based grounding (too slow/unreliable).
- **Consequences**: Windows-centric implementation initially.
- **Status**: ACCEPTED

## ADR-023: Local Memory Storage
- **Context**: Omnix needs to recall past events and user preferences without a heavy vector database initially.
- **Decision**: Use SQLite with FTS5.
- **Reason**: Zero-setup, lightweight, highly performant for text search.
- **Alternatives considered**: ChromaDB, Pinecone, FAISS.
- **Consequences**: Advanced semantic search might require a dedicated embedding model later if FTS5 is insufficient.
- **Status**: ACCEPTED

## ADR-024: Provider Abstraction Requirement
- **Context**: Technologies change rapidly.
- **Decision**: All third-party technologies (LLM, TTS, STT, OCR) must be hidden behind provider interfaces (e.g., `ModelProvider`).
- **Reason**: Prevents vendor lock-in and allows easy swapping of technologies.
- **Alternatives considered**: Direct coupling.
- **Consequences**: Slight abstraction overhead.
- **Status**: ACCEPTED
"""
        content = content + "\n" + adrs
    
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

def update_memory():
    path = os.path.join(base_dir, "docs/MEMORY.md")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
        
    if "TECHNOLOGY.md created" not in content:
        content = content.replace("## Completed", "## Completed\n- Technology architecture documented.\n- `TECHNOLOGY.md` created.\n- Approved technology baseline established.\n- No implementation has begun solely because technology documentation exists.")
        
        content = content.replace("## Known Issues\n- None yet.", "## Known Issues\n- None yet.\n\n## Validations Required (Future Tasks)\n- Validate Chatterbox-Turbo under exact Python 3.13.15 runtime environment.\n- Validate Rhubarb integration/runtime behavior.\n- Validate Python <-> Godot IPC method.\n- Validate exact character asset format and packaging composition.\n- Validate exact GPU allocation strategy and latency/performance targets.")
        
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

def update_test_plan():
    path = os.path.join(base_dir, "docs/TEST_PLAN.md")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
        
    if "## Technology-Specific Validation Requirements" not in content:
        tech_tests = """
## Technology-Specific Validation Requirements
These tests ensure the technology stack functions correctly, but do not replace behavioral end-to-end testing:
- **Python 3.13.15 environment compatibility**
- **Ollama connectivity & Gemma model loading**
- **Gemma text inference & Gemma image inference**
- **Gemma cancellation/timeouts**
- **Microphone capture & DeepFilterNet**
- **Silero VAD & openWakeWord**
- **faster-whisper & Whisper large-v3-turbo**
- **Chatterbox speaker output & barge-in**
- **DXcam multi-monitor capture**
- **UI Automation (pywinauto) & RapidOCR**
- **Playwright & SQLite/FTS**
- **Godot bridge, character state & lip sync**
- **Nuitka packaging**

*Note: Technology working individually != Omnix working. Real end-to-end tests remain required.*
"""
        content = content + "\n" + tech_tests
        
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

def update_security():
    path = os.path.join(base_dir, "docs/SECURITY.md")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
        
    if "## Technology Security Implications" not in content:
        tech_sec = """
## Technology Security Implications
Security implications of the approved technology stack (Refer to `TECHNOLOGY.md`):
- **Ollama local model access**: Ensure local API is bound to localhost to prevent network exploitation. Ensure model files are safe.
- **Audio/Video**: Microphone access, screen capture (DXcam), wake-word audio, STT audio, and TTS output must be secured and clearly indicated to the user.
- **Godot IPC**: Ensure IPC mechanisms (e.g., local WebSocket/named pipe) authenticate or restrict connections to the Python Omnix process only.
- **Browser Automation**: Playwright profiles/sessions must be isolated to prevent accidental credential leakage or cookie hijacking.
- **Windows APIs & Clipboard**: Restrict arbitrary access; capability router must mediate clipboard reads/writes.
- **Storage & Config**: SQLite memory, logs, `.env` files must be protected. Prefer Windows Credential Manager / DPAPI for production secrets.
- **Third-Party**: Ensure downloaded models and third-party character/audio asset licenses are reviewed.
"""
        content = content + "\n" + tech_sec
        
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

def update_phase_files():
    phases_dir = os.path.join(base_dir, "docs/phases")
    tech_mappings = {
        "PHASE_00_BLUEPRINT.md": "`TECHNOLOGY.md` is part of blueprint documentation.",
        "PHASE_01_RUNTIME_FOUNDATION.md": "Python 3.13.15, `.venv`, `pip`, Pydantic, `asyncio`, logging/testing foundation.",
        "PHASE_02_OMNIX_EXECUTIVE.md": "No provider-specific Omnix Executive coupling.",
        "PHASE_03_AGENT_CAPABILITY_FRAMEWORK.md": "Custom Agent/Capability framework, Pydantic contracts.",
        "PHASE_04_INPUT_OUTPUT_VOICE.md": "Voice/input stack (`sounddevice`, DeepFilterNet, Silero VAD, openWakeWord, faster-whisper, Chatterbox).",
        "PHASE_05_WORLD_STATE_CONTEXT.md": "SQLite/world-state technology where relevant.",
        "PHASE_06_BRAIN_GOALS_PLANNING.md": "Ollama, Gemma 4 31B, Model Manager.",
        "PHASE_07_APPLICATION_WINDOW_SYSTEM.md": "Windows native APIs, `pywin32`, `pywinauto`, `psutil`.",
        "PHASE_08_PERCEPTION_VISION_GROUNDING.md": "DXcam, OpenCV, UIA, RapidOCR, ONNX Runtime, Gemma visual reasoning.",
        "PHASE_09_GENERIC_DESKTOP_INTERACTION.md": "Same perception/control foundations.",
        "PHASE_10_BROWSER_INTELLIGENCE.md": "Playwright.",
        "PHASE_11_FILESYSTEM_INTELLIGENCE.md": "`pathlib`, filesystem capabilities.",
        "PHASE_12_VERIFICATION_ENGINE.md": "Verification providers built from existing perception/state technologies.",
        "PHASE_13_RECOVERY_REPLANNING.md": "Gemma reasoning through Model Manager (no special second recovery LLM).",
        "PHASE_14_MEMORY.md": "SQLite + FTS5.",
        "PHASE_15_COMMUNICATION_PERSONALITY.md": "Chatterbox, Godot, Blender-created assets, Rhubarb, PySide6/QML integration.",
        "PHASE_16_SAFETY_PERMISSIONS.md": "Windows credential/security technologies.",
        "PHASE_17_MULTI_AGENT_COLLABORATION.md": "Custom Omnix multi-agent framework.",
        "PHASE_18_COMPLEX_LONG_RUNNING_TASKS.md": "`asyncio`/task persistence technologies.",
        "PHASE_19_BACKGROUND_AUTOMATION_EVENTS.md": "`asyncio`/custom scheduling (APScheduler only if later justified).",
        "PHASE_20_EXTERNAL_INTEGRATIONS.md": "`httpx`/provider/plugin abstractions."
    }
    
    for filename, tech_text in tech_mappings.items():
        path = os.path.join(phases_dir, filename)
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
            if "## Technology Baseline" not in content:
                tech_section = f"""
## Technology Baseline
This phase must follow the approved technologies and provider boundaries defined in:
`../TECHNOLOGY.md`

Relevant technologies for this phase: {tech_text}
"""
                content = content.replace("## Scope", tech_section + "\n## Scope")
                with open(path, "w", encoding="utf-8") as f:
                    f.write(content)

def update_phases_readme():
    path = os.path.join(base_dir, "docs/phases/README.md")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    if "TECHNOLOGY.md" not in content:
        content = content.replace("1. **READ**: Thoroughly read the Phase document and core architecture docs.", "1. **READ**: Thoroughly read the Phase document and core architecture docs (including `../TECHNOLOGY.md`).\n**Prerequisites**: Before implementing any phase, coding agents should read README, PRD, ARCHITECTURE, TECHNOLOGY, RULES, DECISIONS, MEMORY, TEST_PLAN, SECURITY, and the relevant phase specification.")
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)

if __name__ == "__main__":
    update_readme()
    update_agents()
    update_prd()
    update_architecture()
    update_design()
    update_rules()
    update_tasks()
    update_decisions()
    update_memory()
    update_test_plan()
    update_security()
    update_phase_files()
    update_phases_readme()
    print("All markdown files updated successfully.")
