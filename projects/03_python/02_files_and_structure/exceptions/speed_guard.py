def set_speed(speed):
    if speed < 0 or speed > 255:
        raise ValueError(f"Speed {speed} is out of range (0-255)")
    print(f"Speed set to {speed}")

for value in [200, -5, 300, 120]:
    try:
        set_speed(value)
    except ValueError as e:
        print(e)
