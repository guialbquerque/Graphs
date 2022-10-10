from graphs_udemy import Graphs
from stack_udemy import Stack

class DepthSearch:
    def __init__(self, start, number_of_elements):
        self.start = start
        self.start.visited = True
        self.stack = Stack(number_of_elements)
        self.stack.Stack_Up(start)
    
    def search(self):
        top = self.stack.view_top()
        
        for adj in top.adjacents:
            print(f'Top is: {top.label}. Is {adj.vertex.label} already visited? {adj.vertex.visited}')
            print()
            if adj.vertex.visited == False:
                adj.vertex.visited = True
                self.stack.Stack_Up(adj.vertex)
                print(f'Stacked : {adj.vertex.label}')
                self.search()
        print(f'Unstacked: {self.stack.Unstack().label}')
        print()

graphs = Graphs()
deph_search = DepthSearch(graphs.arad, 20)
deph_search.search()
