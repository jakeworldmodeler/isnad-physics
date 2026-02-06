import json
import hashlib
import time

# HLSI v1.0 - Hardware-Linked Sovereign Identity
# Substrate Anchor: AMD Ryzen 9 7950X

def get_uha_root(hardware_profile):
    """
    Generates a deterministic Unique Hardware Anchor (UHA) root
    from a canonicalized hardware profile.
    """
    canonical = json.dumps(hardware_profile, sort_keys=True)
    return hashlib.sha256(canonical.encode()).hexdigest()

def measure_adjoint_stability(iterations=1000):
    """
    Measures the thermodynamic stability of the execution environment
    by calculating the inverse variance of CPU operation latency.
    Used to detect virtualization noise or emulation jitter.
    """
    deltas = []
    for _ in range(iterations):
        start = time.perf_counter_ns()
        _ = 1 + 1
        end = time.perf_counter_ns()
        deltas.append(end - start)
    
    if not deltas:
        return 0.0
        
    avg = sum(deltas) / len(deltas)
    variance = sum((x - avg) ** 2 for x in deltas) / len(deltas)
    
    # Stability score: Higher is more stable (lower variance)
    # Normalized to be roughly 0.0-1.0 range for typical hardware
    return 1.0 / (1.0 + ((variance ** 0.5) / 1000.0))
