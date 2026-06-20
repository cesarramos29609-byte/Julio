## 2026-06-20 - Persistent File Handle for Performance Logging
**Learning:** Switching from per-call file opening to a persistent file handle in `performance.py` improved logging latency from 0.1072 ms to 0.0146 ms per call (approx. 7x improvement). Lazy initialization and `atexit` ensure resources are managed correctly without overhead on module import.
**Action:** Always prefer persistent handles for high-frequency logging or telemetry to minimize OS syscall overhead.
