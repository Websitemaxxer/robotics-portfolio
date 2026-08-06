import csv

with open("readings.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["sensor", "value"])
    writer.writerow(["front", "22"])
    writer.writerow(["rear", "45"])
    writer.writerow(["left", "9"])
    writer.writerow(["right", "88"])

pairs = []

with open("readings.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        sensor = row[0]
        value = int(row[1])
        pairs.append((sensor, value))
        print(f"{sensor}: {value}")

values = [value for sensor, value in pairs]
average = sum(values) / len(values)
highest_sensor, highest_value = max(pairs, key=lambda pair: pair[1])

with open("summary.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["metric", "value"])
    writer.writerow(["average", round(average, 1)])
    writer.writerow(["highest", f"{highest_sensor} ({highest_value})"])

print(f"Average value: {round(average, 1)}")
print(f"Highest: {highest_sensor} at {highest_value}")
