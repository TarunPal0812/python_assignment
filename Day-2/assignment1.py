# 1. Student Result Analyzer 
# Create a program that accepts multiple students: 
# students = [ 
# {"name": "Tarun", "marks": [80, 72, 91]}, 
# {"name": "Ashmita", "marks": [65, 88, 79]}, 
# {"name": "Alinda", "marks": [35, 42, 38]}, 
# {"name": "Pritam", "marks": [79, 41, 26]}, 
# {"name": "Anirban", "marks": [81, 91, 31]}, 
# ] 
# Create functions to: 
# ● Calculate average marks 
# ● Determine PASS/FAIL 
# ● Find the topper 
# ● Find the lowest-performing student 
# ● Calculate class average

PASS_THRESHOLD = 60.0


def calculate_average(marks: list[float]) -> float:
    """Return the average of a list of marks."""
    if not marks:
        raise ValueError("Cannot calculate average of an empty marks list.")

    return sum(marks) / len(marks)


def determine_status(
    average: float,
    threshold: float = PASS_THRESHOLD
) -> str:
    """Return PASS if average meets the threshold, otherwise FAIL."""
    return "PASS" if average >= threshold else "FAIL"


def find_topper(students: list[dict]):
    """Return the student with the highest average."""
    if not students:
        return None

    return max(
        students,
        key=lambda student: calculate_average(student["marks"])
    )


def find_lowest_performer(students: list[dict]):
    """Return the student with the lowest average."""
    if not students:
        return None

    return min(
        students,
        key=lambda student: calculate_average(student["marks"])
    )


def calculate_class_average(students: list[dict]) -> float:
    """Return the average of all students' averages."""
    if not students:
        raise ValueError("Cannot calculate class average with no students.")

    averages = [
        calculate_average(student["marks"])
        for student in students
    ]

    return sum(averages) / len(averages)


def print_report(students):

    print("Name\tAverage\tStatus")

    for student in students:
        name = student["name"]
        marks = student["marks"]

        average = calculate_average(marks)
        status = determine_status(average)

        print(f"{name:<8}{average:<10.2f}{status}")

    topper = find_topper(students)
    lowest = find_lowest_performer(students)
    class_average = calculate_class_average(students)

    print("\nClass Average:", round(class_average, 2))
    print("Topper:", topper["name"])
    print("Lowest Performer:", lowest["name"])


def main() -> None:

    students = [
        {"name": "Tarun", "marks": [80, 72, 91]},
        {"name": "Ashmita", "marks": [65, 88, 79]},
        {"name": "Alinda", "marks": [35, 42, 38]},
        {"name": "Pritam", "marks": [79, 41, 26]},
        {"name": "Anirban", "marks": [81, 91, 31]},
    ]

    print_report(students)


if __name__ == "__main__":
    main()



# Output:

# Name    Average Status
# Tarun   81.00     PASS
# Ashmita 77.33     PASS
# Alinda  38.33     FAIL
# Pritam  48.67     FAIL
# Anirban 67.67     PASS

# Class Average: 62.6
# Topper: Tarun
# Lowest Performer: Alinda
