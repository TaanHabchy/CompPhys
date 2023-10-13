"""
Created on October 11th

Radioactive decay solution using Heun's method
"""


import numpy as np
import matplotlib.pyplot as plt


"""
Initalizing the parameters
k1 and k2 have units of 1 / time
"""
k1 = 0.15
k2 = 0.2

"""
define rates, the rates are derivates
"""

def R1(N1):
    return -k1 * N1

def R2(N1, N2):
    return k1 * N1 - k2 * N2

"""
defining a grid of times
"""

t = np.linspace(0, 30, 200)
h = t[1] - t[0]


"""
defining an array for numbers of nuclei
"""

N1 = np.zeros(200)
N2 = np.zeros(200)

"""
Initial Value
"""
N1[0] = 1000
N2[0] = 0


"""
Heun's Method
"""
for i in range(1, 200):
    N1end = N1[i-1] + R1(N1[i-1]) * h
    N1[i] = N1[i-1] + (R1(N1[i-1]) + R1(N1end)) / 2*h

    N2end = N2[i-1] + R2(N1[i-1], N2[i-1]) * h
    N2[i] = N2[i-1] + (R2(N1[i-1], N2[i-1]) + R2(N1end, N2end)) / 2*h

"""
Plotting
"""

# plt.plot(t, N1, "b-", label = "Parent")
# plt.plot(t, N2, "g-", label = "Child")
plt.semilogy(t, N1, "g-", label="parent")
plt.semilogy(t, N2, "b-", label="child")
plt.xlabel("Time (s)")
plt.ylabel("Number")
plt.legend()
plt.show()