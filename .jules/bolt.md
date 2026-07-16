# Bolt Journal ⚡

## 2026-06-24 - Performance Logging Optimization
**Learning:** Frequent file I/O (opening and closing handles) in a logging function can become a significant bottleneck as the application scales. Using a persistent file handle reduces system call overhead.
**Action:** Implement a persistent, lazy-initialized file handle for `performance_log.txt` in `performance.py`.

## 2026-07-16 - Timestamp Caching and Thread Safety
**Learning:** `time.strftime` is fast, but calling it thousands of times per second is redundant. Caching the string and only updating it when the system second changes can save ~20% latency in high-frequency logging. However, global caching requires thread safety via locks to prevent race conditions.
**Action:** Use a `threading.Lock` and double-checked locking to cache formatted timestamps in module-level variables.
