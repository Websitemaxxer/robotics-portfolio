import time

start = time.time()
last_read = start
last_report = start

while time.time() - start < 3:
    now = time.time()
    if now - last_read >= 0.5:
        print("read")
        last_read = now
    if now - last_report >= 1.0:
        print("report")
        last_report = now
