import numpy as np
from graphs_udemy import Graphs

class CircularQueue:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__begin = 0
        self.__final = -1
        self.number_elements = 0
        self.__values = np.empty(self.__capacity, dtype = object) 

    def __full_Queue(self):
        return self.number_elements == self.__capacity

    def __empty_Queue(self):
        return self.number_elements == 0

    def queue(self, value):
        if self.__full_Queue():
            print("Full queue!")
            return

        if self.__final == self.__capacity - 1:
            self.__final = - 1
        self.__final += 1
        self.__values[self.__final] = value
        self.number_elements += 1

    def unqueue(self):
        if self.__empty_Queue():
            print("Queue is already empty!")
            return

        element = self.__values[self.__begin]
        self.__begin += 1
        if self.__begin == self.__capacity:
            self.__begin = 0
        self.number_elements -= 1
        return element

    def first_queue(self):
        if self.__empty_Queue():
            return -1

        return self.__values[self.__begin]

    def view_queue(self):
        return self.__values

    def first_final_queue(self):
        return f"First element: {self.__values[self.__begin]}\nFinal element: {self.__values[self.__final]}"


if __name__ == "__main__":
     graphs = Graphs()
     queue = CircularQueue(5)
     queue.queue(graphs.arad)
     queue.queue(graphs.bucharest)
     queue.queue(graphs.fagaras)
     queue.queue(graphs.craiova)
     queue.queue(graphs.oradea)
     queue.queue(graphs.giurgiu)

     print("-----")

     cities = queue.view_queue()
     for i in cities:
        print(i.label)

     print("-----")
     print(queue.first_final_queue())