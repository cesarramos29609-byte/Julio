# Bolt Journal ⚡

## 2026-06-24 - Performance Logging Optimization
**Learning:** Frequent file I/O (opening and closing handles) in a logging function can become a significant bottleneck as the application scales. Using a persistent file handle reduces system call overhead.
**Action:** Implement a persistent, lazy-initialized file handle for `performance_log.txt` in `performance.py`.

## 2026-07-20 - Hot Path Imports and Micro-optimizations Overhead
**Learning:** Performing dynamic imports and filesystem path resolutions (e.g., `os.path.abspath`) inside high-frequency class methods (like a circuit breaker's failure callback) introduces massive CPU overhead that completely degrades application latency. Additionally, splitting stream writes to avoid f-strings is a misguided micro-optimization that actually slows down I/O in Python due to duplicate method call overhead.
**Action:** Always import modules statically or at the module level rather than dynamically on hot paths. Keep stream writes as single unified calls using f-string interpolation rather than splitting them.
