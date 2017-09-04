import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab
import math

mu = 0
sigma = 0.1
x = np.linspace(-3, 3, 100)
plt.plot(x,mlab.normpdf(x, mu, sigma))

plt.show()
