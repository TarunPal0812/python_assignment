from student import Student


class ResultAnalyzer:
    """
    Analyzes academic performance across a list of Student objects.
    """

    def __init__(self, students: list[Student] | None = None) -> None:
        self.students: list[Student] = students if students is not None else []

    def add_student(self, student: Student) -> None:
        """Add a Student instance to the analyzer."""
        self.students.append(student)

    def calculate_class_average(self) -> float:
        """Calculate and return average mark across all students."""
        if not self.students:
            raise ValueError("Cannot calculate class average with no students.")

        total_average = sum(student.get_average() for student in self.students)
        return total_average / len(self.students)

    def find_topper(self) -> Student | None:
        """Return student with highest average mark."""
        if not self.students:
            return None
        return max(self.students, key=lambda s: s.get_average())

    def find_lowest_performer(self) -> Student | None:
        """Return student with lowest average mark."""
        if not self.students:
            return None
        return min(self.students, key=lambda s: s.get_average())

    def print_report(self) -> None:
        """Print detailed tabular performance report."""
        print(f"{'Name':<8}{'Average':<10}{'Status'}")

        for student in self.students:
            avg = student.get_average()
            status = student.get_status()
            print(f"{student.name:<8}{avg:<10.2f}{status}")

        class_avg = self.calculate_class_average()
        topper = self.find_topper()
        lowest = self.find_lowest_performer()

        print(f"\nClass Average: {class_avg:.1f}")
        if topper:
            print(f"Topper: {topper.name}")
        if lowest:
            print(f"Lowest Performer: {lowest.name}")
