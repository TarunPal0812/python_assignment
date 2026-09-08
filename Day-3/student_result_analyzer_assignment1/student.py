class Student:
    """
    Represents a student with name and marks.
    """

    PASS_THRESHOLD: float = 60.0

    def __init__(self, name: str, marks: list[float]) -> None:
        if not name or not name.strip():
            raise ValueError("Student name cannot be empty.")
        if not marks:
            raise ValueError("Marks list cannot be empty.")

        self.name: str = name.strip()
        self.marks: list[float] = [float(m) for m in marks]

    def get_average(self) -> float:
        """Calculate and return the average mark for the student."""
        return sum(self.marks) / len(self.marks)

    def get_status(self, threshold: float = PASS_THRESHOLD) -> str:
        """Determine whether the student passed or failed."""
        return "PASS" if self.get_average() >= threshold else "FAIL"
