import csv

with open("readings.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["sensor", "value"])
    writer.writerow(["temp", "89"])
    writer.writerow(["humidity", "24"])
    writer.writerow(["wind", "19"])
    writer.writerow(["distance", "439"])
    writer.writerow(["pressure", "oops"])

valid = []
with open("readings.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        try:
            value = int(row[1].strip())
        except (ValueError, IndexError):
            continue
        valid.append(value)
        print(f"{row[0]}: {value}")

average = round(sum(valid) / len(valid), 1)
print(f"{len(valid)} valid readings, average {average}")

with open("summary.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["metric", "value"])
    writer.writerow(["valid_readings", len(valid)])
    writer.writerow(["average", average])
