"""
Created on October 4
"""
import numpy as np
import matplotlib.pyplot as plt

# define the slope
def der(y):
    return y * y + 1

# create discrete values of t
# N is the number of points
N = 20
t = np.linspace(0, 1, N)
h = t[1] - t[0]

y = np.zeros(N)

#initial conditions
# y[0] = 0

#Euler algorithm
for i in range(1, N):
    y[i] = y[i-1] + der(y[i - 1]) * h
plt.plot(t, y, "bo", label="Euler")

# modified Euler using midpoint
for i in range(1,N):
    yMid = y[i - 1] + der(y[i-1]) * h/2
    y[i] = y[i-1] + der(yMid) * h
plt.plot(t, y, "g^", label="Euler Plus")


"""
Heun
"""
for i in range(1, N):
    yend = y[i - 1] + der(y[i - 1]) * h # use Euler to make a prediction
    y[i] = y[i-1] + (der(y[i-1]) + der(yend))/2 * h
plt.plot(t, y, "gx", label="Heun")


plt.xlabel("t")
plt.ylabel("y")
plt.plot(t, np.tan(t), "r-", label="Exact")
plt.legend()
plt.show()