import screen
from src.shapescalculatorpython.models.circle import Circle
from src.shapescalculatorpython.models.square import Square
from src.shapescalculatorpython.models.parallelogram import Parallelogram
from src.shapescalculatorpython.models.triangle import Triangle
from src.shapescalculatorpython.models.trapezium import Trapezium
from src.shapescalculatorpython.models.rectangle import Rectangle


def run_calculator():
    calculation: int
    shape_selection = screen.first_menu()

    if shape_selection == 1:
        calculation = screen.second_menu()
        if calculation == 1:
            Triangle().calculate_area()
        else:
            Triangle().calculate_perimeter()

    elif shape_selection == 2:
        calculation = screen.second_menu()
        if calculation == 1:
            Circle().calculate_area()
        else:
            Circle().calculate_perimeter()

    elif shape_selection == 3:
        calculation = screen.second_menu()
        if calculation == 3:
            Square().calculate_area()
        else:
            Square().calculate_perimeter()

    elif shape_selection == 4:
        calculation = screen.second_menu()
        if calculation == 1:
            Rectangle().calculate_area()
        else:
            Rectangle().calculate_perimeter()

    elif shape_selection == 5:
        calculation = screen.second_menu()
        if calculation == 1:
            Parallelogram().calculate_area()
        else:
            Parallelogram().calculate_perimeter()

    elif shape_selection == 6:
        calculation = screen.second_menu()
        if calculation == 1:
            Trapezium().calculate_area()
        else:
            Trapezium().calculate_perimeter()

    screen.third_menu()
    # End of run_calculator function
