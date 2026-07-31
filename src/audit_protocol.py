class AuditProtocol:
    """
    Implements the 'Agente verifica a agente' (Agent verifies Agent) protocol.
    Ensures tiered defense through autonomous auditing.
    Optimized get_audit_summary from O(N) to O(1) by maintaining an inline count of verified logs.
    """
    def __init__(self):
        self.logs = []
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
        if verified:
            self._verified_count += 1
        return verified

    def verify_integrity(self, data, result):
        # Placeholder for complex verification logic
        # In a real scenario, this would involve comparing outputs,
        # checking constraints, etc.
        return True

    def get_audit_summary(self):
        """
        Returns a summary of the audit logs.
        Optimized to run in O(1) time rather than O(N) by using the cached _verified_count.
        """
        total = len(self.logs)
        return {
            "total_audits": total,
            "verified_count": self._verified_count,
            "integrity_score": f"{(self._verified_count / total if total > 0 else 1.0):.2%}"
        }

if __name__ == "__main__":
    ap = AuditProtocol()
    print(f"Initial summary: {ap.get_audit_summary()}")
    ap.audit("Agent_A", "Agent_B", {"task": "process_data"}, "Success")
    print(f"Summary after audit: {ap.get_audit_summary()}")
