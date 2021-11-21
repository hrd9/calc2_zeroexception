"""Testing Division Functionality"""
from calc.calculations.division import Division

def test_calculation_division():
    """Testing the functionality for the division"""
    mynumbers = (1.0, 2.0)
    division = Division(mynumbers)
    assert division.get_result() == 0.5
