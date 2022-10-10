import numpy as np
from graphs import Graphs

class OrderedVector:

    def __init__(self, capacity):
        self._capacity = capacity
        self._lastPosition = -1
        self.values = np.empty(self._capacity, dtype = object)

    # O(N)
    def printer(self):
        if self._lastPosition == -1:
            print("Vector is empty!")
        else:
            for i in range(self._lastPosition + 1):
                print(f"Position: {i} - Element: {self.values[i].label} - Distance: {self.values[i].distance}")

    def insert(self, value):
        if self._lastPosition == len(self.values) - 1:
            print("The vector is full, max capacity reached!")
        else:
            position = 0
            for i in range(self._lastPosition + 1):
                position = i
                if self.values[i].distance > value.distance:
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
    graphs = Graphs()

    vector = OrderedVector(5)
    vector.insert(Graphs().arad)
    vector.insert(graphs.oradea)
    vector.insert(graphs.sibiu)
    vector.insert(graphs.timisoara)
    vector.insert(graphs.pitesti)
    vector.printer()   
