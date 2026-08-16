import time
import serial

PORT = "/dev/cu.usbmodem1101"
ser = serial.Serial(PORT, 9600, timeout=1)

start = time.time()
while time.time() - start < 10:
    line = ser.readline().decode().strip()
    if not line:
        continue
    reading = int(line)
    if reading > 80:
        ser.write(b"STOP\n")
    else:
        ser.write(b"GO\n")
    print(reading)

ser.close()
