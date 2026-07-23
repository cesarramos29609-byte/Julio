import sys
import os

# Import record_performance at module load time to avoid performance degradation in hot paths
try:
    from performance import record_performance
except ImportError:
    # Handle path when imported from a different directory (e.g. src/)
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    from performance import record_performance

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
        if not self.is_autonomous_mode_safe():
            # Call record_performance when failure threshold is exceeded
            record_performance(
                f"Tasa de fallos ({self.failure_rate:.2%}) supera el umbral de autonomía de seguridad ({self.threshold:.2%})",
                status="fallido"
            )

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
