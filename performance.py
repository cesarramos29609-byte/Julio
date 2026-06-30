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
    Optimized with a persistent file handle and time.strftime for maximum efficiency.
    """
    # time.strftime() defaults to current time and is faster than datetime.now().strftime
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

    # Using f-strings is faster than .format() in Python 3.6+
    message = (
        f"[{timestamp}] Estimado colega, me complace informarte que la acción '{action}' "
        f"se ha completado de manera {status}. Sigamos trabajando con integridad y entusiasmo "
        f"para alcanzar la soberanía tecnológica de Géminis 2026. ¡Buen trabajo!\n"
    )

    try:
        handle = _get_log_handle()
        handle.write(message)
    except Exception as e:
        # Fallback if persistent handle fails
        print(f"Error escribiendo al log persistente: {e}")
        with open(LOG_FILE, "a", encoding='utf-8') as f:
            f.write(message)

    # Note: Maintaining synchronous print for protocol visibility as per UX requirements
    print(f"Protocolo GPA-K963: {message}", end="")

if __name__ == "__main__":
    record_performance("Inicialización de componentes base")
    record_performance("Implementación de Auditoría Autónoma")
