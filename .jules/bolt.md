# Bolt Journal ⚡

## 2026-06-24 - Performance Logging Optimization
**Learning:** Frequent file I/O (opening and closing handles) in a logging function can become a significant bottleneck as the application scales. Using a persistent file handle reduces system call overhead.
**Action:** Implement a persistent, lazy-initialized file handle for `performance_log.txt` in `performance.py`.

## 2026-07-04 - Timestamp and String Allocation Efficiency
**Learning:** In high-frequency logging, `time.strftime()` is significantly faster than `datetime.datetime.now().strftime()` (approx. 5.8x in this environment). Additionally, pre-calculating the message string with the newline character prevents redundant allocations and simplifies both file writing and console output.
**Action:** Replace `datetime` with `time` for timestamps and consolidate string formatting in `performance.py`.
