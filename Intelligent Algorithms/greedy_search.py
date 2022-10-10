from graphs import Graphs
from ordered_vector import OrderedVector

class GreedySearch:
    def __init__(self, target):
        self.target = target
        self.found = False
    
    def search(self, actual):

        if actual ==  self.target:
            self.found = True

            print(f'Target found: {actual.label}')
        else:
            vector = OrderedVector(len(actual.adjacents))
            for adj in actual.adjacents:
                if adj.vertex.visited == False:
                    adj.vertex.visited = True
                    vector.insert(adj.vertex)
            vector.printer()
            print("--------------------")
            print(f'City chosen: {vector.values[0].label  }')
            print("--------------------")

            if vector.values[0] != None:
                self.search(vector.values[0])


greedy = GreedySearch(Graphs().bucharest)
greedy.search(Graphs().arad)