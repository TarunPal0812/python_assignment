from bank_account import BankAccount
from exceptions import InvalidAccountError, DuplicateAccountError


class Bank:
    """
    Manages accounts registry, deposits, withdrawals, transfers, and balance lookup.
    """

    def __init__(self) -> None:
        self.accounts: dict[str, BankAccount] = {}

    def create_account(self, account_number: str, name: str, balance: float) -> BankAccount:
        """Create and register a new bank account."""
        acc_num = account_number.strip()
        if acc_num in self.accounts:
            raise DuplicateAccountError("Account number already exists.")
        account = BankAccount(acc_num, name, balance)
        self.accounts[acc_num] = account
        return account

    def get_account(self, account_number: str) -> BankAccount:
        """Retrieve account by account number."""
        acc_num = account_number.strip()
        if acc_num not in self.accounts:
            raise InvalidAccountError("Account not found.")
        return self.accounts[acc_num]

    def deposit(self, account_number: str, amount: float) -> None:
        """Deposit into an account."""
        account = self.get_account(account_number)
        account.deposit(amount)

    def withdraw(self, account_number: str, amount: float) -> None:
        """Withdraw from an account."""
        account = self.get_account(account_number)
        account.withdraw(amount)

    def get_balance(self, account_number: str) -> float:
        """Check balance of an account."""
        account = self.get_account(account_number)
        return account.get_balance()

    def transfer(self, from_account_number: str, to_account_number: str, amount: float) -> None:
        """Transfer funds between two accounts atomically."""
        sender = self.get_account(from_account_number)
        receiver = self.get_account(to_account_number)
        sender.withdraw(amount)
        receiver.deposit(amount)
