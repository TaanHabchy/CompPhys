import numpy as np

# question 2
def factorial(i): # returns (i)!
    rv = 1
    for i in range(1, i + 1):
        rv *= i
    return rv

def numerator(i):
    return factorial(4 * i) * (1103 + 26390 * i)

def denominator(i):
    return (factorial(i) ** 4) * (396 ** (4 * i))

def piMaker(n):
    rootConst = (2 * np.sqrt(2)) / 9801
    total = 0
    for i in range(0, n): # on test it asked 
       total += (numerator(i)/denominator(i))
    pie = 1 / (rootConst * total)
    print("The pi produced is {0:50.45f}. Numpy holds pi as: {1:50.45}".format(pie, np.pi))
    return pie
# piMaker(2)



# 3. Finding the Madelung Constant
def Madelung(L):
    constant = 0 
    for i in range(-L, L + 1):
        if i == 0:
            j += 1
        for j in range(-L, L + 1):
            if j == 0:
                j += 1
            for k in range(-L, L + 1): # triple for loop gets every possible point
                if k == 0: # prevents dividing by zero
                    k += 1
                test = i + j + k 
                frac = (1 / np.sqrt(i**2  + j**2 + k**2))
                if test % 2 == 0: # add if even
                    constant += frac
                else: # subtract if test is odd
                    constant -= frac
    print("When L equals {0:1.1f} the Madelung Constant equals {1:50.45f}".format(L, constant))
    return constant
#Madelung(100)



# 4a: Determining the mean and Standard Deviation for magnitudes and temps
import numpy as np
import matplotlib.pyplot as plt
fileName = "Data/stars.txt"
data = np.loadtxt("Data/stars.txt", float, skiprows = 0)
temp = data[:,0]
mag = data[:,1]

def meanSTD(): # finds and prints the magnitude and standard deviation of temperature and magnitude
    magMean = np.mean(mag) # creating the mean of the second column which describes the magnitude of the stars
    magSTD = np.std(mag) 
    tempMean = np.mean(temp) # first column is all temperature data
    tempSTD = np.std(temp)
    print("The magnitude mean is: {0:50.45f} and the standard deviation is: {1:50.45f}".format(magMean, magSTD))
    print("The temperature mean is: {0:50.45f} and the standard deviation is: {1:50.45f}".format(tempMean, tempSTD))

# 4b: Plot a histogram of (a) number of stars versus temperature and (b) number of
#     stars versus magnitude. Do the values peak around your answers in (a)?
def histogram():
    plt.hist(temp, bins=100, color="darkgreen")
    plt.xlabel("Temperature(Kelvin)")
    plt.ylabel("Number of Stars")
    plt.title("Number of Stars vs Temperature")
    plt.grid(True)
    plt.show()

    plt.hist(mag, bins=100, color="darkblue")
    plt.xlabel("Magnitude - Luminosity")
    plt.ylabel("Number of Stars")
    plt.title("Number of Stars vs Magnitude(Luminosity)")
    plt.grid(True)
    plt.show()
# histogram()
"""
Yes the values peak around my answers from part (a)
"""

# 4c: Construct a graph of magnitude versus temperature with the most negative
#     magnitudes higher on the vertical axis and temperatures going from hottest to
#     coolest along the horizontal axis. (You will need to look up how to reverse axes in
#     Matplotlib; it is very easy.)
def magVtemp(): # creates a scatter plot of temperature vs luminosity
    plt.scatter(data[:,0], data[:,1], marker="o", c="darkgreen", s=1)
    plt.ylabel("Luminosity in Magnitude")
    plt.xlabel("Temperature - Kelvin")
    plt.grid(True)
    plt.title("Temperature vs Luminosity")
    # reverse the x and y axis
    plt.gca().invert_xaxis() 
    plt.gca().invert_yaxis()
    plt.savefig("Data/starfig.png")
    plt.show()
# magVtemp()

# 4d: What information can you infer from your graph in (c)?
"""
According to graph produced in 4c, as temperature decreases, the luminosity of the stars will decrease.
Also the majority of stars have a temperature around 4000 - 7700 K, and a luminosity of 2.7 - 8.4
"""



# Question 5
pearsonData = np.loadtxt("Data/antarctica_mass_200204_202006.txt", float, skiprows=31) # skips all the notes
time = pearsonData[:,0]
mass = pearsonData[:,1]
uncertainMass = pearsonData[:,2]

# 5a. Find the Pearson correlation coefficient for the data
def findPearsonCoef():
    timeMean = np.mean(time) 
    massMean = np.mean(mass)

    # subtractions performed in coefficient formula
    timeDif = time[:] - timeMean
    massDif = mass[:] - massMean
    
    pearsonTop = sum((timeDif) * (massDif)) # numerator for pearson coefficient formula
    pearsonBottom = np.sqrt(sum(np.square(timeDif)) * sum(np.square(massDif))) # denominator

    pearsonCoef = pearsonTop / pearsonBottom
    print(pearsonCoef)
    return pearsonCoef

findPearsonCoef()
# 5b. Determine the linear regression for the data
num = len(time)
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
    Delta = (num * sumXX) - (sumX ** 2)
    A = (sumXX * sumY - sumX * sumXY) / Delta
    B = (num * sumXY - sumX * sumY) / Delta
    return [A, B]

coefficients = leastSqrs(time, mass)
A = coefficients[0]
B = coefficients[1] 
# print('The best straight line fit is y = {0:4.2f} + {1:4.2f}x' .format(A,B))

xc = np.linspace(min(time), max(time), 50)
yc = A + B*xc # formula for linear regression

# 5c. Plot the data and the model curve (linear regression)
def plotAntartica():
    plt.plot(xc, yc, "darkblue") # line of best fit
    plt.legend(('y = 287074.04 + -143.24x',), loc=1)
    plt.scatter(time, mass, marker="o", s=5, c="darkgreen") # scatter of time vs mass
    plt.grid(True)
    plt.xlabel("time of the year")
    plt.ylabel("mass(gigatons)")
    plt.title("Scatter Plot of Time vs Mass")
    plt.show()

#plotAntartica()
# 5d. What do you note about yearly and decadal changes in mass?
"""
The yearly decrease in mass after ~ 2006 is practically constant, and the 
decade from 2002 - 2012 experience a less steep decrease in mass as opposed to 
the decade from 2012 - 2022
"""