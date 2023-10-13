import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

data = np.loadtxt("Data/UZLyrO_C_Residuals.txt")

t = data[:,0] # time
y = data[:,1]

ySigma = np.std(y) / np.sqrt(2)

# We bouta curve fit, data is going up and down, so we gonna try COS
# initial values of parameters
A0, B0, C0, D0 = ySigma, 1668.76, 0, np.mean(y)

#define model function
def fun(t, A, B, C, D):
    return A * (np.cos((2 * np.pi * t) / B + C) + D)

# optimize our curve fit
# popt: optimized curve parameters
# pcov: covariance
# curve fit returns 2 arrays
popt, pcov = curve_fit(fun, t, y, p0= [A0, B0, C0, D0], sigma=None)

punc = np.sqrt(np.diag(pcov)) # computes the standard deciation uncertainties 

# format output using pythonic formatting
print("Amplitude = {0:8.6f} +/- {1:8.6f},\n \
      Period = {2:8.6f} +/- {3:8.6f}".format(popt[0], punc[0], popt[1], punc[1]))

print("Amplitude = {0:8.6f} +/- {1:8.6f},\n \
      Period = {2:8.6f} +/- {3:8.6f}".format(popt[2], punc[2], popt[3], punc[3]))

#plot our results
plt.plot(t,y, ".", label="Residuals")
plt.plot(t, fun(t, *popt), "r-", label="Model Curve Fit")
plt.title("Model Curve Fit to Residuals of UZ Lyr")
plt.ticklabel_format(axis = "y", style="sci", scilimits=(-4, 3))
plt.xlabel("Cycle Number n")
plt.ylabel("Residuals (mag)", va = "center")
plt.legend()
plt.show()