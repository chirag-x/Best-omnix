# Omnix Experience & UI Design

## 1. Core Experience Principle
Omnix is designed to feel like a tangible entity living on your desktop, not a terminal window or a chatbox. The experience is Voice-First and deeply integrated into the user's natural workflow.

## 2. Voice Experience
Voice interaction is the primary modality. Implemented through the approved TTS/STT stack defined in `TECHNOLOGY.md` (faster-whisper, Chatterbox, openWakeWord).
- **Barge-in**: Users can interrupt Omnix at any time by speaking or using a hotkey.
- **Latency**: Responses must be fast. Short acknowledgments (e.g., "On it") are preferred while complex tasks execute.

## 3. Visual Interface & Character
The primary UI is transparent/overlay based. 
- **Application UI**: PySide6/QML for settings, debug logs, and standard windowing needs.
- **Character**: A 3D avatar rendered in Godot 4, authored in Blender, with lip sync via Rhubarb.
- **Strict Separation**: The Character and UI are for **presentation only**. They must not directly control the computer, bypass the Policy Engine, or own intelligence loops. All execution runs through the Python Omnix Executive.

## 4. Emotional Expression
Omnix maps technical execution states to emotional/physical expressions.
- Task failed -> Confusion/Concern.
- Task succeeded -> Happy/Satisfied.
- Listening -> Attentive.
- Executing -> Focused.
This translation is handled by the Communication Agent mapping technical state to `CharacterState`.

## 5. Trust and Transparency
Users must trust Omnix.
- **Confirmation Prompts**: Before executing `DESTRUCTIVE` or `SENSITIVE` tasks, Omnix clearly asks for permission via UI or voice.
- **Visibility**: The user must be able to see what Omnix is doing (e.g., via a subtle status overlay or task graph visualization in the PySide6 UI).

## 6. Desktop Integration
Omnix operates directly on the user's desktop, moving the mouse and typing when necessary, but preferring background API calls (like UIA) when possible to avoid wrestling for control of the input devices.
