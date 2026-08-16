import serial

PORT = "/dev/cu.usbmodem1101"
ser = serial.Serial(PORT, 9600, timeout=1)

for _ in range(10):
    line = ser.readline().decode().strip()
    if line:
        value = float(line)
        print(value)

ser.close()
