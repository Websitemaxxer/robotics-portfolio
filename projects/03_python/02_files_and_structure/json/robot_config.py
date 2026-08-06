import json

robot = {"name": "scout",
         "battery": 87,
         "active": True,
         "sensors": ["distance", "temp", "camera"]}

with open("robot.json", "w") as f:
    json.dump(robot, f, indent=2)

with open("robot.json", "r") as f:
    loaded = json.load(f)

print(f"Robot: {loaded['name']}")
print(f"Battery in 10 mins: {loaded['battery'] + 10}")
print(f"Sensors: {len(loaded['sensors'])}")
