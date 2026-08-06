commands = ["start", "speed_up", "obstacle", "clear", "stop"]
state = "idle"

for command in commands:
    if command == "start" and state == "idle":
        state = "moving"
    elif command == "obstacle" and state == "moving":
        state = "paused"
    elif command == "clear" and state == "paused":
        state = "moving"
    elif command == "stop":
        state = "idle"
    print(f"{command} -> {state}")
