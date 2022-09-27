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
    arad = Vertex("Arad")
    timisoara = Vertex("Timisoara")
    lugoj = Vertex("Lugoj")
    mehadia = Vertex("Mehadia")
    dobreta = Vertex("Dobreta")
    craiova = Vertex("Craiova")
    rimnicu_vilcea = Vertex("Rimnicu Vilcea")
    fagaras = Vertex("Fagaras")
    pitesti = Vertex("Pitesti")
    bucharest = Vertex("Bucharest")
    giurgiu = Vertex("Giurgiu")

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
    sibiu.add_adjacents(Adjacent(rimnicu_vilcea, 80))

    rimnicu_vilcea.add_adjacents(Adjacent(sibiu, 80))
    rimnicu_vilcea.add_adjacents(Adjacent(craiova, 146))
    rimnicu_vilcea.add_adjacents(Adjacent(pitesti, 97))

    craiova.add_adjacents(Adjacent(rimnicu_vilcea, 146))
    craiova.add_adjacents(Adjacent(dobreta, 120))
    craiova.add_adjacents(Adjacent(pitesti, 138))

    pitesti.add_adjacents(Adjacent(craiova, 138))
    pitesti.add_adjacents(Adjacent(rimnicu_vilcea, 97))
    pitesti.add_adjacents(Adjacent(bucharest, 101))

    fagaras.add_adjacents(Adjacent(sibiu, 99))
    fagaras.add_adjacents(Adjacent(bucharest, 211))

    bucharest.add_adjacents(Adjacent(fagaras, 211))
    bucharest.add_adjacents(Adjacent(pitesti, 101))
    bucharest.add_adjacents(Adjacent(giurgiu, 90))

    giurgiu.add_adjacents(Adjacent(bucharest, 90))

if __name__ == "__main__":
    graphs = Graphs()

    graphs.oradea.display_adjacents()

    print("-----")
    graphs.arad.display_adjacents()

    