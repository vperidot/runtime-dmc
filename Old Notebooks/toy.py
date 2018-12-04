import numpy as np
import matplotlib.pyplot as plt

mean = [0, 0]
cov = [[10, 0], [0, 10]]
x, y = np.random.multivariate_normal(mean, cov, 50).T

print(x)
print(y)
plt.plot(x, y, 'x')
plt.axis('equal')
plt.show()