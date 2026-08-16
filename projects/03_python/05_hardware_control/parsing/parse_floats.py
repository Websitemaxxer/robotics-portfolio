raw_lines = [b"45.2\r\n", b"46.8\r\n", b"44.1\r\n", b"47.5\r\n"]

values = []
for raw in raw_lines:
    value = float(raw.decode().strip())
    values.append(value)
    print(value)

print(round(sum(values) / len(values), 1))
