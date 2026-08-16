import time

start = time.time()
ticks = 0
next_tick = 1

while ticks < 5:
    if time.time() - start >= next_tick:
        print("tick")
        ticks += 1
        next_tick += 1
