import csv
import os

import pytest
from src import calculator

# ---------------------------------------------------------------
# Original tests from the lab
# ---------------------------------------------------------------

def test_fun1():
    assert calculator.fun1(2, 3) == 5
    assert calculator.fun1(5,0) == 5
    assert calculator.fun1 (-1, 1) == 0
    assert calculator.fun1 (-1, -1) == -2


def test_fun2():
    assert calculator.fun2(2, 3) == -1
    assert calculator.fun2(5,0) == 5
    assert calculator.fun2 (-1, 1) == -2
    assert calculator.fun2 (-1, -1) == 0

def test_fun3():
    assert calculator.fun3(2, 3) == 6
    assert calculator.fun3(5,0) == 0
    assert calculator.fun3 (-1, 1) == -1

    assert calculator.fun3 (-1, -1) == 1

def test_fun4():
    assert calculator.fun4(2, 3, 5) == 10
    assert calculator.fun4(5,0, -1) == 4
    assert calculator.fun4 (-1, -1, -1) == -3

    assert calculator.fun4 (-1, -1, 100) == 98


# ---------------------------------------------------------------
# New tests (my modifications)
# ---------------------------------------------------------------

def test_fun4_rejects_non_numbers():
    with pytest.raises(ValueError):
        calculator.fun4(1, "2", 3)


def test_divide():
    assert calculator.divide(10, 2) == 5
    assert calculator.divide(-6, 3) == -2
    assert calculator.divide(1, 4) == 0.25


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        calculator.divide(5, 0)


def test_power():
    assert calculator.power(2, 3) == 8
    assert calculator.power(10, 0) == 1
    assert calculator.power(4, -1) == 0.25


def test_average():
    assert calculator.average([1, 2, 3, 4]) == 2.5
    assert calculator.average([5]) == 5
    assert calculator.average([-2, 2]) == 0


def test_average_empty_list():
    with pytest.raises(ValueError):
        calculator.average([])


@pytest.mark.parametrize("func", ["divide", "power"])
def test_new_functions_reject_non_numbers(func):
    with pytest.raises(ValueError):
        getattr(calculator, func)("a", 2)


# ---------------------------------------------------------------
# Data-driven tests: cases are read from data/test_cases.csv
# ---------------------------------------------------------------

CSV_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "test_cases.csv")


def load_test_cases():
    """Reads each row of the CSV into (operation, args, expected)."""
    cases = []
    with open(CSV_PATH, newline="") as f:
        for row in csv.DictReader(f):
            args = [float(row["x"]), float(row["y"])]
            if row["z"]:
                args.append(float(row["z"]))
            cases.append((row["operation"], args, float(row["expected"])))
    return cases


@pytest.mark.parametrize("operation, args, expected", load_test_cases())
def test_cases_from_csv(operation, args, expected):
    result = getattr(calculator, operation)(*args)
    assert result == pytest.approx(expected)
