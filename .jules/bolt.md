# Bolt Journal ⚡

## 2026-06-24 - Performance Logging Optimization
**Learning:** Frequent file I/O (opening and closing handles) in a logging function can become a significant bottleneck as the application scales. Using a persistent file handle reduces system call overhead.
**Action:** Implement a persistent, lazy-initialized file handle for `performance_log.txt` in `performance.py`.

## 2026-07-24 - Double-Checked Locking Timestamp Cache
**Learning:** High-frequency logging can be throttled by Python's `time.strftime` overhead. Caching timestamps with a fast `time.time() // 1` boundary and double-checked locking avoids thread race conditions while bypassing formatting calls on identical seconds.
**Action:** Implement thread-safe timestamp caching with lock pre-initialization, assigning the cached timestamp before updating the time float boundary to protect concurrent readers from stale data.
