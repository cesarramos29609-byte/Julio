# Bolt's Journal - Critical Learnings

## 2025-06-26 - Persistent File Handle Optimization
**Learning:** Opening and closing a file handle for every log entry in high-frequency operations creates significant I/O overhead. Synchronous console printing also acts as a bottleneck.
**Action:** Use a persistent, thread-safe file handle with lazy initialization and remove console print for performance-critical logging.
