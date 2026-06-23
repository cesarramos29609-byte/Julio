## 2026-06-23 - Persistent File Handle for Logging
**Learning:** Opening and closing a file for each log entry introduces significant I/O overhead. In Python, using a persistent file handle with `buffering=1` (line buffering) can improve logging performance by ~68% while still ensuring data is written promptly.
**Action:** Use a thread-safe, persistent file handle with `atexit` cleanup for high-frequency logging tasks.
