# Bolt Journal ⚡

## 2026-06-24 - Performance Logging Optimization
**Learning:** Frequent file I/O (opening and closing handles) in a logging function can become a significant bottleneck as the application scales. Using a persistent file handle reduces system call overhead.
**Action:** Implement a persistent, lazy-initialized file handle for `performance_log.txt` in `performance.py`.

## 2026-06-25 - Audit Protocol O(1) Optimization
**Learning:** Checking or verifying logs incrementally during status/state updates using internal tracking avoids O(N) list-iteration lookups (like sum generators) on frequent calls, converting O(N) tasks into O(1) operations.
**Action:** Always maintain incremental running statistics or counters within state tracker instances instead of iterating over historical records to generate summaries.

## 2026-06-26 - Semantic-Safe Circuit Breaker Optimization
**Learning:** When optimizing cumulative-rate state machines (like `CircuitBreaker`), wrapping threshold checks directly within an `if not success:` block causes state regressions because successful calls with historical failures can still exceed thresholds.
**Action:** Correct semantic bypassing must only occur when cumulative failures are strictly zero (using `elif self.failures == 0:` on success) to achieve the best of both worlds: 100% semantic safety and a high-performance hot path.
