from src.shapescalculatorpython.models.shape import Shape


class Trapezium(Shape):

    def __init__(self):
        self.top_length = 0.0
        self.base_length = 0.0
        self.height = 0.0
        self.side_length_1 = 0.0
        self.side_length_2 = 0.0

    def area(self) -> float:
        return (0.5 * (self.top_length + self.base_length)) * self.height

    def perimeter(self) -> float:
        return self.top_length + self.base_length \
               + self.side_length_1 + self.side_length_2

    def calculate_area(self):
        while True:
            try:
                print("Type in the TopLength of the Trapezium")
                arg1 = float(input())
                self.top_length = arg1
                print(f"TopLength: {arg1}")

                print("Type in the BaseLength of the Trapezium")
                arg2 = float(input())
                self.base_length = arg2
                print(f"BaseLength: {arg2}")

                print("Type in the Height of the Trapezium")
                arg3 = float(input())
                self.height = arg3
                print(f"Height: {arg3}")

                print(f"Area of Trapezium: {self.area()}")
                break
            except (ValueError, TypeError):
                print("\nYOU ENTERED INVALID DATA\n")

    def calculate_perimeter(self):
        while True:
            try:
                print("Type in the TopLength of the Trapezium")
                arg1 = float(input())
                self.top_length = arg1
                print(f"TopLength: {arg1}")

                print("Type in the BaseLength of the Trapezium")
                arg2 = float(input())
                self.base_length = arg2
                print(f"BaseLength: {arg2}")

                print("Type in the first SideLength of the Trapezium")
                arg3 = float(input())
                self.side_length_1 = arg3
                print(f"SideLength-1: {arg3}")

                print("Type in the second SideLength of the Trapezium")
                arg4 = float(input())
                self.side_length_2 = arg3
                print(f"SideLength-2: {arg4}")

                print(f"Perimeter of Trapezium: {self.perimeter()}")
                break
            except (ValueError, TypeError):
                print("\nYOU ENTERED INVALID DATA\n")
