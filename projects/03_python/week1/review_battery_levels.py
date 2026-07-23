battery = [12, 14, 15, 39, 98]

for i, reading in enumerate(battery, start=1):
    if reading < 30:
        status = "LOW"
    else:
        status = "OK"
    print(f"Module {i}: {reading}% - {status}")

low = [reading for reading in battery if reading < 30]

print(f"{len(low)} modules are low")
