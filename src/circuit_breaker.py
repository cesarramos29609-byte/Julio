# Safe cross-directory import of performance module at load time (executed only once)
try:
    import sys
    import os
    _root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    if _root_dir not in sys.path:
        sys.path.append(_root_dir)
    from performance import record_performance
except Exception:
    record_performance = None

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
        # If failure threshold is exceeded, log autonomy reduction to satisfy integration requirements safely
        if not self.is_autonomous_mode_safe() and record_performance is not None:
            try:
                record_performance("Reducción de autonomía por exceso de fallas en Cortacircuitos", "fallido")
            except Exception:
                pass

    @property
    def failure_rate(self):
        if self.total_calls == 0:
            return 0.0
        return self.failures / self.total_calls

    def is_autonomous_mode_safe(self):
        """
        Checks if it's safe to operate in full autonomous mode.
        Returns False if the failure rate is above the threshold.
        """
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
