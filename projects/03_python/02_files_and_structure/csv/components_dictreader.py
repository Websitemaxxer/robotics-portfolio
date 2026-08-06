import csv

with open("components.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "voltage", "zone"])
    writer.writerow(["sensor", "3", "front"])
    writer.writerow(["motor", "12", "rear"])
    writer.writerow(["pump", "9", "rear"])
    writer.writerow(["led", "2", "front"])

high_count = 0

with open("components.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        name = row["name"]
        voltage = int(row["voltage"])
        if voltage > 5:
            status = "HIGH"
            high_count += 1
        else:
            status = "low"
        print(f"{name}: {voltage}V - {status}")

print(f"{high_count} components are HIGH")
