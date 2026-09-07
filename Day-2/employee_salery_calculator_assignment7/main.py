# 7. Employee Salary Calculator 
# Input: 
# employee = { 
# "name": "Ashmita", 
# "basic_salary": 100000, 
# "experience": 1 
# } 
# Calculate: 
# Basic Salary 
# HRA 
# DA 
# Bonus 
# Tax 
# Net Salary 
# Create separate functions for each calculation. 
# Structure 
# salary/ 
# ├── main.py 
# ├── calculations.py 
# └── validators.py 
# Invalid salary or experience should raise appropriate exceptions.


from calculations import (
    calculate_hra,
    calculate_da,
    calculate_bonus,
    calculate_tax,
    calculate_net_salary
)

from validators import (
    validate_salary,
    validate_experience
)


def main() -> None:
    """
    Calculate and display employee salary details.
    """

    employee = {
        "name": "Ashmita",
        "basic_salary": 100000,
        "experience": 1
    }

    try:
        basic_salary = employee["basic_salary"]
        experience = employee["experience"]

       
        validate_salary(basic_salary)
        validate_experience(experience)

       
        hra = calculate_hra(basic_salary)
        da = calculate_da(basic_salary)
        bonus = calculate_bonus(
            basic_salary,
            experience
        )

        gross_salary = (
            basic_salary
            + hra
            + da
            + bonus
        )

        tax = calculate_tax(gross_salary)

        net_salary = calculate_net_salary(
            basic_salary,
            hra,
            da,
            bonus,
            tax
        )

  
        print("Employee:", employee["name"])
        print("Basic Salary:", "₹", basic_salary)
        print("HRA:", "₹", hra)
        print("DA:", "₹", da)
        print("Bonus:", "₹", bonus)
        print("Tax:", "₹", tax)
        print("Net Salary:", "₹", net_salary)

    except ValueError as error:
        print("Error:", error)


if __name__ == "__main__":
    main()


# Output
#
# Employee: Ashmita
# Basic Salary: ₹ 100000
# HRA: ₹ 20000.0
# DA: ₹ 10000.0
# Bonus: ₹ 5000.0
# Tax: ₹ 13500.0
# Net Salary: ₹ 121500.0
