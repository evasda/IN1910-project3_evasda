
import numpy as np
import matplotlib.pyplot as plt
from math import sin, cos, pi
from numpy import random, linspace

#1a)

class ChaosGame:
	def __init__(self, n, r):
		if type(n) == int and n>=3:
			self.n = n
		else:
			raise ValueError("n must be an integer, and greater or equal to 3.")
		if type(r) == float and r<1 and r>0:
			self.r = r
		else:
			raise ValueError("r must be a float, and strictly between 0 and 1.")
		self.c = self._generate_ngon(n)

	def _starting_point(self):
		"""Takes zero arguments, create random starting point as a linear combination of vertices, and returns a list."""
		x_0 = []
		r_norm = []
		n = self.n
		r = random.random(self.n)
		c = self.c
		c = np.asarray(c)
		for i in range(n):
			r_norm += [r[i]/sum(r)]
			x_0 += [r_norm[i]*c[i]]
		return(sum(x_0))

	def _generate_ngon(self, n):
		"""Takes in number of vertices, and returns a list."""
		c = []
		theta = linspace(0,2*np.pi,n+1)
		for i in theta:
			c += [(sin(i), cos(i))]
		return c

	def plot_ngon(self):
		"""Plots the generated n-gon."""
		plt.scatter(*zip(*self.c))
		plt.axis('equal')
		plt.axis('off')
		marker='.'
		plt.show()

	def iterate(self, steps, discard=5):
		j= np.random.randint(3)
		x = []
		col = []
		x += [self._starting_point()]
		c = np.asarray(self.c)
		for i in range(0,steps):						# n+1+1 as we want to remove the first 5
			j = random.randint(self.n)
			col += [j]
			x += [self.r*(x[i] + (1-self.r)*c[j])]
		self.x = x

	def show(self, show =1):
		"""Added a predefined parameter show (with 1 for true, 0 for false) to be able to use the show method in savepng."""
		plt.scatter(*zip(*self.x), s=0.1)
		plt.axis('equal')
		plt.axis('off')
		marker='.'
		if show== 1:
			plt.show()

	def savepng(self, outfile):
		"""Takes in a filename as either png or with non-specified format. Creates a png-file."""
		if ".png" in outfile:
			o = outfile
		elif "." in outfile and "png" not in outfile:
			raise ValueError("Non-valid file format as input. Please use .png or nothing.")
		else:
			o = outfile + ".png"
		self.show(0)
		plt.savefig(o, dpi = 300)
		plt.close()



if __name__ == "__main__":
	c = []
	n3 =ChaosGame(3, 0.5)
	n4 =ChaosGame(4, 0.4)
	n5 =ChaosGame(5, 0.5)
	n6 =ChaosGame(6, 0.4)
	n7 =ChaosGame(7, 0.4)
	n8 =ChaosGame(8, 0.4)
	"""
	n2.plot_ngon()
	n3.plot_ngon()
	n4.plot_ngon()
	n5.plot_ngon()
	n6.plot_ngon()
	n7.plot_ngon()
	n8.plot_ngon()
	for i in range(10000):
		c += [n4._starting_point()]
	plt.scatter(*zip(*c), s=0.2)
	plt.axis('equal')
	plt.show()
	"""
	n3.iterate(10000)
	n3.show()
	n3.savepng("plot_ngon")

	#2i)
	nn3 = ChaosGame(3, 0.5)
	nn4 = ChaosGame(4, 1./3)
	nn5 = ChaosGame(5, 1./3)
	nn5_ = ChaosGame(5, 3./8)
	nn6 = ChaosGame(6, 1./3)
	
	nn3.iterate(10000)
	nn4.iterate(10000)
	nn5.iterate(10000)
	nn5_.iterate(10000)
	nn6.iterate(10000)

	import os
	os.chdir(r'C:\Users\Eva\IN1910\project3_evasda\figures')

	nn3.savepng("chaos1")
	nn4.savepng("chaos2")
	nn5.savepng("chaos3")
	nn5_.savepng("chaos4")
	nn6.savepng("chaos5")

	#import os
	#os.chdir(r'C:\Users\Eva\IN1910\project3_evasda\figures')