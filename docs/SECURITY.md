# Omnix Security and Safety Architecture (SECURITY.md)

## Security Goals
- Prevent unintended destructive actions on the user's computer.
- Prevent arbitrary code execution by hallucinating LLMs.
- Protect user privacy (screen, mic, files).
- Provide transparent authorization mechanisms.

## Threat Model
1. **LLM Hallucination**: Model invents a dangerous command.
2. **Prompt Injection**: A web page or document contains text instructing Omnix to perform malicious actions.
3. **Over-privileged Execution**: An agent exploits a generic capability to bypass intent.
4. **Data Exfiltration**: Sensitive on-screen data is sent to an untrusted third-party API.

## Trust Boundaries
- **User Input**: Untrusted (could contain prompt injection).
- **LLM Output (Plans/Reasoning)**: Untrusted. Must be validated.
- **Agent Output**: Untrusted.
- **Capability Router**: **TRUSTED**. This is the enforcement boundary.
- **Controlled Capabilities**: **TRUSTED**. These actually execute code.

## LLM Trust Model
The LLM is treated as an unreliable, untrusted reasoning engine. It cannot directly interact with the OS. It can only emit structured JSON requesting the execution of a registered Capability.

## Agent Permissions
Agents do not have permissions. They only propose plans.

## Capability Permissions
Capabilities are strictly typed and registered with a Risk Classification.

## Risk Categories
- **LOW RISK**: Read-only, local operations (e.g., get window list, read config).
- **SENSITIVE**: Reads private data (e.g., take screenshot, read user files).
- **DESTRUCTIVE**: Modifies or deletes state (e.g., close app, delete file).
- **IRREVERSIBLE**: Actions that cannot be undone (e.g., empty recycle bin, send email).
- **PRIVACY-SENSITIVE**: Records audio/video.
- **EXTERNAL-SIDE-EFFECT**: Interacts with the internet (e.g., post a tweet).

## User Authorization / Confirmation Policies
- LOW RISK: Auto-allow.
- SENSITIVE: Auto-allow (assuming user opted into AI assistant), but audited.
- DESTRUCTIVE: Requires explicit user confirmation ("Should I delete this?").
- IRREVERSIBLE: Requires explicit user confirmation.
- EXTERNAL-SIDE-EFFECT: Requires explicit user confirmation unless pre-authorized for a specific domain.

## Filesystem Safety
Generic filesystem capabilities must prevent directory traversal attacks (e.g., `../../Windows/System32`).

## Process Safety
Killing processes must be restricted. Omnix should not be able to kill critical OS processes (e.g., `csrss.exe`, `explorer.exe`).

## Shell Safety
**CRITICAL**: There is NO generic `execute_shell_command(string)` capability exposed to the LLM. If shell commands are needed, they must be pre-written in a specific Capability with parameterized inputs (e.g., `git_commit(message)`), and the inputs must be sanitized.

## Web Content / Prompt Injection
When reading web pages or untrusted files, the Context Engine must demarcate the content clearly to the LLM to prevent the content from overriding the system prompt (e.g., using delimiters or separate LLM calls for analysis).

## Network Safety
No generic `curl(url, method, body)` capability. External calls must go through specific Integrations.

## Credentials and Secrets
Credentials (API keys) are stored in `.env` or the OS Credential Manager. They are NEVER passed into the LLM prompt. Capabilities fetch secrets directly at execution time.

## Screen / Microphone Privacy
Clear visual indicators must be present when the screen is being captured or the mic is hot.

## Logging Privacy
Logs must not contain raw screenshots, API keys, or sensitive user text by default.

## Cancellation / Emergency Stop
A hardware/OS level interrupt (e.g., global hotkey) must immediately kill all active Capabilities and Agents.

## Agent Isolation
Agents cannot read each other's memory directly to prevent a compromised/hallucinating agent from poisoning others.

## Capability Validation
The Capability Router must strictly validate JSON schemas for all arguments before executing a capability.

## Audit Logging
All capability executions, especially SENSITIVE and above, must be logged with timestamp, requested agent, arguments, and outcome.


## Technology Security Implications
Security implications of the approved technology stack (Refer to `TECHNOLOGY.md`):
- **Ollama local model access**: Ensure local API is bound to localhost to prevent network exploitation. Ensure model files are safe.
- **Audio/Video**: Microphone access, screen capture (DXcam), wake-word audio, STT audio, and TTS output must be secured and clearly indicated to the user.
- **Godot IPC**: Ensure IPC mechanisms (e.g., local WebSocket/named pipe) authenticate or restrict connections to the Python Omnix process only.
- **Browser Automation**: Playwright profiles/sessions must be isolated to prevent accidental credential leakage or cookie hijacking.
- **Windows APIs & Clipboard**: Restrict arbitrary access; capability router must mediate clipboard reads/writes.
- **Storage & Config**: SQLite memory, logs, `.env` files must be protected. Prefer Windows Credential Manager / DPAPI for production secrets.
- **Third-Party**: Ensure downloaded models and third-party character/audio asset licenses are reviewed.
