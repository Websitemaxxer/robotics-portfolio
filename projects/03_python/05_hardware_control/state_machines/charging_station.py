commands = ["plug", "boost", "full", "unplug"]
state = "IDLE"

for command in commands:
    if state == "IDLE" and command == "plug":
        state = "CHARGING"
    elif state == "CHARGING" and command == "full":
        state = "FULL"
    elif state == "FULL" and command == "unplug":
        state = "IDLE"
    print(f"{command} -> {state}")
