class Calculator:
    """
    Object-Oriented Calculator supporting basic arithmetic operations and history tracking.
    """

    def __init__(self) -> None:
        self.history: list[str] = []

    def add(self, a: float, b: float) -> float:
        """Add two numbers."""
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result

    def subtract(self, a: float, b: float) -> float:
        """Subtract second number from first number."""
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result

    def multiply(self, a: float, b: float) -> float:
        """Multiply two numbers."""
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result

    def divide(self, a: float, b: float) -> float:
        """Divide first number by second number. Raises ValueError on division by zero."""
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return result

    def execute_operation(self, operation: str, num1: float, num2: float) -> float:
        """Execute selected arithmetic operation by string symbol."""
        if operation == "+":
            return self.add(num1, num2)
        elif operation == "-":
            return self.subtract(num1, num2)
        elif operation == "*":
            return self.multiply(num1, num2)
        elif operation == "/":
            return self.divide(num1, num2)
        else:
            raise ValueError("Invalid operation")
