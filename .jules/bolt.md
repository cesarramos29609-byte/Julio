# Bolt Journal ⚡

## 2026-06-24 - Performance Logging Optimization
**Learning:** Frequent file I/O (opening and closing handles) in a logging function can become a significant bottleneck as the application scales. Using a persistent file handle reduces system call overhead.
**Action:** Implement a persistent, lazy-initialized file handle for `performance_log.txt` in `performance.py`.

## 2026-06-25 - O(N) to O(1) Audit Summary Optimization
**Learning:** Performing list comprehension/summation over growing internal lists during summary or telemetry checks turns high-frequency lookups into O(N) bottlenecks. Tracking metrics with an incremental counter on write paths converts checks to O(1).
**Action:** Cache state values and maintain incremental/running counters during state-changing operations instead of scanning full datasets on read operations.
