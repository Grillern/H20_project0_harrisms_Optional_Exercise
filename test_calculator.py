import calculator
import math
import sys
import pytest

def test_py_version():
    assert sys.version_info.major == 3



def test_add_exercise_1():
    assert calculator.add(1, 2) == 3

def test_add_exercise_2():
    assert abs(calculator.add(0.1, 0.2) - 0.3) < 1e-9

def test_add_exercise_3():
    assert calculator.add("Hello ", "World") == "Hello World"



def test_factorial_exercise_4():
    assert calculator.factorial(53610) == math.factorial(53610)

def test_factorial_is_not_int_exercise_4():
    with pytest.raises(Exception):   
        calculator.factorial("hello")

def test_factorial_negative_number_exercise_4():
    with pytest.raises(Exception):   
        calculator.factorial(-36)


def test_sin_exercise_4():
    assert abs(calculator.sin(5, 1000) - math.sin(5)) < 1e-6

def test_sin_is_not_int_exercise_4():
    with pytest.raises(Exception):   
        calculator.sin("Cookies", 1000)


def test_divide_exercise_4():
    assert abs(calculator.divide(1, 3) - 0.333333333) <= 1e-9

def test_divide_is_not_number_exercise_4():
    with pytest.raises(TypeError):   
        calculator.divide("Snacks", "Bro")


def test_cos_exercise_4():
    assert abs(calculator.cos(5, 1000) - math.cos(5)) < 1e-6

def test_cos_is_not_int_exercise_4():
    with pytest.raises(Exception):   
        calculator.cos("Cake", 1000)


def test_power_exercise_4():
    assert calculator.power(5.2, 4.5) == math.pow(5.2, 4.5)

def test_power_is_not_number_exercise_4():
    with pytest.raises(Exception):   
        calculator.power("Soda", 3)



def test_add_exercise_5():
    with pytest.raises(TypeError):   
        calculator.add("hello", 4)

def test_divide_exercise_5():
    with pytest.raises(ZeroDivisionError):   
        calculator.divide(1, 0)



@pytest.mark.parametrize("x, y, z", [(1, 2, 3), (0.1, 0.2, 0.3), ("Hello ", "World", "Hello World"), (134, 43.2, 177.2)])
def test_add_exercise_6(x, y, z):
    if type(calculator.add(x, y)) == float:
        assert abs(calculator.add(x, y) - z) < 1e-9
    else:
        assert calculator.add(x, y) == z

@pytest.mark.parametrize("x", [0, 53610, 21, 9])
def test_factorial_exercise_6(x):
    assert calculator.factorial(x) == math.factorial(x)

@pytest.mark.parametrize("x", [0.5, 5.15, "Hello", "Python", [1, 4.5, "Code"]])
def test_factorial_is_not_int_exercise_6(x):
    with pytest.raises(Exception):   
        calculator.factorial(x)

@pytest.mark.parametrize("x", [-1, -53610, -21])
def test_factorial_negative_number_exercise_6(x):
    with pytest.raises(Exception):   
        calculator.factorial(x)


@pytest.mark.parametrize("x, N", [(2, 1000), (5, 1000), (17, 1000)]) 
def test_sin_exercise_6(x, N):
    assert abs(calculator.sin(x, N) - math.sin(x)) < 1e-6

@pytest.mark.parametrize("x, N", [(2.4, 1000), ("Tea", 1000), ([2, "Party"], 1000)]) 
def test_sin_is_not_int_exercise_6(x, N):
    with pytest.raises(Exception):   
        calculator.sin(x, N)


@pytest.mark.parametrize("x, y, z", [(1, 3, 0.3333333333), (-4, 8, -0.5), (121, 2.5, 48.4)])
def test_divide_exercise_6(x, y, z):
    assert abs(calculator.divide(x, y) - z) <= 1e-9

@pytest.mark.parametrize("x, y", [("Hey", "He"), (False, False), ([1, 2], [3, 4])])
def test_divide_is_not_number_exercise_6(x, y):
    with pytest.raises(Exception):   
        calculator.divide(x, y)


@pytest.mark.parametrize("x, N", [(2, 1000), (5, 1000), (17, 1000)])
def test_cos_exercise_6(x, N):
    assert abs(calculator.cos(x, N) - math.cos(x)) < 1e-6

@pytest.mark.parametrize("x, N", [(2.4, 1000), ("Tea", 1000), ([2, "Party"], 1000)]) 
def test_cos_is_not_int_exercise_6(x, N):
    with pytest.raises(Exception):   
        calculator.cos(x, N)


@pytest.mark.parametrize("x, y", [(5.2, 4.5), (2, 8), (0, 0)])
def test_power_exercise_6(x, y):
    assert calculator.power(x, y) == math.pow(x, y)

@pytest.mark.parametrize("x, y", [(4, "Candy"), ("Black", "Belt")])
def test_power_is_not_number_exercise_6(x, y):
    with pytest.raises(Exception):   
        calculator.power(x, y)


@pytest.mark.parametrize("x, y", [("Hello", 4), ("Python", 8.5), ("Programmers", 0)])
def test_add_TypeError_exercise_6(x, y):
    with pytest.raises(TypeError):   
        calculator.add(x, y)

@pytest.mark.parametrize("x, y", [(5.2, 0), (74, 0), (1, 0), (0, 0)])
def test_divide_ZeroDivisionError_exercise_6(x, y):
    with pytest.raises(ZeroDivisionError):   
        calculator.divide(x, y)
