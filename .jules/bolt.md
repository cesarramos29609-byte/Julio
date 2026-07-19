# Bolt Journal ⚡

## 2026-06-24 - Performance Logging Optimization
**Learning:** Frequent file I/O (opening and closing handles) in a logging function can become a significant bottleneck as the application scales. Using a persistent file handle reduces system call overhead.
**Action:** Implement a persistent, lazy-initialized file handle for `performance_log.txt` in `performance.py`.

## 2026-07-19 - Thread-Safe Timestamp Caching & Write Splitting
**Learning:** High-frequency logging spends significant CPU time on string parsing and generation for timestamps (like `time.strftime`). Caching the formatted timestamp on a per-second boundary using a thread-safe double-checked lock avoids redundant CPU overhead under heavy concurrency. Additionally, splitting `sys.stdout.write` into multiple sequential calls avoids f-string interpolation allocation of large message bodies.
**Action:** Always pre-initialize timestamp cache flags on module load, assign the formatted timestamp before updating the second boundary flag to prevent readers from seeing stale/empty timestamps, and use split `sys.stdout.write` calls.
