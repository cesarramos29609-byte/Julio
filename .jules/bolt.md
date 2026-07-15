# Bolt Journal ⚡

## 2026-06-24 - Performance Logging Optimization
**Learning:** Frequent file I/O (opening and closing handles) in a logging function can become a significant bottleneck as the application scales. Using a persistent file handle reduces system call overhead.
**Action:** Implement a persistent, lazy-initialized file handle for `performance_log.txt` in `performance.py`.

## 2026-07-15 - Timestamp Caching Optimization
**Learning:** Even fast operations like `time.strftime` can become a bottleneck when called in high-frequency loops. Caching the formatted timestamp and only updating it when the system second changes (via `int(time.time())`) significantly reduces latency.
**Action:** Use module-level variables to cache formatted timestamps for high-frequency logging utilities.
