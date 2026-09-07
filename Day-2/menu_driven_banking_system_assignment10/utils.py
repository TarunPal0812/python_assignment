from custom_exceptiom import DuplicateAccountError,NegativeAmountError,InsufficientBalanceError,InvalidAccountError

def create_account(
    accounts: dict,
    account_number: str,
    name: str,
    balance: float = 0
) -> None:
    """
    Create a new bank account.

    Args:
        accounts: Dictionary containing all accounts.
        account_number: Unique account number.
        name: Name of the account holder.
        balance: Initial account balance.

    Raises:
        DuplicateAccountError: If account already exists.
        NegativeAmountError: If initial balance is negative.
    """

    if account_number in accounts:
        raise DuplicateAccountError(
            "Account number already exists."
        )

    if balance < 0:
        raise NegativeAmountError(
            "Balance cannot be negative."
        )

    accounts[account_number] = {
        "account_number": account_number,
        "name": name,
        "balance": balance
    }


def deposit(
    accounts: dict,
    account_number: str,
    amount: float
) -> None:
    """
    Deposit money into an account.

    Args:
        accounts: Dictionary containing all accounts.
        account_number: Account to deposit into.
        amount: Amount to deposit.

    Raises:
        InvalidAccountError: If account does not exist.
        NegativeAmountError: If amount is zero or negative.
    """

    if account_number not in accounts:
        raise InvalidAccountError(
            "Account does not exist."
        )

    if amount <= 0:
        raise NegativeAmountError(
            "Amount must be greater than zero."
        )

    accounts[account_number]["balance"] += amount




def withdraw(
    accounts: dict,
    account_number: str,
    amount: float
) -> None:
    """
    Withdraw money from an account.

    Args:
        accounts: Dictionary containing all accounts.
        account_number: Account to withdraw from.
        amount: Amount to withdraw.

    Raises:
        InvalidAccountError: If account does not exist.
        NegativeAmountError: If amount is zero or negative.
        InsufficientBalanceError: If balance is insufficient.
    """

    if account_number not in accounts:
        raise InvalidAccountError(
            "Account does not exist."
        )

    if amount <= 0:
        raise NegativeAmountError(
            "Amount must be greater than zero."
        )

    if amount > accounts[account_number]["balance"]:
        raise InsufficientBalanceError(
            "Insufficient balance."
        )

    accounts[account_number]["balance"] -= amount


def transfer(
    accounts: dict,
    from_account: str,
    to_account: str,
    amount: float
) -> None:
    """
    Transfer money from one account to another.

    Args:
        accounts: Dictionary containing all accounts.
        from_account: Account sending the money.
        to_account: Account receiving the money.
        amount: Amount to transfer.

    Raises:
        InvalidAccountError: If either account does not exist.
        NegativeAmountError: If amount is zero or negative.
        InsufficientBalanceError: If sender has insufficient balance.
    """

    if from_account not in accounts:
        raise InvalidAccountError(
            "Sender account does not exist."
        )

    if to_account not in accounts:
        raise InvalidAccountError(
            "Receiver account does not exist."
        )

    if amount <= 0:
        raise NegativeAmountError(
            "Amount must be greater than zero."
        )

    if amount > accounts[from_account]["balance"]:
        raise InsufficientBalanceError(
            "Insufficient balance."
        )

    accounts[from_account]["balance"] -= amount
    accounts[to_account]["balance"] += amount



def get_balance(
    accounts: dict,
    account_number: str
) -> float:
    """
    Get the balance of an account.

    Args:
        accounts: Dictionary containing all accounts.
        account_number: Account number.

    Returns:
        Current account balance.

    Raises:
        InvalidAccountError: If account does not exist.
    """

    if account_number not in accounts:
        raise InvalidAccountError(
            "Account does not exist."
        )

    return accounts[account_number]["balance"]

