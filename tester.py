import matplotlib.pyplot as plt
from scipy.special import gamma
import numpy as np

x = np.linspace(0,28,100)
sigma = [0.5, 1.0, 2.0, 5.0]

def f(x, sigma): 
    return 1/(2*sigma*sqrt(2*np.pi))*np.exp(-(x-0)**2/2*sigma)
fmax = np.zeros(2)

import plotly.express as px
import pandas as pd
import plotly.io as pio

data = pd.read_csv("Data/weekEarthquakes.csv")

# look up loadtxt vs gettxt
# drop rows with missing or invalid values in file
data = data.dropna(subset=["mag"])
data = data[data.mag >= 0]

# cerate scatter map
fig = px.scatter_geo(data, lat = "latitude", lon = "longitude", color = "mag", 
                      hover_name = "place", size= "mag")

pio.write_html(fig, file="earthquakes.html", auto_open=True)