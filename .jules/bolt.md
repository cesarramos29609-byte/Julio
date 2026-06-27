## 2026-06-27 - Persistent File Handle for High-Frequency Logging
**Learning:** In high-frequency logging scenarios, repeated open/close operations on a file handle create significant I/O overhead. Additionally, synchronous console output (print) can be a major bottleneck.
**Action:** Use a global persistent file handle with lazy initialization and `atexit` for cleanup. Implement thread safety with `threading.Lock` and remove or minimize synchronous `print()` calls in hot paths to maximize throughput.

## 2026-06-27 - Robust Handle Management and Fast Timestamps
**Learning:** Persistent handles must be reset to `None` if an I/O error occurs to allow for recovery. Also, `time.strftime` with `time.localtime` is significantly faster than `datetime.now().strftime` for high-frequency operations.
**Action:** Always reset shared handles on failure in try-except blocks. Prefer `time` module for performance-critical timestamping.
