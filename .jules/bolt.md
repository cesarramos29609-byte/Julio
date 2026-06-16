# Bolt's Journal - Critical Learnings

## 2026-06-16 - Persistent File Handle Optimization
**Learning:** Switching from opening/closing a file on every log call to using a persistent file handle significantly reduces I/O overhead and improves latency, especially in high-frequency logging scenarios. Lazy initialization is crucial to handle environments where the log file might be deleted or moved during runtime.
**Action:** Use a persistent, thread-safe file handle with `atexit` cleanup for logging in `performance.py`.
