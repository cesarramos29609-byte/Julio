class CircuitBreaker:
    """
    Implements the 'Cortacircuitos' logic as defined in Gemini 2026.
    Reduces system autonomy if the failure rate exceeds 3%.
    """
    def __init__(self, threshold=0.03):
        self.threshold = threshold
        self.total_calls = 0
        self.failures = 0

    def record_success(self):
        self.total_calls += 1

    def record_failure(self):
        self.total_calls += 1
        self.failures += 1

    @property
    def failure_rate(self):
        if self.failures == 0 or self.total_calls == 0:
            return 0.0
        return self.failures / self.total_calls

    def is_autonomous_mode_safe(self):
        """
        Checks if it's safe to operate in full autonomous mode.
        Returns False if the failure rate is above the threshold.
        Optimized: Short-circuits when zero failures exist to bypass division and property lookup.
        """
        if self.failures == 0:
            return self.threshold >= 0.0
        return self.failure_rate <= self.threshold

    def get_status(self):
        return {
            "total_calls": self.total_calls,
            "failures": self.failures,
            "failure_rate": f"{self.failure_rate:.2%}",
            "autonomous_safe": self.is_autonomous_mode_safe()
        }

if __name__ == "__main__":
    # Basic verification
    cb = CircuitBreaker()
    for _ in range(97): cb.record_success()
    for _ in range(3): cb.record_failure()
    print(f"Status at 3% failures: {cb.get_status()}")

    cb.record_failure()
    print(f"Status after exceeding 3%: {cb.get_status()}")
