class AuditProtocol:
    """
    Implements the 'Agente verifica a agente' (Agent verifies Agent) protocol.
    Ensures tiered defense through autonomous auditing.
    """
    def __init__(self):
        self.logs = []
        # Optimization: Use inline counters to track audit stats in O(1) time
        # instead of scanning the full log list on every get_audit_summary call.
        self._total_count = 0
        self._verified_count = 0

    def audit(self, action_agent_id, auditor_agent_id, action_data, result):
        """
        Record an audit event where one agent verifies the work of another.
        """
        verified = self.verify_integrity(action_data, result)
        audit_entry = {
            "action_agent": action_agent_id,
            "auditor_agent": auditor_agent_id,
            "data": action_data,
            "result": result,
            "verified": verified
        }
        self.logs.append(audit_entry)

        # Increment inline counters
        self._total_count += 1
        if verified:
            self._verified_count += 1

        return verified

    def verify_integrity(self, data, result):
        # Placeholder for complex verification logic
        # In a real scenario, this would involve comparing outputs,
        # checking constraints, etc.
        return True

    def get_audit_summary(self):
        # Optimization: O(1) lookup using inline counters
        # This replaces the O(N) list-comprehension scan.
        total = self._total_count
        verified = self._verified_count
        return {
            "total_audits": total,
            "verified_count": verified,
            "integrity_score": f"{(verified/total if total > 0 else 1):.2%}"
        }

if __name__ == "__main__":
    ap = AuditProtocol()
    print(f"Initial summary: {ap.get_audit_summary()}")
    ap.audit("Agent_A", "Agent_B", {"task": "process_data"}, "Success")
    print(f"Summary after audit: {ap.get_audit_summary()}")
