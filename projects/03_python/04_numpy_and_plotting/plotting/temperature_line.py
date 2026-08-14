import matplotlib.pyplot as plt

times = [0, 1, 2, 3, 4, 5]
temps = [22, 30, 41, 55, 62, 70]

plt.plot(times, temps, marker="o")
plt.xlabel("Time (s)")
plt.ylabel("Temperature (C)")
plt.title("Motor temperature over time")
plt.savefig("temperature_line.png")
