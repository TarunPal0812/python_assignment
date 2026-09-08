from exceptions import NegativeAmountError, InsufficientBalanceError


class BankAccount:
    """
    Represents an individual bank account.
    """

    def __init__(self, account_number: str, name: str, balance: float = 0.0) -> None:
        if balance < 0:
            raise NegativeAmountError("Initial balance cannot be negative.")
        self.account_number: str = account_number.strip()
        self.name: str = name.strip()
        self.balance: float = float(balance)

    def deposit(self, amount: float) -> None:
        """Deposit money into account."""
        if amount <= 0:
            raise NegativeAmountError("Deposit amount must be positive.")
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        """Withdraw money from account."""
        if amount <= 0:
            raise NegativeAmountError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise InsufficientBalanceError("Insufficient balance.")
        self.balance -= amount

    def get_balance(self) -> float:
        """Return current balance."""
        return self.balance
