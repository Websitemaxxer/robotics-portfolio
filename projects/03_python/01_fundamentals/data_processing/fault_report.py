faults = [("scout", "E12", 3),
          ("digger", "E07", 5),
          ("scout", "E12", 5),
          ("hauler", "E33", 2),
          ("digger", "E12", 6),
          ("scout", "E07", 1),
          ("hauler", "E12", 2),
          ("digger", "E33", 7),
          ("scout", "E33", 3),
          ("hauler", "E07", 1)]

code_counts = {}
severity_by_robot = {}
serious = set()

for robot, code, severity in faults:
    code_counts[code] = code_counts.get(code, 0) + 1
    if robot in severity_by_robot:
        severity_by_robot[robot].append(severity)
    else:
        severity_by_robot[robot] = [severity]
    if severity >= 5:
        serious.add(robot)

top_code, top_count = max(code_counts.items(), key=lambda pair: pair[1])
print(f"Most common fault: {top_code} ({top_count} times)")

for robot, severities in sorted(severity_by_robot.items()):
    total = sum(severities)
    average = total / len(severities)
    print(f"{robot}: total severity {total}, average {round(average, 1)}")

print(f"Robots with a serious fault: {', '.join(sorted(serious))}")
