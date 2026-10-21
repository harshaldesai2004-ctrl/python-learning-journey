# Check Exam Result

marks = int(input("Enter your marks: "))

# Check Result Category
if marks >= 75:
    print("Distinction")
elif marks >= 60:
    print("First Class")
elif marks >= 40:
    print("Pass")
else:
    print("Fail")