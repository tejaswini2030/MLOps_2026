# MLOps Lab 1 - Calculator with GitHub Actions

This is my submission for Lab Assignment 1 in IE-7374 (MLOps). I picked the GitHub Actions lab (`Github_Labs/Lab1`) from the [course repo](https://github.com/raminmohammadi/MLOps).

In the lab, we set up a virtual environment, organize the project into `src`, `test` and `data` folders, write a small calculator, test it with both pytest and unittest, and then use GitHub Actions so the tests run automatically every time we push to `main`.

## What I changed from the original lab

**1. Added three new functions to the calculator**

The original `calculator.py` had `fun1` to `fun4` (add, subtract, multiply, and add three numbers). I kept those and added:

- `divide(x, y)` - divides x by y, and raises a `ZeroDivisionError` if y is 0
- `power(x, y)` - returns x to the power of y
- `average(numbers)` - returns the average of a list, and raises a `ValueError` if the list is empty

**2. Added input validation to `fun4`**

I noticed `fun1`, `fun2` and `fun3` check that their inputs are numbers, but `fun4` didn't. So I added a helper function `_check_numbers()` that checks any number of values, and used it in `fun4` and in the new functions. Now they all raise a `ValueError` if you pass something like a string.

**3. Used the `data` folder for test cases**

The `data` folder was empty in the original lab. I added `data/test_cases.csv`, where each row has a function name, its inputs and the expected answer:

```
operation,x,y,z,expected
fun1,2,3,,5
divide,10,4,,2.5
power,2,10,,1024
```

Both test files read this CSV.

**4. More tests**

I kept the 4 original tests in each file and added tests for the new functions, including the error cases (dividing by zero, empty list, wrong input types). The pytest file now has 26 test cases and the unittest file has 9 tests.

## Project structure

```
MLOps_Lab_1/
├── .github/workflows/
│   ├── github_lab1_pytest_action.yml
│   └── github_lab2_unittest_action.yml
├── data/
│   ├── __init__.py
│   └── test_cases.csv
├── src/
│   ├── __init__.py
│   └── calculator.py
├── test/
│   ├── __init__.py
│   ├── test_pytest.py
│   └── test_unittest.py
├── .gitignore
├── README.md
└── requirements.txt
```

## How to run it

Create and activate a virtual environment:

```
python -m venv lab_01
lab_01\Scripts\activate        (Windows)
source lab_01/bin/activate     (Mac/Linux)
```

Install pytest and run the tests:

```
pip install -r requirements.txt
pytest -v
python -m unittest test.test_unittest -v
```

`pytest` picks up both test files, so it shows 35 tests in total. The second command only runs the unittest file.

## GitHub Actions

There are two workflows, and both run on every push to `main`:

- **Testing with Pytest** runs pytest and saves the results as an XML report, which you can download from the run page under "test-results".
- **Python Unittests** runs the unittest file.

You can see the results in the Actions tab of this repo.
