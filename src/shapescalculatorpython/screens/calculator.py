from screen import menuToSelectShape, menuToSelectMeasurement, menuToContinueOrEnd
from src.shapescalculatorpython.models.circle import Circle
from src.shapescalculatorpython.models.shape import Shapes, measureShape
from src.shapescalculatorpython.models.square import Square
from src.shapescalculatorpython.models.parallelogram import Parallelogram
from src.shapescalculatorpython.models.triangle import Triangle
from src.shapescalculatorpython.models.trapezium import Trapezium
from src.shapescalculatorpython.models.rectangle import Rectangle


def runCalculator():
    selectedMeasurement: int
    selectedShape = menuToSelectShape()

    if selectedShape is Shapes.Triangle:
        selectedMeasurement = menuToSelectMeasurement()
        measureShape(selectedMeasurement, Triangle())
    elif selectedShape is Shapes.Circle:
        selectedMeasurement = menuToSelectMeasurement()
        measureShape(selectedMeasurement, Circle())
    elif selectedShape is Shapes.Square:
        selectedMeasurement = menuToSelectMeasurement()
        measureShape(selectedMeasurement, Square())
    elif selectedShape is Shapes.Rectangle:
        selectedMeasurement = menuToSelectMeasurement()
        measureShape(selectedMeasurement, Rectangle())
    elif selectedShape is Shapes.Parallelogram:
        selectedMeasurement = menuToSelectMeasurement()
        measureShape(selectedMeasurement, Parallelogram())
    elif selectedShape is Shapes.Trapezium:
        selectedMeasurement = menuToSelectMeasurement()
        measureShape(selectedMeasurement, Trapezium())

    menuToContinueOrEnd()
    # End of run_calculator function
