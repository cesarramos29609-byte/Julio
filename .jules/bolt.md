# Bolt Journal ⚡

## 2026-06-24 - Performance Logging Optimization
**Learning:** Frequent file I/O (opening and closing handles) in a logging function can become a significant bottleneck as the application scales. Using a persistent file handle reduces system call overhead.
**Action:** Implement a persistent, lazy-initialized file handle for `performance_log.txt` in `performance.py`.

## 2026-07-23 - Thread-Safe Timestamp Caching with Double-Checked Locking
**Learning:** High-frequency logging functions often spend a significant portion of execution time formatting current timestamps (e.g. calling `time.strftime` repeatedly). Implementing thread-safe, double-checked lock caching aligned to second boundaries (`time.time() // 1`) completely eliminates redundant formatting calls. To ensure other threads don't see inconsistent state under high concurrency, the formatted string variable must always be assigned before updating the time boundary flag.
**Action:** Implement module-level thread-safe cached variables and update them atomically using double-checked locking in critical-path utilities.
