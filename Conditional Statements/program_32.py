# Check exam eligibility

attendance = float(input("Enter attendance percentage: "))
marks = int(input("Enter marks: "))

# Check attendance and marks
if attendance >= 75 and marks >= 40:
    print("Eligible for exam")
else:
    print("Not eligible for exam")