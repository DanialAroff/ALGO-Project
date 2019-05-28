from number2 import ADistance


d = ADistance()
locations = ['Jakarta', 'Dhaka', 'Manila', 'Bandar Seri Begawan', 'Shanghai', 'Kuala Lumpur', 'Tokyo']

for current in range(len(locations)):
    for other in range(len(locations)):
        if current is not other:
            print(locations[current], '<->', locations[other])
            print('Distance: ' + str(d.distance(locations[current], locations[other])) + 'km')
    print('\n')

graph = Graph([
    ("a", "b", 7),  ("a", "c", 9),  ("a", "f", 14), ("b", "c", 10),
    ("b", "d", 15), ("c", "d", 11), ("c", "f", 2),  ("d", "e", 6),
    ("e", "f", 9)])

print(graph.dijkstra("a", "e"))