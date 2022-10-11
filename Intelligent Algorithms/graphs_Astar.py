"""
    This implementation is an adaptation of the classic graphs problem of the book AIMA, where we have the distances between 
    some cities to Bucharest, here we have the distante in line straight to the objective and the real cust each vertex, the A-Star
    algorithm will be implemented.
"""

class Adjacent:
    def __init__(self, vertex, cust):
        self.vertex = vertex
        self.cust = cust
        self.Astar_distance = self.cust + self.vertex.distance
        

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

    oradea.add_adjacents(Adjacent(zerind, 71))
    oradea.add_adjacents(Adjacent(sibiu, 151))

    zerind.add_adjacents(Adjacent(arad, 75))
    zerind.add_adjacents(Adjacent(oradea, 71))

    arad.add_adjacents(Adjacent(zerind, 75))
    arad.add_adjacents(Adjacent(sibiu, 140))
    arad.add_adjacents(Adjacent(timisoara, 118))

    timisoara.add_adjacents(Adjacent(arad, 118))
    timisoara.add_adjacents(Adjacent(lugoj, 111))

    lugoj.add_adjacents(Adjacent(timisoara, 111))
    lugoj.add_adjacents(Adjacent(mehadia, 70))

    mehadia.add_adjacents(Adjacent(lugoj, 70))
    mehadia.add_adjacents(Adjacent(dobreta, 75))

    dobreta.add_adjacents(Adjacent(mehadia, 75))
    dobreta.add_adjacents(Adjacent(craiova, 120))

    sibiu.add_adjacents(Adjacent(arad, 140))
    sibiu.add_adjacents(Adjacent(oradea, 151))
    sibiu.add_adjacents(Adjacent(fagaras, 99))
    sibiu.add_adjacents(Adjacent(rimnicu, 80))

    rimnicu.add_adjacents(Adjacent(sibiu, 80))
    rimnicu.add_adjacents(Adjacent(craiova, 146))
    rimnicu.add_adjacents(Adjacent(pitesti, 97))

    craiova.add_adjacents(Adjacent(rimnicu, 146))
    craiova.add_adjacents(Adjacent(dobreta, 120))
    craiova.add_adjacents(Adjacent(pitesti, 138))

    pitesti.add_adjacents(Adjacent(craiova, 138))
    pitesti.add_adjacents(Adjacent(rimnicu, 97))
    pitesti.add_adjacents(Adjacent(bucharest, 101))

    fagaras.add_adjacents(Adjacent(sibiu, 99))
    fagaras.add_adjacents(Adjacent(bucharest, 211))

    bucharest.add_adjacents(Adjacent(fagaras, 211))
    bucharest.add_adjacents(Adjacent(pitesti, 101))
    bucharest.add_adjacents(Adjacent(giurgiu, 90))

    giurgiu.add_adjacents(Adjacent(bucharest, 90))

if __name__ == "__main__":

    graph = Graphs()
    graph.arad.display_adjacents()
