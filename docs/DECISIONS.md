# Architecture Decision Records (DECISIONS.md)

This file tracks major architectural decisions for Omnix.

## ADR-001: Omnix Executive and Specialist Architecture
- **Context**: The system needs to handle diverse user goals across different domains without becoming a monolithic, unmaintainable codebase.
- **Decision**: Omnix uses a central Executive + Specialist Agent architecture.
- **Reason**: Allows domain separation while maintaining a single cohesive user experience.
- **Consequences**: Requires a robust registry and dynamic routing mechanism.
- **Status**: ACCEPTED

## ADR-002: Goal Ownership
- **Context**: Who decides when a user's request is satisfied?
- **Decision**: Omnix Core (Executive) owns the global user goal. Specialists only own sub-goals.
- **Reason**: Prevents agents from endlessly looping or failing silently without the system being able to report back to the user.
- **Consequences**: Agents must report clear SUCCESS/FAIL/UNCERTAIN states back to the Executive.
- **Status**: ACCEPTED

## ADR-003: Dynamic Goal Representation
- **Context**: Natural language can be mapped to hardcoded commands (brittle) or abstract goals (flexible).
- **Decision**: User input represents abstract goals. No hard-coded natural-language command routing.
- **Reason**: Adheres to the core product vision. Enables handling of novel, unanticipated requests.
- **Consequences**: Requires a complex LLM-driven planning phase before execution.
- **Status**: ACCEPTED

## ADR-004: General vs App-Specific Intelligence
- **Context**: Building automations for Chrome, Spotify, etc., individually is unscalable.
- **Decision**: No app-specific general automation architecture. Omnix relies on generic Desktop, Window, and Vision intelligence.
- **Reason**: Maximizes software compatibility and future-proofs the system against UI updates.
- **Consequences**: Perception layer (Vision, UIA, OCR) must be highly robust.
- **Status**: ACCEPTED

## ADR-005: Agents vs Capabilities
- **Context**: Mixing reasoning (LLM calls) and execution (Win32 API calls) leads to dangerous, untestable code.
- **Decision**: Agents and capabilities are strictly separate concepts. Agents reason; controlled capabilities execute.
- **Reason**: Enforces security, testability, and reusability.
- **Consequences**: Execution logic cannot reside inside Agent classes.
- **Status**: ACCEPTED

## ADR-006: Registries
- **Context**: How do components find each other dynamically?
- **Decision**: A Capability Registry and an Agent Registry exist as central discovery mechanisms.
- **Reason**: Allows drop-in extensibility without core rewrites.
- **Consequences**: Requires standard metadata schemas for registration.
- **Status**: ACCEPTED

## ADR-007: World State as First-Class Entity
- **Context**: Passing state arbitrarily between functions loses context.
- **Decision**: World State is a first-class, centralized entity updated continuously.
- **Reason**: Provides a single source of truth for planning and perception.
- **Consequences**: Requires careful state synchronization.
- **Status**: ACCEPTED

## ADR-008: Verification Requirement
- **Context**: Blind automation often fails due to UI lag or unexpected popups.
- **Decision**: Verification is a first-class requirement. Meaningful side effects must be checked.
- **Reason**: Reliability.
- **Consequences**: Execution speed may be slightly slower, but success rates will be vastly higher.
- **Status**: ACCEPTED

## ADR-009: Recovery Requirement
- **Context**: What happens when verification fails?
- **Decision**: Recovery is a first-class citizen.
- **Reason**: System must be resilient.
- **Consequences**: Requires a Recovery Agent or core loop to handle fallback strategies.
- **Status**: ACCEPTED

## ADR-010: Canonical Execution Model
- **Context**: Voice input, text input, and automated crons might take different paths.
- **Decision**: One canonical execution architecture exists for all inputs.
- **Reason**: Prevents divergent behavior and duplicated maintenance.
- **Consequences**: Input gateways must normalize all triggers into a standard format.
- **Status**: ACCEPTED

## ADR-011: Separation of Communication and Execution
- **Context**: Users do not want to hear technical logs read aloud.
- **Decision**: Communication is separated from technical execution. Personality/expression is applied at the output edge.
- **Reason**: UX quality.
- **Consequences**: Requires an explicit Communication Agent.
- **Status**: ACCEPTED

## ADR-012: Safety and Policy Boundary
- **Context**: AI models can hallucinate dangerous actions.
- **Decision**: Safety policies sit strictly between reasoning and controlled execution. LLMs do NOT receive unrestricted shell authority.
- **Reason**: Security and trust.
- **Consequences**: Strict validation on the Capability Router.
- **Status**: ACCEPTED

## ADR-013: Provider Abstraction
- **Context**: AI ecosystems change rapidly.
- **Decision**: Models/providers must be replaceable behind standard interfaces.
- **Reason**: Prevents vendor lock-in.
- **Consequences**: Cannot use provider-specific SDK features in core reasoning loops.
- **Status**: ACCEPTED

## ADR-014: Layered Perception
- **Context**: No single perception method (Vision vs UIA) is 100% reliable.
- **Decision**: Perception is layered (OS -> UIA -> OCR -> Vision).
- **Reason**: Combines the speed of APIs with the robustness of Vision.
- **Consequences**: Requires a complex Scene Modeler to fuse data.
- **Status**: ACCEPTED

## ADR-015: Runtime Testing
- **Context**: Unit tests cannot verify if a system can actually click a Windows button.
- **Decision**: Real runtime verification is required for major milestones.
- **Reason**: Ensures the system actually works in the real world.
- **Consequences**: CI/CD and testing requirements are significantly more complex.
- **Status**: ACCEPTED


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
