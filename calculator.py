import pytest
from calculator import add, subtract, multiply, divide, integer_divide, modulo

def test_add():
    assert add(3, 5) == 8
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(10, 7) == 3
    assert subtract(-1, 1) == -2
    assert subtract(5, 5) == 0

def test_multiply():
    assert multiply(3, 5) == 15
    assert multiply(-2, 4) == -8
    assert multiply(0, 10) == 0

def test_divide():
    assert divide(10, 5) == 2.0
    assert divide(7, 3) == pytest.approx(2.3333, 0.001)
    assert divide(-10, 2) == -5.0
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)

def test_integer_divide():
    assert integer_divide(10, 3) == 3
    assert integer_divide(7, 3) == 2
    assert integer_divide(-10, 3) == -4
    with pytest.raises(ZeroDivisionError):
        integer_divide(5, 0)

def test_modulo():
    assert modulo(10, 3) == 1
    assert modulo(7, 3) == 1
    assert modulo(-10, 3) == 2
    with pytest.raises(ZeroDivisionError):
        modulo(5, 0)
