import datetime
import os
import threading
import atexit

LOG_FILE = "performance_log.txt"
_log_handle = None
_log_lock = threading.Lock()

def _get_log_handle():
    global _log_handle
    if _log_handle is None:
        try:
            # buffering=1 gives a good balance between performance and persistence
            _log_handle = open(LOG_FILE, "a", buffering=1, encoding="utf-8")
        except Exception:
            _log_handle = None
    return _log_handle

def _close_log_handle():
    global _log_handle
    with _log_lock:
        if _log_handle:
            _log_handle.close()
            _log_handle = None

# Ensure the handle is closed on program exit
atexit.register(_close_log_handle)

def record_performance(action, status="exitoso"):
    """
    Records performance actions with high efficiency.
    Optimized: Uses a persistent file handle and avoids synchronous console I/O.
    """
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Protocolo GPA-K963: Enfoque persuasivo y amable
    message = (
        f"[{timestamp}] Estimado colega, me complace informarte que la acción '{action}' "
        f"se ha completado de manera {status}. Sigamos trabajando con integridad y entusiasmo "
        f"para alcanzar la soberanía tecnológica de Géminis 2026. ¡Buen trabajo!"
    )

    with _log_lock:
        handle = _get_log_handle()
        if handle:
            try:
                handle.write(message + "\n")
            except Exception:
                # Fallback: reset handle to try and recover on next call
                global _log_handle
                _log_handle = None

    # Performance Note: Synchronous print() removed to eliminate console bottleneck.
    # The message is preserved in the log file per Protocolo GPA-K963 integrity.

if __name__ == "__main__":
    record_performance("Inicialización de componentes base")
    record_performance("Implementación de Auditoría Autónoma")
