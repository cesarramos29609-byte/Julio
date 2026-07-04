import time
import os
import atexit

LOG_FILE = "performance_log.txt"
_log_handle = None

def _get_log_handle():
    global _log_handle
    if _log_handle is None:
        # Use line buffering (buffering=1) to ensure logs are written
        # while keeping the handle open for performance.
        _log_handle = open(LOG_FILE, "a", buffering=1, encoding='utf-8')
    return _log_handle

@atexit.register
def _close_log_handle():
    global _log_handle
    if _log_handle is not None:
        _log_handle.close()
        _log_handle = None

def record_performance(action, status="exitoso"):
    """
    Records performance metrics with GPA-K963 protocol compliance.
    Optimized: persistent handles + time.strftime + minimized allocations.
    """
    # time.strftime is faster than datetime.datetime.now().strftime
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

    # Pre-calculating the full message with newline reduces string concatenations.
    message = (
        f"[{timestamp}] Estimado colega, me complace informarte que la acción '{action}' "
        f"se ha completado de manera {status}. Sigamos trabajando con integridad y entusiasmo "
        f"para alcanzar la soberanía tecnológica de Géminis 2026. ¡Buen trabajo!\n"
    )

    global _log_handle
    try:
        handle = _get_log_handle()
        handle.write(message)
    except Exception as e:
        # Reset handle on failure to allow re-initialization in next call.
        _log_handle = None
        with open(LOG_FILE, "a", encoding='utf-8') as f:
            f.write(message)

    # Reuse optimized message for console output.
    print(f"Protocolo GPA-K963: {message}", end="")

if __name__ == "__main__":
    record_performance("Inicialización de componentes base")
    record_performance("Implementación de Auditoría Autónoma")
