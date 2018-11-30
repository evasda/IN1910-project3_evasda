import numpy as np
import matplotlib.pyplot as plt
from math import sin, cos, pi
from numpy import random, linspace

class AffineTransform():
	def __init__(self, a=0, b=0, c=0, d=0, e=0, f=0):
		self.a = a
		self.b = b
		self.c = c
		self.d = d
		self.e = e
		self.f = f

	def __call__(self, x, y):
		x_ = self.a*x + self.b*y + self.e
		y_ = self.c*x + self.d*y + self.f
		return [x_, y_]



if __name__ == "__main__":
	functions = []
	functions += [AffineTransform(0,0,0,0.16,0,0)]
	functions += [AffineTransform(0.85,0.04,-0.04,0.85,0,1.60)]
	functions += [AffineTransform(0.20,-0.26,0.23,0.22, 0, 1.60)]
	functions += [AffineTransform(-0.15,0.28,0.26,0.24,0,0.44)]
	def weighted_functions(x, y):
		p_c = [0.1, 0.86, 0.93, 1.0]
		r = np.random.random()
		for i in range(len(p_c)):
			if r < p_c[i]:
				return functions[i](x, y)

	def iterate(n):
		x = []
		x += [[0, 0]]
		for i in range(n):
			x += [weighted_functions(x[i][0], x[i][1])]
		return x

	xx = iterate(50000)
	def plot_ngon():
		"""Plots the generated Barnsley fern."""
		plt.scatter(*zip(*xx), s=0.05, color="green")
		plt.axis('equal')
		plt.axis('off')
		marker='.'
		plt.show()
	plot_ngon()