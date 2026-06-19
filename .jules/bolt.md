## 2025-05-22 - Persistent File Handle Optimization
**Learning:** Opening and closing a file on every log entry in `performance.py` introduces significant I/O overhead. Using a persistent file handle improves latency by ~50-75%.
**Action:** Implement a persistent file handle with lazy initialization and thread-safety for logging.
