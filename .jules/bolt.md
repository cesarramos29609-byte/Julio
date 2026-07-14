# Bolt Journal ⚡

## 2026-06-24 - Performance Logging Optimization
**Learning:** Frequent file I/O (opening and closing handles) in a logging function can become a significant bottleneck as the application scales. Using a persistent file handle reduces system call overhead.
**Action:** Implement a persistent, lazy-initialized file handle for `performance_log.txt` in `performance.py`.

## 2026-06-24 - Timestamp Caching in High-Frequency Logging
**Learning:** In high-frequency logging paths, repeated calls to `time.strftime` (or `datetime.now().strftime`) introduce measurable overhead. Caching the formatted timestamp and only updating it when the system second changes can significantly reduce latency.
**Action:** Use a simple module-level cache (`_last_time_int` and `_last_timestamp`) to store the formatted time and avoid redundant formatting calls within the same second.
