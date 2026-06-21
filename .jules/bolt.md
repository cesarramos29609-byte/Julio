# Bolt's Journal - Critical Learnings

This journal contains critical learnings discovered during performance optimization of the Géminis 2026 framework.

## 2025-05-15 - Persistent File Handles for Performance Logging
**Learning:** In high-frequency logging scenarios, opening and closing a file on every call introduces significant I/O overhead. Using a persistent file handle with lazy initialization and thread safety significantly reduces latency.
**Action:** Prefer persistent file handles for logging components that are expected to be called frequently.
