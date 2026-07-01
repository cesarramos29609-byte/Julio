# Bolt Journal ⚡

## 2026-06-24 - Performance Logging Optimization
**Learning:** Frequent file I/O (opening and closing handles) in a logging function can become a significant bottleneck as the application scales. Using a persistent file handle reduces system call overhead.
**Action:** Implement a persistent, lazy-initialized file handle for `performance_log.txt` in `performance.py`.

## 2026-07-01 - Optimized Timestamp and String Handling
**Learning:** `time.strftime` is significantly faster than `datetime.datetime.now().strftime` for basic timestamp formatting. Pre-calculating the newline character in the log message also avoids additional string concatenation during I/O.
**Action:** Use `time.strftime` and embed `\n` in f-string templates for high-frequency logging.
