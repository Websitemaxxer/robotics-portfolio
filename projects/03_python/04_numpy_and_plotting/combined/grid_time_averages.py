import numpy as np
import matplotlib.pyplot as plt

plt.style.use("fivethirtyeight")

grid = np.array([[20, 24, 30, 28, 35],
                 [40, 45, 42, 50, 48],
                 [10, 12, 15, 14, 20]])
times = np.array([0, 1, 2, 3, 4])

print(np.mean(grid, axis=1))
print(np.mean(grid, axis=0))
print(len(grid[grid > 30]))

plt.plot(times, np.mean(grid, axis=0), marker="o")
plt.xlabel("Time step")
plt.ylabel("Average reading")
plt.title("Average sensor reading per time step")
plt.savefig("grid_time_averages.png")
