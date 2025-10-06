import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from src.calculator import fun1, fun2, fun3, fun4, fun5

def test_fun1():
    assert fun1(2, 3) == 5
    with pytest.raises(ValueError):
        fun1("a", 3)

def test_fun2():
    assert fun2(5, 3) == 2
    with pytest.raises(ValueError):
        fun2(5, "b")

def test_fun3():
    assert fun3(4, 3) == 12
    with pytest.raises(ValueError):
        fun3("x", 3)

def test_fun4():
    assert fun4(1, 2, 3) == 6
    with pytest.raises(ValueError):
        fun4(1, "two", 3)


@pytest.mark.parametrize("x, y, expected", [
    (2, 3, 8),
    (5, 0, 1),
    (3, 2, 9),
])
def test_fun5(x, y, expected):
    assert fun5(x, y) == expected
    with pytest.raises(ValueError):
        fun5(x, "y")
