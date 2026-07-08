# Bolt Journal ⚡

## 2026-06-24 - Performance Logging Optimization
**Learning:** Frequent file I/O (opening and closing handles) in a logging function can become a significant bottleneck as the application scales. Using a persistent file handle reduces system call overhead.
**Action:** Implement a persistent, lazy-initialized file handle for `performance_log.txt` in `performance.py`.

## 2026-07-02 - Fast Timestamp Generation in Python
**Learning:** `time.strftime` (wrapping the C library) is significantly faster than `datetime.datetime.now().strftime` because it avoids the overhead of creating high-level Python `datetime` objects. Additionally, pre-calculating the log message string with its newline prevents redundant allocations during repeated I/O.
**Action:** Use `time.strftime` for simple timestamp formatting in high-frequency paths and pre-calculate formatted strings to avoid repeated concatenation.
