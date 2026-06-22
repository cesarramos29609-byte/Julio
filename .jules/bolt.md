## 2025-05-15 - Optimize performance logging with persistent handle
**Learning:** Using a persistent file handle instead of repeatedly opening and closing a log file significantly reduces I/O overhead. In this environment, it reduced latency by ~56% (from 0.0433ms to 0.0189ms).
**Action:** Always prefer persistent handles for logging or frequent file operations, ensuring thread-safety and proper resource cleanup with `atexit`.
