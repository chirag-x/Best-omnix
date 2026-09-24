# Phase 0: Blueprint + Architecture + Technology

## 1. What is being introduced?
The foundational architectural documentation, blueprints, rulesets, and technology selection for the entire Omnix project.

## 2. Why is it introduced now?
To ensure no ambiguity exists before implementation begins. Coding agents must have a unified, strict understanding of the system's design, boundaries, and dependencies.

## 3. What components exist after this phase?
No runtime components. Only markdown documentation (README, PRD, ARCHITECTURE, TECHNOLOGY, DESIGN, RULES, TASKS, DECISIONS, MEMORY, TEST_PLAN, SECURITY, AGENTS) and canonical phase specifications.

## 4. What interfaces/contracts exist?
None (documentation only).

## 5. What data models/concepts exist?
None (documentation only).

## 6. How does this specific subsystem work?
By reading the documents, developers and agents understand the strict single-model architecture, the deterministic safety/verification engines, the acyclic PlanRevision models, the SQLite/FTS5 memory limits, and the exact dependency tree.

## 7. What depends on it?
Every subsequent implementation phase (Phases 1-20).

## 8. What is explicitly out of scope?
Writing Python code, installing packages, testing real runtimes, configuring real LLMs.

## 9. What are the actual development tasks?
1. Write PRD.
2. Write ARCHITECTURE.
3. Write TECHNOLOGY.
4. Write DECISIONS.
5. Write RULES.
6. Generate specific phase files.
7. Resolve all conflicting statements across documentation.

## 10. What exact tests are required?
Documentation completeness validation. Link validation. Consistency review. Architecture dependency review. Forbidden-pattern review.

## 11. What real runtime validation is meaningful?
No real runtime validation required. Success is based on architectural clarity and human approval.

## 12. What constitutes success?
A fully consistent set of documentation without 'TBD' placeholders, contradictory architectures, or missing dependency rules.

## 13. What failures must block progression?
Contradictions regarding the LLM model strategy, presence of global shell execution switches, missing architectural dependencies, or vague phase documents block progression.

## 14. What documentation must be updated?
All core markdown files in the root and `docs/`.

## 15. What does the next phase depend on?
Phase 1 depends on this exact blueprint to begin coding.

## Technology Baseline
This phase must follow the approved technologies and provider boundaries defined in `../TECHNOLOGY.md`.
