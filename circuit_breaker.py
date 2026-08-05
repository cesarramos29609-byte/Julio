import time
import random

class CircuitBreaker:
    """
    Implements a Circuit Breaker (Cortacircuitos) that reduces system autonomy/performance
    if the failure rate exceeds the failure_threshold (default 3%).

    Optimized:
    - Introduced fast path in `record_call` when `self.failures == 0`, avoiding
      any float division or comparisons on the hot success path.
    - Optimized `get_status` to return early without division when `self.failures == 0`.
    """
    def __init__(self, failure_threshold=0.03):
        self.failure_threshold = failure_threshold
        self.failures = 0
        self.total_calls = 0
        self.performance_factor = 1.0

    def record_call(self, success):
        self.total_calls += 1
        if not success:
            self.failures += 1

        if self.failures == 0:
            self.performance_factor = 1.0
            return

        failure_rate = self.failures / self.total_calls
        if failure_rate > self.failure_threshold:
            print(f"ALERTA: Tasa de fallos ({failure_rate:.2%}) supera el umbral ({self.failure_threshold:.2%}).")
            print("Activando Cortacircuitos: Reduciendo rendimiento para garantizar soberanía.")
            self.performance_factor = max(0.1, 1.0 - (failure_rate * 5))
            time.sleep(1.0 / self.performance_factor)
        else:
            self.performance_factor = 1.0

    def get_status(self):
        if self.failures == 0:
            return {
                "failure_rate": 0.0,
                "performance_factor": self.performance_factor
            }
        return {
            "failure_rate": self.failures / self.total_calls if self.total_calls > 0 else 0,
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
