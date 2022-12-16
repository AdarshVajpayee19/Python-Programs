# Base Class use karna hai .

from abc import ABC, abstractmethod


class shape(ABC):
    @abstractmethod
    def printarea(self):
        return 0


class Rectangle(shape):
    type = "Rectangle"
    sides = 4

    def __init__(self):
        self.length = 6
        self.breadth = 10

    # if printarea method is not defined in Rectangle class then it leads to error.
    def printarea(self):
        return self.length * self.breadth


rect1 = Rectangle()
print(rect1.printarea())

# We cannot Create an object of Abstract Class.