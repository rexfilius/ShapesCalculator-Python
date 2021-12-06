from src.shapescalculatorpython.models.shape import Shape


class Square(Shape):

    def __init__(self):
        self.side_length = 0.0

    def area(self) -> float:
        return self.side_length * self.side_length

    def perimeter(self) -> float:
        return 4 * self.side_length

    def calculate_area(self):
        while True:
            try:
                self._get_side_length()
                print(f"Area of Square: {self.area()}")
                break
            except (ValueError, TypeError):
                print("\nYOU ENTERED INVALID DATA\n")

    def calculate_perimeter(self):
        while True:
            try:
                self._get_side_length()
                print(f"Perimeter of Square: {self.perimeter()}")
                break
            except (ValueError, TypeError):
                print("\nYOU ENTERED INVALID DATA\n")

    def _get_side_length(self):
        print("Type in the SideLength of the Square")
        arg = float(input())
        self.side_length = arg
        print(f"SideLength: {arg}")
