from math import pi

from src.shapescalculatorpython.models.shape import Shape


class Circle(Shape):

    def __init__(self):
        self.radius = 0.0

    def area(self) -> float:
        return pi * self.radius * self.radius

    def perimeter(self) -> float:
        return 2 * pi * self.radius

    def calculate_area(self):
        while True:
            try:
                self._get_radius_of_circle()
                print(f"Area of circle: {self.area()}")
                break
            except (ValueError, TypeError):
                print("\nYOU ENTERED INVALID DATA\n")

    def calculate_perimeter(self):
        while True:
            try:
                self._get_radius_of_circle()
                print(f"Perimeter of circle: {self.perimeter()}")
                break
            except(ValueError, TypeError):
                print("\nYOU ENTERED INVALID DATA\n")

    def _get_radius_of_circle(self):
        print('Type in the radius of the Circle')
        arg = float(input())
        self.radius = arg
        print(f"Radius: {arg}")
