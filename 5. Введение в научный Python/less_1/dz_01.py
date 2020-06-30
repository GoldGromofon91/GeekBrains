import matplotlib.pyplot as plt
import numpy as np

k=1
x = np.linspace(0, 10, 120)
plt.plot(x, np.cos(x*k))

k=2
y= np.linspace(0,10,120)
plt.plot(y, np.cos(y*k))
plt.show()

