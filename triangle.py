import numpy as np
import matplotlib.pyplot as plt
from math import sin, pi
from numpy import random

#1a)
"""Corners of equilateral triangle. """
corners = np.array([(0,0),(0,1),(sin(pi/3),0.5)])

plt.scatter(*zip(*corners))
plt.axis('equal')
plt.show()

#1b)
def tri(n):
	""" Generates n points inside the triangle. Takes the number of iterations as input, returns list of points."""
	x_0 = []
	r = []
	for i in range(n):
		rand = random.random(3)
		r += [rand/(rand[0]+rand[1]+rand[2])]
		x_0 += [corners[0]*r[i][0] + corners[1]*r[i][1] + corners[2]*r[i][2]]
	return(x_0)

plt.scatter(*zip(*tri(1000)))
plt.axis('equal')
plt.show()

#1c)

def points(n):
	""" Takes the number of iterations as input, and returns the sequence of points as a list."""
	j= np.random.randint(3)
	x = []
	x += tri(1)
	for i in range(1,n+6):						# n+1+1 as we want to remove the first 5
		j = np.random.randint(3)
		x += [(x[i-1] + corners[j])/2]
	return(x[4:])


#1d)
plt.scatter(*zip(*points(10000)), s=0.1)
plt.axis('equal')
plt.axis('off')
marker='.'
plt.show()


#1e)
def points_col(n):
	""" Takes the number of iterations as input, and returns the sequence of points as a list."""
	j= np.random.randint(3)
	x = []
	col = []
	x += tri(1)
	for i in range(0,n+3):						# n+1+1 as we want to remove the first 5
		j = np.random.randint(3)
		col += [j]
		x += [(x[i] + corners[j])/2]
	return x[4:], col[3:]

points, colors = points_col(10000)
red=[]; blue=[]; green=[]
for i in range(len(points)):
	if colors[i] ==0:
		red += [points[i]]
	elif colors[i] ==1:
		blue += [points[i]]
	else:
		green += [points[i]]

plt.scatter(*zip(*red), s=0.1, color="red")
plt.scatter(*zip(*blue), s=0.1, color="blue")
plt.scatter(*zip(*green), s=0.1, color="green")
plt.axis('equal')
plt.axis('off')
marker='.'
plt.show()


#1f)
col = []
col += [np.zeros(3)]
for i in range(len(points)-1):
	col += [(col[i] + colors[i+1])/2]
col = np.asarray(col)
plt.scatter(*zip(*points), c=col[:,0], s=0.1)
plt.axis('equal')
plt.axis('off')
marker='.'
plt.show()

