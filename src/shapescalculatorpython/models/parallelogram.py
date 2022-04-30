from src.shapescalculatorpython.models.shape import Shape


class Parallelogram(Shape):

    def __init__(self):
        self.base_length = 0.0
        self.side_length = 0.0
        self.height = 0.0

    def area(self) -> float:
        return self.base_length * self.height

    def perimeter(self) -> float:
        return 2 * (self.base_length + self.side_length)

    def calculate_area(self):
        while True:
            try:
                print('Type in the BaseLength of the Parallelogram')
                arg1 = float(input())
                self.base_length = arg1
                print(f"BaseLength: {arg1}")

                print('Type in the Height of the Parallelogram')
                arg2 = float(input())
                self.height = arg2
                print(f"Height: {arg2}")

                print(f"Area of parallelogram: {self.area():.3f}")
                break
            except (ValueError, TypeError):
                print("\nYOU ENTERED INVALID DATA\n")

    def calculate_perimeter(self):
        while True:
            try:
                print("Type in the BaseLength of the Parallelogram")
                arg1 = float(input())
                self.base_length = arg1
                print(f"BaseLength: {arg1}")

                print("Type in the SideLength of the Parallelogram")
                arg2 = float(input())
                self.side_length = arg2
                print(f"SideLength: {arg2}")

                print(f"Perimeter of Parallelogram: {self.perimeter():.3f}")
                break
            except (ValueError, TypeError):
                print("\nYOU ENTERED INVALID DATA\n")
