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
		mult = np.array([[a, b], [c, d]])
		addit = np.array([e, f])
		xy = np.array([x, y])
		transform = mult*xy + addit
	



if __name__ == "__main__":
	f1 = AffineTransform(0,0,0,0.16,0,0)
	f2 = AffineTransform(0.85,0.04,-0.04,0.85,0,1.60)
	f3 = AffineTransform(0.20,-0.26,0.23,0.22, 0, 1.60)
	f4 = AffineTransform(-0.15,0.28,0.26,0.24,0,0.44)

	p_ = []
	p_ += 0.1
	p_ += 0.86
	p_ += 0.93
	p_ += 1.0


	r = np.random.random()
	for j, p in enumerate(p_):
		if r < p:
			return functions[j]