## 2026-06-26 - Optimized Performance Logging with Persistent Handle
**Learning:** In high-frequency logging scenarios, the overhead of opening and closing file handles synchronously for every write, combined with console I/O (`print()`), can be a significant bottleneck. Moving to a persistent, thread-safe file handle with line buffering significantly reduces latency.
**Action:** Use persistent file handles and lazy initialization for logging utilities. Avoid synchronous console output in performance-critical paths.
