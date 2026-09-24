# Phase 15: Memory

## 1. What is being introduced?
Working, conversational, and episodic memory using SQLite and FTS5.

## 2. Why is it introduced now?
Omnix must remember user preferences and past task context. We use SQLite/FTS5 to avoid the overhead of vector DBs/embedding models.

## 3. What components exist after this phase?
MemoryManager, SQLiteDatabase, FTS5Indexer.

## 4. What interfaces/contracts exist?
IMemoryStore.

## 5. What data models/concepts exist?
MemoryEntry, MemoryMetadata, ConversationContext.

## 6. How does this specific subsystem work?
Important observations, task outcomes, and user facts are stored in SQLite. Retrieval uses FTS5 text search, timestamps, and entity tags. The Model Manager injects relevant memories into Gemma's context window.

## 7. What depends on it?
Long-term personalization.

## 8. What is explicitly out of scope?
Vector databases, dedicated embedding AI models.

## 9. What are the actual development tasks?
1. Initialize SQLite schema with FTS5.
2. Implement `MemoryManager` (store/retrieve/forget).
3. Integrate memory retrieval into the Executive/Model Manager context preparation.
4. Implement privacy/forget semantics.

## 10. What exact tests are required?
SQLite CRUD tests, FTS5 search relevance tests, forget/delete compliance tests.

## 11. What real runtime validation is meaningful?
Tell Omnix a fact, restart the application, and ask Omnix to recall the fact.

## 12. What constitutes success?
Reliable text-based memory retrieval without heavy ML overhead.

## 13. What failures must block progression?
Database locking, unmanaged context window bloat, failure to delete memories when requested.

## 14. What documentation must be updated?
Update `MEMORY.md`.

## 15. What does the next phase depend on?
Phase 16 uses memory for conversational personality.

## Technology Baseline
This phase must follow the approved technologies and provider boundaries defined in `../TECHNOLOGY.md`.
