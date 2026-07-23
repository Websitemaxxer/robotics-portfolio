readings = [12.3, 12, 11, 29.9, 28.9]

for i, reading in enumerate(readings, start=1):
    if reading >= 20:
        print(f"Reading {i}: {reading} cm - clear")
    else:
        print(f"Reading {i}: {reading} cm - TOO CLOSE")

close = [reading for reading in readings if reading < 20]

print(f"{len(close)} readings were too close")
