from collections import deque, namedtuple

# we'll use infinity as a default distance to nodes.
inf = float('inf')
Edge = namedtuple('Edge', 'start, end, cost')


def make_edge(start, end, cost=1):
    return Edge(start, end, cost)


class Graph:
    def __init__(self, edges):
        # let's check that the data is right
        wrong_edges = [i for i in edges if len(i) not in [2, 3]]
        if wrong_edges:
            raise ValueError('Wrong edges data: {}'.format(wrong_edges))

        self.edges = [make_edge(*edge) for edge in edges]

    @property
    def vertices(self):
        return set(
            sum(
                ([edge.start, edge.end] for edge in self.edges), []
            )
        )

    def get_node_pairs(self, n1, n2, both_ends=True):
        if both_ends:
            node_pairs = [[n1, n2], [n2, n1]]
        else:
            node_pairs = [[n1, n2]]
        return node_pairs

    def remove_edge(self, n1, n2, both_ends=True):
        node_pairs = self.get_node_pairs(n1, n2, both_ends)
        edges = self.edges[:]
        for edge in edges:
            if [edge.start, edge.end] in node_pairs:
                self.edges.remove(edge)

    def add_edge(self, n1, n2, cost=1, both_ends=True):
        node_pairs = self.get_node_pairs(n1, n2, both_ends)
        for edge in self.edges:
            if [edge.start, edge.end] in node_pairs:
                return ValueError('Edge {} {} already exists'.format(n1, n2))

        self.edges.append(Edge(start=n1, end=n2, cost=cost))
        if both_ends:
            self.edges.append(Edge(start=n2, end=n1, cost=cost))

    @property
    def neighbours(self):
        neighbours = {vertex: set() for vertex in self.vertices}
        for edge in self.edges:
            neighbours[edge.start].add((edge.end, edge.cost))

        return neighbours

    def dijkstra(self, source, dest):
        assert source in self.vertices, 'Such source node doesn\'t exist'
        distances = {vertex: inf for vertex in self.vertices}
        previous_vertices = {
            vertex: None for vertex in self.vertices
        }
        distances[source] = 0
        vertices = self.vertices.copy()

        while vertices:
            current_vertex = min(
                vertices, key=lambda vertex: distances[vertex])
            vertices.remove(current_vertex)
            if distances[current_vertex] == inf:
                break
            for neighbour, cost in self.neighbours[current_vertex]:
                alternative_route = distances[current_vertex] + cost
                if alternative_route < distances[neighbour]:
                    distances[neighbour] = alternative_route
                    previous_vertices[neighbour] = current_vertex

        path, current_vertex = deque(), dest
        while previous_vertices[current_vertex] is not None:
            path.appendleft(current_vertex)
            current_vertex = previous_vertices[current_vertex]
        if path:
            path.appendleft(current_vertex)
        return path


graph = Graph([
    ("Kuala Lumpur", "Dhaka", 2584.787), ("Kuala Lumpur", "Jakarta", 1178.665),
    ("Kuala Lumpur", "Bandar Seri Begawan", 1483.521), ("Jakarta", "Bandar Seri Begawan", 1519.996),
    ("Dhaka", "Bandar Seri Begawan", 3361.34), ("Dhaka", "Shanghai", 3171.866), ("Dhaka", "Tokyo", 4903.439),
    ("Bandar Seri Begawan", "Manila", 1260.663), ("Manila", "Shanghai", 1842.992), ("Manila", "Tokyo", 2995.407),
    ("Shanghai", "Tokyo", 1766.048)])


# driver program
# mapp=list(graph.dijkstra("Kuala Lumpur", "Tokyo"))
#
# for i in mapp:
#     if i is mapp[-1]:
#         print(i)
#     else:
#         print(i,"--> ",end="")
#
# # declare center of the map
# gmap = gmplot.GoogleMapPlotter(3.1516636, 101.6943028, 6)
# # Scatter map
# gmap.scatter(lats, lons, '#FF0000', size=50000, marker=False)
#
# for i in range(len(mapp)-1):
#    gmap.plot([d.get_lat(mapp[i]), d.get_lat(mapp[i+1])], [d.get_lon(mapp[i]), d.get_lon(mapp[i+1])],
#              'cornflowerblue', edge_width=2.0)
#
# gmap.apikey = "AIzaSyDeRNMnZ__VnQDiATiuz4kPjF_c9r1kWe8"
# gmap.draw("maps/graph_after.html")
#
# url = r"maps\graph_after.html"
# webbrowser.open(url, new=2)