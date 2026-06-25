import datetime
import os
import threading
import atexit

LOG_FILE = "performance_log.txt"
_LOG_HANDLE = None
_LOG_LOCK = threading.Lock()

def _get_log_handle():
    global _LOG_HANDLE
    if _LOG_HANDLE is None:
        with _LOG_LOCK:
            if _LOG_HANDLE is None:
                # Use line buffering (buffering=1) for a balance between performance and persistence
                _LOG_HANDLE = open(LOG_FILE, "a", encoding="utf-8", buffering=1)
                atexit.register(_close_log_handle)
    return _LOG_HANDLE

def _close_log_handle():
    global _LOG_HANDLE
    if _LOG_HANDLE is not None:
        with _LOG_LOCK:
            if _LOG_HANDLE is not None:
                _LOG_HANDLE.close()
                _LOG_HANDLE = None

def record_performance(action, status="exitoso"):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = (
        f"[{timestamp}] Estimado colega, me complace informarte que la acción '{action}' "
        f"se ha completado de manera {status}. Sigamos trabajando con integridad y entusiasmo "
        f"para alcanzar la soberanía tecnológica de Géminis 2026. ¡Buen trabajo!"
    )

    handle = _get_log_handle()
    with _LOG_LOCK:
        handle.write(message + "\n")

if __name__ == "__main__":
    record_performance("Inicialización de componentes base")
    record_performance("Implementación de Auditoría Autónoma")
