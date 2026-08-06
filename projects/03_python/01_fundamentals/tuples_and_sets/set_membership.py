required = ["front", "rear", "left", "gps", "sonar"]
online = {"front", "rear", "gps"}

for sensor in required:
    if sensor in online:
        print(f"{sensor}: online")
    else:
        print(f"{sensor}: OFFLINE")

missing = [sensor for sensor in required if sensor not in online]
print(f"{len(missing)} sensors offline: {', '.join(missing)}")
