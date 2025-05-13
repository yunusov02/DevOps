import pytest
from src.main import add, substraction, division, multiplication



def test_add_function():
    assert add(2, 3) == 5
    assert add(0, 0) == 0
    assert add(5.0, 5) == 10

def test_substraction():
    assert substraction(4, 2) == 2
    assert substraction(4, 4) == 0  
    assert substraction(0.0, 0) == 0
    assert substraction(1, 4) == -3

def test_multiplication():
    assert multiplication(4, 4) == 16
    assert multiplication(0, 1) == 0
    assert multiplication(4, -3) == -12 
    assert multiplication(-1, -5) == 5

def test_division():
    assert division(10, 2) == 5
    assert division(6, 3) == 2
    assert division(0, 2) == 0
    assert division(0.5, 0.25) == 2
    assert round(division(7, 3), 1) == 2.3

    with pytest.raises(ZeroDivisionError):
        division(10, 0)
