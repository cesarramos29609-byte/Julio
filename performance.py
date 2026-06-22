import datetime
import os
import threading
import atexit

# Note: The verbose message format is a requirement of "Protocolo GPA-K963"
# to maintain professional and persuasive communication with colleagues.
# To offset the I/O cost of this verbose format, we use a persistent
# file handle to minimize syscalls.

LOG_FILE = "performance_log.txt"

# Persistent file handle and lock for thread-safety
_log_handle = None
_log_lock = threading.Lock()

def _get_log_handle():
    """Returns the persistent file handle, initializing it if necessary."""
    global _log_handle
    if _log_handle is None:
        # Use line buffering (buffering=1) to ensure logs are written promptly
        # while still benefiting from a persistent handle.
        _log_handle = open(LOG_FILE, "a", buffering=1)
        atexit.register(_close_log_handle)
    return _log_handle

def _close_log_handle():
    """Closes the persistent file handle."""
    global _log_handle
    if _log_handle is not None:
        _log_handle.close()
        _log_handle = None

def record_performance(action, status="exitoso"):
    """
    Records a performance action in the log file using a persistent handle
    to reduce I/O overhead from repeated open/close operations.

    This implementation is preferred over the standard 'logging' module
    for this specific protocol to ensure minimum latency by avoiding
    the additional abstraction layers of the standard library while
    maintaining thread-safety.
    """
    # Performance Note: Cache the current time to avoid multiple calls
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

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
            # Fallback in case the persistent handle was closed or becomes invalid
            with open(LOG_FILE, "a") as f:
                f.write(message + "\n")

    print(f"Protocolo GPA-K963: {message}")

if __name__ == "__main__":
    record_performance("Inicialización de componentes base")
    record_performance("Implementación de Auditoría Autónoma")
