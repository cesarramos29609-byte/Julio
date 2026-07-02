# Bolt Journal ⚡

## 2026-06-24 - Performance Logging Optimization
**Learning:** Frequent file I/O (opening and closing handles) in a logging function can become a significant bottleneck as the application scales. Using a persistent file handle reduces system call overhead.
**Action:** Implement a persistent, lazy-initialized file handle for `performance_log.txt` in `performance.py`.

## 2026-06-25 - Efficient Timestamping and String Reuse
**Learning:** `time.strftime` is significantly faster than `datetime.datetime.now().strftime` for high-frequency logging because it avoids the overhead of creating a `datetime` object. Reusing a single formatted message string for both file I/O and console output further reduces memory allocations.
**Action:** Replace `datetime` with `time.strftime` and pre-calculate the log message in `performance.py`.
