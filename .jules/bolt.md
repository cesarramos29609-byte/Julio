# Bolt's Journal - Critical Learnings Only

## 2026-06-16 - Persistent File Handle vs. Filesystem Deletion
**Learning:** Using a persistent file handle with lazy initialization is faster than opening/closing per call, but it can cause issues if the log file is deleted by external processes while the handle is still open.
**Action:** Implement lazy initialization and ensure the handle is valid before writing, or handle the error gracefully.
