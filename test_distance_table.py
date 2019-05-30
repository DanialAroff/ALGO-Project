from number2 import ADistance
import pandas as pd
from scipy.spatial import distance_matrix

d = ADistance()
locations = ['Kuala Lumpur', 'Dhaka', 'Jakarta', 'Bandar Seri Begawan', 'Manila', 'Shanghai', 'Tokyo']

# get latitude and longitude points of different cities
coord = []
for j in range(len(locations)):
    coord.append(d.get_coord_in_list(locations[j]))
# lats, lons = zip(*coord)

print(coord)
df = pd.DataFrame(coord, columns=['xcord', 'ycord'], index=locations)
print(df)

# distance_mat = pd.DataFrame(distance_matrix(df.values, df.values), index=df.index, columns=df.index)
# print(distance_mat)
