# Product Requirements Document

## Product
Omnix

## Vision
Omnix turns natural human goals into verified computer outcomes through dynamic reasoning, specialized agents, controlled capabilities, perception, verification, and recovery.

## Problem
Current AI assistants rely on rigid commands, brittle scripts, and hardcoded application workflows. They lack the ability to adapt to unknown applications, verify whether their actions actually succeeded, or recover from unexpected UI states, making them unreliable for robust, long-running computer use.

## Target User
Users seeking an intelligent, voice-first desktop companion capable of executing complex, multi-step goals across various applications without needing explicit step-by-step programming.

## Core Outcome
A reliable, general-purpose computer-use agent that handles intent resolution, task planning, and error recovery autonomously.

## Product Principles
- **Goal-Driven**: Users declare outcomes; the system figures out the steps.
- **Dynamic Adaptability**: The system must operate unfamiliar software via general capabilities (vision, OCR, UI automation) rather than requiring a dedicated plugin for every app.
- **Trust via Verification**: No action is assumed successful without evidence.
- **Resilient**: Graceful degradation and recovery are expected behaviors.

## User Experience
The user interacts with a single entity, "Omnix". The communication is natural, contextual, and uninterrupted by internal technical jargon. If Omnix is unsure, it asks for clarification. If it fails, it explains why and offers alternatives.

---

## Functional Requirements

### Omnix Executive Requirements
- **OMX-FR-EXEC-001**: The Omnix Executive shall own the global user goal and the orchestration of all sub-tasks.
- **OMX-FR-EXEC-002**: Omnix shall not depend on hard-coded mappings between natural-language user requests and task-specific implementation functions.
- **OMX-FR-EXEC-003**: The Executive shall maintain a single canonical execution model for all inputs (voice, text, event).

### Goal Understanding Requirements
- **OMX-FR-GOAL-001**: User input must be parsed into an abstract representation of a desired outcome, including constraints and success criteria.

### Planning Requirements
- **OMX-FR-PLAN-001**: Omnix shall generate a dynamic task graph (plan) to achieve the goal.
- **OMX-FR-PLAN-002**: The plan must be mutable at runtime based on new observations.

### Agent Requirements
- **OMX-FR-AGENT-001**: Omnix shall dynamically select specialists and capabilities based on the goal and environment.
- **OMX-FR-AGENT-002**: Agents shall only contain reasoning logic for their domain, not direct execution scripts.

### Capability Requirements
- **OMX-FR-CAP-001**: Capabilities shall expose generic primitive actions (e.g., click, type, launch).
- **OMX-FR-CAP-002**: Capabilities must be discoverable at runtime via a Capability Registry.

### World State Requirements
- **OMX-FR-STATE-001**: The system must maintain a structured representation of the current World State (desktop, windows, apps).

### Context Requirements
- **OMX-FR-CTX-001**: The system must resolve contextual pronouns (e.g., "it", "that one") against recent conversation and perceptual history.

### Perception Requirements
- **OMX-FR-PERC-001**: Perception shall use a layered approach (OS APIs, Accessibility/UIA, OCR, Vision) to build a unified Scene Model.

### Application Control Requirements
- **OMX-FR-APP-001**: Omnix must be able to discover, launch, focus, and terminate applications dynamically.

### Window Control Requirements
- **OMX-FR-WIN-001**: Omnix must be able to manipulate window states (move, resize, focus).

### Desktop Interaction Requirements
- **OMX-FR-DESK-001**: Omnix shall support generic interactions (mouse, keyboard) independent of the specific application.

### Browser Requirements
- **OMX-FR-BROW-001**: Browser interactions shall leverage DOM and accessibility trees in addition to visual fallback.

### Filesystem Requirements
- **OMX-FR-FS-001**: Omnix shall interact with the filesystem (read, write, move, search) via generic capabilities.

### Verification Requirements
- **OMX-FR-VERIFY-001**: Meaningful side-effecting actions must be verified before the task is considered complete.
- **OMX-FR-VERIFY-002**: Unverified or failed actions must explicitly halt forward progress on that task branch.

### Recovery Requirements
- **OMX-FR-REC-001**: Omnix shall attempt bounded recovery (retry, replan, alternative capability) upon verification failure.

### Memory Requirements
- **OMX-FR-MEM-001**: Omnix shall maintain working memory for the session and episodic memory for past actions to inform future context.

### Voice Requirements
- **OMX-FR-VOICE-001**: The system must support asynchronous voice input, wake words, and barge-in (interruption).

### Communication Requirements
- **OMX-FR-COMM-001**: System logs and technical execution state shall not be directly read to the user.
- **OMX-FR-COMM-002**: The system must generate natural language progress updates and failure explanations.

### Personality Requirements
- **OMX-FR-PERS-001**: Omnix shall maintain a consistent, helpful, and transparent persona without claiming human consciousness.

### Safety Requirements
- **OMX-FR-SAFE-001**: Destructive actions (e.g., file deletion) must require explicit user confirmation.
- **OMX-FR-SAFE-002**: LLMs shall never be granted unrestricted, unvalidated shell/terminal access.

### Automation Requirements
- **OMX-FR-AUTO-001**: The system shall support scheduling and background execution of task graphs.

### External Integration Requirements
- **OMX-FR-EXT-001**: External service calls must utilize the identical capability/verification architecture as local actions.

---

## Technology Constraints / Platform Requirements
- Windows 11 initial target
- Python 3.13.15 baseline
- Local/free-first operation
- Ollama/Gemma baseline intelligence
- Voice-first operation
- Animated character/presence
- Local perception/control
- Provider replaceability

Reference `TECHNOLOGY.md` for detailed implementation technology decisions.

## Non-Functional Requirements

### Observability Requirements
- **OMX-NFR-OBS-001**: All agent decisions, plans, and capability executions must emit structured telemetry and trace data.

### Performance Requirements
- **OMX-NFR-PERF-001**: Perception extraction (OS state + UIA) should complete in under 500ms to allow responsive voice interaction.

### Extensibility Requirements
- **OMX-NFR-EXT-001**: The Agent and Capability registries must allow dynamic registration of new modules without altering the Core Executive code.

---

## Out of Scope / Non-Goals
- Building a custom web browser.
- Replacing the underlying Operating System.
- Perfect deterministic execution of every legacy app (graceful failure is acceptable).
- Creating rigid macros for specific third-party applications.

## Golden User Scenarios
1. **Contextual Editing**: "Open Notepad. Type a recipe for pancakes. Save it to my desktop as breakfast."
2. **Visual Navigation**: "What's the error message in the center of the screen?" -> "Close that window."
3. **Research**: "Search the web for the latest AI models and summarize the top three in a new text file."

## Acceptance Principles
- If a user asks for something, and it works, but it relied on a hardcoded "if intent == X" rule, the requirement fails.
- If a task succeeds, but verification was not performed, the requirement fails.
- If a step fails, and the system crashes or hangs instead of attempting recovery or notifying the user gracefully, the requirement fails.

## Definition of Success
A functional prototype where a user can speak a multi-step goal involving an application Omnix has never been explicitly programmed to handle, and Omnix successfully plans, executes, verifies, and communicates the result.
