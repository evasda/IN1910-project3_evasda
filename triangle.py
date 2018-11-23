
import numpy as np
import matplotlib.pyplot as plt
from math import sin, pi

corners = np.array([(0,0),(0,1),(sin(pi/3),0.5)])

plt.scatter(*zip(*corners))
plt.axis('equal')
plt.show()
