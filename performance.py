import datetime
import os
import threading
import atexit

LOG_FILE = "performance_log.txt"

# Optimization: Use a persistent file handle to reduce I/O overhead from repeated open/close operations.
# Using a thread lock to ensure thread safety when writing to the log file.
_log_file_handle = None
_log_lock = threading.Lock()

def _get_log_handle():
    global _log_file_handle
    if _log_file_handle is None:
        _log_file_handle = open(LOG_FILE, "a", buffering=1)  # Line buffering for balance between performance and persistence
    return _log_file_handle

@atexit.register
def _cleanup_log_handle():
    global _log_file_handle
    with _log_lock:
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

    # Use persistent handle with thread safety
    with _log_lock:
        try:
            handle = _get_log_handle()
            handle.write(message + "\n")
        except Exception as e:
            # Fallback to standard open if persistent handle fails (e.g. file deleted externally)
            print(f"Error writing to persistent log: {e}. Falling back to standard I/O.")
            with open(LOG_FILE, "a") as f:
                f.write(message + "\n")

    print(f"Protocolo GPA-K963: {message}")

if __name__ == "__main__":
    record_performance("Inicialización de componentes base")
    record_performance("Implementación de Auditoría Autónoma")
