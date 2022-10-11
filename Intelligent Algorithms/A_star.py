from graphs_Astar import Graphs
from ordered_vector_Astar import OrderedVector

class Astar:
    def __init__(self, target):
        self.target = target
        self.found = False
    
    def search(self, actual):
        print(f'Actual: {actual.label}')
        actual.visited = True

        if actual == self.target:
            self.found = True

            print(f'Target found: {actual.label}')
        else:
            vector = OrderedVector(len(actual.adjacents))
            for adj in actual.adjacents:
                if adj.vertex.visited == False:
                    adj.vertex.visited = True
                    vector.insert(adj)
            vector.printer()
            print("--------------------")
            print(f'City chosen: {vector.values[0].vertex.label}')
            print("--------------------")

            if vector.values[0] != None:
                self.search(vector.values[0].vertex)

if __name__ == '__main__':

    A_star = Astar(Graphs().bucharest)
    A_star.search(Graphs().arad)