
# Student Marks and Grade Report
students = int(input("Enter number of students: "))
while students <= 0:
    print("Number of students must be greater than 0.")
    students = int(input("Enter number of students: "))
total_marks = 0
pass_count = 0
fail_count = 0
# Enter details of each student
for i in range(1, students + 1):
    name = input(f"\nEnter student {i} name: ")
    marks = float(input("Enter marks out of 100: "))
    # Validate marks
    while marks < 0 or marks > 100:
        print("Marks must be between 0 and 100.")
        marks = float(input("Enter marks out of 100: "))
    # Calculate grade
    if marks >= 75:
        grade = "A"
    elif marks >= 60:
        grade = "B"
    elif marks >= 50:
        grade = "C"
    elif marks >= 40:
        grade = "D"
    else:
        grade = "Fail"
    # Count pass and fail students
    if marks >= 40:
        pass_count += 1
    else:
        fail_count += 1
    # Calculate total marks
    total_marks += marks
    print(f"Student: {name}")
    print(f"Marks: {marks:g}")
    print(f"Grade: {grade}")
# Calculate class average
average = total_marks / students
# Display class summary
print("\n--- Class Performance Summary ---")
print(f"Class average: {average:.2f}")
print(f"Pass students: {pass_count}")
print(f"Fail students: {fail_count}")
