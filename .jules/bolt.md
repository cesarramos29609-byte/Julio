## 2026-06-17 - Persistent File Handle for Logging
**Learning:** Using a persistent file handle instead of opening/closing the file for every log entry significantly reduces I/O overhead, especially when logging frequently.
**Action:** Use a global handle with lazy initialization and atexit for cleanup.
