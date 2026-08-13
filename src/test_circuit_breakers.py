import unittest
from src.circuit_breaker import CircuitBreaker as SrcCircuitBreaker
from circuit_breaker import CircuitBreaker as RootCircuitBreaker

class TestSrcCircuitBreaker(unittest.TestCase):
    def test_initial_state(self):
        cb = SrcCircuitBreaker()
        self.assertEqual(cb.total_calls, 0)
        self.assertEqual(cb.failures, 0)
        self.assertEqual(cb.failure_rate, 0.0)
        self.assertTrue(cb.is_autonomous_mode_safe())
        status = cb.get_status()
        self.assertEqual(status["total_calls"], 0)
        self.assertEqual(status["failures"], 0)
        self.assertEqual(status["failure_rate"], "0.00%")
        self.assertTrue(status["autonomous_safe"])

    def test_success_path_keeps_autonomous_safe(self):
        cb = SrcCircuitBreaker(threshold=0.03)
        for _ in range(100):
            cb.record_success()
        self.assertEqual(cb.total_calls, 100)
        self.assertEqual(cb.failures, 0)
        self.assertEqual(cb.failure_rate, 0.0)
        self.assertTrue(cb.is_autonomous_mode_safe())
        status = cb.get_status()
        self.assertEqual(status["total_calls"], 100)
        self.assertEqual(status["failures"], 0)
        self.assertEqual(status["failure_rate"], "0.00%")
        self.assertTrue(status["autonomous_safe"])

    def test_failure_rate_threshold_exceeded(self):
        cb = SrcCircuitBreaker(threshold=0.03)
        for _ in range(97):
            cb.record_success()
        for _ in range(3):
            cb.record_failure()
        # Exactly 3% failures, which is safe (rate <= threshold)
        self.assertEqual(cb.total_calls, 100)
        self.assertEqual(cb.failures, 3)
        self.assertEqual(cb.failure_rate, 0.03)
        self.assertTrue(cb.is_autonomous_mode_safe())

        # One more failure pushes failure rate to 4/101 (~3.96%), which exceeds threshold
        cb.record_failure()
        self.assertEqual(cb.total_calls, 101)
        self.assertEqual(cb.failures, 4)
        self.assertFalse(cb.is_autonomous_mode_safe())
        status = cb.get_status()
        self.assertFalse(status["autonomous_safe"])


class TestRootCircuitBreaker(unittest.TestCase):
    def test_initial_state(self):
        cb = RootCircuitBreaker()
        self.assertEqual(cb.total_calls, 0)
        self.assertEqual(cb.failures, 0)
        self.assertEqual(cb.performance_factor, 1.0)
        status = cb.get_status()
        self.assertEqual(status["failure_rate"], 0.0)
        self.assertEqual(status["performance_factor"], 1.0)

    def test_success_path(self):
        cb = RootCircuitBreaker()
        for _ in range(50):
            cb.record_call(True)
        self.assertEqual(cb.total_calls, 50)
        self.assertEqual(cb.failures, 0)
        self.assertEqual(cb.performance_factor, 1.0)
        status = cb.get_status()
        self.assertEqual(status["failure_rate"], 0.0)

    def test_failure_handling(self):
        cb = RootCircuitBreaker(failure_threshold=0.10)
        # 10 calls, 1 failure => 10% failure rate
        for _ in range(9):
            cb.record_call(True)
        cb.record_call(False)
        self.assertEqual(cb.total_calls, 10)
        self.assertEqual(cb.failures, 1)
        # Should exceed 10% on next failure (tested with sleep bypass or we can expect print & sleep)
        cb.record_call(False)
        # Total calls = 11, failures = 2 => failure rate = 18.18%
        # performance_factor should drop
        self.assertTrue(cb.performance_factor < 1.0)

if __name__ == "__main__":
    unittest.main()
