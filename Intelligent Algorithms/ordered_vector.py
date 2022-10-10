import numpy as np
from graphs import Graphs

class OrderedVector:

    def __init__(self, capacity):
        self._capacity = capacity
        self._lastPosition = -1
        self._values = np.empty(self._capacity, dtype = object)

    # O(N)
    def printer(self):
        if self._lastPosition == -1:
            print("Vector is empty!")
        else:
            for i in range(self._lastPosition + 1):
                print(f"Position: {i} - Element: {self._values[i]. label} - Distance: {self._values[i]. distance}")

    def insert(self, value):
        if self._lastPosition == len(self._values) - 1:
            print("The vector is full, max capacity reached!")
        else:
            position = 0
            for i in range(self._lastPosition + 1):
                position = i
                if self._values[i].distance > value.distance:
                    break
                elif i == self._lastPosition:
                    position += 1

            x = self._lastPosition
            while x >= position:
                self._values[x + 1] = self._values[x]
                x -= 1

            self._values[position] = value
            self._lastPosition += 1

if __name__ == "__main__":
    graphs = Graphs()

    vector = OrderedVector(5)
    vector.insert(graphs.arad)
    vector.insert(graphs.oradea)
    vector.insert(graphs.sibiu)
    vector.insert(graphs.timisoara)
    vector.insert(graphs.pitesti)
    vector.printer()   