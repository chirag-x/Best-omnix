# Omnix

## Vision
Omnix turns natural human goals into verified computer outcomes through dynamic reasoning, specialized agents, controlled capabilities, perception, verification, and recovery.

## What Omnix Is
Omnix is a voice-first, natural-language, multi-agent AI computer-use system. It acts as the central executive intelligence, orchestrator, and identity that the user interacts with. Internally, it coordinates a fleet of specialized agents and controlled capabilities to fulfill user goals on a computer.

## What Omnix Is Not
Omnix is NOT a hardcoded command system. It is not a collection of `if command == "open chrome": open_chrome()` scripts. It is not an application-specific automation engine, and it does not map predefined phrases to fixed workflows.

## Problem Omnix Solves
Current automation and assistant tools rely on rigid command structures, hardcoded workflows, and brittle application-specific scripts. They lack contextual awareness, fail ungracefully, and cannot reason about novel situations or unknown applications. Omnix solves this by introducing dynamic reasoning, generic capabilities, and robust verification, enabling true goal-oriented computer use.

## Ultimate User Experience
The user communicates with ONE assistant: Omnix. The experience is seamless, contextual, and natural. The user provides a goal, and Omnix reasons about the state of the world, creates a plan, coordinates specialists, executes actions, verifies success, and communicates progress—all without the user feeling like they are managing a swarm of disconnected bots.

## Core Philosophy
The user tells Omnix what they want. Omnix does not search for a prewritten command; it understands the goal, reasons about the situation, dynamically selects specialists, builds a task graph, executes generic capabilities, and verifies outcomes. 

## Multi-Agent Philosophy
Internally, Omnix is a multi-agent system, but externally, it is a single identity. Specialists (e.g., Vision, Browser, Filesystem) own their specialized domains, while the Omnix Executive owns the global goal. Specialists do not act as independent peer-to-peer swarms; they are coordinated by the Executive.

## Omnix Executive
The central orchestrator of the system. It receives user input, maintains context, manages the global task lifecycle, routes sub-tasks to specialized agents, and ensures the overarching goal is met safely and effectively.

## Zero Hardcoded Command Philosophy
This is the most important architectural law. There are no fixed mappings between natural language intents and execution functions. Every action is determined dynamically based on the goal, the context, and the available generic capabilities.

## Agents vs Capabilities
**Agents think. Capabilities act.**
Agents reason about domains (e.g., Application Agent reasons about app state). Capabilities are the reusable, primitive operations they invoke (e.g., `launch_application`, `click`, `type_text`). Agents do not contain hardcoded app-specific scripts.

## Goal-Oriented Interaction
User input is interpreted as a Desired Outcome (Goal), not a command. The system works backward from the expected state to generate a dynamic execution plan.

## Dynamic Planning
Omnix builds a task graph dynamically based on the goal, available agents, and world state. The plan can change at runtime based on intermediate observations.

## Perception
Perception is layered (OS state, UI Automation, OCR, Vision, etc.). Structured information is preferred when reliable, falling back to visual understanding when necessary. Omnix builds a "Scene Model" before acting.

## Verification
Issuing an action does not mean success. Meaningful actions must be verified against an expected state (e.g., checking if a window appeared after clicking an icon). Success is never blindly assumed.

## Recovery
Failure is expected. When an action fails verification, Omnix enters a recovery phase: diagnose, retry, re-ground, or replan, avoiding infinite loops and safely aborting when necessary.

## Memory
Omnix maintains contextual awareness of the conversation, task state, computer state, and history. References like "open the second one" are resolved using this memory architecture.

## Voice-First Interaction
Designed for fluid, natural voice communication, supporting barge-in, interruption, and contextual conversation without confusing technical execution with spoken output.

## Communication / Personality
Internal system results are separated from user-facing speech. A dedicated Communication layer handles personality, phrasing, and emotional tone, ensuring Omnix sounds natural and distinct from its technical logs.

## Safety
Safety sits between reasoning and execution. Destructive, privacy-sensitive, or external actions require confirmation. LLMs never receive unrestricted shell access.

## Technology
- Python 3.13.15, `.venv`
- Ollama, Gemma 4 31B
- Local voice pipeline (DeepFilterNet, Silero VAD, openWakeWord, faster-whisper, Chatterbox-Turbo)
- PySide6/QML, Godot character
- Windows-native capabilities, layered perception
- SQLite, Playwright

See: `docs/TECHNOLOGY.md` for the authoritative complete technology stack.

## High-Level Architecture
```text
USER GOAL -> OMNIX EXECUTIVE -> UNDERSTAND -> REASON -> SELECT SPECIALISTS -> CREATE TASK GRAPH -> EXECUTE CAPABILITIES -> OBSERVE -> VERIFY -> (SUCCESS/RECOVER) -> COMMUNICATE
```

## Canonical Execution Lifecycle
All requests, whether from voice, text, or events, flow through a single canonical execution model. There are no parallel, disconnected automation pipelines.

## Major Subsystems
- Omnix Executive
- Brain / Goal Planner
- Context / Memory Engine
- Perception / Scene Modeler
- Agent Registry & Specialist Agents (Browser, Desktop, etc.)
- Capability Router & Controlled Capabilities
- Verification & Recovery Engine
- Communication / Personality Layer

## Example Interactions
User: "Open Chrome, search for AI agents, and open the second result."
Omnix dynamically translates this into a sequence of goals: ensure browser running, navigate to search, interpret visual/DOM results, interact with the target element.

## Golden Path Goals
- "Open Notepad and type Hello Omnix."
- "Find the PDF I downloaded yesterday."
- "What's on my screen right now?"

## Development Roadmap
See `docs/TASKS.md` for the Phase 0 to Phase 20 rollout plan.

## Current Project Status
**Phase 0 - Blueprinting**: Establishing foundational architecture and documentation. See `docs/MEMORY.md`.

## Documentation Map
- `docs/PRD.md`: Requirements
- `docs/ARCHITECTURE.md`: System design
- `docs/RULES.md`: Core architectural laws
- `docs/TASKS.md`: Roadmap
- `docs/DECISIONS.md`: ADRs
- `docs/MEMORY.md`: Project state
- `docs/TEST_PLAN.md`: Testing strategy
- `docs/SECURITY.md`: Safety model

## Contribution / Development Philosophy
Read `AGENTS.md` and `docs/RULES.md` before coding. Never silently reinterpret the architecture. If a task conflicts with the Zero Hardcoded Command philosophy, stop and report it.

## North Star
Omnix turns natural human goals into verified computer outcomes through dynamic reasoning, specialized agents, controlled capabilities, perception, verification and recovery.
