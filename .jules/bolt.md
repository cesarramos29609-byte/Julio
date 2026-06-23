# Bolt's Journal - Critical Learnings

## 2025-05-15 - [Persistent File Handles for Logging]
**Learning:** In Python, repeatedly opening and closing a file for logging (using 'with open(...) as f') introduces significant I/O overhead, especially when logging frequently. Using a persistent file handle with lazy initialization and atexit cleanup can reduce latency by over 60%.
**Action:** Always prefer persistent file handles for performance-critical logging paths, ensuring thread safety and proper resource cleanup.
