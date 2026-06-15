## 2026-06-15 - [Persistent File Handles for Logging]
**Learning:** In Python, opening and closing a file for every log entry (using `with open(..., 'a')`) introduces significant I/O overhead, especially in performance-critical paths. Using a persistent file handle with `atexit` cleanup and a `threading.Lock` for safety can measurably improve execution speed.
**Action:** Use persistent file handles for frequent logging operations, ensuring proper closure with `atexit` and thread safety with locks.
