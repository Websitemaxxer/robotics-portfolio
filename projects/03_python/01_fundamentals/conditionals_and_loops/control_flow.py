countdown = 5

while countdown > 0:
    print(f"Launching in {countdown}")
    countdown -= 1
print("Go")

readings = [15, 22, -1, 30, 8, -1, 99, 40]

for reading in readings:
    if reading < 0:
        continue
    if reading > 90:
        print("Sensor fault, stopping")
        break
    if reading < 20:
        print(f"{reading} cm - too close")
    else:
        print(f"{reading} cm - clear")
