# from Calculator import run_calculator
import calculator

INVALID_DATA = "\nYOU ENTERED INVALID DATA\n"
INVALID_CASING = "\nCHECK YOUR CASING/WORDS. TYPE CORRECTLY\n"

select = ""
parameter = ""


def first_menu() -> str:
    firstMessage = ('This Application Calculates The Area And Perimeter Of 2-Dimensional Shapes'
                    '\nList of Shapes: [Triangle, Circle, Square, Rectangle, Parallelogram, Trapezium]'
                    '\nSelect a Shape: [Type it in]')
    print(firstMessage)
    global select
    select = str(input())
    check_first_menu()
    return select


def check_first_menu():
    while (select != 'Circle' or select != 'Triangle' or select != 'Square'
           or select != 'Rectangle' or select != 'Parallelogram'
           or select != 'Trapezium'):
        print(INVALID_CASING)
        first_menu()


def second_menu() -> str:
    print("What do you want to calculate: Area? or Perimeter? [Type it in]")
    global parameter
    parameter = str(input())
    check_second_menu()
    return parameter


def check_second_menu():
    while parameter != 'Area' or parameter != 'Perimeter':
        print(INVALID_CASING)
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
