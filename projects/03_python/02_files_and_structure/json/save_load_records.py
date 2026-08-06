import json

robots = [{"name": "scout", "battery": 87, "sensors": 3},
          {"name": "digger", "battery": 42, "sensors": 5},
          {"name": "hauler", "battery": 15, "sensors": 2}]

with open("fleet.json", "w") as f:
    json.dump(robots, f, indent=2)

with open("fleet.json", "r") as f:
    loaded = json.load(f)

low = [r["name"] for r in loaded if r["battery"] < 50]
average = sum([r["battery"] for r in loaded]) / len(loaded)

print(f"Fleet size: {len(loaded)}")
print(f"Low battery: {', '.join(low)}")
print(f"Average battery: {round(average, 1)}%")
