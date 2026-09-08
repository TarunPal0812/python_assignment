from datetime import date
from exceptions import InvalidDateError


class DateUtility:
    """
    Object-Oriented Utility for date parsing, age calculations,
    days difference, leap year checks, and day of week lookup.
    """

    @staticmethod
    def parse_date(date_string: str) -> date:
        """Parse ISO formatted string (YYYY-MM-DD) into datetime.date object."""
        try:
            return date.fromisoformat(date_string.strip())
        except ValueError:
            raise InvalidDateError("Invalid date. Please use YYYY-MM-DD format.")

    @classmethod
    def calculate_age(cls, dob: date) -> int:
        """Calculate age in complete years given date of birth."""
        today = date.today()
        if dob > today:
            raise InvalidDateError("Date of birth cannot be in the future.")

        age = today.year - dob.year
        if (today.month, today.day) < (dob.month, dob.day):
            age -= 1
        return age

    @staticmethod
    def days_between_dates(first_date: date, second_date: date) -> int:
        """Calculate total number of days between two dates."""
        difference = second_date - first_date
        return abs(difference.days)

    @staticmethod
    def is_leap_year(year: int) -> bool:
        """Check if a given year is a leap year."""
        return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

    @staticmethod
    def get_day_of_week(input_date: date) -> str:
        """Get full weekday name (e.g. Sunday, Monday)."""
        return input_date.strftime("%A")
