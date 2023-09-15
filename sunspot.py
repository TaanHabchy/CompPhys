import numpy as np
import matplotlib.pyplot as plt

#load our data
data = np.loadtxt("sunspots.txt", float, skiprows = 0)
print(data)

#determine the number of rows

monthNumber = data[0:1000,0] # taking all of the first column
sunspotNumber = data[0:1000,1] 

numRows = len(sunspotNumber) # number of rows of data

# calculate the running avg
r = 10 # sets the number of points for previous and pos
runAvg = np.zeros(numRows - 2 * r, float)
for k in range(len(runAvg)):  
    for m in range(-r, r + 1): # # this loop runs through all the points before and after the point k
        runAvg[k] = sunspotNumber[k + m + r] + runAvg[k]
    runAvg[k] = runAvg[k] / (2 * r + 1)

err = np.std(sunspotNumber)

# plotting values
plt.errorbar(monthNumber, sunspotNumber, yerr= err, barsabove= True, fmt = "g")
plt.plot(monthNumber, sunspotNumber, "darkgreen", )
plt.plot(monthNumber[r : numRows - r], runAvg, "blue") 
plt.xlabel("Time (months)")
plt.ylabel("Sunspot (Number)")
plt.savefig("sunspots.png")
plt.show() # generates graph