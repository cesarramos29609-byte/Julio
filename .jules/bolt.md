# Bolt Journal ⚡

## 2026-06-24 - Performance Logging Optimization
**Learning:** Frequent file I/O (opening and closing handles) in a logging function can become a significant bottleneck as the application scales. Using a persistent file handle reduces system call overhead.
**Action:** Implement a persistent, lazy-initialized file handle for `performance_log.txt` in `performance.py`.

## 2026-07-11 - Timestamp Caching and I/O Optimization
**Learning:** For high-frequency logging, `time.strftime` can still be a bottleneck. Caching the formatted timestamp and only updating it when the integer second changes significantly reduces overhead. Additionally, splitting `sys.stdout.write` into separate calls for prefix and message avoids redundant string allocation/interpolation of large f-strings.
**Action:** Use timestamp caching and split I/O calls in performance-critical logging functions.
