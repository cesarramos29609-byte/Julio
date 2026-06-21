import datetime
import os
import threading
import atexit

LOG_FILE = "performance_log.txt"

# Optimization: Use a persistent file handle to avoid repeated open/close overhead.
# We use a lock to ensure thread safety and atexit to close the handle properly.
_log_file_handle = None
_log_lock = threading.Lock()

def _get_log_handle():
    global _log_file_handle
    if _log_file_handle is None:
        _log_file_handle = open(LOG_FILE, "a", buffering=1) # Line buffering for performance/safety balance
        atexit.register(_close_log_handle)
    return _log_file_handle

def _close_log_handle():
    global _log_file_handle
    if _log_file_handle is not None:
        _log_file_handle.close()
        _log_file_handle = None

def record_performance(action, status="exitoso"):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = (
        f"[{timestamp}] Estimado colega, me complace informarte que la acción '{action}' "
        f"se ha completado de manera {status}. Sigamos trabajando con integridad y entusiasmo "
        f"para alcanzar la soberanía tecnológica de Géminis 2026. ¡Buen trabajo!"
    )

    # Optimization: Use the persistent handle within a lock
    with _log_lock:
        handle = _get_log_handle()
        handle.write(message + "\n")

    print(f"Protocolo GPA-K963: {message}")

if __name__ == "__main__":
    record_performance("Inicialización de componentes base")
    record_performance("Implementación de Auditoría Autónoma")
