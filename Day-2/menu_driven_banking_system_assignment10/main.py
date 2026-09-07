# 10. Menu-Driven Banking System 
# Use dictionaries and functions. 
# Support: 
# 1. Create account 
# 2. Deposit 
# 3. Withdraw 
# 4. Check balance 
# 5. Transfer 
# 6. Exit 
# Example account: 
# { 
# } 
# "account_number": "ACC1001", 
# "name": "Poku", 
# "balance": 5000 
# Create functions: 
# create_account() 
# deposit() 
# withdraw() 
# transfer() 
# get_balance() 
# Handle 
# ● Invalid account 
# ● Negative amount 
# ● Insufficient balance 
# ● Duplicate account number 



# 10. Menu-Driven Banking System
#
# Support:
# 1. Create account
# 2. Deposit
# 3. Withdraw
# 4. Check balance
# 5. Transfer
# 6. Exit
#
# Handle:
# ● Invalid account
# ● Negative amount
# ● Insufficient balance
# ● Duplicate account number

from utils import create_account,deposit,withdraw,get_balance,transfer
from custom_exceptiom import InvalidAccountError,NegativeAmountError,InsufficientBalanceError,DuplicateAccountError

def main() -> None:
    """
    Run the menu-driven banking system.
    """

    accounts = {
        "ACC1001": {
            "account_number": "ACC1001",
            "name": "Poku",
            "balance": 5000
        }
    }

    while True:

        print("\n--- Banking System ---")
        print("1. Create account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check balance")
        print("5. Transfer")
        print("6. Exit")

        choice = input("Enter your choice: ")

        try:

            if choice == "1":

                account_number = input(
                    "Enter account number: "
                )

                name = input("Enter name: ")

                balance = float(
                    input("Enter initial balance: ")
                )

                create_account(
                    accounts,
                    account_number,
                    name,
                    balance
                )

                print("Account created successfully.")

            elif choice == "2":

                account_number = input(
                    "Enter account number: "
                )

                amount = float(
                    input("Enter deposit amount: ")
                )

                deposit(
                    accounts,
                    account_number,
                    amount
                )

                print("Deposit successful.")

            elif choice == "3":

                account_number = input(
                    "Enter account number: "
                )

                amount = float(
                    input("Enter withdrawal amount: ")
                )

                withdraw(
                    accounts,
                    account_number,
                    amount
                )

                print("Withdrawal successful.")

            elif choice == "4":

                account_number = input(
                    "Enter account number: "
                )

                balance = get_balance(
                    accounts,
                    account_number
                )

                print("Balance:", "₹", balance)

            elif choice == "5":

                from_account = input(
                    "Enter sender account: "
                )

                to_account = input(
                    "Enter receiver account: "
                )

                amount = float(
                    input("Enter transfer amount: ")
                )

                transfer(
                    accounts,
                    from_account,
                    to_account,
                    amount
                )

                print("Transfer successful.")

            elif choice == "6":

                print("Thank you for using the banking system.")
                break

            else:

                print("Invalid choice.")

        except (
            InvalidAccountError,
            NegativeAmountError,
            InsufficientBalanceError,
            DuplicateAccountError,
            ValueError
        ) as error:

            print("Error:", error)


if __name__ == "__main__":
    main()


# Example Output
#
# --- Banking System ---
# 1. Create account
# 2. Deposit
# 3. Withdraw
# 4. Check balance
# 5. Transfer
# 6. Exit
#
# Enter your choice: 4
# Enter account number: ACC1001
# Balance: ₹ 5000
#
# Enter your choice: 2
# Enter account number: ACC1001
# Enter deposit amount: 2000
# Deposit successful.
#
# Enter your choice: 4
# Enter account number: ACC1001
# Balance: ₹ 7000
