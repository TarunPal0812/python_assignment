from exception import InsufficientBalanceError,InvalidAmountError,PINValidationError,ATMError

PIN: str = "1234"
balance: float = 5000.0
MAX_PIN_ATTEMPTS: int = 3


def validate_pin(pin: str) -> bool:
    """
    Validate whether the entered PIN matches the stored PIN.

    Args:
        pin: PIN entered by the user.

    Returns:
        True if the PIN is correct, otherwise False.
    """

    global PIN

    return pin == PIN


def login() -> bool:
    """
    Authenticate the user using a PIN.

    The user gets a maximum of three attempts.

    Returns:
        True if login is successful, otherwise False.
    """

    for attempt in range(1, MAX_PIN_ATTEMPTS + 1):

        entered_pin: str = input("Enter your PIN: ").strip()

        if validate_pin(entered_pin):
            print("Login successful.")
            return True

        remaining_attempts: int = MAX_PIN_ATTEMPTS - attempt

        print(
            f"Incorrect PIN. "
            f"Remaining attempts: {remaining_attempts}"
        )

    print("Maximum incorrect attempts reached.")
    return False


def check_balance() -> None:
    """
    Display the current account balance.

    Returns:
        None.
    """

    print(f"Current Balance: ₹{balance:.2f}")


def withdraw(amount: float) -> None:
    """
    Withdraw money from the account.

    Args:
        amount: Amount of money to withdraw.

    Raises:
        InvalidAmountError: If the amount is zero or negative.
        InsufficientBalanceError: If the amount exceeds the balance.
    """

    global balance

    if amount <= 0:
        raise InvalidAmountError(
            "Withdrawal amount must be positive."
        )

    if amount > balance:
        raise InsufficientBalanceError(
            "Insufficient balance."
        )

    balance -= amount

    print(
        f"₹{amount:.2f} withdrawn successfully."
    )

    print(
        f"Remaining Balance: ₹{balance:.2f}"
    )


def deposit(amount: float) -> None:
    """
    Deposit money into the account.

    Args:
        amount: Amount of money to deposit.

    Raises:
        InvalidAmountError: If the amount is zero or negative.
    """

    global balance

    if amount <= 0:
        raise InvalidAmountError(
            "Deposit amount must be positive."
        )

    balance += amount

    print(
        f"₹{amount:.2f} deposited successfully."
    )

    print(
        f"Updated Balance: ₹{balance:.2f}"
    )


def validate_new_pin(new_pin: str) -> None:
    """
    Validate the format of a new PIN.

    Rules:
        - Must contain exactly 4 digits.
        - Must contain only numeric characters.

    Args:
        new_pin: New PIN entered by the user.

    Raises:
        PINValidationError: If the PIN does not satisfy
            the validation rules.
    """

    if not new_pin.isdigit():
        raise PINValidationError(
            "PIN must contain only numbers."
        )

    if len(new_pin) != 4:
        raise PINValidationError(
            "PIN must contain exactly 4 digits."
        )


def change_pin() -> None:
    """
    Change the current ATM PIN.

    The new PIN must satisfy the PIN validation rules.

    Returns:
        None.

    Raises:
        PINValidationError: If the new PIN is invalid.
    """

    global PIN

    new_pin: str = input(
        "Enter new 4-digit PIN: "
    ).strip()

    validate_new_pin(new_pin)

    confirm_pin: str = input(
        "Confirm new PIN: "
    ).strip()

    if new_pin != confirm_pin:
        raise PINValidationError(
            "PIN confirmation does not match."
        )

    PIN = new_pin

    print("PIN changed successfully.")


def get_valid_amount(message: str) -> float:
    """
    Get a valid numeric amount from the user.

    Args:
        message: Message displayed to the user.

    Returns:
        A valid floating-point amount.

    Raises:
        InvalidAmountError: If the entered value is invalid.
    """

    try:
        amount: float = float(input(message))

        return amount

    except ValueError:
        raise InvalidAmountError(
            "Please enter a valid numeric amount."
        )


def show_menu() -> None:
    """
    Display the ATM menu.

    Returns:
        None.
    """

    print("\n===== ATM MENU =====")

    print("1. Check Balance")
    print("2. Withdraw")
    print("3. Deposit")
    print("4. Change PIN")
    print("5. Exit")


def run_atm() -> None:
    """
    Run the main ATM application.

    Handles login, menu operations, and exceptions.

    Returns:
        None.
    """

    if not login():
        print("ATM session terminated.")
        return

    while True:

        show_menu()

        choice: str = input(
            "Enter your choice: "
        ).strip()

        try:

            if choice == "1":
                check_balance()

            elif choice == "2":

                amount: float = get_valid_amount(
                    "Enter withdrawal amount: ₹"
                )

                withdraw(amount)

            elif choice == "3":

                amount: float = get_valid_amount(
                    "Enter deposit amount: ₹"
                )

                deposit(amount)

            elif choice == "4":
                change_pin()

            elif choice == "5":

                print(
                    "Thank you for using the ATM."
                )

                break

            else:
                print(
                    "Invalid choice. "
                    "Please select between 1 and 5."
                )

        except ATMError as error:
            print(f"Error: {error}")

        except Exception as error:
            print(
                f"Unexpected error occurred: {error}"
            )
