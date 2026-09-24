# Agent Development Guidelines (AGENTS.md)

This file contains the mandatory constitution for all coding agents (like Codex) and developers working on the Omnix project.

## MANDATORY PRE-FLIGHT CHECKLIST

**BEFORE modifying the project, you MUST read and understand:**
- `README.md`
- `docs/PRD.md`
- `docs/ARCHITECTURE.md`
- `docs/TECHNOLOGY.md`
- `docs/RULES.md`
- `docs/TASKS.md`
- `docs/DECISIONS.md`
- `docs/MEMORY.md`
- `docs/TEST_PLAN.md`
- `docs/SECURITY.md`
- The relevant `PHASE_XX_*.md` file in `docs/phases/`

## AGENT EXECUTION WORKFLOW

1. **Understand the requested task:** Clarify ambiguous requirements before writing code.
2. **Inspect existing implementation:** Do not assume project structure; check the filesystem and code.
3. **Identify architecture constraints:** Ensure your plan aligns with the `RULES.md` and the Phase documentation.
4. **Produce an implementation plan:** Share this plan if requested, or keep it internal but concrete.
5. **Modify only relevant areas:** Do not refactor unrelated systems or perform drive-by rewrites.
6. **Test:** Add and run tests alongside your implementation.
7. **Review:** Check your work against the Acceptance Criteria of the current Phase.
8. **Fix failures:** Resolve any regressions or test failures before proceeding.
9. **Update project documentation:** Update `docs/MEMORY.md` and any relevant ADRs in `docs/DECISIONS.md`.
10. **Report evidence:** Prove that the code works (e.g., via real runtime testing).


- **Before adding or replacing a technology dependency, read `TECHNOLOGY.md` and `DECISIONS.md`.**
- Do not silently substitute approved technology. If implementation testing shows an approved technology is unsuitable, report the evidence first. Then update the relevant ADR/documentation before changing architecture.

## CRITICAL DIRECTIVE

**Never silently reinterpret the architecture.**
If the requested work conflicts with the core architecture (e.g., you are asked to hardcode a command, or bypass safety, or give an LLM direct shell access):
**STOP and report the conflict.**
Do not create a parallel solution. Do not create a workaround. Enforce the architectural laws defined in `docs/RULES.md`.
