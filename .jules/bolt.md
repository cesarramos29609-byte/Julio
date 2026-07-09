# Bolt Journal ⚡

## 2026-06-24 - Performance Logging Optimization
**Learning:** Frequent file I/O (opening and closing handles) in a logging function can become a significant bottleneck as the application scales. Using a persistent file handle reduces system call overhead.
**Action:** Implement a persistent, lazy-initialized file handle for `performance_log.txt` in `performance.py`.

## 2026-06-28 - Latency reduction in high-frequency logging
**Learning:** Console I/O (synchronous `print()`) and `datetime` object creation are significant bottlenecks in high-frequency paths. `time.strftime` with `time.localtime` is notably faster than `datetime.datetime.now().strftime`.
**Action:** Remove synchronous prints and use `time` module for timestamping in performance-critical logging functions.
