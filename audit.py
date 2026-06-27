import os
import sys

def check_pillars():
    pillars = ["flow", "antigravedad", "notebooklm", "mcp"]
    missing = [p for p in pillars if not os.path.isdir(p)]
    return missing

def check_manifesto():
    return os.path.exists("README.md")

def main():
    print("--- INICIANDO PROTOCOLO DE AUDITORÍA AUTÓNOMA ---")

    manifesto_ok = check_manifesto()
    print(f"Verificación de Manifiesto: {'PASSED' if manifesto_ok else 'FAILED'}")

    missing_pillars = check_pillars()
    if not missing_pillars:
        print("Verificación de Pilares: PASSED")
    else:
        print(f"Verificación de Pilares: FAILED (Faltan: {', '.join(missing_pillars)})")

    if manifesto_ok and not missing_pillars:
        print("\nSTATUS: AUDIT_PROTOCOL_ACTIVE")
        sys.exit(0)
    else:
        print("\nSTATUS: AUDIT_PROTOCOL_INACTIVE")
        sys.exit(1)

if __name__ == "__main__":
    main()
