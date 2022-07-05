# _*_ coding: utf-8 _*_
"""
Created on 04/07/2022
	Functions to solve differential eqs using sympy applied to rx kinetic study
@author: ADOB

require matplotlib, sympy, numpy, scipy
execute: pip install matplotlib sympy numpy scipy
"""

import numpy as np
import matplotlib.pyplot as plt
import sympy
from scipy import integrate

# Print with math latex notation
sympy.init_printing(use_latext="mathjax")

# define vars
t = sympy.Symbol("t")
A = sympy.Function("A")
A0 = 10
c = 100
x = np.arange(0, 2, 0.01)
x_vec = np.linspace(-3, 3, 100)
y = A0-(c*x)

# Def eq
f = -c*(A(t))**0
sympy.Eq(A(t).diff(t), f)

# Solve eq
solv = sympy.dsolve(A(t).diff(t)-f)
print(solv)

fig = plt.figure(2)
fig.clf()
ax = fig.add_subplot(1,1,1)
ax.plot(x, y)

# Add title and labels to plot.
ax.set_xlabel("Time (s)")
ax.set_ylabel("Concentration")
ax.set_title("Order zero rx")
ax.grid(True)

# Show the plot.
plt.show()

