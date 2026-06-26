import datetime
import os
import atexit
import threading

LOG_FILE = "performance_log.txt"

# Persistencia: Usamos un handle de archivo persistente para evitar la sobrecarga
# de abrir y cerrar el archivo en cada llamada.
_log_handle = None
_log_lock = threading.Lock()

def _get_log_handle():
    """Obtiene el handle del archivo de forma perezosa (lazy initialization)."""
    global _log_handle
    if _log_handle is None:
        try:
            # Abrimos con buffering de línea (1) para un balance entre rendimiento y seguridad.
            _log_handle = open(LOG_FILE, "a", encoding="utf-8", buffering=1)
        except Exception:
            _log_handle = None
    return _log_handle

@atexit.register
def _cleanup_log_handle():
    """Asegura que el handle se cierre correctamente al finalizar el proceso."""
    global _log_handle
    with _log_lock:
        if _log_handle is not None:
            _log_handle.close()
            _log_handle = None

def record_performance(action, status="exitoso"):
    """
    Registra el desempeño con integridad y eficiencia.
    Optimizado por Bolt ⚡: Handle persistente y eliminación de print() síncrono.
    """
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = (
        f"[{timestamp}] Estimado colega, me complace informarte que la acción '{action}' "
        f"se ha completado de manera {status}. Sigamos trabajando con integridad y entusiasmo "
        f"para alcanzar la soberanía tecnológica de Géminis 2026. ¡Buen trabajo!"
    )

    with _log_lock:
        handle = _get_log_handle()
        if handle:
            handle.write(message + "\n")
        else:
            # Fallback en caso de que el handle no se pueda abrir (poco probable)
            try:
                with open(LOG_FILE, "a", encoding="utf-8") as f:
                    f.write(message + "\n")
            except Exception:
                pass

    # Bolt: Eliminamos el print() síncrono para maximizar el rendimiento.
    # El registro permanece íntegro en el archivo log.

if __name__ == "__main__":
    record_performance("Inicialización de componentes base")
    record_performance("Implementación de Auditoría Autónoma")
