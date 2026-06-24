import datetime
import os
import atexit

LOG_FILE = "performance_log.txt"
_LOG_HANDLE = None

def _get_log_handle():
    """Returns a persistent file handle for logging, with lazy initialization."""
    global _LOG_HANDLE
    if _LOG_HANDLE is None:
        # Using line buffering (buffering=1) to ensure logs are written promptly
        # while maintaining the performance benefit of a persistent handle.
        _LOG_HANDLE = open(LOG_FILE, "a", encoding="utf-8", buffering=1)
        atexit.register(_close_log_handle)
    return _LOG_HANDLE

def _close_log_handle():
    """Closes the global log handle at exit."""
    global _LOG_HANDLE
    if _LOG_HANDLE:
        _LOG_HANDLE.close()
        _LOG_HANDLE = None

def record_performance(action, status="exitoso"):
    """Records a performance action using a persistent file handle to reduce I/O overhead."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = (
        f"[{timestamp}] Estimado colega, me complace informarte que la acción '{action}' "
        f"se ha completado de manera {status}. Sigamos trabajando con integridad y entusiasmo "
        f"para alcanzar la soberanía tecnológica de Géminis 2026. ¡Buen trabajo!"
    )

    try:
        handle = _get_log_handle()
        handle.write(message + "\n")
    except Exception:
        # Fallback to standard open/close if the persistent handle fails
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(message + "\n")

    print(f"Protocolo GPA-K963: {message}")

if __name__ == "__main__":
    record_performance("Inicialización de componentes base")
    record_performance("Implementación de Auditoría Autónoma")
