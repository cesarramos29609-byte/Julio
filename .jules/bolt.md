# Bolt Journal ⚡

## 2026-06-24 - Performance Logging Optimization
**Learning:** Frequent file I/O (opening and closing handles) in a logging function can become a significant bottleneck as the application scales. Using a persistent file handle reduces system call overhead.
**Action:** Implement a persistent, lazy-initialized file handle for `performance_log.txt` in `performance.py`.

## 2026-06-30 - Micro-optimization and CI Hygiene
**Learning:** Even small speedups (like switching from datetime to time.strftime) are valuable for high-frequency functions. However, cleaning up benchmark artifacts (like log file growth) is critical to avoid PR noise. Also, removing console I/O from a utility should not break the UX of calling scripts.
**Action:** Always verify log file state before submitting and ensure calling scripts maintain necessary user feedback.
