
import numpy as np
import matplotlib.pyplot as plt
from math import sin, pi
from numpy import random

#1a)

corners = np.array([(0,0),(0,1),(sin(pi/3),0.5)])

#plt.scatter(*zip(*corners))
#plt.axis('equal')
#plt.show()

#1b)
"""
rand_ = np.zeros([1000, 3])
x_0 = np.zeros([1000])

for i in range(1000):
	rand = random.random(3)
	for j in range(0,3):
		rand_[i,j] = rand[j]/(rand[0]+rand[1]+rand[2])
	x_0 = sum(rand_[i,]*corners)
"""

def tri(n):
	x_0 = []
	r = []
	for i in range(n):
		""" Generates 1000 points inside the triangle. Takes the number of iterations as input, returns list of points."""
		rand = random.random(3)
		r += [rand/(rand[0]+rand[1]+rand[2])]
		x_0 += [corners[0]*r[i][0] + corners[1]*r[i][1] + corners[2]*r[i][2]]
	return(x_0)
"""
plt.scatter(*zip(*tri(1000)))
plt.axis('equal')
plt.show()
"""

#1c)

def points(n):
	""" Takes the number of iterations as input, and returns the sequence of points as a list."""
	j= np.random.randint(3)
	x2 = []
	x2 += tri(1)
	for i in range(1,n+6):						# n+1+1 as we want to remove the first 5
		j = np.random.randint(3)
		x2 += [(x2[i-1] - corners[j])/2]
	return(x2[4:])



plt.scatter(*zip(*points(10000)), s=0.1)
plt.axis('equal')
plt.show()