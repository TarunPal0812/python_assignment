# 17. Expense Report Generator 
# Given: 
# expenses = [ 
#     {"category": "Food", "amount": 500}, 
#     {"category": "Travel", "amount": 1000}, 
#     {"category": "Food", "amount": 300}, 
#     {"category": "Shopping", "amount": 2000}, 
# ] 
# Generate: 
# Total Expense: ₹3800 
 
# Food: ₹800 
# Travel: ₹1000 
# Shopping: ₹2000 
 
# Highest Category: Shopping 
# Functions should include: 
# calculate_total() 
# group_by_category() 
# get_highest_category() 
# generate_report() 
# Handle empty expenses and invalid amounts. 


class InvalidExpenseError(ValueError):
    """Raised when an expense contains invalid data."""


def calculate_total(expenses: list) -> float:
    """
    Calculate the total amount of all expenses.

    Args:
        expenses: List of expense records.

    Returns:
        Total expense amount.

    Raises:
        InvalidExpenseError: If an amount is invalid.
    """
    total: float = 0

    for expense in expenses:
        amount = expense.get("amount")

        if not isinstance(amount, (int, float)) or isinstance(amount, bool):
            raise InvalidExpenseError(
                f"Invalid amount: {amount}"
            )

        if amount < 0:
            raise InvalidExpenseError(
                f"Amount cannot be negative: {amount}"
            )

        total += amount

    return total


def group_by_category(expenses: list) -> dict[str, float]:
    """
    Group expenses and calculate the total for each category.

    Args:
        expenses: List of expense records.

    Returns:
        Dictionary containing category-wise expense totals.

    Raises:
        InvalidExpenseError: If an expense category or amount is invalid.
    """
    category_totals: dict[str, float] = {}

    for expense in expenses:
        category = expense.get("category")
        amount = expense.get("amount")

        if not isinstance(category, str) or not category.strip():
            raise InvalidExpenseError("Category must be a non-empty string.")

        if not isinstance(amount, (int, float)) or isinstance(amount, bool):
            raise InvalidExpenseError(
                f"Invalid amount: {amount}"
            )

        if amount < 0:
            raise InvalidExpenseError(
                f"Amount cannot be negative: {amount}"
            )

        category_totals[category] = (
            category_totals.get(category, 0) + amount
        )

    return category_totals


def get_highest_category(
    category_totals: dict[str, float]
) -> str | None:
    """
    Find the category with the highest total expense.

    Args:
        category_totals: Dictionary of category-wise totals.

    Returns:
        Name of the highest spending category.
        Returns None if there are no categories.
    """
    if not category_totals:
        return None

    return max(category_totals, key=category_totals.get)


def generate_report(expenses: list) -> str:
    """
    Generate a formatted expense report.

    Args:
        expenses: List of expense records.

    Returns:
        Formatted expense report.

    Raises:
        InvalidExpenseError: If expense data is invalid.
    """
    if not expenses:
        return "No expenses recorded."

    total: float = calculate_total(expenses)
    category_totals: dict[str, float] = group_by_category(expenses)
    highest_category: str | None = get_highest_category(category_totals)

    report: list[str] = [
        f"Total Expense: ₹{total:g}"
    ]

    for category, amount in category_totals.items():
        report.append(f"{category}: ₹{amount:g}")

    report.append(
        f"Highest Category: {highest_category}"
    )

    return "\n".join(report)


def main() -> None:
    """Run the expense report generator."""

    expenses: list = [
        {"category": "Food", "amount": 500},
        {"category": "Travel", "amount": 1000},
        {"category": "Food", "amount": 300},
        {"category": "Shopping", "amount": 2000},
    ]

    try:
        report: str = generate_report(expenses)
        print(report)

    except InvalidExpenseError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()


# Output
# Total Expense: ₹3800
# Food: ₹800
# Travel: ₹1000
# Shopping: ₹2000
# Highest Category: Shopping