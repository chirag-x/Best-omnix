# Phase 16: Communication + Personality + Voice Expression + Character

## 1. What is being introduced?
The natural language generation, emotion mapping, Godot avatar rendering, and Rhubarb lip sync.

## 2. Why is it introduced now?
Omnix needs a tangible presence. Technical execution states must be translated into warm, expressive communication.

## 3. What components exist after this phase?
CommunicationAgent, CharacterBridge, GodotRuntime, RhubarbProvider.

## 4. What interfaces/contracts exist?
ICharacterBridge.

## 5. What data models/concepts exist?
CharacterState (IDLE, THINKING, SPEAKING, etc.), Emotion, Utterance.

## 6. How does this specific subsystem work?
`CommunicationAgent` (Gemma) generates natural text based on TaskState. TTS generates audio. `Rhubarb` generates visemes. `CharacterBridge` (IPC WebSocket/Named Pipe) sends State/Visemes to the Godot application, which renders the Blender-authored 3D character.

## 7. What depends on it?
User Experience.

## 8. What is explicitly out of scope?
Godot executing intelligence or managing state. The character is presentation-only.

## 9. What are the actual development tasks?
1. Implement `CommunicationAgent`.
2. Build Python `CharacterBridge` IPC.
3. Integrate Rhubarb lip sync.
4. Build basic Godot receiver scene.
5. Map technical states to CharacterStates.

## 10. What exact tests are required?
IPC latency tests, state transition mapping tests, lip sync timing tests.

## 11. What real runtime validation is meaningful?
Execute a task and observe the Godot character transition from IDLE to THINKING to SPEAKING with synchronized lip movements.

## 12. What constitutes success?
A seamless, responsive visual and auditory presence completely decoupled from the heavy Python intelligence loop.

## 13. What failures must block progression?
IPC latency causing audio/visual desync, Godot crashing the Python process.

## 14. What documentation must be updated?
Update `MEMORY.md`.

## 15. What does the next phase depend on?
Phase 17.

## Technology Baseline
This phase must follow the approved technologies and provider boundaries defined in `../TECHNOLOGY.md`.
