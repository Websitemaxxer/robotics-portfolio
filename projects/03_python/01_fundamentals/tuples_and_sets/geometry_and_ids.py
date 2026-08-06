positions = [(0, 0), (3, 4), (5, 12)]

for x, y in positions:
    distance = (x ** 2 + y ** 2) ** 0.5
    print(f"Point ({x}, {y}) is {round(distance, 1)} units from origin")

sensor_ids = ["front", "rear", "front", "left", "rear", "front"]
unique_ids = set(sensor_ids)

print(f"{len(sensor_ids)} readings from {len(unique_ids)} sensors")
print(f"Sensors: {', '.join(sorted(unique_ids))}")
