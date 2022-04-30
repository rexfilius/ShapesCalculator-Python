# from Calculator import run_calculator
import calculator

shape_menu_selection: int
calculation_menu_selection: int

calculation_menu = {1: 'Area', 2: 'Perimeter'}
shape_menu = {1: 'Triangle',
              2: 'Circle',
              3: 'Square',
              4: 'Rectangle',
              5: 'Parallelogram',
              6: 'Trapezium'}


def first_menu() -> int:
    firstMessage = """
        This Application Calculates The Area And Perimeter Of 2-Dimensional Shapes
        Type in a NUMBER corresponding to the SHAPE
        """
    print(firstMessage.strip())
    for key, value in shape_menu.items():
        print(f"{key} - {value}")

    global shape_menu_selection
    try:
        shape_menu_selection = int(input())
        check_first_menu()
        return shape_menu_selection
    except ValueError:
        print("\nInvalid Input\n")
        first_menu()


def check_first_menu():
    while shape_menu_selection not in shape_menu:
        print('\nPlease type in the NUMBER corresponding with the SHAPE\n')
        first_menu()


def second_menu() -> int:
    print("What do you want to calculate:")
    for key, value in calculation_menu.items():
        print(f"{key} - {value}")

    global calculation_menu_selection
    try:
        calculation_menu_selection = int(input())
        check_second_menu()
        return calculation_menu_selection
    except ValueError:
        print("\nInvalid Input\n")
        second_menu()


def check_second_menu():
    while calculation_menu_selection not in calculation_menu:
        print('Please type in the corresponding NUMBER')
        second_menu()


def third_menu():
    print("\nPress 1 to go back to MENU\nPress 2 to END")
    try:
        thirdMenuInput = int(input())
        if thirdMenuInput == 1:
            calculator.run_calculator()
        elif thirdMenuInput == 2:
            print('End of program\n')
        else:
            print('Invalid input')
            third_menu()
    except (ValueError, TypeError):
        print("\nInvalid Input\n")
        third_menu()
