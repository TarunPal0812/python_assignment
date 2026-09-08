import sys
from employee import Employee
from calculator import SalaryCalculator

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def main() -> None:
    try:
        emp = Employee(name="Ashmita", basic_salary=100000, experience=1)
        calc = SalaryCalculator(emp)
        calc.print_pay_slip()

    except ValueError as error:
        print("Error:", error)


if __name__ == "__main__":
    main()
