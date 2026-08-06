log = [("alpha", "north", 22),
       ("bravo", "south", 35),
       ("alpha", "north", 18),
       ("charlie", "east", 12),
       ("bravo", "north", 40),
       ("alpha", "west", 28),
       ("charlie", "south", 9),
       ("bravo", "east", 31),
       ("alpha", "north", 20),
       ("charlie", "north", 15)]

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

averages = []
for drone, values in battery_by_drone.items():
    average = sum(values) / len(values)
    averages.append((drone, average))
    print(f"{drone}: {len(values)} readings, average {round(average, 1)}%")

busiest_zone, busiest_count = max(zone_counts.items(), key=lambda pair: pair[1])
top_drone, top_average = max(averages, key=lambda pair: pair[1])

print(f"Busiest zone: {busiest_zone} with {busiest_count} readings")
print(f"Drones over 30%: {', '.join(sorted(heavy_drones))}")
print(f"Highest average battery use: {top_drone} at {round(top_average, 1)}%")
