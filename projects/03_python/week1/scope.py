# Scope — completed Jul 13, 2026
# A name assigned inside a function is local unless declared `global`.
# Naive `total_readings += 1` without the declaration -> UnboundLocalError.

total_readings = 0

def record():
    global total_readings
    total_readings += 1
    return total_readings
