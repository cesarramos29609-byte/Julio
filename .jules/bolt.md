# Bolt Journal ⚡

## 2026-06-24 - Performance Logging Optimization
**Learning:** Frequent file I/O (opening and closing handles) in a logging function can become a significant bottleneck as the application scales. Using a persistent file handle reduces system call overhead.
**Action:** Implement a persistent, lazy-initialized file handle for `performance_log.txt` in `performance.py`.

## 2026-07-12 - Timestamp Caching in High-Frequency Logging
**Learning:** Even efficient calls like `time.strftime` can add measurable overhead when called thousands of times per second. Caching the formatted timestamp and updating it only when the system second changes (using `int(time.time())`) further reduces latency.
**Action:** Use timestamp caching for logging functions that are expected to be called in tight loops or high-frequency scenarios.
