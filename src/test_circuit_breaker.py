import unittest
from src.circuit_breaker import CircuitBreaker

class TestCircuitBreaker(unittest.TestCase):
    def test_initial_state(self):
        cb = CircuitBreaker()
        self.assertEqual(cb.total_calls, 0)
        self.assertEqual(cb.failures, 0)
        self.assertEqual(cb.failure_rate, 0.0)
        self.assertTrue(cb.is_autonomous_mode_safe())
        status = cb.get_status()
        self.assertEqual(status["total_calls"], 0)
        self.assertEqual(status["failures"], 0)
        self.assertEqual(status["failure_rate"], "0.00%")
        self.assertTrue(status["autonomous_safe"])

    def test_successful_operations(self):
        cb = CircuitBreaker()
        for _ in range(100):
            cb.record_success()
        self.assertEqual(cb.total_calls, 100)
        self.assertEqual(cb.failures, 0)
        self.assertEqual(cb.failure_rate, 0.0)
        self.assertTrue(cb.is_autonomous_mode_safe())
        status = cb.get_status()
        self.assertEqual(status["failure_rate"], "0.00%")
        self.assertTrue(status["autonomous_safe"])

    def test_threshold_boundaries(self):
        cb = CircuitBreaker(threshold=0.03)
        # 97 successes, 3 failures = 3.00% failure rate (safe)
        for _ in range(97):
            cb.record_success()
        for _ in range(3):
            cb.record_failure()
        self.assertEqual(cb.total_calls, 100)
        self.assertEqual(cb.failures, 3)
        self.assertAlmostEqual(cb.failure_rate, 0.03)
        self.assertTrue(cb.is_autonomous_mode_safe())
        status = cb.get_status()
        self.assertEqual(status["failure_rate"], "3.00%")
        self.assertTrue(status["autonomous_safe"])

        # 1 more failure = 4/101 = ~3.96% failure rate (unsafe)
        cb.record_failure()
        self.assertFalse(cb.is_autonomous_mode_safe())
        status = cb.get_status()
        self.assertFalse(status["autonomous_safe"])

if __name__ == "__main__":
    unittest.main()
