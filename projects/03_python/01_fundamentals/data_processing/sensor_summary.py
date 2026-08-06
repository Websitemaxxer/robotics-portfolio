log = [("temp", 22), ("pressure", 101), ("temp", 25), ("temp", 19),
       ("pressure", 98), ("humidity", 60), ("humidity", 55), ("pressure", 103)]

readings_by_type = {}
for sensor, value in log:
    if sensor in readings_by_type:
        readings_by_type[sensor].append(value)
    else:
        readings_by_type[sensor] = [value]

summary = []
for sensor, values in readings_by_type.items():
    average = sum(values) / len(values)
    summary.append((sensor, round(average, 1), len(values)))

summary.sort(key=lambda row: row[1], reverse=True)

for sensor, average, count in summary:
    print(f"{sensor}: {count} readings, average {average}")
