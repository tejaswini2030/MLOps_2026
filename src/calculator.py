def _check_numbers(*values):
    """
    Checks that every value is an int or a float.
    Raises:
        ValueError: If any value is not a number.
    """
    for value in values:
        if not isinstance(value, (int, float)):
            raise ValueError("All inputs must be numbers.")


def fun1(x, y):
    """
    Adds two numbers together.
    Args:
        x (int/float): First number.
        y (int/float): Second number.
    Returns:
        int/float: Sum of x and y.
        Raises:
        ValueError: If x or y is not a number.
    """
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Both inputs must be numbers.")

    return x + y

def fun2(x, y):
    """
    Subtracts two numbers.
    Args:
        x (int/float): First number.
        y (int/float): Second number.
    Returns:
        int/float: Difference of x and y.
        Raises:
        ValueError: If x or y is not a number.
    """
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Both inputs must be numbers.")
    return x - y

def fun3(x, y):
    """
    Multiplies two numbers together.
    Args:
        x (int/float): First number.
        y (int/float): Second number.
    Returns:
        int/float: Product of x and y.
        Raises:
        ValueError: If either x or y is not a number.
    """
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Both inputs must be numbers.")
    return x * y

def fun4(x, y, z):
    """
    Adds three numbers together.
    Args:
        x (int/float): First number.
        y (int/float): Second number.
        z (int/float): Third number.
    Returns:
        int/float: Sum of x, y and z.
    Raises:
        ValueError: If x, y or z is not a number.   (MODIFIED: added validation)
    """
    _check_numbers(x, y, z)
    total_sum = x + y + z
    return total_sum


# ---------------------------------------------------------------
# New functions (my modifications)
# ---------------------------------------------------------------

def divide(x, y):
    """
    Divides x by y.
    Args:
        x (int/float): Numerator.
        y (int/float): Denominator.
    Returns:
        float: x divided by y.
    Raises:
        ValueError: If x or y is not a number.
        ZeroDivisionError: If y is 0.
    """
    _check_numbers(x, y)
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return x / y


def power(x, y):
    """
    Raises x to the power of y.
    Args:
        x (int/float): Base.
        y (int/float): Exponent.
    Returns:
        int/float: x to the power of y.
    Raises:
        ValueError: If x or y is not a number.
    """
    _check_numbers(x, y)
    return x ** y


def average(numbers):
    """
    Returns the average (mean) of a list of numbers.
    Args:
        numbers (list): A list of ints/floats.
    Returns:
        float: The average of the numbers.
    Raises:
        ValueError: If the list is empty or contains a non-number.
    """
    if not numbers:
        raise ValueError("Cannot average an empty list.")
    _check_numbers(*numbers)
    return sum(numbers) / len(numbers)
