import numpy as np

grid = np.array([[12, 15, 16],
                 [98, 35, 87],
                 [45, 63, 85]])

print(grid[1, 2])
print(grid[0])
print(grid[:, 1])
print(grid.mean(axis=0))
print(grid.max(axis=1))
print((grid > 50).sum())
