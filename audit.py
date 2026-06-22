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
    record_performance("Inicio de Auditoría")

    manifesto_ok = check_manifesto()
    print(f"Verificación de Manifiesto: {'PASSED' if manifesto_ok else 'FAILED'}")
    record_performance("Verificación de Manifiesto", "exitoso" if manifesto_ok else "fallido")

    missing_pillars = check_pillars()
    if not missing_pillars:
        print("Verificación de Pilares: PASSED")
        record_performance("Verificación de Pilares", "exitoso")
    else:
        print(f"Verificación de Pilares: FAILED (Faltan: {', '.join(missing_pillars)})")
        record_performance("Verificación de Pilares", "fallido")

    if manifesto_ok and not missing_pillars:
        print("\nSTATUS: AUDIT_PROTOCOL_ACTIVE")
        record_performance("Estatus de Auditoría: ACTIVO")
        sys.exit(0)
    else:
        print("\nSTATUS: AUDIT_PROTOCOL_INACTIVE")
        record_performance("Estatus de Auditoría: INACTIVO", "fallido")
        sys.exit(1)

if __name__ == "__main__":
    main()
