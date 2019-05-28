import time
from geopy.geocoders import Nominatim
from number2 import ADistance


def edge(a, b, cost):
    return a, b, cost


# print(time.strftime('%Y/%m/%d %I:%M:%S  %A\n'))
start = time.time()
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

# f = open('edges.txt', 'w')
# f.write(str(edges))
# f.close()
# print(edges)
end = time.time()
total_time = end - start
print('\nTotal running time in seconds: ' + str(total_time))
