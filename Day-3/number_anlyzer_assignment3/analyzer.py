class NumberAnalyzer:
    """
    Object-Oriented analyzer for inspecting mathematical properties of integers.
    """

    def __init__(self, number: int) -> None:
        self.original_number: int = number
        self.number: int = abs(number)

    def is_even(self) -> bool:
        """Check if number is even."""
        return self.number % 2 == 0

    def is_odd(self) -> bool:
        """Check if number is odd."""
        return self.number % 2 != 0

    def is_prime(self) -> bool:
        """Check if number is prime."""
        if self.number <= 1:
            return False
        for i in range(2, int(self.number**0.5) + 1):
            if self.number % i == 0:
                return False
        return True

    def get_factors(self) -> list[int] | str:
        """Return list of factors or 'Not defined' for 0."""
        if self.number == 0:
            return "Not defined"
        factors = []
        for i in range(1, self.number + 1):
            if self.number % i == 0:
                factors.append(i)
        return factors

    def get_prime_factors(self) -> list[int] | str:
        """Return unique prime factors or 'Not defined' for 0."""
        if self.number == 0:
            return "Not defined"
        factors = self.get_factors()
        if isinstance(factors, str):
            return factors
        prime_factors = []
        for factor in factors:
            if NumberAnalyzer(factor).is_prime():
                prime_factors.append(factor)
        return prime_factors

    def display_analysis(self) -> None:
        """Display comprehensive analysis report of the number."""
        if self.original_number < 0:
            print("Negative number converted to:", self.number)

        if self.number == 0:
            print("Even: Yes")
            print("Prime: No")
            print("Factors: Not defined")
            print("Prime Factors: Not defined")
        elif self.number == 1:
            print("Even: No")
            print("Prime: No")
            print("Factors: [1]")
            print("Prime Factors: []")
        else:
            print("Even:", "Yes" if self.is_even() else "No")
            print("Prime:", "Yes" if self.is_prime() else "No")
            print("Factors:", self.get_factors())
            print("Prime Factors:", self.get_prime_factors())
