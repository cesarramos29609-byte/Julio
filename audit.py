import os
import sys
from performance import record_performance

def check_pillars():
    pillars = ["flow", "antigravedad", "notebooklm", "mcp"]
    missing = [p for p in pillars if not os.path.isdir(p)]
    return missing

def check_manifesto():
    return os.path.exists("README.md")

def main():
    print("--- INICIANDO PROTOCOLO DE AUDITORÍA AUTÓNOMA ---")

    manifesto_ok = check_manifesto()
    record_performance(f"Verificación de Manifiesto: {'PASSED' if manifesto_ok else 'FAILED'}")

    missing_pillars = check_pillars()
    if not missing_pillars:
        record_performance("Verificación de Pilares: PASSED")
    else:
        record_performance(f"Verificación de Pilares: FAILED (Faltan: {', '.join(missing_pillars)})", status="fallido")

    if manifesto_ok and not missing_pillars:
        print("\nSTATUS: AUDIT_PROTOCOL_ACTIVE")
        sys.exit(0)
    else:
        print("\nSTATUS: AUDIT_PROTOCOL_INACTIVE")
        sys.exit(1)

if __name__ == "__main__":
    main()
