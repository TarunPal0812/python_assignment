from student import Student
from analyzer import ResultAnalyzer


def main() -> None:
    raw_students = [
        {"name": "Tarun", "marks": [80, 72, 91]},
        {"name": "Ashmita", "marks": [65, 88, 79]},
        {"name": "Alinda", "marks": [35, 42, 38]},
        {"name": "Pritam", "marks": [79, 41, 26]},
        {"name": "Anirban", "marks": [81, 91, 31]},
    ]

    students = [Student(data["name"], data["marks"]) for data in raw_students]
    analyzer = ResultAnalyzer(students)
    analyzer.print_report()


if __name__ == "__main__":
    main()

# Output:
# Name    Average   Status
# Tarun   81.00     PASS
# Ashmita 77.33     PASS
# Alinda  38.33     FAIL
# Pritam  48.67     FAIL
# Anirban 67.67     PASS
#
# Class Average: 62.6
# Topper: Tarun
# Lowest Performer: Alinda
