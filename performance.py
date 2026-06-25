import datetime
import os
import threading
import atexit

LOG_FILE = "performance_log.txt"

# Persistent file handle for performance optimization
_log_handle = None
_log_lock = threading.Lock()

def _get_log_handle():
    """Lazy initialization of the persistent log file handle."""
    global _log_handle
    if _log_handle is None:
        # Use line buffering (buffering=1) for a balance between performance and persistence
        _log_handle = open(LOG_FILE, "a", encoding="utf-8", buffering=1)
    return _log_handle

@atexit.register
def _close_log_handle():
    """Ensure the file handle is closed gracefully on exit."""
    global _log_handle
    with _log_lock:
        if _log_handle is not None:
            _log_handle.close()
            _log_handle = None

def record_performance(action, status="exitoso"):
    """
    Records performance actions with a high-performance persistent file handle.
    Optimized to avoid repeated open/close operations.
    """
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = (
        f"[{timestamp}] Estimado colega, me complace informarte que la acción '{action}' "
        f"se ha completado de manera {status}. Sigamos trabajando con integridad y entusiasmo "
        f"para alcanzar la soberanía tecnológica de Géminis 2026. ¡Buen trabajo!"
    )

    # Thread-safe writing to the persistent handle
    with _log_lock:
        try:
            handle = _get_log_handle()
            handle.write(message + "\n")
        except (IOError, ValueError):
            # Fallback in case of handle issues (e.g. file deleted externally)
            with open(LOG_FILE, "a", encoding="utf-8") as f:
                f.write(message + "\n")
            _log_handle = None # Reset handle to attempt re-open on next call

    print(f"Protocolo GPA-K963: {message}")

if __name__ == "__main__":
    record_performance("Inicialización de componentes base")
    record_performance("Implementación de Auditoría Autónoma")
