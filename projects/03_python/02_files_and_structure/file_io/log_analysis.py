entries = ["OK boot",
           "OK sensors",
           "ERROR motor",
           "OK battery",
           "ERROR gyro",
           "OK standby"]

with open("system.log", "w") as f:
    for entry in entries:
        f.write(entry + "\n")

errors = 0
with open("system.log", "r") as f:
    for line in f:
        line = line.strip()
        if "ERROR" in line:
            errors += 1
            print(f"Found: {line}")

print(f"{errors} errors in the log")
