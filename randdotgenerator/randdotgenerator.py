import numpy as np
import matplotlib.pyplot as plt

# Create random points
N = 3000
x = np.random.rand(N)
y = np.random.rand(N)
area = 18

# Plot
plt.scatter(x, y, s=area, marker='s', edgecolors='none')
plt.show()

