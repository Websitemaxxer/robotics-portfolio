robot = {"motor_1": 12,
         "motor_2": 13,
         "motor_3": 14,
         "motor_4": 89,
         "motor_5": 87
}

hottest_name = ""
hottest_temp = 0

for key, value in robot.items():
    if value > 70:
        status = "Overheating"
    else:
        status = "Normal"
    print(f"{key}: {value}C - Status: {status}")

    if value > hottest_temp:
        hottest_temp = value
        hottest_name = key

overheating = [value for value in robot.values() if value > 70]

print(f"{len(overheating)} motors are overheating.")
print(f"The hottest motor temperature is {hottest_temp}C from {hottest_name}.")

average_temp = sum(robot.values()) / len(robot)
print(f"The average motor temperature is {round(average_temp, 1)}C.")
