class Adjacent:
    def __init__(self, vertex, cust):
        self.vertex = vertex
        self.cust = cust

class Vertex:
    def __init__(self, label):
        self.label = label
        self.visited = False
        self.adjacents = []

    def add_adjacents(self, adjacent):
        return self.adjacents.append(adjacent)

    def display_adjacents(self):
        for i in self.adjacents:
            print(i.vertex.label, i.cust)


class Graphs:

    oradea = Vertex("Oradea")
    zerind = Vertex("Zerind")
    sibiu = Vertex("Sibiu")

    oradea.add_adjacents(Adjacent(zerind, 71))
    oradea.add_adjacents(Adjacent(sibiu, 151))


graphs = Graphs()

graphs.oradea.display_adjacents()