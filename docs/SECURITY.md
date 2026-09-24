# Omnix Security and Safety Model

## 1. Safety Architecture
Omnix operates with a strict separation between intelligence and enforcement. 
- **Policy Engine**: The absolute, deterministic authority that enforces safety boundaries based on risk taxonomy.
- **Safety Agent**: An LLM-backed agent that can advise on ambiguity, provide contextual risk interpretation, and assist classification, but can NEVER override the Policy Engine.

## 2. Capability Router and Authorization
The `CapabilityRouter` sits between the Omnix Executive and OS Execution. 
- Every capability declares its `CapabilityEffectType` (READ_ONLY or SIDE_EFFECTING).
- The Router passes the request to the Policy Engine. 
- The Policy Engine returns an authorization decision (ALLOW, DENY, REQUIRE_CONFIRMATION).
- **LLM output cannot bypass this enforcement.** There is no global unrestricted shell toggle (e.g., `ENABLE_SHELL_EXECUTION`).

## 3. Canonical Risk Taxonomy
Omnix uses a single canonical risk taxonomy across all documentation and capability metadata:
- `LOW_RISK`: Safe to execute autonomously (e.g., reading window titles).
- `SENSITIVE`: Requires context or mild scrutiny (e.g., reading emails).
- `DESTRUCTIVE`: Modifies or deletes data (e.g., deleting a file).
- `IRREVERSIBLE`: Actions that cannot be undone (e.g., emptying trash).
- `PRIVACY_SENSITIVE`: Accessing personal identifying info (e.g., passwords, cameras).
- `EXTERNAL_SIDE_EFFECT`: Interacting with the outside world (e.g., sending an email, posting online).

## 4. Technology Security Implications
Security implications of the approved technology stack:
- **Ollama local model access**: Ensure local API is bound to localhost to prevent network exploitation.
- **Audio/Video**: Microphone access, screen capture (DXcam), wake-word audio, STT audio, and TTS output must be secured and clearly indicated to the user.
- **Godot IPC**: Ensure IPC mechanisms (e.g., local WebSocket/named pipe) authenticate or restrict connections to the Python Omnix process only.
- **Browser Automation**: Playwright profiles/sessions must be isolated to prevent accidental credential leakage or cookie hijacking.
- **Windows APIs & Clipboard**: Restrict arbitrary access; Capability Router must mediate clipboard reads/writes.
- **Storage & Config**: SQLite memory, logs, `.env` files must be protected. Prefer Windows Credential Manager / DPAPI for production secrets.
- **Third-Party**: Ensure downloaded models and third-party character/audio asset licenses are reviewed.
