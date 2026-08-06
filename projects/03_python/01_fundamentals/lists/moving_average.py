readings = [10, 12, 14, 20, 18, 30, 28, 25]
window = 3

for i in range(len(readings) - window + 1):
    chunk = readings[i:i + window]
    average = sum(chunk) / window
    print(f"Readings {i + 1}-{i + window}: average {round(average, 1)}")
