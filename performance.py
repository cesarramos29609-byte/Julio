import time
import sys
import os
import atexit

LOG_FILE = "performance_log.txt"
_log_handle = None

def _get_log_handle():
    global _log_handle
    if _log_handle is None:
        try:
            # Use line buffering (buffering=1) for performance and reliability.
            _log_handle = open(LOG_FILE, "a", buffering=1, encoding='utf-8')
        except Exception as e:
            sys.stderr.write(f"Error abriendo el archivo de log: {e}\n")
            _log_handle = None
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
    Optimized:
    - Persistent handle (prevents open/close overhead)
    - time.strftime (faster than datetime.strftime)
    - sys.stdout.write (lower overhead than print)
    - Optimized string template with pre-embedded newline
    """
    global _log_handle

    # time.strftime() defaults to current time if no second argument is provided.
    # It is significantly faster than datetime.datetime.now().strftime().
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

    # Pre-calculate the full message with a newline to avoid redundant concatenations.
    full_message = (
        f"[{timestamp}] Estimado colega, me complace informarte que la acción '{action}' "
        f"se ha completado de manera {status}. Sigamos trabajando con integridad y entusiasmo "
        f"para alcanzar la soberanía tecnológica de Géminis 2026. ¡Buen trabajo!\n"
    )

    try:
        handle = _get_log_handle()
        if handle:
            handle.write(full_message)
    except Exception as e:
        # Reset handle on failure to allow recovery
        _log_handle = None
        sys.stderr.write(f"Error escribiendo al log persistente: {e}\n")
        try:
            with open(LOG_FILE, "a", encoding='utf-8') as f:
                f.write(full_message)
        except Exception:
            pass

    # Use sys.stdout.write for lower overhead than print()
    sys.stdout.write(f"Protocolo GPA-K963: {full_message}")

if __name__ == "__main__":
    record_performance("Inicialización de componentes base")
    record_performance("Implementación de Auditoría Autónoma")
