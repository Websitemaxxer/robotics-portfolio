raw_lines = [b"temp:45.2\r\n", b"temp:52.9\r\n", b"temp:39.4\r\n", b"temp:60.1\r\n"]

high_count = 0
for raw in raw_lines:
    label, number = raw.decode().strip().split(":")
    value = float(number)
    print(label, value)
    if value > 50:
        high_count += 1

print(f"{high_count} readings above 50")
