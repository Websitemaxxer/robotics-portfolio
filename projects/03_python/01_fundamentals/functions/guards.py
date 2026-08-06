def scale(value, factor=2):
    return value * factor

def clamp(value, low=0, high=100):
    if value < low:
        return low
    if value > high:
        return high
    return value

readings = [12, 55, 130, -5, 88]

for r in readings:
    boosted = scale(r, factor=3)
    safe = clamp(boosted)
    print(f"{r} -> scaled {boosted} -> clamped {safe}")
