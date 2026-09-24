# Phase 7: Input / Output / Voice Foundation

## 1. What is being introduced?
The audio pipeline: sounddevice, DeepFilterNet, Silero VAD, openWakeWord, faster-whisper, and TTS integration (Chatterbox).

## 2. Why is it introduced now?
Voice is the primary interaction modality. It must be processed locally, quickly, and cleanly before generating a Goal.

## 3. What components exist after this phase?
AudioCapture, WakeWordDetector, STTProvider, TTSProvider, InputGateway, OutputGateway.

## 4. What interfaces/contracts exist?
IAudioCapture, IWakeWord, ISTT, ITTS.

## 5. What data models/concepts exist?
VoiceSessionState, TranscriptionResult.

## 6. How does this specific subsystem work?
Continuous audio stream -> VAD -> Wake Word -> STT -> InputGateway -> Executive -> TTS -> Speaker. Barge-in triggers cancellation of current TTS/Task.

## 7. What depends on it?
Phase 16 (Personality/Character).

## 8. What is explicitly out of scope?
Godot character rendering and lip sync (Rhubarb).

## 9. What are the actual development tasks?
1. Implement `sounddevice` capture.
2. Integrate DeepFilterNet/Silero VAD.
3. Integrate openWakeWord.
4. Integrate `faster-whisper`.
5. Integrate Chatterbox TTS behind `ITTS` interface.
6. Implement Barge-in/cancellation.

## 10. What exact tests are required?
Audio routing tests, VAD threshold tests, STT mock tests, barge-in cancellation tests.

## 11. What real runtime validation is meaningful?
Speak the wake word and a command, verify STT transcribes it and Executive receives it. Verify TTS plays audio.

## 12. What constitutes success?
A seamless, local voice-in, voice-out pipeline with working barge-in.

## 13. What failures must block progression?
High latency (>2s STT), audio device locking, VAD failing to detect speech ends.

## 14. What documentation must be updated?
Update `MEMORY.md`, record latency benchmarks.

## 15. What does the next phase depend on?
Phase 8 provides the actual actions to execute.

## Technology Baseline
This phase must follow the approved technologies and provider boundaries defined in `../TECHNOLOGY.md`.
