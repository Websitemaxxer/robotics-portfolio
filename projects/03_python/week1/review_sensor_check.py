# Week 1 review: proximity sensor check
# Combines lists, enumerate, conditionals, comprehensions, f-strings
# Jul 18, 2026 — corrected after review (added reading number, fixed the 20 cm boundary)

readings = [12.3, 12, 11, 29.9, 28.9]

for i, reading in enumerate(readings, start=1):
    if reading >= 20:
        print(f"Reading {i}: {reading} cm - clear")
    else:
        print(f"Reading {i}: {reading} cm - TOO CLOSE")

close = [reading for reading in readings if reading < 20]

print(f"{len(close)} readings were too close")
