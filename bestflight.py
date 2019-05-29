from gmplot import *
from number2 import ADistance
from Graph import Graph
from geopy.geocoders import Nominatim
import webbrowser
import time
import os

start = time.time()

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
gmap2.plot([3.1516636, 23.7593572, 35.6828387, 14.5906216, 4.8895453, -6.1753942, 3.1516636, 4.8895453],
           [101.6943028, 90.3788136, 139.7594549, 120.9799696, 114.9417574, 106.827183, 101.6943028, 114.9417574],
           'cornflowerblue', edge_width=2.0)
gmap2.plot([23.7593572, 31.2252985, 35.6828387], [90.3788136, 121.4890497, 139.7594549],
           'cornflowerblue', edge_width=2.0)
gmap2.plot([31.2252985, 14.5906216], [121.4890497, 120.9799696], 'cornflowerblue', edge_width=2.0)
gmap2.plot([23.7593572, 4.8895453], [90.3788136, 114.9417574], 'cornflowerblue', edge_width=2.0)

gmap2.apikey = "AIzaSyDeRNMnZ__VnQDiATiuz4kPjF_c9r1kWe8"

# draw map into html
gmap2.draw("maps/graph.html")

geolocator = Nominatim(user_agent='WIA2005_Assignment')
d = ADistance()
locations = ['Jakarta', 'Dhaka', 'Manila', 'Bandar Seri Begawan', 'Shanghai', 'Kuala Lumpur', 'Tokyo']
edges = []

for current in range(len(locations)):
    for other in range(len(locations)):
        if current is not other:
            print(locations[current], '<->', locations[other])
            distance = d.distance(locations[current], locations[other])
            print('Distance: ' + str(distance) + 'km')
            # edges.append(edge(locations[current], locations[other], distance))
    print('\n')

graph = Graph([
    ("Kuala Lumpur", "Dhaka", 2584.787), ("Kuala Lumpur", "Jakarta", 1178.665),
    ("Kuala Lumpur", "Bandar Seri Begawan", 1483.521), ("Jakarta", "Bandar Seri Begawan", 1519.996),
    ("Dhaka", "Bandar Seri Begawan", 3361.34), ("Dhaka", "Shanghai", 3171.866), ("Dhaka", "Tokyo", 4903.439),
    ("Bandar Seri Begawan", "Manila", 1260.663), ("Manila", "Shanghai", 1842.992), ("Manila", "Tokyo", 2995.407),
    ("Shanghai", "Tokyo", 1766.048)])


shortest_route = list(graph.dijkstra("Kuala Lumpur", "Tokyo"))

print("Shortest route from Kuala Lumpur to Tokyo")
for i in shortest_route:
    if i is shortest_route[-1]:
        print(i)
    else:
        print(i, "--> ", end="")

# declare center of the map
gmap = gmplot.GoogleMapPlotter(3.1516636, 101.6943028, 6)
# Scatter map

for i in range(len(shortest_route) - 1):
    gmap.plot([d.get_lat(shortest_route[i]), d.get_lat(shortest_route[i + 1])], [d.get_lon(shortest_route[i]), d.get_lon(shortest_route[i + 1])],
              'cornflowerblue', edge_width=2.0)

gmap.apikey = "AIzaSyDeRNMnZ__VnQDiATiuz4kPjF_c9r1kWe8"
gmap.draw("maps/graph_after.html")

graph_before = r"maps\graph_before.html"
webbrowser.open(graph_before, new=2)

graph_after = r"maps\graph_after.html"
webbrowser.open(graph_after, new=2)

end = time.time() - start
print("Total running time:", end, "s")
