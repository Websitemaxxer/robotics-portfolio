def classify(distance, threshold=20):
    if distance < threshold:
        return "too close"
    return "clear"

def summarise(readings):
    average = sum(readings) / len(readings)
    return average, min(readings), max(readings)

readings = [15, 40, 8, 33, 22]

for r in readings:
    print(f"{r} cm - {classify(r)}")

average, closest, furthest = summarise(readings)
print(f"Average {round(average, 1)}, closest {closest}, furthest {furthest}")
