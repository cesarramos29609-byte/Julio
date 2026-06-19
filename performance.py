import datetime
import os
import threading
import atexit

LOG_FILE = "performance_log.txt"
_log_file_handle = None
_log_lock = threading.Lock()

def _get_log_handle():
    """
    Returns the persistent file handle for logging, initializing it if necessary.
    Uses lazy initialization to avoid issues if the log file is deleted after import.
    """
    global _log_file_handle
    if _log_file_handle is None:
        # Open with line buffering (buffering=1) to balance performance and reliability
        _log_file_handle = open(LOG_FILE, "a", buffering=1)
        atexit.register(_close_log_handle)
    return _log_file_handle

def _close_log_handle():
    """Closes the persistent file handle."""
    global _log_file_handle
    if _log_file_handle is not None:
        _log_file_handle.close()
        _log_file_handle = None

def record_performance(action, status="exitoso"):
    """
    Records performance metrics with Protocolo GPA-K963 compliance.
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
        except (OSError, IOError):
            # Fallback to standard open if the persistent handle fails
            with open(LOG_FILE, "a") as f:
                f.write(message + "\n")

    print(f"Protocolo GPA-K963: {message}")

if __name__ == "__main__":
    record_performance("Inicialización de componentes base")
    record_performance("Implementación de Auditoría Autónoma")
