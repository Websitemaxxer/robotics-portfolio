# Loops: skipping invalid sensor readings with `continue`
# First-try-correct exercise — Jul 14, 2026

distances = [-3, -4, -9, 1, 2, 3, 4, 5]

for distance in distances:
    if distance < 0:
        continue
    else:
        print(distance)
