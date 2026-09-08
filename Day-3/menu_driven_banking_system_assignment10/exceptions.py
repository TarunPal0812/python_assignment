class BankingError(Exception):
    """Base exception class for banking system operations."""
    pass


class InvalidAccountError(BankingError):
    """Raised when an account number does not exist."""
    pass


class NegativeAmountError(BankingError):
    """Raised when an invalid/negative monetary amount is supplied."""
    pass


class InsufficientBalanceError(BankingError):
    """Raised when withdrawal or transfer exceeds account balance."""
    pass


class DuplicateAccountError(BankingError):
    """Raised when trying to create an account that already exists."""
    pass
