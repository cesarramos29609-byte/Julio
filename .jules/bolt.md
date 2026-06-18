# Bolt's Journal

## 2025-06-18 - Persistent File Handles vs. I/O Overhead
**Learning:** In Python, opening/closing files for every log entry introduces significant syscall overhead.
**Action:** Use persistent handles with `buffering=1` for high-frequency logging.
