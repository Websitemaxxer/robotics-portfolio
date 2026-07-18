# Week 1 review: battery level check
# Combines lists, enumerate, conditionals, comprehensions, f-strings
# Jul 18, 2026 — correct on the first attempt; `elif` tidied to `else`, enumerate set to start=1

battery = [12, 14, 15, 39, 98]

for i, reading in enumerate(battery, start=1):
    if reading < 30:
        status = "LOW"
    else:
        status = "OK"
    print(f"Module {i}: {reading}% - {status}")

low = [reading for reading in battery if reading < 30]

print(f"{len(low)} modules are low")
