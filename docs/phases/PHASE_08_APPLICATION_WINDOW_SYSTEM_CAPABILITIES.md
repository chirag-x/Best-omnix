# Phase 8: Application + Window + System Capabilities

## 1. What is being introduced?
Deterministic capabilities to interact with the OS: application discovery, window enumeration, focus, keyboard, mouse, clipboard.

## 2. Why is it introduced now?
Omnix needs safe, generic ways to manipulate the computer without relying on hardcoded application macros or pure LLM hallucination.

## 3. What components exist after this phase?
ApplicationCapabilities, WindowCapabilities, InputCapabilities, SystemCapabilities.

## 4. What interfaces/contracts exist?
None (implements `ICapability`).

## 5. What data models/concepts exist?
WindowInfo, ProcessInfo, Capability effect types.

## 6. How does this specific subsystem work?
Using `pywin32`, `pywinauto`, `ctypes`, and `psutil`. E.g., `enumerate_windows` returns a list of `WindowInfo`. `focus_window` takes a handle and brings it to foreground using Win32 APIs. All wrapped as formal Capabilities.

## 7. What depends on it?
Phase 12 (Generic Desktop Interaction).

## 8. What is explicitly out of scope?
Web browser specific DOM interaction (Playwright). Reading text from screenshots (OCR).

## 9. What are the actual development tasks?
1. Implement window enumeration/focus/resize.
2. Implement application launch/discovery (generic).
3. Implement native SendInput for keyboard/mouse.
4. Implement clipboard read/write.
5. Register all with `CapabilityRegistry`.

## 10. What exact tests are required?
Unit tests for pywin32 wrappers (with mock handles). Integration tests for window enumeration.

## 11. What real runtime validation is meaningful?
Execute a plan that launches Notepad, focuses it, types text, and reads the clipboard.

## 12. What constitutes success?
Reliable, deterministic control over standard Windows elements without using visual AI.

## 13. What failures must block progression?
SendInput locking the user out, failing to find active windows, bypassing the Policy Engine.

## 14. What documentation must be updated?
Update `MEMORY.md`, document capability schemas.

## 15. What does the next phase depend on?
Phase 9 needs to perceive what these capabilities do.

## Technology Baseline
This phase must follow the approved technologies and provider boundaries defined in `../TECHNOLOGY.md`.
