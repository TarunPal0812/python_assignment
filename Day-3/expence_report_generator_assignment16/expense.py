class InvalidExpenseError(ValueError):
    """Raised when an expense contains invalid category or amount data."""
    pass


class Expense:
    """
    Represents an individual expense entry with validation.
    """

    def __init__(self, category: str, amount: float) -> None:
        if not isinstance(category, str) or not category.strip():
            raise InvalidExpenseError("Category must be a non-empty string.")
        if not isinstance(amount, (int, float)) or isinstance(amount, bool):
            raise InvalidExpenseError(f"Invalid amount: {amount}")
        if amount < 0:
            raise InvalidExpenseError(f"Amount cannot be negative: {amount}")

        self.category: str = category.strip()
        self.amount: float = float(amount)
