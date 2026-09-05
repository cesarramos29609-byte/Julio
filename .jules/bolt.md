# Bolt Journal ⚡

## 2026-06-24 - Performance Logging Optimization
**Learning:** Frequent file I/O (opening and closing handles) in a logging function can become a significant bottleneck as the application scales. Using a persistent file handle reduces system call overhead.
**Action:** Implement a persistent, lazy-initialized file handle for `performance_log.txt` in `performance.py`.

## 2026-06-25 - Audit Protocol O(1) Optimization
**Learning:** Checking or verifying logs incrementally during status/state updates using internal tracking avoids O(N) list-iteration lookups (like sum generators) on frequent calls, converting O(N) tasks into O(1) operations.
**Action:** Always maintain incremental running statistics or counters within state tracker instances instead of iterating over historical records to generate summaries.

## 2026-09-05 - Avoid Micro-Optimizing CPython Primitive Division
**Learning:** Short-circuiting basic floating-point arithmetic (e.g. `self.failures == 0` check before division) in property getters introduces extra branch overhead and attribute lookups, especially when `failures > 0`, without offering real-world speedups since Python dynamic attribute lookup dominates execution time over C-level division.
**Action:** Avoid short-circuiting basic primitive operations unless there is a proven heavy calculation or I/O bottleneck.
