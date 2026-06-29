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
    Optimized with a persistent file handle and fast timestamping to reduce latency.
    """
    # Using time.strftime instead of datetime.now() for performance
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    message = (
        f"[{timestamp}] Estimado colega, me complace informarte que la acción '{action}' "
        f"se ha completado de manera {status}. Sigamos trabajando con integridad y entusiasmo "
        f"para alcanzar la soberanía tecnológica de Géminis 2026. ¡Buen trabajo!"
    )

    try:
        handle = _get_log_handle()
        handle.write(message + "\n")
    except Exception as e:
        # Fallback if persistent handle fails
        with open(LOG_FILE, "a", encoding='utf-8') as f:
            f.write(message + "\n")

    # Removed synchronous print() to eliminate console I/O bottleneck

if __name__ == "__main__":
    record_performance("Inicialización de componentes base")
    record_performance("Implementación de Auditoría Autónoma")
