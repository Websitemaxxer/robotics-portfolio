import numpy as np
import matplotlib.pyplot as plt

plt.style.use("fivethirtyeight")

grid = np.array([[20, 24, 30, 28, 35],
                 [40, 45, 42, 50, 48],
                 [10, 12, 15, 14, 20]])
times = np.array([0, 1, 2, 3, 4])

print(np.max(grid[1]))
print(np.max(grid, axis=0))
print(np.mean(grid, axis=0))
print(len(grid[grid < 20]))

plt.plot(times, np.max(grid, axis=0), marker="*", label="max")
plt.plot(times, np.mean(grid, axis=0), marker="o", label="mean")
plt.xlabel("Time step")
plt.ylabel("Reading")
plt.title("Per-time-step max and mean")
plt.legend()
plt.savefig("grid_max_and_mean.png")
