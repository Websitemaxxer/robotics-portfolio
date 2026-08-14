import numpy as np

readings = np.array([12, 55, 8, 90, 33, 61, 5])

high = readings[readings > 50]

print(high)
print(len(high))
print(round(high.mean(), 1))
