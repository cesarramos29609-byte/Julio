# Bolt Journal ⚡

## 2026-06-24 - Performance Logging Optimization
**Learning:** Frequent file I/O (opening and closing handles) in a logging function can become a significant bottleneck as the application scales. Using a persistent file handle reduces system call overhead.
**Action:** Implement a persistent, lazy-initialized file handle for `performance_log.txt` in `performance.py`.

## 2026-06-29 - Micro-optimizing Python Logging Latency
**Learning:** In high-frequency logging paths, `time.strftime` with `time.localtime` is significantly faster than `datetime.datetime.now().strftime` due to reduced object creation. Furthermore, synchronous `print()` calls are a major bottleneck as they block on console I/O.
**Action:** Prefer `time.strftime` for timestamps in performance-critical paths and avoid synchronous console output for high-frequency logs.
