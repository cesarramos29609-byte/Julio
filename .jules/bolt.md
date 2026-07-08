# Bolt Journal ⚡

## 2026-06-24 - Performance Logging Optimization
**Learning:** Frequent file I/O (opening and closing handles) in a logging function can become a significant bottleneck as the application scales. Using a persistent file handle reduces system call overhead.
**Action:** Implement a persistent, lazy-initialized file handle for `performance_log.txt` in `performance.py`.

## 2026-07-01 - Faster Timestamp Generation and Optimized String I/O
**Learning:** In Python, `time.strftime` is significantly faster than `datetime.datetime.now().strftime` for generating formatted timestamps as it avoids object instantiation overhead. Additionally, reusing a pre-calculated message string for both file writing and console output minimizes allocations.
**Action:** Use `time.strftime` for logging timestamps and construct the base message once, appending newlines only when writing to files via f-strings to avoid `.strip()` calls.
