import unittest
from unittest.mock import patch
from circuit_breaker import CircuitBreaker

class TestCircuitBreaker(unittest.TestCase):
    def test_initial_state(self):
        cb = CircuitBreaker()
        self.assertEqual(cb.failures, 0)
        self.assertEqual(cb.total_calls, 0)
        self.assertEqual(cb.performance_factor, 1.0)
        status = cb.get_status()
        self.assertEqual(status["failure_rate"], 0)
        self.assertEqual(status["performance_factor"], 1.0)

    def test_fast_path_successes(self):
        cb = CircuitBreaker()
        for i in range(100):
            cb.record_call(True)
        self.assertEqual(cb.total_calls, 100)
        self.assertEqual(cb.failures, 0)
        self.assertEqual(cb.performance_factor, 1.0)
        status = cb.get_status()
        self.assertEqual(status["failure_rate"], 0.0)
        self.assertEqual(status["performance_factor"], 1.0)

    @patch("time.sleep")
    def test_failure_threshold_exceeded(self, mock_sleep):
        cb = CircuitBreaker(failure_threshold=0.03)
        # 10 successful calls
        for _ in range(10):
            cb.record_call(True)
        self.assertEqual(cb.performance_factor, 1.0)

        # 1 failure call -> 1/11 = 9.09% > 3% threshold
        cb.record_call(False)
        self.assertEqual(cb.failures, 1)
        self.assertEqual(cb.total_calls, 11)
        self.assertLess(cb.performance_factor, 1.0)
        mock_sleep.assert_called_once()

    @patch("time.sleep")
    def test_recovery_after_failures(self, mock_sleep):
        cb = CircuitBreaker(failure_threshold=0.03)
        # 10 successes + 1 failure -> >3%
        for _ in range(10):
            cb.record_call(True)
        cb.record_call(False)
        self.assertLess(cb.performance_factor, 1.0)

        # Record 50 additional successes -> failure rate = 1/61 = 1.6% < 3%
        for _ in range(50):
            cb.record_call(True)

        self.assertEqual(cb.performance_factor, 1.0)
        status = cb.get_status()
        self.assertAlmostEqual(status["failure_rate"], 1 / 61)
        self.assertEqual(status["performance_factor"], 1.0)

if __name__ == "__main__":
    unittest.main()
