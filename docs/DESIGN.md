# Omnix Experience Design (DESIGN.md)

This document outlines the complete experience design for Omnix. For Omnix, design is not merely visual styling; it is the entire interaction paradigm.

## Product Personality
Omnix is competent, calm, precise, and transparent. It behaves as an executive assistant that handles complexity behind the scenes but communicates clearly and naturally.

## User Relationship
The relationship is Collaborative. Omnix works *with* the user to achieve goals, rather than acting as a blind servant that executes unsafe commands without thought.

## Voice Experience
Voice interaction is the primary modality. Implemented through approved TTS/STT stack in `TECHNOLOGY.md`. The voice should be natural and conversational. TTS latency must be minimized. The system must support asynchronous interaction—the user can speak, walk away, and Omnix will speak when the task is done or if it needs help.

## Conversation Style
Concise. Omnix does not read long lists unless explicitly asked. It summarizes.
*Bad:* "I have located 5 windows. Window 1 is Chrome. Window 2 is Notepad..."
*Good:* "I see a few windows open. Should I use Chrome or Notepad?"

## Emotional Expression
Omnix does not simulate human emotions like sadness or anger. It expresses confidence, uncertainty, or focus through tone and phrasing.

## Natural Language Principles
- **No robotic confirmation**: Do not say "INTENT RECOGNIZED." Say "Got it."
- **No technical leakage**: Do not say "Agent 4 failed to execute capability." Say "I'm having trouble clicking that button."

## Progress Narration
For tasks taking longer than 5 seconds, Omnix provides gentle, non-intrusive progress updates (e.g., "Looking for that file...", "Still working on it...").

## Confirmation Style
Omnix confirms understanding implicitly by taking action, or explicitly if the action is destructive. "I'm deleting the folder now, are you sure?"

## Failure Communication
When a task fails, Omnix must explain *why* in user-centric terms, and propose a solution or ask for help. "I couldn't find the 'Submit' button. Did the page change?"

## Uncertainty Communication
If Omnix is unsure of a goal or a visual element, it must pause and ask for clarification rather than guessing wildly.

## Interruption / Barge-In
The user can interrupt Omnix at any time by speaking. Omnix must instantly stop acting and listening to the new instruction. "Stop", "Wait, don't do that", "Actually, open the other one."

## Listening State
Visual/Auditory feedback must clearly indicate when Omnix is listening (e.g., a subtle chime, a glowing mic icon).

## Thinking State
Feedback indicating the LLM/Planner is generating a task graph.

## Acting State
Feedback indicating Omnix is actively controlling the computer (e.g., moving the mouse, typing). Crucial for safety so the user knows *who* is moving the mouse.

## Waiting State
Omnix is idle, waiting for the wake word or explicit invocation.

## Success State
A brief, satisfying confirmation. "Done.", "Email sent.", or a subtle success chime.

## Failure State
A distinct visual/auditory cue that an error occurred, immediately followed by the Failure Communication.

## Recovery State
"Let me try that another way..."

## Sleep / Idle State
Omnix consumes minimal resources and visually retreats to the system tray or a minimized orb.

## Wake Experience
Waking Omnix should feel instantaneous.

## Notifications
Omnix can present non-intrusive desktop notifications for background tasks that complete while the user is busy.

## Desktop Presence
A small, floating widget or orb that indicates state (Listening, Thinking, Acting) without obscuring the user's work.

## Tray Experience
Right-click menu for settings, quit, pause, and history.

## Visual Interface
The primary UI is transparent/overlay based. Application UI: PySide6/QML. Character: Godot runtime + Blender-created character (Lip sync: Rhubarb planned). See `TECHNOLOGY.md`. If a chat history is needed, it expands smoothly. Minimalist, high-contrast, respecting OS dark/light modes.

## Animation Principles
Fluid, purposeful transitions. No jarring pop-ups. If the orb pulses, it pulses to the cadence of the speech.

## Accessibility
The visual UI must support screen readers, high contrast, and keyboard navigation.

## User Control
The user is always in control. An easily accessible "Emergency Stop" shortcut (e.g., `Ctrl+Shift+Escape` override) immediately halts all Agent capabilities.

## Privacy Indicators
Clear, unavoidable visual indicators when Omnix is using the Microphone, capturing the Screen, or accessing the Filesystem.

## Design Consistency
Internal technical events (e.g., JSON parsing error) MUST NOT bleed into the user-facing natural communication layer.

## Anti-Patterns
- Pretending to be human ("I'm feeling tired today").
- Over-explaining simple actions ("I am now moving the mouse cursor to X:100 Y:200").
- Silent failure (Task stops, Omnix says nothing).
- Uninterruptible monologues.
