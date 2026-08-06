raw = ["22", "45", "oops", "88", "", "30"]

values = []
for item in raw:
    try:
        values.append(int(item))
    except ValueError:
        print(f"Skipping invalid reading: {item}")

print(f"Kept {len(values)} valid readings")
print(f"Average: {round(sum(values) / len(values), 1)}")
