import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# reading the data
data = np.loadtxt("Data/star_var.txt", skiprows=0)

# slice the array to separate independent and dependent variables
x = data[:,0]
y = data[:,1]

def model(x, a, b):
    return a*np.sin(b*x)

# takes data you hoping to model with
# returns coefficients you have in your model
# 2 coefficients, thus returns a 2 by 2 array
param, param_cov = curve_fit(model, x, y)

print("Fitter Sin Function Coefficients:", end="")
print(param)
print("Covariance of Coefficients:",end="")
print(param_cov)

fit = (param[0] * np.sin(param[1] * x))

plt.title("Variable Star Fluctuations")
plt.xlabel('Time [d]')
plt.ylabel('Magnitude')
plt.plot(x, y, "o", color = "darkgreen", label = 'data')
plt.plot(x, fit, '--', color='brown', label='Optimized Fit')
plt.legend()
plt.show()