import unittest
from unittest.mock import patch
import sys
import os

# Ensure root directory and src directory are on python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from circuit_breaker import CircuitBreaker as RootCB
from src.circuit_breaker import CircuitBreaker as SrcCB
from src.audit_protocol import AuditProtocol

class TestCircuitBreakersAndAudit(unittest.TestCase):
    def test_root_circuit_breaker_slots(self):
        cb = RootCB(failure_threshold=0.03)
        self.assertTrue(hasattr(cb, "__slots__"))
        with self.assertRaises(AttributeError):
            cb.arbitrary_attr = "invalid"

    def test_root_circuit_breaker_behavior(self):
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
        cb.record_call(success=True)
        cb.record_call(success=False)

        status = cb.get_status()
        self.assertEqual(status["failure_rate"], 0.5)
        self.assertLess(status["performance_factor"], 1.0)
        self.assertEqual(cb.total_calls, 2)
        self.assertEqual(cb.failures, 1)
        mock_sleep.assert_called_once()

    def test_src_circuit_breaker_slots(self):
        cb = SrcCB(threshold=0.03)
        self.assertTrue(hasattr(cb, "__slots__"))
        with self.assertRaises(AttributeError):
            cb.arbitrary_attr = "invalid"

    def test_src_circuit_breaker_behavior(self):
        cb = SrcCB(threshold=0.03)
        for _ in range(97):
            cb.record_success()
        for _ in range(3):
            cb.record_failure()

        self.assertAlmostEqual(cb.failure_rate, 0.03, places=4)
        self.assertTrue(cb.is_autonomous_mode_safe())

        status = cb.get_status()
        self.assertEqual(status["total_calls"], 100)
        self.assertEqual(status["failures"], 3)
        self.assertEqual(status["failure_rate"], "3.00%")
        self.assertTrue(status["autonomous_safe"])

        # Exceed threshold
        cb.record_failure()
        self.assertFalse(cb.is_autonomous_mode_safe())

    def test_audit_protocol_slots_and_behavior(self):
        ap = AuditProtocol()
        self.assertTrue(hasattr(ap, "__slots__"))
        with self.assertRaises(AttributeError):
            ap.arbitrary_attr = "invalid"

        self.assertEqual(ap.get_audit_summary()["total_audits"], 0)
        ap.audit("AgentA", "AgentB", {"task": "verify"}, "Success")
        summary = ap.get_audit_summary()
        self.assertEqual(summary["total_audits"], 1)
        self.assertEqual(summary["verified_count"], 1)

if __name__ == "__main__":
    unittest.main()
