import time
import random

class CircuitBreaker:
    def __init__(self, failure_threshold=0.03):
        self.failure_threshold = failure_threshold
        self.failures = 0
        self.total_calls = 0
        self.performance_factor = 1.0
        self._failure_rate = 0.0

    def record_call(self, success):
        self.total_calls += 1
        if not success:
            self.failures += 1

        self._failure_rate = self.failures / self.total_calls
        if self._failure_rate > self.failure_threshold:
            print(f"ALERTA: Tasa de fallos ({self._failure_rate:.2%}) supera el umbral ({self.failure_threshold:.2%}).")
            print("Activando Cortacircuitos: Reduciendo rendimiento para garantizar soberanía.")
            # Lazy load performance integration on cold failure path to prevent overhead and ImportError at startup
            try:
                from performance import record_performance
                record_performance("Reducción de autonomía por exceso de fallos", "exitoso")
            except (ImportError, AttributeError):
                pass
            self.performance_factor = max(0.1, 1.0 - (self._failure_rate * 5))
            time.sleep(1.0 / self.performance_factor)
        else:
            self.performance_factor = 1.0

    def get_status(self):
        return {
            "failure_rate": self._failure_rate,
            "performance_factor": self.performance_factor
        }

if __name__ == "__main__":
    cb = CircuitBreaker()
    print("Simulando operaciones...")
    for i in range(20):
        # Simular éxito el 95% de las veces para probar el umbral del 3%
        success = random.random() > 0.05
        cb.record_call(success)
        status = cb.get_status()
        print(f"Operación {i+1}: {'OK' if success else 'FAIL'} | Tasa Fallos: {status['failure_rate']:.2%} | Rendimiento: {status['performance_factor']:.2%}")
