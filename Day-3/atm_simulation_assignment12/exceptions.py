class ATMError(Exception):
    """Base exception class for ATM operations."""
    pass


class InsufficientBalanceError(ATMError):
    """Raised when withdrawal amount exceeds available balance."""
    pass


class InvalidAmountError(ATMError):
    """Raised when withdrawal or deposit amount is invalid."""
    pass


class PINValidationError(ATMError):
    """Raised when PIN fails formatting or confirmation checks."""
    pass
