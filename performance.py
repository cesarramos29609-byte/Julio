import datetime
import os
import atexit
import threading

LOG_FILE = "performance_log.txt"
_log_file_handle = None
_log_lock = threading.Lock()

def _get_log_handle():
    """Provides a persistent file handle for logging."""
    global _log_file_handle
    if _log_file_handle is None:
        _log_file_handle = open(LOG_FILE, "a", encoding="utf-8")
        # Ensure the handle is closed when the program exits
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
    Records a performance action to the log file and prints to console.
    Optimized with a persistent file handle to reduce I/O overhead.
    """
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = (
        f"[{timestamp}] Estimado colega, me complace informarte que la acción '{action}' "
        f"se ha completado de manera {status}. Sigamos trabajando con integridad y entusiasmo "
        f"para alcanzar la soberanía tecnológica de Géminis 2026. ¡Buen trabajo!"
    )

    # Use a lock to ensure thread safety when writing to the shared handle
    with _log_lock:
        handle = _get_log_handle()
        handle.write(message + "\n")
        # We don't explicitly flush here to maximize performance;
        # the OS and atexit closure will handle it.

    print(f"Protocolo GPA-K963: {message}")

if __name__ == "__main__":
    record_performance("Inicialización de componentes base")
    record_performance("Implementación de Auditoría Autónoma")
