from gmplot import *
from number2 import ADistance
import webbrowser
import os

# coordinate for KL -- 3.1516636, 101.6943028

d = ADistance()
locations = ['Jakarta', 'Dhaka', 'Manila', 'Bandar Seri Begawan', 'Shanghai', 'Kuala Lumpur', 'Tokyo']

for i in range(len(locations)):
    city = locations[i]
    lat, lon = d.get_coord(city)

    # place Map
    # First 2 arguments are the geographical coordinates and the zoom resolution
    gmap = gmplot.GoogleMapPlotter(lat, lon, 15)

    gmap.apikey = "AIzaSyDeRNMnZ__VnQDiATiuz4kPjF_c9r1kWe8"
    # Location of where you want to save the map
    gmap.draw("maps/" + city + ".html")

# get latitude and longitude points of different cities
coord = []
for j in range(len(locations)):
    coord.append(d.get_coord(locations[j]))
lats, lons = zip(*coord)

# declare center of the map
gmap2 = gmplot.GoogleMapPlotter(3.1516636, 101.6943028, 13)

# Scatter map
gmap2.scatter(lats, lons, '#FF0000', size=500, marker=False)

# Plot method Draw a line in between given coordinates
gmap2.plot(lats, lons, 'cornflowerblue', edge_width=2.0)
gmap2.apikey = "AIzaSyDeRNMnZ__VnQDiATiuz4kPjF_c9r1kWe8"
gmap2.draw("maps/scatter map.html")

url = r"maps\scatter map.html"
webbrowser.open(url, new=2)
