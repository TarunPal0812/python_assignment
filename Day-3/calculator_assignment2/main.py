from calculator import Calculator


def main() -> None:
    calc = Calculator()

    try:
        raw_num1 = input("Enter first number: ")
        num1 = float(raw_num1)

        raw_num2 = input("Enter second number: ")
        num2 = float(raw_num2)

        operation = input("Enter operation (+, -, *, /): ").strip()

        result = calc.execute_operation(operation, num1, num2)
        print("Result:", result)

    except ValueError as e:
        err_msg = str(e)
        if "could not convert" in err_msg.lower() or "invalid literal" in err_msg.lower():
            print("Invalid number")
        else:
            print(err_msg)


if __name__ == "__main__":
    main()

# Output
# Enter first number: 10
# Enter second number: 20
# Enter operation (+, -, *, /): +
# Result: 30.0
