"""Testing the Calculator"""
from calculator.main import Calculator

def test_calculator_result():
    """testing calculator result is 0"""
    calc = Calculator()
    assert calc.result == 0

def test_calculator_add():
    """Testing the Add function of the calculator"""
    calc = Calculator()
    calc.add_number(4)
    assert calc.result == 4

def test_calculator_get_result():
    """Testing the Get result method of the calculator"""
    calc = Calculator()
    assert calc.get_result() == 0

def test_calculator_subtract():
    """Testing the subtract method of the calculator"""
    calc = Calculator()
    calc.subtract_number(1)
    assert calc.get_result() == -1

def test_calculator_multiply():
    """ tests multiplication of two numbers"""
    calc = Calculator()
    result  = calc.multiply_numbers(1,2)
    assert result == 2

def test_calculator_divide():
    """ tests divide of two numbers"""
    calc = Calculator()
    result = calc.divide_numbers(2,2)
    assert result == 1

def test_zeroexception():
    """Testing the zero exception logic"""
    calc = Calculator()
    calc.divide_numbers(3,0)
