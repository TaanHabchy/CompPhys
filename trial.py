# c. Plot the data and the model curve(linear regression)
def graphing():
    answer = linReg(days, amtO2)

    A = answer[0]
    B = answer[2]
    unc_A = answer[1]
    unc_B = answer[3]
    xc = np.linspace(days[0], days[-1], 100)
    y = A + B * xc

    plt.xlabel("days")
    plt.ylabel("O2 Amount(mm)")
    plt.scatter(days, amtO2, marker="o", c="darkgreen", s=2, label= "Days vs O2 Amount")
    plt.plot(xc, y, "brown", label = "Line of Best Fit")
    plt.show()

graphing()
