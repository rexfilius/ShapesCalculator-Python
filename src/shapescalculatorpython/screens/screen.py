import calculator
from src.shapescalculatorpython.models.shape import Shapes


selectedShape: int
selectedCalculation: int

menuForCalculation = {1: 'Area', 2: 'Perimeter'}
menuForShape = {1: Shapes.Triangle,
                2: Shapes.Circle,
                3: Shapes.Square,
                4: Shapes.Rectangle,
                5: Shapes.Parallelogram,
                6: Shapes.Trapezium}


def menuToSelectShape() -> Shapes:
    firstMessage = """
            This Application Calculates The Area And Perimeter Of 2-Dimensional Shapes
            Type in a NUMBER corresponding to the SHAPE
            """
    print(firstMessage.strip())
    for key, shape in menuForShape.items():
        print(f"{key} - {shape.name}")

    global selectedShape
    try:
        selectedShape = int(input())
        checkMenuToSelectShape()
        return menuForShape[selectedShape]
    except ValueError:
        print("\nInvalid Input\n")
        menuToSelectShape()


def checkMenuToSelectShape():
    while selectedShape not in menuForShape:
        print('\nPlease type in the NUMBER corresponding with the SHAPE\n')
        menuToSelectShape()


def menuToSelectMeasurement() -> int:
    print("What do you want to calculate:")
    for key, value in menuForCalculation.items():
        print(f"{key} - {value}")

    global selectedCalculation
    try:
        selectedCalculation = int(input())
        checkMenuToSelectMeasurement()
        return selectedCalculation
    except ValueError:
        print("\nInvalid Input\n")
        menuToSelectMeasurement()


def checkMenuToSelectMeasurement():
    while selectedCalculation not in menuForCalculation:
        print('Please type in the corresponding NUMBER')
        menuToSelectMeasurement()


def menuToContinueOrEnd():
    print("\nPress 1 to go back to MENU\nPress 2 to END")
    try:
        thirdMenuInput = int(input())
        if thirdMenuInput == 1:
            calculator.runCalculator()
        elif thirdMenuInput == 2:
            print('End of program\n')
        else:
            print('Invalid input')
            menuToContinueOrEnd()
    except (ValueError, TypeError):
        print("\nInvalid Input\n")
        menuToContinueOrEnd()
