## 2026-06-25 - Persistent File Handle for Performance Logging
**Learning:** Implementing a persistent file handle with lazy initialization and thread safety significantly reduces I/O overhead in frequently called logging functions. In this environment, it reduced latency from ~0.0419ms to ~0.0194ms per call (approx. 53% improvement).
**Action:** Use persistent handles for high-frequency I/O operations, ensuring robust cleanup with `atexit` and thread safety with `threading.Lock`. Include fallbacks for cases where the handle might become invalid (e.g., file deletion).
