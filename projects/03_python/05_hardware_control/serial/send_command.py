import serial

PORT = "/dev/cu.usbmodem1101"
ser = serial.Serial(PORT, 9600, timeout=1)

for _ in range(10):
    line = ser.readline().decode().strip()
    if not line:
        continue
    reading = int(line)
    if reading < 20:
        command = b"STOP\n"
    elif reading <= 60:
        command = b"SLOW\n"
    else:
        command = b"GO\n"
    ser.write(command)
    print(reading, command)

ser.close()
