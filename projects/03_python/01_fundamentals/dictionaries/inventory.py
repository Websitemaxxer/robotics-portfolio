parts_used = ["motor", "screw", "motor", "gear", "screw", "screw", "motor"]

counts = {}
for part in parts_used:
    counts[part] = counts.get(part, 0) + 1

for part, count in sorted(counts.items()):
    print(f"{part}: {count}")

most_used = max(counts, key=counts.get)
print(f"Most used: {most_used}")
