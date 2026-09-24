# Omnix Test Plan

## 1. Testing Philosophy
Omnix testing focuses on proving the reliability of critical architectural contracts, safety boundaries, and generic interaction.
**We do not require arbitrary 100% code coverage.** Instead, coverage must be strong for:
- Agent/Capability contracts
- Policy Engine and Safety boundaries
- Capability Router authorization
- Verification PASS/FAIL/UNCERTAIN logic
- Recovery limits and replanning
- State transitions (WorldState revisions, Plan revisions)

## 2. Core Infrastructure Testing
- **Configuration & DI**: Verify the environment loads correctly and dependencies inject cleanly.
- **Agent/Capability Contracts**: Validate Pydantic schemas (AgentRequest, AgentResult, CapabilityRequest, CapabilityResult).
- **WorldState Revisions**: Ensure concurrent reads/writes against the `WorldStateStore` yield consistent snapshots.
- **Plan Revisions**: Validate that `PlanRevisions` remain strictly acyclic.

## 3. Safety & Policy Testing
- **Risk Categories**: Test all categories (`LOW_RISK`, `SENSITIVE`, `DESTRUCTIVE`, etc.).
- **Permission Decisions**: Ensure the Policy Engine deterministically returns ALLOW, DENY, or REQUIRE_CONFIRMATION based on state and risk.
- **Capability Routing**: Verify that no side-effecting capability bypasses the Policy Engine.

## 4. Execution & Verification Testing
- **Single-Model Routing**: Ensure all cognitive roles route to the same underlying Gemma provider interface.
- **Provider Abstraction**: Swap providers in tests to ensure core logic remains decoupled.
- **Verification Outcomes**: Test that deterministic verifiers accurately report PASS, FAIL, or UNCERTAIN.
- **Recovery Loops**: Test recovery limits and ensure replanning triggers correctly without infinite loops.

## 5. End-to-End Desktop Interaction (The Ultimate Test)
Omnix's success relies on generic interaction.
- **Unknown Application Interaction**: Command Omnix to interact with a dummy application it has no prior code for. Verify it uses generic UI automation/vision to achieve the goal.
- **No Hardcoded Flows**: Ensure no tests rely on `open_notepad()` or specific application macros to succeed.

## 6. Technology-Specific Validation Requirements
These tests ensure the technology stack functions correctly, but do not replace behavioral end-to-end testing:
- **Python 3.13.15 environment compatibility**
- **Ollama connectivity & Gemma model loading**
- **Microphone capture & DeepFilterNet**
- **Silero VAD & openWakeWord**
- **faster-whisper & Whisper large-v3-turbo**
- **Chatterbox speaker output & barge-in**
- **DXcam multi-monitor capture**
- **UI Automation (pywinauto) & RapidOCR**
- **Playwright & SQLite/FTS**
- **Godot bridge, character state & lip sync**
- **Nuitka packaging**
