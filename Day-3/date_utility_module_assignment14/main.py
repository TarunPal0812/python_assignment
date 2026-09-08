from date_util import DateUtility
from exceptions import InvalidDateError


def main() -> None:
    print(" DATE UTILITY ")

   
    while True:
        try:
            dob_input = input("Enter DOB (YYYY-MM-DD): ").strip()
            dob = DateUtility.parse_date(dob_input)
            age = DateUtility.calculate_age(dob)
            day = DateUtility.get_day_of_week(dob)

            print(f"Age: {age}")
            print(f"Day: {day}")
            break
        except InvalidDateError as error:
            print(f"Error: {error}")

  
    while True:
        try:
            first_input = input("\nEnter first date (YYYY-MM-DD): ").strip()
            second_input = input("Enter second date (YYYY-MM-DD): ").strip()

            first_date = DateUtility.parse_date(first_input)
            second_date = DateUtility.parse_date(second_input)

            total_days = DateUtility.days_between_dates(first_date, second_date)
            print(f"Days between dates: {total_days}")
            break
        except InvalidDateError as error:
            print(f"Error: {error}")

 
    while True:
        try:
            year_input = input("\nEnter a year: ").strip()
            year = int(year_input)
            if DateUtility.is_leap_year(year):
                print(f"{year} is a leap year.")
            else:
                print(f"{year} is not a leap year.")
            break
        except ValueError:
            print("Error: Please enter a valid year.")


if __name__ == "__main__":
    main()
