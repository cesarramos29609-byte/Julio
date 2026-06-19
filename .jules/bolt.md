# Bolt's Journal - Critical Learnings

## 2025-05-15 - [Persistent File Handle Optimization]
**Learning:** Repeatedly opening and closing a file for logging in a hot path (like `record_performance`) introduces significant I/O overhead. Using a persistent file handle with lazy initialization and thread-safety improves throughput.
**Action:** Always prefer persistent handles for high-frequency logging, ensuring proper cleanup with `atexit` and thread-safety with `threading.Lock`.
