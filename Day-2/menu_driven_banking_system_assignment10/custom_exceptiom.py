class InvalidAccountError(Exception):
    """Raised when an account does not exist."""

    pass


class NegativeAmountError(Exception):
    """Raised when the amount is negative or zero."""

    pass


class InsufficientBalanceError(Exception):
    """Raised when there is not enough balance."""

    pass


class DuplicateAccountError(Exception):
    """Raised when an account number already exists."""

    pass