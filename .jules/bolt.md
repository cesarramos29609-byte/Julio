# Bolt Journal ⚡

## 2026-06-24 - Performance Logging Optimization
**Learning:** Frequent file I/O (opening and closing handles) in a logging function can become a significant bottleneck as the application scales. Using a persistent file handle reduces system call overhead.
**Action:** Implement a persistent, lazy-initialized file handle for `performance_log.txt` in `performance.py`.

## 2026-07-03 - Optimizing Python Timestamp and String Operations
**Learning:** `time.strftime` is significantly faster (~50-60%) than `datetime.datetime.now().strftime` for basic timestamp formatting in Python. Additionally, pre-calculating message strings (e.g., including `\n` in the template) avoids redundant string concatenations during high-frequency I/O operations.
**Action:** Use `time.strftime("%Y-%m-%d %H:%M:%S")` for logging timestamps and optimize f-strings to include delimiters/newlines.
