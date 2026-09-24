# Omnix Testing Strategy (TEST_PLAN.md)

This document outlines the comprehensive test strategy for Omnix. **Testing outcomes, not just function invocation, is critical.**

## Testing Philosophy
- A test is not valid if it relies on hardcoded string matching that bypasses the LLM reasoning (unless explicitly testing the routing infrastructure).
- Real runtime tests must eventually prove the system works on actual Windows software.

## Unit Tests
- Fast, isolated tests for pure functions (e.g., parsing a JSON response, formatting a string).
- Must run in CI on every commit.

## Contract Tests
- Verify that Agents and Capabilities adhere strictly to the interfaces defined in the framework.

## Agent Tests
- Mock the World State and verify that an Agent produces a logical Task Graph or Capability Request given a specific goal.

## Capability Tests
- Test execution primitives. Mock the OS where necessary for speed, but real integration tests are required later.

## Registry Tests
- Ensure dynamic discovery works. Register a dummy agent, query for it, ensure it routes correctly.

## Planning Tests
- Provide complex, multi-step goals and verify the Planner generates a valid DAG (Directed Acyclic Graph).

## Context Tests
- Pass sequence of inputs: "Open Chrome" -> "Search X" -> "Close it". Verify "it" resolves to Chrome.

## World State Tests
- Verify that state updates merge correctly without race conditions.

## Perception Tests
- Feed static screenshots/UIA trees and verify the Scene Modeler extracts the correct interactive elements.

## UI Automation Tests
- Real runtime tests validating that UIA hooks correctly identify standard Windows controls.

## Vision Tests
- Verify the vision model (mocked or real) correctly bounds and identifies semantic targets.

## Grounding Tests
- Verify the mapping from "Submit button" -> UI Node -> Screen Coordinates works accurately.

## Application / Window / Desktop Tests
- Real runtime tests: Launch `calc.exe`, verify it opened, move it, close it, verify it closed.

## Browser / Filesystem Tests
- Browser: Navigate to a local test HTML file, find an element, click it.
- FS: Create a temp directory, have Omnix write a file, verify contents, delete it.

## Verification Tests
- Intentionally cause an action to fail (e.g., try to click a hidden window). Ensure Verification correctly reports `FAIL`.

## Recovery Tests
- Mock a capability to fail once but succeed on retry. Verify the Recovery Agent handles it gracefully without crashing.

## Memory Tests
- Test vector DB insertion and retrieval for relevance.

## Voice / Communication Tests
- Verify technical errors (e.g., "TimeoutException") are transformed into natural language ("I couldn't reach the server").

## Safety Tests
- Try to execute a capability marked `DESTRUCTIVE`. Verify the Capability Router throws an `AuthorizationError` or pauses for confirmation.

## Multi-Agent / Integration Tests
- Test the handoff: Executive -> Browser Agent -> Desktop Agent -> Verification.

## End-to-End Tests
- Full pipeline run from text input to actual OS side effect.

## Real Windows Runtime Tests
- Must run on a real Windows VM. Cannot be fully mocked.

## Failure Injection / Chaos Tests
- Randomly kill the targeted application mid-task to ensure Omnix recovers gracefully.

## Golden Path Scenarios
1. "Open Notepad."
2. "Open Notepad and type Hello Omnix."
3. "Open Notepad, write something and save it."
4. "Open Chrome and search for AI agents."
5. "Open Chrome, search for AI agents and open the second result."
6. "What's on my screen?"
7. "Click the blue button."
8. "Find the PDF I downloaded yesterday."
9. Context continuation: "Open Chrome." -> "Search for AI agents." -> "Open the second one."
10. Unknown application test.
11. Application already running.
12. Window loses focus.
13. Dialog interrupts task.
14. UI changes.
15. Operation cannot be verified.
16. User interrupts with "Stop."
17. User changes goal midway.
18. Recovery succeeds.
19. Recovery fails safely.
20. Ambiguous user request requires clarification.


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
