import numpy as np
import matplotlib.pyplot as plt
from scipy.special import gamma

# create indep. variable
x = np.linspace(-6, 6, 100)
sigma = [0.5, 1.0, 2.0, 5.0]

def funk(x, sigma):
    return 1/(2*sigma*np.sqrt(2*np.pi)) * np.exp(-(x-0)**2/(2*sigma))

fmax = np.zeros(4)
xmax = np.zeros(4)

j = 0
for i in sigma:
    y = funk(x, i)
    fmax[j] = np.amax(y)
    xmax[j] = x[np.argmax(y)]
    plt.plot(x, y)
    plt.text(15, 0.15 - j *0.01, r"$\sigma$ = %i Max = %.2f, at %.2f" % (i, fmax[j], xmax[j]))
    j = j + 1

plt.title(r"$\chi^{2}$ Probability Curve for $\sigma = 4, 10$")
plt.xlabel(r"#\chi^2$")
plt.ylabel(r"$f(\chi^2$)")
plt.show()

def func(x):
    return np.cos(x) - np.exp(-x)

x = np.arange(-2, 2, 0.01)
y = func(x)

print("max y = ", np.max(y))


h = 0.01
derivative = np.diff(y)/h
plt.plot(x[:-1], derivative, "b-")

plt.plot(x, y, "gx")
plt.plot(x, -x*x, "r-")
plt.xlabel("x ")
plt.ylabel("y")


plt.legend(('cos(x) - exp(-x)', "-x ** 2"), loc=2)
plt.show()