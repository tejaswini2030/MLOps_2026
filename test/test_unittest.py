import csv
import sys
import os
import unittest

# Get the path to the project's root directory
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)

from src import calculator

CSV_PATH = os.path.join(project_root, "data", "test_cases.csv")


class TestCalculator(unittest.TestCase):

    # -----------------------------------------------------------
    # Original tests from the lab
    # -----------------------------------------------------------

    def test_fun1(self):
        self.assertEqual(calculator.fun1(2, 3), 5)
        self.assertEqual(calculator.fun1(5, 0), 5)

        self.assertEqual(calculator.fun1(-1, 1), 0)
        self.assertEqual(calculator.fun1(-1, -1), -2)

    def test_fun2(self):
        self.assertEqual(calculator.fun2(2, 3), -1)
        self.assertEqual(calculator.fun2(5, 0), 5)
        self.assertEqual(calculator.fun2(-1, 1), -2)
        self.assertEqual(calculator.fun2(-1, -1), 0)

    def test_fun3(self):
        self.assertEqual(calculator.fun3(2, 3), 6)
        self.assertEqual(calculator.fun3(5, 0), 0)
        self.assertEqual(calculator.fun3(-1, 1), -1)
        self.assertEqual(calculator.fun3(-1, -1), 1)

    def test_fun4(self):
        self.assertEqual(calculator.fun4(2, 3, 5), 10)
        self.assertEqual(calculator.fun4(5, 0, -1), 4)
        self.assertEqual(calculator.fun4(-1, -1, -1), -3)
        self.assertEqual(calculator.fun4(-1, -1, 100), 98)

    # -----------------------------------------------------------
    # New tests (my modifications)
    # -----------------------------------------------------------

    def test_fun4_rejects_non_numbers(self):
        with self.assertRaises(ValueError):
            calculator.fun4(1, None, 3)

    def test_divide(self):
        self.assertEqual(calculator.divide(10, 2), 5)
        self.assertEqual(calculator.divide(-6, 3), -2)
        with self.assertRaises(ZeroDivisionError):
            calculator.divide(5, 0)

    def test_power(self):
        self.assertEqual(calculator.power(2, 3), 8)
        self.assertEqual(calculator.power(10, 0), 1)
        with self.assertRaises(ValueError):
            calculator.power("2", 3)

    def test_average(self):
        self.assertEqual(calculator.average([1, 2, 3, 4]), 2.5)
        with self.assertRaises(ValueError):
            calculator.average([])
        with self.assertRaises(ValueError):
            calculator.average([1, "x"])

    def test_cases_from_csv(self):
        """Runs every row of data/test_cases.csv as its own sub-test."""
        with open(CSV_PATH, newline="") as f:
            for row in csv.DictReader(f):
                args = [float(row["x"]), float(row["y"])]
                if row["z"]:
                    args.append(float(row["z"]))
                with self.subTest(row=row):
                    result = getattr(calculator, row["operation"])(*args)
                    self.assertAlmostEqual(result, float(row["expected"]))


if __name__ == '__main__':
    unittest.main()
