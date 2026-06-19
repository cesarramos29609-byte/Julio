import datetime
import os
import threading
import atexit

LOG_FILE = "performance_log.txt"
_log_handle = None
_log_lock = threading.Lock()

def _get_log_handle():
    """Lazily initializes and returns a persistent file handle."""
    global _log_handle
    if _log_handle is None:
        # Use line buffering (buffering=1) to ensure logs are written to disk
        # without the overhead of repeated open/close operations.
        _log_handle = open(LOG_FILE, "a", buffering=1, encoding="utf-8")
    return _log_handle

@atexit.register
def _close_log_handle():
    """Ensures the file handle is closed upon program exit."""
    global _log_handle
    if _log_handle:
        _log_handle.close()
        _log_handle = None

def record_performance(action, status="exitoso"):
    """
    Records a performance message to a log file.
    Optimized with a persistent file handle and thread-safety.
    """
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = (
        f"[{timestamp}] Estimado colega, me complace informarte que la acción '{action}' "
        f"se ha completado de manera {status}. Sigamos trabajando con integridad y entusiasmo "
        f"para alcanzar la soberanía tecnológica de Géminis 2026. ¡Buen trabajo!"
    )

    # Thread-safe write to the persistent file handle
    with _log_lock:
        handle = _get_log_handle()
        handle.write(message + "\n")

    print(f"Protocolo GPA-K963: {message}")

if __name__ == "__main__":
    record_performance("Inicialización de componentes base")
    record_performance("Implementación de Auditoría Autónoma")
