# Bolt Journal ⚡

## 2026-06-24 - Performance Logging Optimization
**Learning:** Frequent file I/O (opening and closing handles) in a logging function can become a significant bottleneck as the application scales. Using a persistent file handle reduces system call overhead.
**Action:** Implement a persistent, lazy-initialized file handle for `performance_log.txt` in `performance.py`.

## 2026-07-24 - Circuit Breaker Read Caching & Dynamic Importing
**Learning:** High-frequency read queries on circuit breakers can degrade performance due to redundant calculation of properties (e.g., division operations on float boundaries). Calculating and caching these properties on state change turns hot-path reads into fast O(1) attribute lookups, reducing latency by over 50%. Additionally, dynamic lazy-loading of monitoring imports on the cold failure path avoids overhead on the hot success path and eliminates startup imports risk.
**Action:** Always cache calculated state properties on write-side updates and lazily import logging/telemetry tools on cold paths only.
