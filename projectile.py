"""
Created October 13, 2023

Initial values and parameters
"""

import numpy as np
import matplotlib.pyplot as plt

g = 9.81
v0 = 20 # magnitude of initial velocity
theta = 39# initial angle in degrees
vy = v0 * np.sin(theta  * np.pi / 180)
vx = v0 * np.cos(theta * np.pi / 180)
h = 0.01
y = 1.5
x = 0
t = 0
"""
Acceleration function
"""
def acc():
    return -g

"""
Creating arrays
"""
tc = np.zeros(0)
yc = np.zeros(0)
xc = np.zeros(0)

"""
Defining two Heun's methods

vHeun
    - 

yHeun
    - 

"""

def vHeun(vy):
    # vendy = vy + acc() * h 
    # vy = vy + (acc() + acc()) / 2*h
    vy = vy + acc()*h
    return vy

def yHeun(y, vy):
    # endy = y + vy * h
    y = y + (vy + vy) / 2 * h
    return y

while y >= 0:
    vy = vHeun(vy)
    y = yHeun(y, vy)
    x = x + vx * h
    t = t + h
    yc = np.append(yc, y)
    xc = np.append(xc, x)
    tc = np.append(tc, t)

plt.plot(xc, yc, "g-", label="Path")
plt.show()

"""
Argmax returns the index of the max value
"""
print('Max height = {:4.2f} m'.format(yc[np.argmax(yc)]))
print('Time at max height {:4.2f} s'.format(tc[np.argmax(yc)]))