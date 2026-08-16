raw_lines = [b"22,45,67\r\n", b"30,50,80\r\n", b"18,40,90\r\n"]

for raw in raw_lines:
    numbers = [int(x) for x in raw.decode().strip().split(",")]
    print(max(numbers))
