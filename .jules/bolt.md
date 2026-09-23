# Bolt Journal ⚡

## 2026-06-24 - Performance Logging Optimization
**Learning:** Frequent file I/O (opening and closing handles) in a logging function can become a significant bottleneck as the application scales. Using a persistent file handle reduces system call overhead.
**Action:** Implement a persistent, lazy-initialized file handle for `performance_log.txt` in `performance.py`.

## 2026-06-25 - Audit Protocol O(1) Optimization
**Learning:** Checking or verifying logs incrementally during status/state updates using internal tracking avoids O(N) list-iteration lookups (like sum generators) on frequent calls, converting O(N) tasks into O(1) operations.
**Action:** Always maintain incremental running statistics or counters within state tracker instances instead of iterating over historical records to generate summaries.

## 2026-09-23 - Python File Handle Truthiness and Getter Encapsulation
**Learning:** In Python, closed file objects still evaluate as truthy (`bool(file_obj) == True`). Bypassing getter functions like `_get_log_handle()` with short-circuiting like `_log_handle or _get_log_handle()` prevents reopening closed handles and breaks lifecycle management for negligible frame overhead savings.
**Action:** Always rely on getter functions for resource handle management rather than bypassing encapsulation with boolean short-circuiting.
