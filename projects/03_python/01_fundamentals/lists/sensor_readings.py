readings = [12, 8, 20, 15, 5, 30, 18]

for i, reading in enumerate(readings, start=1):
    if reading < 15:
        status = "BLOCKED"
    else:
        status = "clear"
    print(f"Reading {i}: {reading} cm - {status}")

blocked = [reading for reading in readings if reading < 15]

print(f"{len(blocked)} readings were blocked")
print(f"Closest object: {min(readings)} cm")
