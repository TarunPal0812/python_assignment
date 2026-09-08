from expense import Expense, InvalidExpenseError


class ExpenseReportGenerator:
    """
    Object-Oriented generator for compiling and rendering expense reports.
    """

    def __init__(self, expenses: list[Expense] | None = None) -> None:
        self.expenses: list[Expense] = expenses if expenses is not None else []

    def add_expense(self, expense: Expense) -> None:
        """Add an Expense object."""
        self.expenses.append(expense)

    def calculate_total(self) -> float:
        """Calculate aggregate total expense amount."""
        return sum(exp.amount for exp in self.expenses)

    def group_by_category(self) -> dict[str, float]:
        """Group expenses and sum totals by category."""
        category_totals: dict[str, float] = {}
        for exp in self.expenses:
            category_totals[exp.category] = (
                category_totals.get(exp.category, 0.0) + exp.amount
            )
        return category_totals

    def get_highest_category(self) -> str | None:
        """Find the category with the highest total expenditure."""
        totals = self.group_by_category()
        if not totals:
            return None
        return max(totals, key=totals.get)

    def generate_report(self) -> str:
        """Format and return multi-line text report."""
        if not self.expenses:
            return "No expenses recorded."

        total = self.calculate_total()
        category_totals = self.group_by_category()
        highest = self.get_highest_category()

        report_lines = [f"Total Expense: ₹{total:g}"]
        for cat, amt in category_totals.items():
            report_lines.append(f"{cat}: ₹{amt:g}")

        report_lines.append(f"Highest Category: {highest}")
        return "\n".join(report_lines)
