# Bolt Journal ⚡

## 2026-06-24 - Performance Logging Optimization
**Learning:** Frequent file I/O (opening and closing handles) in a logging function can become a significant bottleneck as the application scales. Using a persistent file handle reduces system call overhead.
**Action:** Implement a persistent, lazy-initialized file handle for `performance_log.txt` in `performance.py`.
## 2026-07-08 - Logging Latency Optimization
**Learning:** Replacing `datetime.datetime.now().strftime` with `time.strftime` and using `sys.stdout.write` with pre-calculated templates (including newlines) significantly reduces logging latency (~17.06 µs down to ~6.55 µs).
**Action:** Always prefer `time.strftime` and `sys.stdout.write` for high-frequency logging paths where every microsecond counts.
