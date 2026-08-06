import telemetry

readings = [22, 45, 88, 30, 12]

print(f"Average: {round(telemetry.average(readings), 1)}")
print(f"Peak: {telemetry.peak(readings)}")

all_ok = True
for r in readings:
    if not telemetry.in_range(r, 0, 100):
        all_ok = False
print(f"All within 0-100? {all_ok}")
