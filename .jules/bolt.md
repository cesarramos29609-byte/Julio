# Bolt Journal ⚡

## 2026-06-24 - Performance Logging Optimization
**Learning:** Frequent file I/O (opening and closing handles) in a logging function can become a significant bottleneck as the application scales. Using a persistent file handle reduces system call overhead.
**Action:** Implement a persistent, lazy-initialized file handle for `performance_log.txt` in `performance.py`.

## 2026-07-13 - Timestamp Caching for High-Frequency Logging
**Learning:** Even efficient calls like `time.strftime` can accumulate significant overhead when called thousands of times per second. Caching the formatted timestamp and only updating it when the system second changes reduces call frequency to at most once per second.
**Action:** Use a module-level cache for timestamps in `performance.py` and update it conditionally based on `int(time.time())`.
