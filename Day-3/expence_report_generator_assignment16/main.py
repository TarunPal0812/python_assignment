import sys
from expense import Expense, InvalidExpenseError
from generator import ExpenseReportGenerator

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def main() -> None:
    raw_expenses = [
        {"category": "Food", "amount": 500},
        {"category": "Travel", "amount": 1000},
        {"category": "Food", "amount": 300},
        {"category": "Shopping", "amount": 2000},
    ]

    try:
        expense_objects = [
            Expense(item["category"], item["amount"]) for item in raw_expenses
        ]
        generator = ExpenseReportGenerator(expense_objects)
        print(generator.generate_report())

    except InvalidExpenseError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
