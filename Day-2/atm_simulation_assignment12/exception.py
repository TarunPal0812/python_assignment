class ATMError(Exception):
    """Base exception for all ATM-related errors."""


class InvalidPINError(ATMError):
    """Raised when the entered PIN is invalid."""


class InsufficientBalanceError(ATMError):
    """Raised when withdrawal amount exceeds the available balance."""


class InvalidAmountError(ATMError):
    """Raised when an invalid transaction amount is entered."""


class PINValidationError(ATMError):
    """Raised when a new PIN does not satisfy validation rules."""

