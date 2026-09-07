def validate_salary(basic_salary: float) -> None:
    """
    Validate the basic salary.

    Args:
        basic_salary: Employee's basic salary.

    Raises:
        ValueError: If salary is zero or negative.
    """

    if basic_salary <= 0:
        raise ValueError("Salary must be greater than zero.")


def validate_experience(experience: int) -> None:
    """
    Validate employee experience.

    Args:
        experience: Employee's experience in years.

    Raises:
        ValueError: If experience is negative.
    """

    if experience < 0:
        raise ValueError("Experience cannot be negative.")
