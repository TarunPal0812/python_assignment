# 2. Calculator Module 
# Create: 
# calculator/ 
# ├── main.py 
# └── operations.py 
# operations.py should contain: 
# add() 
# subtract() 
# multiply() 
# divide() 
# main.py should: 
# ● Take user input 
# ● Perform the selected operation 
# ● Handle invalid numbers 
# ● Handle invalid operations 
# ● Handle division by zero

from operations import add, subtract, multiply, divide


try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    operation = input("Enter operation (+, -, *, /): ")

    if operation == "+":
        print("Result:", add(num1, num2))

    elif operation == "-":
        print("Result:", subtract(num1, num2))

    elif operation == "*":
        print("Result:", multiply(num1, num2))

    elif operation == "/":
        print("Result:", divide(num1, num2))

    else:
        print("Invalid operation")

except ValueError:
    print("Invalid number")


# Output

# Enter first number: 10
# Enter second number: 20
# Enter operation (+, -, *, /): +
# Result: 30.0