readings = [("front", 22), ("rear", 45), ("left", 9), ("right", 88), ("top", 30)]

by_value = sorted(readings, key=lambda pair: pair[1], reverse=True)

print("Ranked by distance:")
for name, value in by_value:
    print(f"  {name}: {value} cm")

top_three = by_value[:3]
print(f"Top 3: {[name for name, value in top_three]}")
