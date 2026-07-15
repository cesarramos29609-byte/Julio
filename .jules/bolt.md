# Bolt Journal ⚡

## 2026-06-24 - Performance Logging Optimization
**Learning:** Frequent file I/O (opening and closing handles) in a logging function can become a significant bottleneck as the application scales. Using a persistent file handle reduces system call overhead.
**Action:** Implement a persistent, lazy-initialized file handle for `performance_log.txt` in `performance.py`.

## 2026-07-15 - Timestamp Caching and Write Splitting
**Learning:** Even efficient operations like `time.strftime` can be optimized by caching the result if the required precision is only one second. Additionally, splitting `sys.stdout.write` calls can be faster than f-string interpolation for large messages as it avoids redundant string allocations.
**Action:** Use `int(time.time())` to detect second-boundary crossings and cache formatted timestamps. Split console output into multiple `write` calls to avoid f-string overhead for combined strings.
