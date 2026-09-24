# Omnix Product Requirements Document (PRD)

## Product Vision
Omnix is a voice-first, fully autonomous, local-first AI assistant for Windows 11. It does not rely on hardcoded command macros or application-specific integrations. Instead, it uses generic computer perception (UI Automation, Vision, OCR) and planning to interact with any application exactly as a human would.

## Core Principles
- **No Hardcoded Commands**: Omnix must figure out how to accomplish a goal dynamically.
- **Local-First**: The primary intelligence and perception run locally on the user's hardware.
- **Voice-First**: The primary interaction modality is conversational voice with barge-in capabilities.
- **Safety-First**: A deterministic Policy Engine protects the user from destructive or sensitive actions.
- **Tangible Presence**: An animated character (rendered in Godot) gives Omnix a visual and emotional presence, distinct from the technical execution loop.

## Functional Requirements
- **Goal Understanding**: Parse natural language into structured, acyclic `PlanRevisions`.
- **Generic Interaction**: Control unfamiliar Windows applications via native APIs, UIA, and vision grounding.
- **Layered Perception**: Observe the world through OS APIs, UIA, OCR, and Gemma Vision, fusing data into a `SceneModel`.
- **Deterministic Verification**: Verify task outcomes using deterministic OS checks before relying on AI reasoning.
- **Dynamic Replanning**: Recover gracefully from failures, UI lag, or unexpected state changes without crashing.
- **Browser Intelligence**: Deeply automate web tasks using Playwright.
- **Contextual Memory**: Remember user preferences and past context using SQLite/FTS5 text search.
- **External Integrations**: Cleanly interface with external APIs (Email, Calendar) via secure capabilities.

## Technology Constraints / Platform Requirements
- Windows 11 initial target.
- Python 3.13.15 baseline.
- Local/free-first operation.
- Ollama / Gemma 4 31B baseline intelligence (One shared model).
- Voice-first operation (faster-whisper, Chatterbox, openWakeWord, Silero, DeepFilterNet).
- Animated character/presence (Godot, Blender, Rhubarb).
- Local perception/control (DXcam, pywinauto, RapidOCR, Playwright).
- Provider replaceability for all external libraries.
- Reference `TECHNOLOGY.md` for detailed implementation technology decisions.

## Safety and Security
- **Deterministic Policy Engine**: Side effects must be authorized by a deterministic engine evaluating rules against a Canonical Risk Taxonomy (`LOW_RISK`, `SENSITIVE`, `DESTRUCTIVE`, `IRREVERSIBLE`, `PRIVACY_SENSITIVE`, `EXTERNAL_SIDE_EFFECT`).
- **No Global Shell**: There is no generic unrestricted shell execution allowed.

## Performance Requirements (TARGET / PROVISIONAL)
*These latency targets are provisional and must be benchmarked during implementation.*
- Wake word to STT processing: < 1.0s (PROVISIONAL)
- UI Automation (UIA) perception tree extraction: < 500ms (PROVISIONAL)
- Goal planning generation: < 3.0s (PROVISIONAL)
- Animation / Character response latency: < 50ms (PROVISIONAL)

## Out of Scope / Non-Goals
- Building a custom web browser or operating system.
- Perfect deterministic execution of every legacy app (graceful failure is acceptable).
- Creating rigid macros for specific third-party applications.
- Distributed task execution across multiple machines.

## Golden User Scenarios
1. **Contextual Editing**: "Open Notepad. Type a recipe for pancakes. Save it to my desktop as breakfast."
2. **Visual Navigation**: "What's the error message in the center of the screen?" -> "Close that window."
3. **Research**: "Search the web for the latest AI models and summarize the top three in a new text file."

## Acceptance Principles
- If a user asks for something, and it works, but it relied on a hardcoded "if intent == X" rule, the requirement fails.
- If a task succeeds, but verification was not performed, the requirement fails.
- If a step fails, and the system crashes or hangs instead of attempting recovery or notifying the user gracefully, the requirement fails.

## Definition of Success
A functional prototype where a user can speak a multi-step goal involving an application Omnix has never been explicitly programmed to handle, and Omnix successfully plans, executes, verifies, and communicates the result safely.
