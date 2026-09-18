# Bolt Journal ⚡

## 2026-06-24 - Performance Logging Optimization
**Learning:** Frequent file I/O (opening and closing handles) in a logging function can become a significant bottleneck as the application scales. Using a persistent file handle reduces system call overhead.
**Action:** Implement a persistent, lazy-initialized file handle for `performance_log.txt` in `performance.py`.

## 2026-06-25 - Audit Protocol O(1) Optimization
**Learning:** Checking or verifying logs incrementally during status/state updates using internal tracking avoids O(N) list-iteration lookups (like sum generators) on frequent calls, converting O(N) tasks into O(1) operations.
**Action:** Always maintain incremental running statistics or counters within state tracker instances instead of iterating over historical records to generate summaries.

## 2026-09-18 - Fast-Path Persistent Handle Retrieval
**Learning:** Checking global `_log_handle` directly via short-circuiting (`_log_handle or _get_log_handle()`) bypasses function frame allocation and call overhead on hot logging paths, reducing handle retrieval overhead by ~32%.
**Action:** Use short-circuit evaluation for initialized persistent handles on high-frequency paths, and ensure global variables are scoped so error handlers can safely reset state.
