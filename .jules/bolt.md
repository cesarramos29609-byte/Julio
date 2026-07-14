# Bolt Journal ⚡

## 2026-06-24 - Performance Logging Optimization
**Learning:** Frequent file I/O (opening and closing handles) in a logging function can become a significant bottleneck as the application scales. Using a persistent file handle reduces system call overhead.
**Action:** Implement a persistent, lazy-initialized file handle for `performance_log.txt` in `performance.py`.

## 2026-07-14 - Timestamp Caching and Split I/O
**Learning:** For high-frequency telemetry, calling `time.strftime` on every call is redundant if the precision is in seconds. Caching the formatted timestamp and only updating it when the second changes significantly reduces latency. Additionally, splitting `sys.stdout.write` calls can be slightly faster than f-string interpolation for large constant prefixes.
**Action:** Use a simple `if now_int != _last_time_int` check to cache timestamps in performance-critical logging functions.
