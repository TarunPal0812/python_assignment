from exceptions import (
    ATMError,
    InsufficientBalanceError,
    InvalidAmountError,
    PINValidationError,
)


class ATM:
    """
    Object-Oriented ATM System encapsulating card pin, account balance,
    and user session management.
    """

    MAX_PIN_ATTEMPTS: int = 3

    def __init__(self, initial_pin: str = "1234", initial_balance: float = 5000.0) -> None:
        self.pin: str = initial_pin
        self.balance: float = float(initial_balance)
        self.is_authenticated: bool = False

    def validate_pin(self, entered_pin: str) -> bool:
        """Check if entered PIN matches stored PIN."""
        return entered_pin.strip() == self.pin

    def login(self) -> bool:
        """Authenticate user with maximum allowed PIN attempts."""
        for attempt in range(1, self.MAX_PIN_ATTEMPTS + 1):
            entered_pin = input("Enter your PIN: ").strip()
            if self.validate_pin(entered_pin):
                print("Login successful.")
                self.is_authenticated = True
                return True

            remaining = self.MAX_PIN_ATTEMPTS - attempt
            print(f"Incorrect PIN. Remaining attempts: {remaining}")

        print("Maximum incorrect attempts reached.")
        self.is_authenticated = False
        return False

    def check_balance(self) -> None:
        """Display current balance."""
        print(f"Current Balance: ₹{self.balance:.2f}")

    def withdraw(self, amount: float) -> None:
        """Withdraw funds from account balance."""
        if amount <= 0:
            raise InvalidAmountError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise InsufficientBalanceError("Insufficient balance.")

        self.balance -= amount
        print(f"₹{amount:.2f} withdrawn successfully.")
        print(f"Remaining Balance: ₹{self.balance:.2f}")

    def deposit(self, amount: float) -> None:
        """Deposit funds into account balance."""
        if amount <= 0:
            raise InvalidAmountError("Deposit amount must be positive.")

        self.balance += amount
        print(f"₹{amount:.2f} deposited successfully.")
        print(f"Updated Balance: ₹{self.balance:.2f}")

    def validate_new_pin(self, new_pin: str) -> None:
        """Validate string format for a new PIN."""
        if not new_pin.isdigit():
            raise PINValidationError("PIN must contain only numbers.")
        if len(new_pin) != 4:
            raise PINValidationError("PIN must contain exactly 4 digits.")

    def change_pin(self) -> None:
        """Process PIN change request."""
        new_pin = input("Enter new 4-digit PIN: ").strip()
        self.validate_new_pin(new_pin)

        confirm_pin = input("Confirm new PIN: ").strip()
        if new_pin != confirm_pin:
            raise PINValidationError("PIN confirmation does not match.")

        self.pin = new_pin
        print("PIN changed successfully.")

    @staticmethod
    def get_valid_amount(prompt: str) -> float:
        """Prompt and parse numeric amount from user input."""
        try:
            amount = float(input(prompt))
            return amount
        except ValueError:
            raise InvalidAmountError("Please enter a valid numeric amount.")

    def show_menu(self) -> None:
        """Print main ATM operation menu."""
        print("\n===== ATM MENU =====")
        print("1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Change PIN")
        print("5. Exit")

    def run(self) -> None:
        """Run interactive ATM session loop."""
        if not self.login():
            print("ATM session terminated.")
            return

        while True:
            self.show_menu()
            choice = input("Enter your choice: ").strip()

            try:
                if choice == "1":
                    self.check_balance()
                elif choice == "2":
                    amount = self.get_valid_amount("Enter withdrawal amount: ₹")
                    self.withdraw(amount)
                elif choice == "3":
                    amount = self.get_valid_amount("Enter deposit amount: ₹")
                    self.deposit(amount)
                elif choice == "4":
                    self.change_pin()
                elif choice == "5":
                    print("Thank you for using the ATM.")
                    break
                else:
                    print("Invalid choice. Please select between 1 and 5.")
            except ATMError as error:
                print(f"Error: {error}")
            except Exception as error:
                print(f"Unexpected error occurred: {error}")
