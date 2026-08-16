import time

start = time.time()
count = 3
next_second = 1

while count > 0:
    if time.time() - start >= next_second:
        print(count)
        count -= 1
        next_second += 1

print("GO")
