# 15. Date Utility Module 
# Use Python's standard-library datetime. 
# Create: 
# date_utils/ 
# ├── main.py 
# └── utils.py 
# Functions: 
# calculate_age() 
# days_between_dates() 
# is_leap_year() 
# get_day_of_week() 
# Example: 
# Enter DOB: 1996-05-12 
# Age: 30 
# Day: Sunday 
# Handle invalid date formats using exceptions. 

from datetime import date

from utils import (
    parse_date,
    calculate_age,
    days_between_dates,
    is_leap_year,
    get_day_of_week,
    InvalidDateError
)


def main() -> None:
    """
    Run the Date Utility application.

    Allows the user to calculate age, compare dates,
    check leap years, and find the day of the week.

    Returns:
        None.
    """

    print("===== DATE UTILITY =====")

    # ---------------- AGE ----------------

    while True:

        try:

            dob_input: str = input(
                "Enter DOB (YYYY-MM-DD): "
            ).strip()

            dob: date = parse_date(dob_input)

            age: int = calculate_age(dob)

            print(f"Age: {age}")
            print(
                f"Day: {get_day_of_week(dob)}"
            )

            break

        except InvalidDateError as error:

            print(f"Error: {error}")


    # ---------------- DAYS BETWEEN DATES ----------------

    while True:

        try:

            first_date_input: str = input(
                "\nEnter first date (YYYY-MM-DD): "
            ).strip()

            second_date_input: str = input(
                "Enter second date (YYYY-MM-DD): "
            ).strip()

            first_date: date = parse_date(
                first_date_input
            )

            second_date: date = parse_date(
                second_date_input
            )

            total_days: int = days_between_dates(
                first_date,
                second_date
            )

            print(
                f"Days between dates: {total_days}"
            )

            break

        except InvalidDateError as error:

            print(f"Error: {error}")


    # ---------------- LEAP YEAR ----------------

    while True:

        try:

            year_input: str = input(
                "\nEnter a year: "
            ).strip()

            year: int = int(year_input)

            result: bool = is_leap_year(year)

            if result:
                print(f"{year} is a leap year.")
            else:
                print(f"{year} is not a leap year.")

            break

        except ValueError:

            print(
                "Error: Please enter a valid year."
            )


if __name__ == "__main__":
    main()


# Output

# ===== DATE UTILITY =====
# Enter DOB (YYYY-MM-DD): 2002-12-8
# Error: Invalid date. Please use YYYY-MM-DD format.
# Enter DOB (YYYY-MM-DD): 2002-12-08
# Age: 23
# Day: Sunday

# Enter first date (YYYY-MM-DD): 2002-12-08
# Enter second date (YYYY-MM-DD): 2026-09-07
# Days between dates: 8674

# Enter a year: 2002
# 2002 is not a leap year.