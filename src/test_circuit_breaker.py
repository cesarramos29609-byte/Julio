import unittest
from src.circuit_breaker import CircuitBreaker

class TestCircuitBreaker(unittest.TestCase):
    def test_initial_state(self):
        cb = CircuitBreaker(threshold=0.03)
        self.assertTrue(cb.is_autonomous_mode_safe())
        self.assertEqual(cb.failure_rate, 0.0)

    def test_zero_failures(self):
        cb = CircuitBreaker(threshold=0.03)
        for _ in range(100):
            cb.record_success()
        self.assertTrue(cb.is_autonomous_mode_safe())
        self.assertEqual(cb.failure_rate, 0.0)

    def test_threshold_exceeded(self):
        cb = CircuitBreaker(threshold=0.03)
        for _ in range(96):
            cb.record_success()
        for _ in range(4):
            cb.record_failure()
        self.assertFalse(cb.is_autonomous_mode_safe())

    def test_negative_threshold(self):
        cb = CircuitBreaker(threshold=-0.01)
        self.assertFalse(cb.is_autonomous_mode_safe())

if __name__ == "__main__":
    unittest.main()
