import plotly.express as px
import pandas as pd
import plotly.io as pio

data = pd.read_csv("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.csv")

# look up loadtxt vs gettxt
# drop rows with missing or invalid values in file
data = data.dropna(subset=["mag"])
data = data[data.mag >= 0]

# cerate scatter map
fig = px.scatter_geo(data, lat = "latitude", lon = "longitude", color = "mag", 
                      hover_name = "place", size= "mag")

pio.write_html(fig, file="earthquakes.html", auto_open=True)