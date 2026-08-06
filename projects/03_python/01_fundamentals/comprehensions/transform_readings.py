readings = [12, 45, 8, 90, 33, 5, 78, 20]

clear = [r for r in readings if r >= 20]
blocked = [r for r in readings if r < 20]
labelled = [f"{r} cm" for r in readings]
scaled = [r * 10 for r in readings]

print(f"Clear: {clear}")
print(f"Blocked: {blocked}")
print(f"Labelled: {labelled}")
print(f"Scaled: {scaled}")
