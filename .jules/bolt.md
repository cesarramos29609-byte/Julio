# Bolt Journal ⚡

## 2026-06-24 - Performance Logging Optimization
**Learning:** Frequent file I/O (opening and closing handles) in a logging function can become a significant bottleneck as the application scales. Using a persistent file handle reduces system call overhead.
**Action:** Implement a persistent, lazy-initialized file handle for `performance_log.txt` in `performance.py`.

## 2026-06-25 - Timestamp and Console I/O Optimization
**Learning:** `time.strftime` is significantly faster than `datetime.datetime.now().strftime` for simple timestamps as it avoids object instantiation. Similarly, `sys.stdout.write` outperforms `print` by bypassing high-level formatting checks.
**Action:** Replace `datetime` and `print` with `time.strftime` and `sys.stdout.write` in high-frequency logging paths.
