import screen
from src.shapescalculatorpython.models.circle import Circle
from src.shapescalculatorpython.models.square import Square
from src.shapescalculatorpython.models.parallelogram import Parallelogram
from src.shapescalculatorpython.models.triangle import Triangle
from src.shapescalculatorpython.models.trapezium import Trapezium
from src.shapescalculatorpython.models.rectangle import Rectangle


def run_calculator():
    select_input: str
    menu_selection = screen.first_menu()

    if menu_selection == "Triangle":
        select_input = screen.second_menu()
        if select_input == "Area":
            Triangle().calculate_area()
        else:
            Triangle().calculate_perimeter()

    elif menu_selection == "Circle":
        select_input = screen.second_menu()
        if select_input == "Area":
            Circle().calculate_area()
        else:
            Circle().calculate_perimeter()

    elif menu_selection == "Square":
        select_input = screen.second_menu()
        if select_input == "Area":
            Square().calculate_area()
        else:
            Square().calculate_perimeter()

    elif menu_selection == "Rectangle":
        select_input = screen.second_menu()
        if select_input == "Area":
            Rectangle().calculate_area()
        else:
            Rectangle().calculate_perimeter()

    elif menu_selection == "Parallelogram":
        select_input = screen.second_menu()
        if select_input == "Area":
            Parallelogram().calculate_area()
        else:
            Parallelogram().calculate_perimeter()

    elif menu_selection == "Trapezium":
        select_input = screen.second_menu()
        if select_input == "Area":
            Trapezium().calculate_area()
        else:
            Trapezium().calculate_perimeter()

    screen.third_menu()
