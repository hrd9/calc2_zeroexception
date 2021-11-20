"""Testing Division Functionality"""
from calc.calculations.division import Division

def test_calculation_addition():
    """testing that our calculator has a static method for addition"""
    #Arrange
    mynumbers = (1.0,2.0)
    addition = Addition(mynumbers)
    #Act
    #Assert
    assert addition.get_result() == 3.0

def test_calculation_division():
    """Testing the functionality for the division"""
    mynumbers = (1.0, 2.0)
    division = Division(mynumbers)
    assert division.get_result() == 0.5
