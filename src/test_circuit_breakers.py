import unittest
from unittest.mock import patch
import sys
import os

# Ensure the root directory and src directory are in python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from circuit_breaker import CircuitBreaker as RootCB
from src.circuit_breaker import CircuitBreaker as SrcCB

class TestCircuitBreakers(unittest.TestCase):
    def test_root_circuit_breaker_all_success(self):
        cb = RootCB(failure_threshold=0.03)
        for _ in range(10):
            cb.record_call(success=True)

        status = cb.get_status()
        self.assertEqual(status["failure_rate"], 0.0)
        self.assertEqual(status["performance_factor"], 1.0)
        self.assertEqual(cb.total_calls, 10)
        self.assertEqual(cb.failures, 0)

    @patch("time.sleep")
    def test_root_circuit_breaker_failures(self, mock_sleep):
        cb = RootCB(failure_threshold=0.03)
        # 1 success
        cb.record_call(success=True)
        # 1 failure -> failure rate 50%
        cb.record_call(success=False)

        status = cb.get_status()
        self.assertEqual(status["failure_rate"], 0.5)
        self.assertLess(status["performance_factor"], 1.0)
        self.assertEqual(cb.total_calls, 2)
        self.assertEqual(cb.failures, 1)
        mock_sleep.assert_called_once()

    def test_src_circuit_breaker_all_success(self):
        cb = SrcCB(threshold=0.03)
        for _ in range(10):
            cb.record_success()

        self.assertEqual(cb.failure_rate, 0.0)
        self.assertTrue(cb.is_autonomous_mode_safe())

        status = cb.get_status()
        self.assertEqual(status["total_calls"], 10)
        self.assertEqual(status["failures"], 0)
        self.assertEqual(status["failure_rate"], "0.00%")
        self.assertTrue(status["autonomous_safe"])

    def test_src_circuit_breaker_failures(self):
        cb = SrcCB(threshold=0.03)
        for _ in range(97):
            cb.record_success()
        for _ in range(3):
            cb.record_failure()

        self.assertAlmostEqual(cb.failure_rate, 0.03, places=4)
        self.assertTrue(cb.is_autonomous_mode_safe())

        # Exceed threshold
        cb.record_failure()
        self.assertFalse(cb.is_autonomous_mode_safe())
        self.assertGreater(cb.failure_rate, 0.03)

if __name__ == "__main__":
    unittest.main()
