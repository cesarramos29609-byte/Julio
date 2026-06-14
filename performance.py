import datetime
import os
import atexit
import threading

LOG_FILE = "performance_log.txt"

# Bolt Optimization: Maintain a persistent, thread-safe file handle to avoid the overhead
# of opening and closing the file on every log entry.
# This reduces I/O wait times significantly in high-frequency logging scenarios.
_log_handle = None
_log_lock = threading.Lock()

def _get_log_handle():
    global _log_handle
    if _log_handle is None:
        with _log_lock:
            if _log_handle is None:
                # Use line buffering (buffering=1) to ensure logs are written to disk
                # promptly while still benefiting from keeping the file open.
                _log_handle = open(LOG_FILE, "a", buffering=1, encoding="utf-8")
                atexit.register(_close_log_handle)
    return _log_handle

def _close_log_handle():
    global _log_handle
    with _log_lock:
        if _log_handle is not None:
            _log_handle.close()
            _log_handle = None

def record_performance(action, status="exitoso"):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = (
        f"[{timestamp}] Estimado colega, me complace informarte que la acción '{action}' "
        f"se ha completado de manera {status}. Sigamos trabajando con integridad y entusiasmo "
        f"para alcanzar la soberanía tecnológica de Géminis 2026. ¡Buen trabajo!"
    )

    # Bolt Optimization: Use the cached file handle with thread-safety
    handle = _get_log_handle()
    with _log_lock:
        if handle:
            handle.write(message + "\n")

    print(f"Protocolo GPA-K963: {message}")

if __name__ == "__main__":
    record_performance("Inicialización de componentes base")
    record_performance("Implementación de Auditoría Autónoma")
