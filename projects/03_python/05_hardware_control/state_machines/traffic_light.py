commands = ["next", "next", "next", "next"]
state = "RED"

for command in commands:
    if command == "next":
        if state == "RED":
            state = "GREEN"
        elif state == "GREEN":
            state = "AMBER"
        elif state == "AMBER":
            state = "RED"

    if state == "RED":
        print("stop")
    elif state == "GREEN":
        print("go")
    elif state == "AMBER":
        print("slow down")
