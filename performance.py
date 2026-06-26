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
            # Persistent handle with line buffering (buffering=1) for efficiency
            _log_handle = open(LOG_FILE, "a", encoding="utf-8", buffering=1)
            atexit.register(_close_log_handle)
        except Exception:
            _log_handle = None
    return _log_handle

def _close_log_handle():
    global _log_handle
    with _log_lock:
        if _log_handle is not None:
            _log_handle.close()
            _log_handle = None

def record_performance(action, status="exitoso"):
    """
    ⚡ Bolt: Optimized performance logging.
    Reduces I/O overhead by using a persistent file handle and removing synchronous print.
    """
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = (
        f"[{timestamp}] Estimado colega, me complace informarte que la acción '{action}' "
        f"se ha completado de manera {status}. Sigamos trabajando con integridad y entusiasmo "
        f"para alcanzar la soberanía tecnológica de Géminis 2026. ¡Buen trabajo!\n"
    )

    with _log_lock:
        handle = _get_log_handle()
        if handle:
            try:
                handle.write(message)
            except Exception:
                # Fallback to standard open if persistent handle fails
                with open(LOG_FILE, "a", encoding="utf-8") as f:
                    f.write(message)
        else:
            # Fallback if handle couldn't be initialized
            with open(LOG_FILE, "a", encoding="utf-8") as f:
                f.write(message)

    # Note: Removed synchronous print(f"Protocolo GPA-K963: {message}")
    # to eliminate console I/O bottleneck.

if __name__ == "__main__":
    record_performance("Inicialización de componentes base")
    record_performance("Implementación de Auditoría Autónoma")
