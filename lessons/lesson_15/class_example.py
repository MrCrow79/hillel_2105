import math
from abc import ABC, abstractmethod


class Figure(ABC):
    @abstractmethod
    def area_of_figure(self):
        pass

    @abstractmethod
    def perimeter_of_figure(self):
        pass


class Rectangle(Figure):

    def __init__(self, width, height):
        self.__private_width = width
        self.__private_height = height

    def area_of_figure(self):
        return self.__private_height * self.__private_width

    def perimeter_of_figure(self):
        return 2 * (self.__private_width + self.__private_height)


class Triangle(Figure):
    def __init__(self, a, b, c):
        self.__private_a = a
        self.__private_b = b
        self.__private_c = c

    def perimeter_of_figure(self):
        return self.__private_a + self.__private_b + self.__private_c

    def area_of_figure(self):
        s = (self.__private_a + self.__private_b + self.__private_c) / 2
        area = math.sqrt(s * (s - self.__private_a) * (s - self.__private_b) * (s - self.__private_c))
        return area


rectangle = Rectangle(10, 20)
triangle = Triangle(3, 4, 5)
results = [rectangle.perimeter_of_figure(), rectangle.area_of_figure(),
           triangle.perimeter_of_figure(), triangle.area_of_figure()]
for result in results:
    print(result)