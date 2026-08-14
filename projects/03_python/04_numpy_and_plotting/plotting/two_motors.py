import matplotlib.pyplot as plt

times = [0, 1, 2, 3, 4, 5]
left_motor = [20, 28, 35, 44, 52, 60]
right_motor = [25, 33, 48, 59, 71, 85]

plt.plot(times, left_motor, label="left")
plt.plot(times, right_motor, label="right")
plt.xlabel("Time (s)")
plt.ylabel("Temperature (C)")
plt.title("Two motor temperatures over time")
plt.legend()
plt.savefig("two_motors.png")
