# Bolt Journal ⚡

## 2026-06-24 - Performance Logging Optimization
**Learning:** Frequent file I/O (opening and closing handles) in a logging function can become a significant bottleneck as the application scales. Using a persistent file handle reduces system call overhead.
**Action:** Implement a persistent, lazy-initialized file handle for `performance_log.txt` in `performance.py`.

## 2026-07-13 - Timestamp Caching and Split I/O
**Learning:** Even with persistent handles, redundant `time.strftime` calls and large string allocations for output can limit logging performance. Caching the formatted timestamp and splitting `sys.stdout.write` calls to avoid interpolation can provide a measurable boost.
**Action:** Use a module-level cache for timestamps (updating only when `int(time.time())` changes) and split prefix/message output calls in high-frequency logging paths.
