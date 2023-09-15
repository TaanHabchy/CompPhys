import numpy as np
import matplotlib.pyplot as plt
from scipy.special import gamma

# create indep. variable
x = np.linspace(0, 28, 100)
nu = [4,10]

def funk(x, nu):
    return 1/((2**(nu/2)) * gamma(nu/2)) * np.exp(-x/2)*(x**((nu/2) - 1))

fmax = np.zeros(2)
xmax = np.zeros(2)

j = 0
for i in nu:
    y = funk(x, i)
    fmax[j] = np.amax(y)
    xmax[j] = x[np.argmax(y)]
    plt.plot(x, y)
    plt.text(15, 0.15 - j *0.01, r"$\nu$ = %i Max = %.2f, at %.2f" % (i, fmax[j], xmax[j]))
    j = j + 1

plt.title(r"$\chi^{2}$ Probability Curve for $\nu = 4, 10$")
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