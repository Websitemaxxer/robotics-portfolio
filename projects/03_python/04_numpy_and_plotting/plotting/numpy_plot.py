import numpy as np
import matplotlib.pyplot as plt

samples = np.array([0, 1, 2, 3, 4, 5])
readings = np.array([12, 30, 25, 48, 40, 65])

plt.plot(samples, readings, marker="o", label="raw")
plt.plot(samples, readings + 10, marker="s", label="calibrated")
plt.xlabel("Sample")
plt.ylabel("Reading")
plt.title("Raw vs calibrated readings")
plt.legend()
plt.savefig("numpy_plot.png")
