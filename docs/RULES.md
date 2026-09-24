# Omnix Architectural Rules

This document outlines the strict architectural laws that govern Omnix development.

## 1. Single Model Architecture
1. **Agent != Model**: Agents are architectural roles, not separate LLM instances.
2. **One Intelligence Baseline**: Omnix uses a single shared Gemma 4 31B model for all cognitive roles (Brain, Planner, Vision, Recovery). Do not introduce a second intelligence model (e.g., for embeddings or vision) without an ADR.

## 2. Safety and Policy
3. **Deterministic Policy Engine**: The Policy Engine is the absolute authority on side-effect execution.
4. **No LLM Overrides**: AI reasoning (e.g., a Safety Agent) cannot override a deterministic DENY from the Policy Engine.
5. **No Unrestricted Shell**: There is no global unrestricted shell toggle (e.g., `ENABLE_SHELL_EXECUTION`). All actions must pass through the Capability Router.
6. **Safety Precedes Action**: The safety architecture must exist before side-effecting computer capabilities are implemented.

## 3. Verification and Recovery
7. **Deterministic-First Verification**: Verification must prioritize deterministic OS checks (Process, Window). Only fallback to AI reasoning when evidence is UNCERTAIN.
8. **Verification is Mandatory**: Omnix must not blindly assume its actions succeed.

## 4. State and Memory
9. **No Mutable Global Singleton**: The World State must use versioned snapshots (`WorldStateStore`), not a global mutable singleton.
10. **SQLite/FTS5 Baseline**: Use SQLite and FTS5 for memory. Do not introduce a vector database without ADR approval.

## 5. Planning and Execution
11. **PlanRevisions**: Plans are acyclic graphs. Replanning creates a new `PlanRevision`. Do not use cyclic graphs for execution.
12. **Canonical Execution**: All interactions must route through the Omnix Executive and Capability Router.
13. **No App-Specific Macros**: Do not hardcode natural language to specific capabilities (e.g., `if command == "open chrome"`).
14. **Capabilities are Controlled**: Capabilities are either READ_ONLY or SIDE_EFFECTING, and explicitly defined via contracts.

## 6. Components and Dependencies
15. **Presentation Separation**: The character renderer (Godot) or UI (PySide6) must not own intelligence or directly control the computer outside the canonical runtime.
16. **No Peer-to-Peer Agent Swarms**: All multi-agent collaboration routes through the Executive.
17. **Provider Abstractions**: Third-party APIs (Ollama, Playwright, Chatterbox) must remain behind provider interfaces.

## 7. Technology Governance
18. Read `TECHNOLOGY.md` before adding a dependency.
19. Do not replace approved technologies silently.
20. Do not downgrade Python (target 3.13.15) or replace `.venv`.
21. Check licenses and compatibility before redistribution.
22. Record permanent technology changes in `DECISIONS.md` and update `TECHNOLOGY.md`.

## 8. Documentation Integrity
23. **Markdown is Authoritative**: Do not create new code-generation scripts that rewrite authoritative documentation without explicit approval.
24. **No Boilerplate Placeholders**: Do not leave architectural 'TBD' or 'To be defined' placeholders in phase documents before implementation.
