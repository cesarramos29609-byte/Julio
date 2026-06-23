import datetime
import os
import atexit
import threading

LOG_FILE = "performance_log.txt"

# Persistent file handle and lock for thread safety
_log_handle = None
_log_lock = threading.Lock()

def _get_log_handle():
    """Lazy initialization of the persistent file handle."""
    global _log_handle
    if _log_handle is None:
        # Use line buffering (buffering=1) for a balance between performance and durability
        _log_handle = open(LOG_FILE, "a", buffering=1)
        # Ensure the handle is closed when the program exits
        atexit.register(_close_log_handle)
    return _log_handle

def _close_log_handle():
    """Cleanup function to close the log handle."""
    global _log_handle
    if _log_handle:
        _log_handle.close()
        _log_handle = None

def record_performance(action, status="exitoso"):
    """
    Records performance actions with high efficiency using a persistent file handle.
    ⚡ Bolt Optimization: Avoids repeated open/close overhead.
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
            # Fallback if the handle was closed or deleted externally
            with open(LOG_FILE, "a") as f:
                f.write(message + "\n")

    print(f"Protocolo GPA-K963: {message}")

if __name__ == "__main__":
    record_performance("Inicialización de componentes base")
    record_performance("Implementación de Auditoría Autónoma")
