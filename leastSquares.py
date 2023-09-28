import numpy as np
import matplotlib.pyplot as plt

fileName = "Data/antarctica_mass_200204_202006.txt"
data = np.loadtxt(fileName, float, skiprows=31)


x = np.array(data[:,0]) # first column
y = np.array(data[:,1]) # second column

#finding the number of entries
N = len(x)

def leastSqrs(x, y):
    # initialize values
    sumX = 0
    sumY = 0
    sumXX = 0
    sumXY = 0
    A = 0
    B = 0

    #perform sums
    sumX = np.sum(x)
    sumY = np.sum(y)
    sumXX = np.sum(x * x)
    sumXY = np.sum(x * y)

    #determine the coefficients A and B
    Delta = (N * sumXX) - (sumX ** 2)
    A = (sumXX * sumY - sumX * sumXY) / Delta
    B = (N * sumXY - sumX * sumY) / Delta
    # B = sum_DepIndep / sumIndepSqr # for forcing a fit through the origin

    sigY = np.std(y)
    sigA = sigY * np.sqrt(np.sum(x * x) / Delta)
    sigB = sigY * np.sqrt(N / Delta)

    return [A, sigA, B, sigB]

def r(x,y):
    meanX = np.mean(x)
    meanY = np.mean(y)
    sumXdiffSqr = sum((x-meanX) ** 2)
    sumYdifSqr = sum((y - meanY) ** 2)
    sumDifxy = sum((x - meanX) * (y - meanY))
    r = sumDifxy / np.sqrt(sumXdiffSqr * sumYdifSqr)
    return r

# calculate chi-squared
def chi_squared(x, y, a, b):
    sigY = np.std(y)
    chi2 = np.sum((y - (A + B * x) ** 2) / sigY ** 2)
    return chi2

# get the coefficients
coefficients = leastSqrs(x, y)
A = coefficients[0]
sigA = coefficients[1]
B = coefficients[2]
sigB = coefficients[3]

#print correlation coefficient
print("The correlation coefficient is: {0:5.2f}".format(r(x,y)))

# print out the straight line fine
print("The best straight line fit is y = ({0:4.2f} +/- {1:4.2f}) + ({2:4.2f} +/- {3:4.2f})x".format(A, sigA, B, sigB))

# print chiSquared per dof
print("The calculated chi_square/dof = {0:4.2f}".format(chi_squared(x,y,A,B) / (len(y) - 2)))
#plot data and the fit
plt.plot(x, y, "g")

#plot fit
xc = np.linspace(min(x), max(x), 50)
yc = A + B*xc

plt.plot(xc, yc, "b-")
plt.title("Sea Level Height Historical Record")
plt.xlabel("Year")
plt.ylabel("Height")
plt.show()

