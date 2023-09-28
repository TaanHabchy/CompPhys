# use a 1D array of data, e.g. from a fild that was read

import numpy as np

#create an array of data

x = np.array([20.5, -10.2, 8.8, -2.2, 5.4, 5.8, -6.3, 1.7, 7.6, -3.3])
y = np.array([41.5, -8.8, 15.2, 11.0, 2.5, 14.2, -10.1, -3.3, 18.7, -7.1])

#find the number of data points
numX = len(x)
numY = len(y)

mean = 0


# Standard Deviation
meanX = np.mean(x)
meanY = np.mean(y)


# literally just std
def sigma(z):
    sigy = 0
    for i in z:
        sigy += (np.mean(z) - i)**2
    sigy = sigy / len(z)
    sigy = np.sqrt(sigy)
    # print(sigy)
    return(sigy)

answer = 0
i = 1
answer = np.inner(x, y)

answer = answer / (numX * np.std(x) * np.std(y))

print(answer)




# for i in x:
#     mean = mean + i

# mean /= numData

# mean_lib = np.mean(x)

# print(mean, "\n",mean_lib)

# #calculate standard deviation
# sumX = 0
# for i in x:
#     sumX = sumX + (i - mean)**2

# sumX /= numData
# sumX = np.sqrt(sumX)

# print(sumX, "\n", np.std(x))

