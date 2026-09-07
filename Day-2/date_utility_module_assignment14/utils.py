from datetime import date


class DateUtilityError(Exception):
    """Base exception for date utility errors."""


class InvalidDateError(DateUtilityError):
    """Raised when an invalid date is provided."""


def parse_date(date_string: str) -> date:
    """
    Convert a date string in YYYY-MM-DD format into a date object.

    Args:
        date_string: Date string in YYYY-MM-DD format.

    Returns:
        A datetime.date object.

    Raises:
        InvalidDateError: If the date format or date value is invalid.
    """

    try:
        return date.fromisoformat(date_string)

    except ValueError:
        raise InvalidDateError(
            "Invalid date. Please use YYYY-MM-DD format."
        )


def calculate_age(dob: date) -> int:
    """
    Calculate a person's age based on their date of birth.

    Args:
        dob: Date of birth as a datetime.date object.

    Returns:
        The person's age in complete years.

    Raises:
        InvalidDateError: If the date of birth is in the future.
    """

    today: date = date.today()

    if dob > today:
        raise InvalidDateError(
            "Date of birth cannot be in the future."
        )

    age: int = today.year - dob.year

    # Birthday has not occurred yet this year.
    if (today.month, today.day) < (dob.month, dob.day):
        age -= 1

    return age


def days_between_dates(
    first_date: date,
    second_date: date
) -> int:
    """
    Calculate the number of days between two dates.

    Args:
        first_date: First date.
        second_date: Second date.

    Returns:
        The absolute number of days between the dates.
    """

    difference = second_date - first_date

    return abs(difference.days)


def is_leap_year(year: int) -> bool:
    """
    Check whether a given year is a leap year.

    Args:
        year: Year to check.

    Returns:
        True if the year is a leap year, otherwise False.
    """

    return (
        year % 400 == 0
        or (
            year % 4 == 0
            and year % 100 != 0
        )
    )


def get_day_of_week(input_date: date) -> str:
    """
    Get the day of the week for a given date.

    Args:
        input_date: Date to check.

    Returns:
        Name of the day, such as Monday or Sunday.
    """

    return input_date.strftime("%A")