"""
October 1
"""
from math import *
from scipy.optimize import fsolve

x1 = float(input("Enter the value of x1: "))
x2 = float(input("Enter the value of x2: "))

def f(x):
    return 3*x + 2*x*x - 5 - 10*cos(x)

def fPrime(x):
    return 3 + 4*x + 10*sin(x)
# while abs(x2 - x1) > 0.0001:
#     xm = (x1 + x2) / x2
#     if f(xm) * f(x1) > 0:
#         x1 = xm
#     else:
#         x2 = xm
#     print("Middle Point: ",xm)

tolerance = float(input("Tolerance: "))
xnew = float(input("Enter starting value of x: "))

for i in range(100):
    x = xnew
    xnew = x - f(x) / fPrime(x)
    if abs(x - xnew) < tolerance:
        print("Root is: ",xnew, " to within ", tolerance)
        break

print("Root 1: ", fsolve(f, -2))
print("Root 2: ", fsolve(f, 1.3))