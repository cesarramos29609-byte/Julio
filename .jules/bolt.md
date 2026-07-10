# Bolt Journal ⚡

## 2026-06-24 - Performance Logging Optimization
**Learning:** Frequent file I/O (opening and closing handles) in a logging function can become a significant bottleneck as the application scales. Using a persistent file handle reduces system call overhead.
**Action:** Implement a persistent, lazy-initialized file handle for `performance_log.txt` in `performance.py`.

## 2026-07-10 - Micro-optimization of Logging Utilities
**Learning:** Significant latency reduction (over 50%) can be achieved in logging utilities by replacing 'datetime' with 'time.strftime' (avoiding redundant Python-level function calls) and using 'sys.stdout.write' instead of 'print'.
**Action:** Always prefer 'time.strftime' for high-frequency timestamping and 'sys.stdout.write' for protocol-heavy output paths.
