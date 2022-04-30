from src.shapescalculatorpython.models.shape import Shape


class Triangle(Shape):

    def __init__(self):
        self.base_length = 0.0
        self.height = 0.0
        self.side_length_1 = 0.0
        self.side_length_2 = 0.0

    def area(self) -> float:
        return 0.5 * (self.base_length * self.height)

    def perimeter(self) -> float:
        return self.side_length_1 + self.side_length_2 + self.base_length

    def calculate_area(self):
        while True:
            try:
                print("Type in the BaseLength of the Triangle")
                arg1 = float(input())
                self.base_length = arg1
                print(f"BaseLength: {arg1}")

                print("Type in the Height of the Triangle")
                arg2 = float(input())
                self.height = arg2
                print(f"Height: {arg2}")

                print(f"Area of Triangle: {self.area():.3f}")
                break
            except (ValueError, TypeError):
                print("\nYOU ENTERED INVALID DATA\n")

    def calculate_perimeter(self):
        while True:
            try:
                print("Type in the first SideLength of the Triangle")
                arg1 = float(input())
                self.side_length_1 = arg1
                print(f"SideLength-1: {arg1}")

                print("Type in the second SideLength of the Triangle")
                arg2 = float(input())
                self.side_length_2 = arg2
                print(f"SideLength-2: {arg2}")

                print("Type in the BaseLength of the Triangle")
                arg3 = float(input())
                self.base_length = arg3
                print(f"BaseLength: {arg3}")

                print(f"Perimeter of Triangle: {self.perimeter():.3f}")
                break
            except (ValueError, TypeError):
                print("\nYOU ENTERED INVALID DATA\n")