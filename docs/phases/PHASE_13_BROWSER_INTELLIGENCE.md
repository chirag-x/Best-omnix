# Phase 13: Browser Intelligence

## 1. What is being introduced?
Deep integration with Playwright for structured web navigation, DOM reasoning, and form interaction.

## 2. Why is it introduced now?
Desktop UIA/Vision is too slow/unreliable for complex web tasks. Playwright provides perfect structured perception and deterministic control.

## 3. What components exist after this phase?
BrowserAgent, PlaywrightProvider, BrowserCapabilities.

## 4. What interfaces/contracts exist?
IBrowserProvider.

## 5. What data models/concepts exist?
DOMNode, PageState.

## 6. How does this specific subsystem work?
`BrowserAgent` uses `PlaywrightProvider` to inspect the DOM/Accessibility tree. Capabilities include `navigate`, `click_selector`, `fill_form`. Fallback to desktop vision if Playwright cannot attach.

## 7. What depends on it?
Advanced web automation tasks.

## 8. What is explicitly out of scope?
Building a custom rendering engine. Chrome-specific extension architecture.

## 9. What are the actual development tasks?
1. Integrate Playwright Python.
2. Implement DOM/Accessibility tree parsing.
3. Implement Browser Capabilities (click, type, scroll, wait).
4. Implement `BrowserAgent` to reason about web state.

## 10. What exact tests are required?
Playwright integration tests, DOM parsing unit tests, form filling tests.

## 11. What real runtime validation is meaningful?
Navigate to a dynamic web page, extract data from a table, and fill out a multi-step form.

## 12. What constitutes success?
Reliable web automation bypassing slow visual reasoning where structured DOM is available.

## 13. What failures must block progression?
Playwright sessions leaking, failing to handle cookies/auth state safely.

## 14. What documentation must be updated?
Update `MEMORY.md`.

## 15. What does the next phase depend on?
Phase 14 for filesystem tasks.

## Technology Baseline
This phase must follow the approved technologies and provider boundaries defined in `../TECHNOLOGY.md`.
