import numpy as np
import matplotlib.pyplot as plt

population = np.zeros((100, 100))

outbreak = np.random.choice(range(100), 2)
population[outbreak[0], outbreak[1]] = 1

plt.imshow(population, cmap='viridis', interpolation='nearest')
plt.show()
