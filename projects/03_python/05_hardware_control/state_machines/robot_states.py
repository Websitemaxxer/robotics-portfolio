commands = ["start", "stop", "reset", "start", "stop"]
state = "IDLE"

for command in commands:
    if state == "IDLE" and command == "start":
        state = "MOVING"
    elif state == "MOVING" and command == "stop":
        state = "STOPPED"
    elif state == "STOPPED" and command == "reset":
        state = "IDLE"
    print(f"{command} -> {state}")
