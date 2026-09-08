import sys
from bank import Bank
from exceptions import BankingError

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def main() -> None:
    bank = Bank()
    bank.create_account("ACC1001", "Poku", 5000)

    while True:
        print("\n--- Banking System ---")
        print("1. Create account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check balance")
        print("5. Transfer")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        try:
            if choice == "1":
                account_number = input("Enter account number: ")
                name = input("Enter name: ")
                balance = float(input("Enter initial balance: "))
                bank.create_account(account_number, name, balance)
                print("Account created successfully.")

            elif choice == "2":
                account_number = input("Enter account number: ")
                amount = float(input("Enter deposit amount: "))
                bank.deposit(account_number, amount)
                print("Deposit successful.")

            elif choice == "3":
                account_number = input("Enter account number: ")
                amount = float(input("Enter withdrawal amount: "))
                bank.withdraw(account_number, amount)
                print("Withdrawal successful.")

            elif choice == "4":
                account_number = input("Enter account number: ")
                balance = bank.get_balance(account_number)
                print(f"Balance: ₹ {balance:g}")

            elif choice == "5":
                from_acc = input("Enter sender account: ")
                to_acc = input("Enter receiver account: ")
                amount = float(input("Enter transfer amount: "))
                bank.transfer(from_acc, to_acc, amount)
                print("Transfer successful.")

            elif choice == "6":
                print("Thank you for using the banking system.")
                break

            else:
                print("Invalid choice.")

        except (BankingError, ValueError) as error:
            print("Error:", error)


if __name__ == "__main__":
    main()
