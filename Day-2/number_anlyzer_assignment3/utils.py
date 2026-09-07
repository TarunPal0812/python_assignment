def is_prime(number: int) -> bool:
    """
    Check whether a number is prime.

    Args:
        number: The integer to check.

    Returns:
        True if the number is prime, otherwise False.

    Notes:
        Numbers less than or equal to 1 are not prime.
    """

    if number <= 1:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True


def is_even(number: int) -> bool:
    """
    Check whether a number is even.

    Args:
        number: The integer to check.

    Returns:
        True if the number is even, otherwise False.
    """

    return number % 2 == 0


def is_odd(number: int) -> bool:
    """
    Check whether a number is odd.

    Args:
        number: The integer to check.

    Returns:
        True if the number is odd, otherwise False.
    """

    return number % 2 != 0


def get_factors(number: int) -> list[int]:
    """
    Return all positive factors of a number.

    Args:
        number: The integer whose factors should be found.

    Returns:
        A list containing all positive factors.

    Raises:
        ValueError: If number is zero.
    """

    if number == 0:
        raise ValueError("Factors of zero are not finite.")

    number = abs(number)

    factors = []

    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)

    return factors


def get_prime_factors(number: int) -> list[int]:
    """
    Return the unique prime factors of a number.

    Args:
        number: The integer to analyze.

    Returns:
        A list containing the unique prime factors.

    Raises:
        ValueError: If number is zero.
    """

    if number == 0:
        raise ValueError("Prime factors of zero are not finite.")

    number = abs(number)

    prime_factors = []

    for i in range(2, number + 1):
        if number % i == 0 and is_prime(i):
            prime_factors.append(i)

    return prime_factors