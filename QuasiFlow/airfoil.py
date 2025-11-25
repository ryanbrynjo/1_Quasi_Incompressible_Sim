import matplotlib.pyplot as plt
import numpy as np
import argparse
import os

"""
From Scratch X-Foil Like Simulator Using Vortex Panel Method
"""

X, Y = np.meshgrid(np.linspace(-2, 2, 20), np.linspace(-2, 2, 20))

U_unif = 10
U = np.ones_like(X)*U_unif
V = np.zeros_like(Y)





plt.streamplot(X, Y, U, V)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Streamplot of a Vortex')

plt.show()