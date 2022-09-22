import numpy as np


class Stack:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__top = -1
        self.__values = np.empty(self.__capacity, dtype = object)

    def __Stack_Full(self):
        if self.__top == self.__capacity - 1:
            return True
        else:
            return False

    def __Stack_empty(self):
        if self.__top == -1:
            return True
        else:
            return False

    def Stack_Up(self, value):
        if self.__Stack_Full():
            print("The stack is full!")
        else:
            self.__top += 1
            self.__values[self.__top] = value

    def Unstack(self):
        if self.__Stack_empty():
            print("The stack is empty!")
            return None
        else:
            temp = self.__values[self.__top]
            self.__top -= 1
            return temp
            
    def view_top(self):
        if self.__top == -1:
            return -1
        else:
            return self.__values[self.__top]