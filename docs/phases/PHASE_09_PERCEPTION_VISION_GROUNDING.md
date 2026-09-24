# Phase 9: Perception + Vision + Scene Model + Grounding

## 1. What is being introduced?
Layered perception: DXcam, UI Automation, RapidOCR, and Gemma visual reasoning to build a Grounded Scene Model.

## 2. Why is it introduced now?
Omnix must understand the screen conceptually to act on it, translating 'click the blue button' into a specific coordinate or UI handle.

## 3. What components exist after this phase?
DXcamCapture, UIAObserver, RapidOCRProvider, GemmaVisionProvider, SceneModeler, GroundingEngine.

## 4. What interfaces/contracts exist?
ICapture, IUIA, IOCR.

## 5. What data models/concepts exist?
SceneModel, GroundedTarget, UIElement, BoundingBox.

## 6. How does this specific subsystem work?
Executive requests observation. 1. Fast path: query UIA for structured tree. 2. Fallback: DXcam capture + RapidOCR. 3. Last resort: Send image to Gemma for reasoning. `GroundingEngine` merges these into a `SceneModel`.

## 7. What depends on it?
Phase 10 (Verification) and Phase 12 (Desktop Interaction).

## 8. What is explicitly out of scope?
Action execution. Perception only observes.

## 9. What are the actual development tasks?
1. Implement DXcam screen capture.
2. Implement UIA tree extraction (`pywinauto`).
3. Integrate RapidOCR.
4. Implement multimodal request to Model Manager (Gemma vision).
5. Build `SceneModeler` to fuse data.

## 10. What exact tests are required?
UIA parsing tests, OCR bounding box tests, Grounding logic tests.

## 11. What real runtime validation is meaningful?
Capture a complex application window and verify the SceneModel accurately locates text and buttons.

## 12. What constitutes success?
Omnix can reliably identify actionable elements on the screen across different perception layers.

## 13. What failures must block progression?
DXcam memory leaks, UIA hanging on unresponsive apps, sending every frame to Gemma.

## 14. What documentation must be updated?
Update `MEMORY.md`.

## 15. What does the next phase depend on?
Phase 10 uses the SceneModel to verify actions.

## Technology Baseline
This phase must follow the approved technologies and provider boundaries defined in `../TECHNOLOGY.md`.
