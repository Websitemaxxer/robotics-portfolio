motors = {"left": 55, "right": 82, "arm": 40, "base": 91, "gripper": 66}

hottest_name = ""
hottest_temp = 0

for name, temp in motors.items():
    if temp > 70:
        status = "OVERHEATING"
    else:
        status = "normal"
    print(f"{name}: {temp}C - {status}")
    if temp > hottest_temp:
        hottest_temp = temp
        hottest_name = name

overheating = [temp for temp in motors.values() if temp > 70]
average = sum(motors.values()) / len(motors)

print(f"{len(overheating)} motors overheating")
print(f"Hottest: {hottest_name} at {hottest_temp}C")
print(f"Average temperature: {round(average, 1)}C")
