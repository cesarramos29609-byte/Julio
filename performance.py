import datetime
import os
import threading
import atexit

LOG_FILE = "performance_log.txt"
_log_handle = None
_log_lock = threading.Lock()

def _get_log_handle():
    """Lazily initializes and returns a persistent file handle for logging."""
    global _log_handle
    if _log_handle is None:
        # Open in append mode with line buffering (buffering=1) for better performance
        # while ensuring logs are written relatively promptly.
        _log_handle = open(LOG_FILE, "a", encoding="utf-8", buffering=1)
    return _log_handle

@atexit.register
def _close_log_handle():
    """Closes the persistent file handle upon program exit."""
    global _log_handle
    with _log_lock:
        if _log_handle is not None:
            _log_handle.close()
            _log_handle = None

def record_performance(action, status="exitoso"):
    """
    Records a performance action to a log file.
    Optimized with a persistent file handle to reduce I/O overhead.
    """
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = (
        f"[{timestamp}] Estimado colega, me complace informarte que la acción '{action}' "
        f"se ha completado de manera {status}. Sigamos trabajando con integridad y entusiasmo "
        f"para alcanzar la soberanía tecnológica de Géminis 2026. ¡Buen trabajo!"
    )

    with _log_lock:
        try:
            handle = _get_log_handle()
            handle.write(message + "\n")
        except (IOError, ValueError):
            # If the handle is closed or another I/O error occurs, try to re-open once
            global _log_handle
            _log_handle = None
            handle = _get_log_handle()
            handle.write(message + "\n")

    print(f"Protocolo GPA-K963: {message}")

if __name__ == "__main__":
    record_performance("Inicialización de componentes base")
    record_performance("Implementación de Auditoría Autónoma")
