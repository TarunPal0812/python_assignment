from employee import Employee


class SalaryCalculator:
    """
    Object-Oriented salary calculation engine for employees.
    """

    HRA_RATE: float = 0.20
    DA_RATE: float = 0.10
    BONUS_RATE: float = 0.05
    TAX_RATE: float = 0.10

    def __init__(self, employee: Employee) -> None:
        self.employee: Employee = employee

    def calculate_hra(self) -> float:
        """Calculate House Rent Allowance."""
        return self.employee.basic_salary * self.HRA_RATE

    def calculate_da(self) -> float:
        """Calculate Dearness Allowance."""
        return self.employee.basic_salary * self.DA_RATE

    def calculate_bonus(self) -> float:
        """Calculate experience-based bonus."""
        if self.employee.experience >= 1:
            return self.employee.basic_salary * self.BONUS_RATE
        return 0.0

    def calculate_gross_salary(self) -> float:
        """Calculate total gross salary before tax."""
        return (
            self.employee.basic_salary
            + self.calculate_hra()
            + self.calculate_da()
            + self.calculate_bonus()
        )

    def calculate_tax(self) -> float:
        """Calculate tax deduction based on gross salary."""
        return self.calculate_gross_salary() * self.TAX_RATE

    def calculate_net_salary(self) -> float:
        """Calculate net take-home salary."""
        return self.calculate_gross_salary() - self.calculate_tax()

    def print_pay_slip(self) -> None:
        """Display itemized salary slip."""
        hra = self.calculate_hra()
        da = self.calculate_da()
        bonus = self.calculate_bonus()
        tax = self.calculate_tax()
        net = self.calculate_net_salary()

        print("Employee:", self.employee.name)
        print("Basic Salary:", f"₹ {self.employee.basic_salary:g}")
        print("HRA:", f"₹ {hra:g}")
        print("DA:", f"₹ {da:g}")
        print("Bonus:", f"₹ {bonus:g}")
        print("Tax:", f"₹ {tax:g}")
        print("Net Salary:", f"₹ {net:g}")
