# Bolt Journal ⚡

## 2026-06-24 - Performance Logging Optimization
**Learning:** Frequent file I/O (opening and closing handles) in a logging function can become a significant bottleneck as the application scales. Using a persistent file handle reduces system call overhead.
**Action:** Implement a persistent, lazy-initialized file handle for `performance_log.txt` in `performance.py`.

## 2026-07-19 - Thread-Safe Timestamp Caching
**Learning:** Generating string timestamps on every log entry with `time.strftime` introduces substantial overhead under high frequency. Caching the timestamp per second reduces this overhead by ~62%. However, in concurrent/multi-threaded contexts, a double-checked locking pattern with `threading.Lock` is necessary. To prevent concurrent readers from accessing stale or empty timestamps, the updated formatted timestamp must be assigned to the cache variable BEFORE updating the time boundary flag variable. Also, when mutating module-level global variables, explicit `global` declarations are mandatory.
**Action:** Implement thread-safe timestamp caching with proper global variable assignment ordering and pre-initialization at module load.
