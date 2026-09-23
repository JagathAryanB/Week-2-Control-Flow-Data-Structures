"""Student Grade Calculator.

This program follows the Week 2 task requirements by using control flow,
list-based data storage, validation loops, and simple statistics for student
performance tracking.
"""

from typing import List, Dict, Tuple


def calculate_grade(average: float) -> Tuple[str, str]:
    """Return the grade and personalized comment for an average mark."""
    if average >= 90:
        return 'A', 'Excellent! Outstanding performance.'
    elif average >= 80:
        return 'B', 'Very Good! Keep up the great work.'
    elif average >= 70:
        return 'C', 'Good. Room for a little more improvement.'
    elif average >= 60:
        return 'D', 'Needs Improvement. Focus on weak areas.'
    else:
        return 'F', 'Failed. Please revisit the core concepts.'


def get_valid_number(prompt: str, min_val: float = 0, max_val: float = 100) -> float:
    """Get a numeric value within a valid range."""
    while True:
        try:
            value = float(input(f"{prompt}: "))
            if min_val <= value <= max_val:
                return value
            print(f"Please enter a value between {min_val} and {max_val}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def display_results_table(students: List[Dict[str, object]]) -> None:
    """Display all student results in a formatted table."""
    print("\n" + "=" * 80)
    print(f"{'Name':<20} {'Math':>8} {'Science':>8} {'English':>8} {'Average':>8} {'Grade':>6} {'Comment':>20}")
    print("-" * 80)

    for student in students:
        print(
            f"{student['name']:<20} "
            f"{student['marks'][0]:>8.1f} {student['marks'][1]:>8.1f} {student['marks'][2]:>8.1f} "
            f"{student['average']:>8.1f} {student['grade']:>6} {student['comment']:>20}"
        )

    print("=" * 80)


def display_statistics(students: List[Dict[str, object]]) -> None:
    """Display class-level averages and extremes."""
    if not students:
        print("No student data available.")
        return

    averages = [student['average'] for student in students]
    class_average = sum(averages) / len(averages)
    highest = max(averages)
    lowest = min(averages)

    print("\nClass Statistics")
    print("-" * 40)
    print(f"Total Students: {len(students)}")
    print(f"Class Average: {class_average:.2f}")
    print(f"Highest Average: {highest:.2f}")
    print(f"Lowest Average: {lowest:.2f}")


def search_student(students: List[Dict[str, object]], target_name: str) -> None:
    """Search for a specific student record."""
    matches = [student for student in students if student['name'].lower() == target_name.strip().lower()]
    if not matches:
        print("Student not found.")
        return

    for student in matches:
        print(f"\nStudent found: {student['name']}")
        print(f"Average: {student['average']:.2f}")
        print(f"Grade: {student['grade']}")
        print(f"Comment: {student['comment']}")


def main() -> None:
    """Run the student grade calculator menu."""
    students: List[Dict[str, object]] = []

    while True:
        print("\n" + "=" * 50)
        print("STUDENT GRADE CALCULATOR")
        print("=" * 50)
        print("1. Add student records")
        print("2. Search student")
        print("3. Display results")
        print("4. Display class statistics")
        print("5. Exit")

        try:
            choice = int(input("Select an option (1-5): "))
        except ValueError:
            print("Invalid choice. Please enter a number from 1 to 5.")
            continue

        if choice == 1:
            while True:
                try:
                    student_count = int(input("How many students would you like to add? "))
                    if student_count > 0:
                        break
                    print("Please enter a positive number.")
                except ValueError:
                    print("Invalid input. Please enter a whole number.")

            for i in range(student_count):
                print(f"\n=== Student {i + 1} ===")

                while True:
                    name = input("Enter student name: ").strip()
                    if name:
                        break
                    print("Name cannot be empty.")

                math = get_valid_number('Enter Math mark', 0, 100)
                science = get_valid_number('Enter Science mark', 0, 100)
                english = get_valid_number('Enter English mark', 0, 100)

                marks = [math, science, english]
                average = sum(marks) / len(marks)
                grade, comment = calculate_grade(average)

                students.append(
                    {
                        'name': name,
                        'marks': marks,
                        'average': average,
                        'grade': grade,
                        'comment': comment,
                    }
                )

        elif choice == 2:
            if not students:
                print("No student records available yet.")
                continue
            target = input("Enter student name to search: ").strip()
            search_student(students, target)

        elif choice == 3:
            if not students:
                print("No student records available yet.")
            else:
                display_results_table(students)

        elif choice == 4:
            display_statistics(students)

        elif choice == 5:
            print("Thank you for using the Student Grade Calculator.")
            break

        else:
            print("Invalid option. Please choose from 1 to 5.")


if __name__ == '__main__':
    main()
