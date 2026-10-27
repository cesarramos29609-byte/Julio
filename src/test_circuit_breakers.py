import unittest
from src.circuit_breaker import CircuitBreaker as SrcCircuitBreaker
import sys
import os

# Import root circuit_breaker module directly by path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import circuit_breaker as root_cb_module

class TestCircuitBreakers(unittest.TestCase):
    def test_src_circuit_breaker_initial_state(self):
        cb = SrcCircuitBreaker(threshold=0.03)
        self.assertEqual(cb.total_calls, 0)
        self.assertEqual(cb.failures, 0)
        self.assertEqual(cb.failure_rate, 0.0)
        self.assertTrue(cb.is_autonomous_mode_safe())

    def test_src_circuit_breaker_healthy_operations(self):
        cb = SrcCircuitBreaker(threshold=0.03)
        for _ in range(100):
            cb.record_success()
        self.assertEqual(cb.total_calls, 100)
        self.assertEqual(cb.failures, 0)
        self.assertEqual(cb.failure_rate, 0.0)
        self.assertTrue(cb.is_autonomous_mode_safe())

    def test_src_circuit_breaker_threshold_exceeded(self):
        cb = SrcCircuitBreaker(threshold=0.03)
        for _ in range(95):
            cb.record_success()
        for _ in range(5):
            cb.record_failure()
        self.assertEqual(cb.total_calls, 100)
        self.assertEqual(cb.failures, 5)
        self.assertEqual(cb.failure_rate, 0.05)
        self.assertFalse(cb.is_autonomous_mode_safe())

    def test_src_circuit_breaker_get_status(self):
        cb = SrcCircuitBreaker(threshold=0.03)
        cb.record_success()
        status = cb.get_status()
        self.assertEqual(status["total_calls"], 1)
        self.assertEqual(status["failures"], 0)
        self.assertEqual(status["failure_rate"], "0.00%")
        self.assertTrue(status["autonomous_safe"])

    def test_root_circuit_breaker_status(self):
        cb = root_cb_module.CircuitBreaker(failure_threshold=0.03)
        cb.record_call(True)
        status = cb.get_status()
        self.assertEqual(status["performance_factor"], 1.0)
        self.assertEqual(status["failure_rate"], 0.0)

if __name__ == "__main__":
    unittest.main()
