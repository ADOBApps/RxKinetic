# _*_ coding: utf-8 _*_
"""
Created on 03/07/2022
	Functions to solve differential eqs using sympy
@author: ADOB

require matplotlib, sympy, numpy, scipy
execute: pip install matplotlib sympy numpy scipy

"""

import matplotlib.pyplot as plt
import numpy as np
import sympy
from scipy import integrate

# Print with math latex notation
sympy.init_printing(use_latext="mathjax")

# Solve diffential es
# define vars
x = sympy.Symbol('x')
y = sympy.Function('y')

# def eq
f = 6*x**2 - 3*x**2*(y(x))
sympy.Eq(y(x).diff(x), f)

# Solve differential eq
edo_solv = sympy.dsolve(y(x).diff(x)-f)
edo_solv

# Show the major grid lines with dark grey lines
plt.grid(visible=True, which='major', color='#666666', linestyle='-')

# Show the minor grid lines with very faint and almost transparent grey lines
plt.minorticks_on()
plt.grid(visible=True, which='minor', color='#999999', linestyle='-', alpha=0.2)

# Initialise the figure and a subplot axes. Each subplot sharing (showing) the
# same range of values for the x and y axis in the plots.
fig, axes = plt.subplots(2, 1, figsize=(8, 6), sharex=True, sharey=True)

# Set the title for the figure
fig.suptitle(r"$%s$" % (sympy.latex(edo_solv)), fontsize=15)


# print(r"$%s$" % (sympy.latex(edo_solv)))

plt.show()