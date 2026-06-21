# Bolt's Journal - Critical Learnings Only

## 2025-05-15 - Persistent File Handles vs Filesystem Deletion
**Learning:** When using a persistent file handle for logging, if an external process or a test cleanup script deletes the log file, the handle remains open but writes may fail or go to a "ghost" file depending on the OS.
**Action:** Use lazy initialization and consider adding basic error handling or checks if the file still exists if reliability is more critical than pure performance.
