PASSING_MARK = 40

def calculate_average(marks):
    """Return the average of the given marks."""
    total = sum(marks)
    return total / len(marks)


def count_above_average(marks):
    """Return how many marks are strictly above the class average."""
    average = calculate_average(marks)
    above_average_count = 0
    for mark in marks:
        if mark > average:
            above_average_count += 1
    return above_average_count


student_marks = [75, 82, 90, 64, 88, 92, 58]

class_average = calculate_average(student_marks[1:])
print(f"The average mark of the class is: {class_average}")

passing_count = 0
for mark in student_marks:
    if mark >= PASSING_MARK:
        passing_count += 1

print(f"Number of passing students: {passing_count} out of {len(student_marks)}")

recalculated_average = calculate_average(student_marks)
print(f"Recalculated average is: {recalculated_average}")
