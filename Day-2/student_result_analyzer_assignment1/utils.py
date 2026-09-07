
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
