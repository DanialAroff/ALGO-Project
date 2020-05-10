from number2 import ADistance
import pandas as pd
from scipy.spatial import distance_matrix

d = ADistance()
locations = ['Kuala Lumpur', 'Dhaka', 'Jakarta', 'Bandar Seri Begawan', 'Manila', 'Shanghai', 'Tokyo']

# get latitude and longitude points of different cities
coord = []
for j in range(len(locations)):
    coord.append(d.get_coord_in_list(locations[j]))


def distance_between(city1):
    print("Calculating distance between " + city1 + " and other cities.....")
    db = []
    for city2 in locations:
        db.append(d.distance(city1, city2))
    return db


# kl_route = distance_between("Kuala Lumpur")
# dhaka_route = distance_between("Dhaka")
# jakarta_route = distance_between("Jakarta")
# bsb_route = distance_between("Bandar Seri Begawan")
# manila_route = distance_between("Manila")
# shanghai_route = distance_between("Shanghai")
# tokyo_route = distance_between("Tokyo")
#
# distance_between_all = [kl_route, dhaka_route, jakarta_route, bsb_route, manila_route, shanghai_route, tokyo_route]

file = open('maps/distance between all cities.txt', 'r')
distance_between_all = file.read()

print(distance_between_all)
# print()
# df = pd.DataFrame(coord, columns=['x-cord', 'y-cord'], index=locations)
# print(df)
#
# print()
# pd.set_option('display.max_columns', 20)
# distance_mat = pd.DataFrame(distance_between_all, index=df.index, columns=df.index)
# print(distance_mat)

# f = open('maps/distance between all cities.txt', 'w')
# f.write(str(distance_between_all))
