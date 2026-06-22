# BOLT'S JOURNAL - Géminis 2026

## 2026-06-22 - Persistent File Handle Optimization
**Learning:** In high-frequency logging scenarios like `record_performance`, opening and closing the file for every entry creates significant I/O overhead. Using a persistent file handle with lazy initialization and line buffering can drastically reduce latency.
**Action:** Transition `performance.py` to use a global persistent file handle managed with `atexit`.
