import datetime
import atexit

LOG_FILE = "performance_log.txt"
_log_handle = None

def _get_log_handle():
    global _log_handle
    if _log_handle is None:
        # Use line buffering (buffering=1) to ensure logs are written promptly
        # while maintaining performance by avoiding repeated open/close.
        # Explicitly setting encoding for cross-platform consistency.
        _log_handle = open(LOG_FILE, "a", buffering=1, encoding="utf-8")
        atexit.register(_cleanup_log_handle)
    return _log_handle

def _cleanup_log_handle():
    global _log_handle
    if _log_handle:
        _log_handle.close()
        _log_handle = None

def record_performance(action, status="exitoso"):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = (
        f"[{timestamp}] Estimado colega, me complace informarte que la acción '{action}' "
        f"se ha completado de manera {status}. Sigamos trabajando con integridad y entusiasmo "
        f"para alcanzar la soberanía tecnológica de Géminis 2026. ¡Buen trabajo!"
    )

    # Use persistent file handle for better performance
    f = _get_log_handle()
    f.write(message + "\n")

    print(f"Protocolo GPA-K963: {message}")

if __name__ == "__main__":
    record_performance("Inicialización de componentes base")
    record_performance("Implementación de Auditoría Autónoma")
