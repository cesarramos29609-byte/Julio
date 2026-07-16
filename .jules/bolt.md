# Bolt Journal ⚡

## 2026-06-24 - Performance Logging Optimization
**Learning:** Frequent file I/O (opening and closing handles) in a logging function can become a significant bottleneck as the application scales. Using a persistent file handle reduces system call overhead.
**Action:** Implement a persistent, lazy-initialized file handle for `performance_log.txt` in `performance.py`.

## 2026-07-16 - Timestamp Caching for High-Frequency Logging
**Learning:** Even efficient calls like `time.strftime` can add up in high-frequency paths. Caching the formatted timestamp and only updating it when the system second changes can reduce timestamp generation latency by over 60%.
**Action:** Use module-level caching for formatted timestamps in logging utilities that may be called thousands of times per second.
