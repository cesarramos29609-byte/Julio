# Bolt Journal ⚡

## 2026-06-24 - Performance Logging Optimization
**Learning:** Frequent file I/O (opening and closing handles) in a logging function can become a significant bottleneck as the application scales. Using a persistent file handle reduces system call overhead.
**Action:** Implement a persistent, lazy-initialized file handle for `performance_log.txt` in `performance.py`.

## 2026-06-28 - Console I/O and Timestamp Optimization
**Learning:** In high-frequency logging paths, synchronous `print()` calls to stdout can be a major bottleneck due to console I/O blocking. Additionally, `time.strftime` with `time.localtime` is measurably faster than `datetime.now().strftime`.
**Action:** Remove synchronous print statements in performance-critical paths and prefer `time.strftime` for timestamp generation.
