# Bolt Journal ⚡

## 2026-06-24 - Performance Logging Optimization
**Learning:** Frequent file I/O (opening and closing handles) in a logging function can become a significant bottleneck as the application scales. Using a persistent file handle reduces system call overhead.
**Action:** Implement a persistent, lazy-initialized file handle for `performance_log.txt` in `performance.py`.

## 2026-07-18 - Thread-Safe Timestamp Caching
**Learning:** Implementing cached values (like formatted timestamps) reduces string-formatting and local-time generation overhead by up to 72% under high frequency. However, without a thread-safe double-checked lock pattern where variables are initialized on load and assigned in correct order (`_last_timestamp` before `_last_time_float`), multi-threaded environments can experience stale/empty reads or race conditions.
**Action:** Always pre-initialize caching states, lock on update using a double-checked pattern, and assign the cached string value before state/boundary markers.
