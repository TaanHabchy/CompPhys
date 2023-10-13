"""
Created on Octeber 9, 2023
"""

import numpy as np
import matplotlib.pyplot as plt

#parameters
a, b, c, P = 0.8, 0.02, 5.5, 5.0

def rate(value, t):    
    return (a * value) - (b * value **2)  - (c * np.sin((2 * np.pi * t) / P))

numpts = 100
t = np.linspace(0, 10, numpts)
h = t[1] - t[0]
N = np.zeros(numpts)
N[0] = 100
t[0] = 0

"""
Implement Heun's Method
"""

for i in range(1, numpts):
    Nend = N[i - 1] + rate(N[i-1], t[i-1]) * h
    tend = t[i-1] + h
    N[i] = (N[i - 1] + (rate(N[i-1], t[i-1]) + rate(Nend, tend)) / 2 * h)


plt.plot(t, N, "darkgreen", label="Heun's Method")
plt.xlabel("Time")
plt.ylabel("Number of Specimens")
plt.ylim(0, 110)
plt.title(r"Solution of $\frac{dN}{dt} - aN - bN^2 + c \sin\frac{2\pi t}{P}$")
plt.legend()
plt.show()