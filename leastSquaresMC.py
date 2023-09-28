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

# calculate MC
nTrials = 1000 # number of trials
FitParms = np.array([])
aValues = np.zeros(nTrials)
unc_A_Values = np.zeros(nTrials)
bValues = np.zeros(nTrials)
unc_B_Values = np.zeros(nTrials)

y_unc = [] 
y_unc = np.std(y) * y/N
xMin = x[0]
xMax = x[-1]

#create random data sets
for j in range(nTrials):
    xTrial = np.random.uniform(xMin, xMax, size=N) # uniform spreads em out so they not all clustered
    yTrial = A + B * xTrial + np.random.normal(loc=0, scale = np.std(y_unc), size = N) # linear fit with randominization
    aValues[j], unc_A_Values[j], bValues[j], unc_B_Values[j] = leastSqrs(xTrial, yTrial)

# plt.hist(aValues, bins=50, color="darkgreen")
# plt.title("Seal Level Height Historical Record")
# plt.show()

A = np.mean(aValues)
B = np.mean(bValues)
uncA = np.mean(unc_A_Values)
uncB = np.mean(unc_B_Values)

# print out the straight line fine
print("The best straight line fit is y = ({0:4.2f} +/- {1:4.2f}) + ({2:4.2f} +/- {3:4.2f})x".format(A, sigA, B, sigB))

# print chiSquared per dof
print(x)
print(B)
print("The calculated chi_square/dof = {0:4.2f}".format(chi_squared(x,y,A,B) / (len(y) - 2)))
#plot data and the fit
#plt.plot(x, y, "g")

#plot fit
xc = np.linspace(min(x), max(x), 186)
yc = A + B*xc

fig, ax = plt.subplots()
ax.fill_between(xc, yc-y_unc, yc+y_unc, alpha=0.2) 
ax.scatter(x, y, color="blue", s=2)

# plt.show()
# plt.plot(xc, yc, "b-")
# plt.title("Sea Level Height Historical Record")
# plt.xlabel("Year")
# plt.ylabel("Height")
# plt.show()