import numpy as np
from graphs_Astar import Graphs
"""
Legends:
Line straight distance - lsd
real cust - rc
A star distance - asd

"""
class OrderedVector:

    def __init__(self, capacity):
        self._capacity = capacity
        self._lastPosition = -1
        self.values = np.empty(self._capacity, dtype = object)

    
    def printer(self):
        if self._lastPosition == -1:
            print("Vector is empty!")
        else:
            for i in range(self._lastPosition + 1):
                print(f"City: {self.values[i].vertex.label} - lsd -> {self.values[i].vertex.distance} - rc -> {self.values[i].cust} - asd - {self.values[i].Astar_distance}")

    def insert(self, value):
        if self._lastPosition == len(self.values) - 1:
            print("The vector is full, max capacity reached!")
        else:
            position = 0
            for i in range(self._lastPosition + 1):
                position = i
                if self.values[i].Astar_distance > value.Astar_distance:
                    break
                elif i == self._lastPosition:
                    position += 1

            x = self._lastPosition
            while x >= position:
                self.values[x + 1] = self.values[x]
                x -= 1

            self.values[position] = value
            self._lastPosition += 1

if __name__ == "__main__":

    vector = OrderedVector(3)
    vector.insert(Graphs().arad.adjacents[0])
    vector.insert(Graphs().arad.adjacents[1])
    vector.insert(Graphs().arad.adjacents[2])
    vector.printer()