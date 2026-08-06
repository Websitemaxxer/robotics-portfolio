try:
    with open("config.txt", "r") as f:
        for line in f:
            print(line.strip())
except FileNotFoundError:
    print("config.txt not found - using defaults")
