class DateUtilityError(Exception):
    """Base exception class for date utility operations."""
    pass


class InvalidDateError(DateUtilityError):
    """Raised when an invalid date string format or invalid date value is encountered."""
    pass
