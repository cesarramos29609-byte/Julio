# Bolt Journal ⚡

## 2026-06-24 - Performance Logging Optimization
**Learning:** Frequent file I/O (opening and closing handles) in a logging function can become a significant bottleneck as the application scales. Using a persistent file handle reduces system call overhead.
**Action:** Implement a persistent, lazy-initialized file handle for `performance_log.txt` in `performance.py`.

## 2026-07-09 - Further Optimization of Performance Logging
**Learning:** Combining `time.strftime`, `sys.stdout.write`, and optimized f-string templates (including the newline character) can significantly reduce latency in high-frequency logging paths. `time.strftime` is ~5x faster than `datetime.now().strftime`, and `sys.stdout.write` avoids the overhead of `print`.
**Action:** Replace `datetime` with `time` and `print` with `sys.stdout.write` in `performance.py`.
