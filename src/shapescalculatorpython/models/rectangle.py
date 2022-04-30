from src.shapescalculatorpython.models.shape import Shape


class Rectangle(Shape):

    def __init__(self):
        self.length = 0.0
        self.breadth = 0.0

    def area(self) -> float:
        return self.length * self.breadth

    def perimeter(self) -> float:
        return 2 * (self.length * self.breadth)

    def calculate_area(self):
        while True:
            try:
                self._get_length_and_breadth()
                print(f"Area of Rectangle: {self.area():.3f}")
                break
            except (ValueError, TypeError):
                print("\nYOU ENTERED INVALID DATA\n")

    def calculate_perimeter(self):
        while True:
            try:
                self._get_length_and_breadth()
                print(f"Perimeter of Rectangle: {self.perimeter():.3f}")
                break
            except (ValueError, TypeError):
                print("\nYOU ENTERED INVALID DATA\n")

    def _get_length_and_breadth(self):
        print("Type in the Length of the Rectangle")
        arg1 = float(input())
        self.length = arg1
        print(f"Length: {arg1}")

        print("Type in the Breadth of the Rectangle")
        arg2 = float(input())
        self.breadth = arg2
        print(f"Breadth: {arg2}")
