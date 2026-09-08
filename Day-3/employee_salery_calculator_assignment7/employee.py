class Employee:
    """
    Represents an employee profile with salary validation.
    """

    def __init__(self, name: str, basic_salary: float, experience: int) -> None:
        if not name or not name.strip():
            raise ValueError("Employee name cannot be empty.")
        if basic_salary <= 0:
            raise ValueError("Salary must be greater than zero.")
        if experience < 0:
            raise ValueError("Experience cannot be negative.")

        self.name: str = name.strip()
        self.basic_salary: float = float(basic_salary)
        self.experience: int = int(experience)
