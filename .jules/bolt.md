# Bolt Journal ⚡

## 2026-06-24 - Performance Logging Optimization
**Learning:** Frequent file I/O (opening and closing handles) in a logging function can become a significant bottleneck as the application scales. Using a persistent file handle reduces system call overhead.
**Action:** Implement a persistent, lazy-initialized file handle for `performance_log.txt` in `performance.py`.

## 2026-07-05 - Advanced Hot-Path Logging Optimization
**Learning:** Even with persistent handles, overhead from `datetime.datetime.now()`, `print()` buffering, and redundant string concatenations adds measurable latency. `time.strftime` is significantly faster than `datetime`, and `sys.stdout.write` avoids the overhead of `print`'s argument processing.
**Action:** Use `time.strftime` for timestamps and `sys.stdout.write` for console output in high-frequency logging paths. Pre-calculate the full message including newlines to minimize I/O calls.
