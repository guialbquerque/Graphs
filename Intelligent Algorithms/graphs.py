"""
    This implementation is an adaptation of the classic graphs problem of the book AIMA, where we have the distances between 
    some cities to Bucharest.
"""

class Adjacent:
    def __init__(self, vertex):
        self.vertex = vertex
        

class Vertex:
    def __init__(self, label, distance):
        self.label = label
        self.visited = False
        self.distance = distance
        self.adjacents = []
        

    def add_adjacents(self, adjacent):
        return self.adjacents.append(adjacent)

    def display_adjacents(self):
        for i in self.adjacents:
            print(f'{i.vertex.label} -- {i.vertex.distance}')

class Graphs:
    arad = Vertex("Arad", 366)
    bucharest = Vertex("Bucharest", 0)
    craiova = Vertex("Craiova", 160)
    dobreta = Vertex("Dobreta", 242)
    eforie = Vertex("Eforie", 161)
    fagaras = Vertex("Fagaras", 178)
    giurgiu = Vertex("Giurgiu", 77)
    hirsova = Vertex("Hirsova", 151)
    iasi = Vertex("Iasi", 226)
    lugoj = Vertex("Lugoj", 244)
    mehadia = Vertex("Mehadia", 241)
    neamt = Vertex("Neamt",234)
    oradea = Vertex("Oradea", 380)
    pitesti = Vertex("Pitesti", 98)
    rimnicu = Vertex("Rimnicu", 193)
    sibiu = Vertex("Sibiu", 253)
    timisoara = Vertex("Timisoara", 329)
    urziceni = Vertex("Urziceni", 80)
    vaslui = Vertex("vaslui", 199)
    zerind = Vertex("zerind", 374)

    oradea.add_adjacents(Adjacent(zerind))
    oradea.add_adjacents(Adjacent(sibiu))

    zerind.add_adjacents(Adjacent(arad))
    zerind.add_adjacents(Adjacent(oradea))

    arad.add_adjacents(Adjacent(zerind))
    arad.add_adjacents(Adjacent(sibiu))
    arad.add_adjacents(Adjacent(timisoara))

    timisoara.add_adjacents(Adjacent(arad))
    timisoara.add_adjacents(Adjacent(lugoj))

    lugoj.add_adjacents(Adjacent(timisoara))
    lugoj.add_adjacents(Adjacent(mehadia))

    mehadia.add_adjacents(Adjacent(lugoj))
    mehadia.add_adjacents(Adjacent(dobreta))

    dobreta.add_adjacents(Adjacent(mehadia))
    dobreta.add_adjacents(Adjacent(craiova))

    sibiu.add_adjacents(Adjacent(arad))
    sibiu.add_adjacents(Adjacent(oradea))
    sibiu.add_adjacents(Adjacent(fagaras))
    sibiu.add_adjacents(Adjacent(rimnicu))

    rimnicu.add_adjacents(Adjacent(sibiu))
    rimnicu.add_adjacents(Adjacent(craiova))
    rimnicu.add_adjacents(Adjacent(pitesti))

    craiova.add_adjacents(Adjacent(rimnicu))
    craiova.add_adjacents(Adjacent(dobreta))
    craiova.add_adjacents(Adjacent(pitesti))

    pitesti.add_adjacents(Adjacent(craiova))
    pitesti.add_adjacents(Adjacent(rimnicu))
    pitesti.add_adjacents(Adjacent(bucharest))

    fagaras.add_adjacents(Adjacent(sibiu))
    fagaras.add_adjacents(Adjacent(bucharest))

    bucharest.add_adjacents(Adjacent(fagaras))
    bucharest.add_adjacents(Adjacent(pitesti))
    bucharest.add_adjacents(Adjacent(giurgiu))

    giurgiu.add_adjacents(Adjacent(bucharest))

if __name__ == "__main__":

    graph = Graphs()
    graph.arad.display_adjacents()
