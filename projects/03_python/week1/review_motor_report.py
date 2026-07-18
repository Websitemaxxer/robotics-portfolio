# Week 1 review: motor temperature report
# Combines dictionaries, .items()/.values(), conditionals, comprehensions, aggregation
# Jul 18, 2026 — corrected after review
#
# Original bug: the hottest motor was found with two separate max() calls,
# max(robot.values()) and max(robot.keys()). max() on the keys ranks them
# alphabetically, not by temperature, so the reported name and temperature
# could belong to different motors (it printed "89C from motor_5" when
# motor_5 was 87C). Fixed by tracking the name and temperature together
# in the loop, so they always update as a pair.

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
