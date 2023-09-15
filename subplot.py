import matplotlib.pyplot as plt
from numpy import exp, linspace

# define a range of time values equally spaced from 0 to 500
time = linspace(0, 500, 1000)
number = 1000*exp(-time/100) # number of radioactive nuclei left after time t
plt.subplot(2, 1, 1)
plt.xlabel("Time")
plt.ylabel("Number")
plt.title("Radioactive Decay")
plt.plot(time, number, "g-")

plt.subplot(2, 1, 2)
plt.xlabel("Time")
plt.ylabel("Log Number")
plt.semilogy(time, number)
plt.title("Semilog Plot")
plt.grid(True)
plt.show()