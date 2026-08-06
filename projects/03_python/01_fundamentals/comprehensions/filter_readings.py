readings = [12, 45, 8, 90, 33, 5, 78, 20]

high = [r for r in readings if r > 30]
labels = [f"{r} cm" for r in readings]
doubled = [r * 2 for r in readings if r < 20]

print(f"High readings: {high}")
print(f"Labelled: {labels}")
print(f"Close readings doubled: {doubled}")
