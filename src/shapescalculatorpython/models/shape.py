from abc import ABC, abstractmethod
from enum import Enum


class Shape(ABC):

    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def perimeter(self) -> float:
        pass

    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass


class Shapes(Enum):
    Triangle = 'Triangle'
    Circle = 'Circle'
    Square = 'Square'
    Rectangle = 'Rectangle'
    Parallelogram = 'Parallelogram'
    Trapezium = 'Trapezium'


def measureShape(number: int, shape: Shape):
    if number == 1:
        shape.calculate_area()
    elif number == 2:
        shape.calculate_perimeter()
