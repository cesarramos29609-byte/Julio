# Bolt Journal ⚡

## 2026-06-24 - Performance Logging Optimization
**Learning:** Frequent file I/O (opening and closing handles) in a logging function can become a significant bottleneck as the application scales. Using a persistent file handle reduces system call overhead.
**Action:** Implement a persistent, lazy-initialized file handle for `performance_log.txt` in `performance.py`.

## 2026-06-25 - Timestamp and String Output Optimization
**Learning:** `time.strftime` is significantly faster than `datetime.datetime.now().strftime` for generating formatted timestamps. Additionally, embedding newlines in f-strings and using `sys.stdout.write` avoids the overhead of `print()` and extra string concatenations in high-frequency logging.
**Action:** Use `time.strftime` and `sys.stdout.write` with pre-calculated message strings (including `\n`) for optimized performance logging.
