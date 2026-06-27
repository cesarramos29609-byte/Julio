import time
import os
import atexit
import threading

LOG_FILE = "performance_log.txt"

# Bolt ⚡ Optimization: Persistent file handle to reduce I/O overhead from repeated open/close.
# We also use a lock to ensure thread safety when writing to the shared handle.
_log_handle = None
_log_lock = threading.Lock()

def _get_log_handle():
    global _log_handle
    if _log_handle is None:
        # Open in append mode with line buffering (buffering=1) for a balance of speed and persistence.
        _log_handle = open(LOG_FILE, "a", encoding="utf-8", buffering=1)
        # Ensure the handle is closed gracefully on exit.
        atexit.register(_close_log_handle)
    return _log_handle

def _close_log_handle():
    global _log_handle
    with _log_lock:
        if _log_handle is not None:
            _log_handle.close()
            _log_handle = None

def record_performance(action, status="exitoso"):
    """
    Records performance actions to a log file.
    Optimized by Bolt ⚡ to use a persistent file handle and remove synchronous print calls.
    """
    # Bolt ⚡: Faster timestamp generation using time.strftime and time.localtime.
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    message = (
        f"[{timestamp}] Estimado colega, me complace informarte que la acción '{action}' "
        f"se ha completado de manera {status}. Sigamos trabajando con integridad y entusiasmo "
        f"para alcanzar la soberanía tecnológica de Géminis 2026. ¡Buen trabajo!"
    )

    with _log_lock:
        global _log_handle
        try:
            handle = _get_log_handle()
            handle.write(message + "\n")
        except (IOError, ValueError):
            # Bolt ⚡: Reset handle to None on failure to allow recovery/re-initialization.
            if _log_handle is not None:
                try:
                    _log_handle.close()
                except:
                    pass
                _log_handle = None

            # Fallback for this call
            with open(LOG_FILE, "a", encoding="utf-8") as f:
                f.write(message + "\n")

    # Bolt ⚡: Removed synchronous print() to eliminate console I/O bottleneck.
    # Protocolo GPA-K963 integrity is maintained in the log file.

if __name__ == "__main__":
    record_performance("Inicialización de componentes base")
    record_performance("Implementación de Auditoría Autónoma")
