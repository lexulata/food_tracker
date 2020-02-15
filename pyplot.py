from matplotlib import pyplot as plt
import numpy as np

population_ages = np.random.randin(1,100,99)
pins = range(0,101,10)

plt.hist(population_ages,pins,histtype='bar',width=0,0)

plt.xlabel('x')
plt.legend()
plt.show()

