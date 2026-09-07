def calculate_hra(basic_salary: float) -> float:
    """
    Calculate HRA.

    Args:
        basic_salary: Employee's basic salary.

    Returns:
        HRA amount.
    """

    return basic_salary * 0.20


def calculate_da(basic_salary: float) -> float:
    """
    Calculate DA.

    Args:
        basic_salary: Employee's basic salary.

    Returns:
        DA amount.
    """

    return basic_salary * 0.10


def calculate_bonus(
    basic_salary: float,
    experience: int
) -> float:
    """
    Calculate employee bonus.

    Args:
        basic_salary: Employee's basic salary.
        experience: Employee's experience in years.

    Returns:
        Bonus amount.
    """

    if experience >= 1:
        return basic_salary * 0.05

    return 0


def calculate_tax(gross_salary: float) -> float:
    """
    Calculate tax.

    Args:
        gross_salary: Salary before tax.

    Returns:
        Tax amount.
    """

    return gross_salary * 0.10


def calculate_net_salary(
    basic_salary: float,
    hra: float,
    da: float,
    bonus: float,
    tax: float
) -> float:
    """
    Calculate the final net salary.

    Args:
        basic_salary: Employee's basic salary.
        hra: House Rent Allowance.
        da: Dearness Allowance.
        bonus: Employee bonus.
        tax: Tax amount.

    Returns:
        Net salary.
    """

    gross_salary = basic_salary + hra + da + bonus

    return gross_salary - tax
