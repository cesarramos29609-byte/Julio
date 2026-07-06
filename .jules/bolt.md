# Bolt Journal ⚡

## 2026-06-24 - Performance Logging Optimization
**Learning:** Frequent file I/O (opening and closing handles) in a logging function can become a significant bottleneck as the application scales. Using a persistent file handle reduces system call overhead.
**Action:** Implement a persistent, lazy-initialized file handle for `performance_log.txt` in `performance.py`.

## 2026-07-06 - Optimized Timestamp and I/O Overhead
**Learning:** `time.strftime` is significantly faster than `datetime.datetime.now().strftime` for generating formatted timestamps in Python. Additionally, minimizing string concatenations by pre-calculating templates and using `sys.stdout.write` instead of `print()` can reduce logging latency by over 50%.
**Action:** Replace `datetime` with `time.strftime` and optimize message formatting and stdout I/O in high-frequency logging paths.
