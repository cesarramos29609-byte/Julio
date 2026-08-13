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
        # Optimize to avoid float division when failures are 0
        if self.failures == 0:
            return 0.0
        if self.total_calls == 0:
            return 0.0
        return self.failures / self.total_calls

    def is_autonomous_mode_safe(self):
        """
        Checks if it's safe to operate in full autonomous mode.
        Returns False if the failure rate is above the threshold.
        """
        # Optimize: if there are no failures, autonomous mode is always safe
        if self.failures == 0:
            return True
        return self.failure_rate <= self.threshold

    def get_status(self):
        # Optimize: avoid float division, f-string formatting, and property lookup when there are zero failures while keeping code DRY
        failures = self.failures
        rate_str, safe = ("0.00%", True) if failures == 0 else (f"{self.failure_rate:.2%}", self.is_autonomous_mode_safe())
        return {
            "total_calls": self.total_calls,
            "failures": failures,
            "failure_rate": rate_str,
            "autonomous_safe": safe
        }

if __name__ == "__main__":
    # Basic verification
    cb = CircuitBreaker()
    for _ in range(97): cb.record_success()
    for _ in range(3): cb.record_failure()
    print(f"Status at 3% failures: {cb.get_status()}")

    cb.record_failure()
    print(f"Status after exceeding 3%: {cb.get_status()}")
