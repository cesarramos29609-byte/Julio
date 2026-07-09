# Bolt Journal ⚡

## 2026-06-24 - Performance Logging Optimization
**Learning:** Frequent file I/O (opening and closing handles) in a logging function can become a significant bottleneck as the application scales. Using a persistent file handle reduces system call overhead.
**Action:** Implement a persistent, lazy-initialized file handle for `performance_log.txt` in `performance.py`.

## 2026-07-09 - High-Frequency Logging Latency Reduction
**Learning:** Switching from `datetime.datetime.now().strftime` to `time.strftime` and replacing `print` with `sys.stdout.write` significantly reduces function latency by avoiding object instantiation and internal print overhead. Embedding the newline character directly in a single f-string allocation further minimizes I/O syscalls.
**Action:** Always prefer `time.strftime` and `sys.stdout.write` for high-frequency performance logging in Python.
