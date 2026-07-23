log = [("alpha", "north", 22),
       ("bravo", "south", 35),
       ("alpha", "north", 18),
       ("charlie", "east", 12),
       ("bravo", "north", 40),
       ("alpha", "west", 28),
       ("charlie", "south", 9),
       ("bravo", "east", 31),
       ("alpha", "north", 20),
       ("charlie", "north", 15)
]

battery_by_drone = {}
zone_counts = {}
heavy_drones = set()

for drone, zone, battery in log:
    if drone in battery_by_drone:
        battery_by_drone[drone].append(battery)
    else:
        battery_by_drone[drone] = [battery]

    if zone in zone_counts:
        zone_counts[zone] += 1
    else:
        zone_counts[zone] = 1

    if battery > 30:
        heavy_drones.add(drone)

if len(log) == 0:
    print("The delivery log is empty.")
else:
    averages = []

    for drone, values in battery_by_drone.items():
        total = sum(values)
        average = total / len(values)
        averages.append((drone, average))

        if average > 25:
            status = "HEAVY USE"
        else:
            status = "efficient"

        print(f"{drone}: total {total}%, average {round(average, 1)}% - {status}")

    busiest_zone, busiest_count = max(zone_counts.items(), key=lambda pair: pair[1])
    print(f"Busiest zone: {busiest_zone} with {busiest_count} deliveries")

    over_30 = [drone for drone in heavy_drones]
    print(f"Drones over 30% on a run: {', '.join(sorted(over_30))}")

    top_name, top_average = max(averages, key=lambda pair: pair[1])
    print(f"Highest average battery use: {top_name} at {round(top_average, 1)}%")
