class CircuitBreaker:
    """
    Implements the 'Cortacircuitos' logic as defined in Gemini 2026.
    Reduces system autonomy if the failure rate exceeds 3%.
    Optimized with pre-calculated and cached state values to convert high-frequency checks into O(1) attribute lookups.
    """
    def __init__(self, threshold=0.03):
        self.threshold = threshold
        self.total_calls = 0
        self.failures = 0
        self._failure_rate = 0.0
        self._autonomous_safe = True

    def _update_state(self):
        if self.total_calls == 0:
            self._failure_rate = 0.0
        else:
            self._failure_rate = self.failures / self.total_calls
        self._autonomous_safe = self._failure_rate <= self.threshold

    def record_success(self):
        self.total_calls += 1
        self._update_state()

    def record_failure(self):
        self.total_calls += 1
        self.failures += 1
        self._update_state()

    @property
    def failure_rate(self):
        return self._failure_rate

    def is_autonomous_mode_safe(self):
        """
        Checks if it's safe to operate in full autonomous mode.
        Returns False if the failure rate is above the threshold.
        """
        return self._autonomous_safe

    def get_status(self):
        return {
            "total_calls": self.total_calls,
            "failures": self.failures,
            "failure_rate": f"{self._failure_rate:.2%}",
            "autonomous_safe": self._autonomous_safe
        }

if __name__ == "__main__":
    # Basic verification
    cb = CircuitBreaker()
    for _ in range(97): cb.record_success()
    for _ in range(3): cb.record_failure()
    print(f"Status at 3% failures: {cb.get_status()}")

    cb.record_failure()
    print(f"Status after exceeding 3%: {cb.get_status()}")
