from graphs_udemy import Graphs
from circular_queue import CircularQueue

class BreadthSearch:
    def __init__(self, start, n_elements):
        self.start = start
        self.start.visited = True
        self.queue = CircularQueue(n_elements)
        self.queue.queue(start)

    def search(self):
        actual = self.queue.first_queue()
        print(f"First element of the queue is: {actual.label}\n")
        
        element = self.queue.unqueue()
        for adj in actual.adjacents:
            
            print(f"Is {adj.vertex.label} already visited? {adj.vertex.visited}")
            if adj.vertex.visited == False:
                adj.vertex.visited = True
                self.queue.queue(adj.vertex)
                print(f"Lined up: {adj.vertex.label}")
        
        print(f"Took out of the queue: {element.label}")
        
        if self.queue.number_elements > 0:

            self.search()
        

if __name__ == '__main__':
    graphs = Graphs()
    breadth_search = BreadthSearch(graphs.arad, 20)
    
    breadth_search.search()