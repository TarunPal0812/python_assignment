def add(a: float, b: float) -> float:
    """
    Add two numbers.

    Args:
        a: The first number.
        b: The second number.

    Returns:
        The sum of a and b.
    """
    return a + b


def subtract(a: float, b: float) -> float:
    """
    Subtract the second number from the first number.

    Args:
        a: The first number.
        b: The second number.

    Returns:
        The difference between a and b.
    """
    return a - b


def multiply(a: float, b: float) -> float:
    """
    Multiply two numbers.

    Args:
        a: The first number.
        b: The second number.

    Returns:
        The product of a and b.
    """
    return a * b


def divide(a: float, b: float) -> float:
    """
    Divide the first number by the second number.

    Args:
        a: The numerator.
        b: The denominator.

    Returns:
        The result of a divided by b.

    Raises:
        ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")

    return a / b
