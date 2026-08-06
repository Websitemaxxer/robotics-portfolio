messages = ["Robot booting up",
            "All motors nominal",
            "Battery at 87 percent",
            "Entering standby"]

with open("status.txt", "w") as f:
    for message in messages:
        f.write(message + "\n")

with open("status.txt", "r") as f:
    for line in f:
        print(line.strip())
