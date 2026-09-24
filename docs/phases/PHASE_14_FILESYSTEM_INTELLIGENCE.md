# Phase 14: Filesystem Intelligence

## 1. What is being introduced?
Capabilities and reasoning for discovering, reading, moving, and organizing local files.

## 2. Why is it introduced now?
Users need Omnix to manage their data. Requires specific safety boundaries (destructive actions) and path reasoning.

## 3. What components exist after this phase?
FilesystemAgent, FilesystemCapabilities.

## 4. What interfaces/contracts exist?
None.

## 5. What data models/concepts exist?
FileMetadata, PathInfo.

## 6. How does this specific subsystem work?
Capabilities use `pathlib`, `os`, `shutil`. `FilesystemAgent` reasons about directory structures. Safety Policy Engine strictly governs `delete`, `move`, and `overwrite` actions based on risk taxonomy.

## 7. What depends on it?
Tasks involving file manipulation.

## 8. What is explicitly out of scope?
Semantic vector indexing of all files. (Memory is Phase 15, and focuses on SQLite/FTS5).

## 9. What are the actual development tasks?
1. Implement filesystem capabilities (read, write, list, move, delete).
2. Implement `FilesystemAgent`.
3. Enforce strict Policy Engine rules for DESTRUCTIVE actions.
4. Implement file verification providers.

## 10. What exact tests are required?
Path traversal prevention tests, Policy Engine denial of destructive actions, file capability unit tests.

## 11. What real runtime validation is meaningful?
Ask Omnix to find all log files in a directory and move them to an archive folder, confirming the action.

## 12. What constitutes success?
Safe, deterministic file management without hallucinating paths.

## 13. What failures must block progression?
Allowing `rm -rf` equivalents without explicit confirmation, path traversal vulnerabilities.

## 14. What documentation must be updated?
Update `MEMORY.md`, `SECURITY.md`.

## 15. What does the next phase depend on?
Phase 15 for storing episodic memory.

## Technology Baseline
This phase must follow the approved technologies and provider boundaries defined in `../TECHNOLOGY.md`.
