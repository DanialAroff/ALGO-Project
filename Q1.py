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
gmap2 = gmplot.GoogleMapPlotter(3.1516636, 101.6943028, 6)

# Scatter map
gmap2.scatter(lats, lons, '#FF0000', size=50000, marker=False)

# Plot method Draw a line in between given coordinates
# Jakarta(-6.1753942, 106.827183)
# Dhaka(23.7593572, 90.3788136)
# Manila(14.5906216, 120.9799696)
# Bandar Seri Begawan(4.8895453, 114.9417574)
# Shanghai(31.2252985, 121.4890497)
# Kuala Lumpur(3.1516636, 101.6943028)
# Tokyo(35.6828387, 139.7594549)
gmap2.plot([3.1516636, 23.7593572, 35.6828387, 14.5906216, 4.8895453, -6.1753942, 3.1516636],
           [101.6943028, 90.3788136, 139.7594549, 120.9799696, 114.9417574, 106.827183, 101.6943028],
           'cornflowerblue', edge_width=2.0)
gmap2.plot([23.7593572, 31.2252985, 35.6828387], [90.3788136, 121.4890497, 139.7594549],
           'cornflowerblue', edge_width=2.0)
gmap2.plot([31.2252985, 14.5906216], [121.4890497, 120.9799696], 'cornflowerblue', edge_width=2.0)
gmap2.plot([23.7593572, 4.8895453], [90.3788136, 114.9417574], 'cornflowerblue', edge_width=2.0)

gmap2.apikey = "AIzaSyDeRNMnZ__VnQDiATiuz4kPjF_c9r1kWe8"
gmap2.draw("maps/graph.html")

url = r"maps\graph.html"
webbrowser.open(url, new=2)
