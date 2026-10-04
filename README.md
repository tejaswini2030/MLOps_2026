# MLOps Lab 1: Calculator with CI (GitHub Actions)

[![Testing with Pytest](https://github.com/tejaswini2030/MLOps_Lab_1/actions/workflows/github_lab1_pytest_action.yml/badge.svg)](https://github.com/tejaswini2030/MLOps_Lab_1/actions/workflows/github_lab1_pytest_action.yml)
[![Python Unittests](https://github.com/tejaswini2030/MLOps_Lab_1/actions/workflows/github_lab2_unittest_action.yml/badge.svg)](https://github.com/tejaswini2030/MLOps_Lab_1/actions/workflows/github_lab2_unittest_action.yml)

Lab Assignment 1 for IE-7374 (MLOps), based on `Github_Labs/Lab1` from the course repository [raminmohammadi/MLOps](https://github.com/raminmohammadi/MLOps). The lab covers a virtual environment, a structured repository, unit tests with **pytest** and **unittest**, and **GitHub Actions** workflows that run those tests automatically on every push to `main`.

## My modifications

| Area | Original lab | This repository |
| --- | --- | --- |
| Functions | `fun1` to `fun4` (add, subtract, multiply, sum of three) | Same four, plus new `divide`, `power` and `average` |
| Input validation | `fun4` accepted any input | `fun4` and all new functions raise `ValueError` for non-numbers; `divide` raises `ZeroDivisionError` for division by zero; `average` raises `ValueError` for an empty list |
| Data | Empty `data/` folder | `data/test_cases.csv`: a table of operations, inputs and expected results that both test suites read |
| Pytest tests | 4 tests | 26 test cases: the original 4, tests for the new functions and their error cases, a parametrized test, and one test per CSV row |
| Unittest tests | 4 tests | 9 tests: the original 4, tests for the new functions and their error cases, and a CSV-driven test using `subTest` |
| Workflows | Located in `workflows/`, which GitHub does not detect; pytest workflow invalid | Moved to `.github/workflows/`; fixed so both run (details below) |

### Data-driven tests

Instead of hard-coding every check, the tests also read `data/test_cases.csv`:

```
operation,x,y,z,expected
fun1,2,3,,5
divide,10,4,,2.5
power,2,10,,1024
...
```

Each row names a calculator function, its inputs (`z` is only used by `fun4`) and the expected result. In pytest, every row becomes its own test through `@pytest.mark.parametrize`, so a failure points to the exact row. In unittest, each row runs as a `subTest`. New cases can be added by adding a line to the CSV, with no code changes.

### Workflow fixes

The original workflow files could not run as provided:

| Change | Reason |
| --- | --- |
| Moved from `workflows/` to `.github/workflows/` | GitHub only detects workflows in `.github/workflows/`. |
| `run-nam` corrected to `run-name` | GitHub rejects workflow files with unknown keys. |
| Removed `branches-ignore` | GitHub does not allow `branches` and `branches-ignore` on the same event. |
| `actions/upload-artifact@v2` to `@v4` | Version 2 is retired, and jobs using it fail automatically. |
| `actions/checkout` and `actions/setup-python` to `@v4` / `@v5`, Python 3.8 to 3.11 | Removes deprecation warnings; Python 3.8 is end-of-life. |

## Project structure

```
MLOps_Lab_1/
├── .github/workflows/
│   ├── github_lab1_pytest_action.yml     # pytest + XML report artifact
│   └── github_lab2_unittest_action.yml   # unittest suite
├── data/
│   ├── __init__.py
│   └── test_cases.csv                    # operations, inputs, expected results
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

## Calculator functions

| Function | Returns | Raises |
| --- | --- | --- |
| `fun1(x, y)` | `x + y` | `ValueError` for non-numbers |
| `fun2(x, y)` | `x - y` | `ValueError` for non-numbers |
| `fun3(x, y)` | `x * y` | `ValueError` for non-numbers |
| `fun4(x, y, z)` | `x + y + z` | `ValueError` for non-numbers |
| `divide(x, y)` | `x / y` | `ValueError` for non-numbers, `ZeroDivisionError` if `y` is 0 |
| `power(x, y)` | `x ** y` | `ValueError` for non-numbers |
| `average(numbers)` | Mean of the list | `ValueError` for an empty list or non-numbers |

## Running locally

```
python -m venv lab_01
lab_01\Scripts\activate          # Windows
source lab_01/bin/activate       # macOS / Linux

pip install -r requirements.txt
pytest -v
python -m unittest test.test_unittest -v
```

`pytest` also collects the unittest file, so it runs both suites. `python -m unittest test.test_unittest` runs only the unittest suite.

## GitHub Actions

Both workflows run on every push to `main` on a fresh `ubuntu-latest` runner: they check out the code, set up Python, install `requirements.txt` and run the tests. The pytest workflow also uploads a JUnit XML report as the `test-results` artifact, even when tests fail. Results are visible in the repository's **Actions** tab and in the badges above.
