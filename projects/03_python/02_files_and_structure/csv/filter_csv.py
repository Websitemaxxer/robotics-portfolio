import csv

with open("motors.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["motor", "temp"])
    writer.writerow(["left", "55"])
    writer.writerow(["right", "82"])
    writer.writerow(["arm", "40"])
    writer.writerow(["base", "91"])
    writer.writerow(["gripper", "66"])

kept = 0
with open("motors.csv", "r") as f:
    with open("overheating.csv", "w", newline="") as out:
        reader = csv.reader(f)
        writer = csv.writer(out)
        next(reader)
        writer.writerow(["motor", "temp"])
        for row in reader:
            motor = row[0]
            temp = int(row[1])
            if temp > 70:
                writer.writerow([motor, temp])
                kept += 1
                print(f"{motor}: {temp}C - flagged")

print(f"Wrote {kept} overheating motors to overheating.csv")
