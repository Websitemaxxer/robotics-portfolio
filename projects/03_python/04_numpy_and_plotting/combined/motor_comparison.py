import numpy as np
import matplotlib.pyplot as plt

plt.style.use("ggplot")

times = np.array([0, 1, 2, 3, 4, 5, 6])
left = np.array([20, 28, 35, 44, 52, 60, 68])
right = np.array([25, 33, 48, 59, 71, 85, 99])

average = (left + right) / 2

print(round(np.mean(left), 1))
print(round(np.mean(right), 1))
print(len(right[right > 70]))

plt.plot(times, left, label="left")
plt.plot(times, right, label="right")
plt.plot(times, average, label="average")
plt.xlabel("Time (s)")
plt.ylabel("Temperature (C)")
plt.title("Left, right, and average motor temperature")
plt.legend()
plt.savefig("motor_comparison.png")
